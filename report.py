from util import load_db, get_integer, get_float
from market_scrap import get_last_traded_price


def show_report(status, holdings, booking, invested):
    returns = 0

    for pool in holdings:
        for stock in holdings[pool]:
            item = holdings[pool][stock]
            # cur_price = get_float("What is the current price of {}?".format(stock))
            cur_price = get_last_traded_price(stock)
            holdings[pool][stock]["current_price"] = cur_price

    print("")
    print("")
    print("*** REPORT ***")
    for key in status:
        print("{} pool: {}".format(key, status[key]))
        returns += status[key]

    print("")

    print("Total amount withdrawn: {}".format(booking))
    returns += booking

    print("")

    print("HOLDINGS - Long term:")
    print("{:<20s} {:<15s} {:<15s} {:<15s} {:<10s} {:<15s}".format(
        "stock", "avg.price", "quantity", "cur.price", "gain", "value"))
    for stock in holdings["long_term"]:
        item = holdings["long_term"][stock]
        quantity = item["quantity"]
        avg_price = item["avg_price"]
        cur_price = item["current_price"]
        gain = cur_price * 100 / avg_price - 100
        value = cur_price * quantity

        print("{:<20s} {:<15f} {:<15d} {:<15f} {:<10f} {:<15f}".format(
            stock, avg_price, quantity, cur_price, gain, value))

        returns += (quantity * cur_price)

    print("")

    print("HOLDINGS - Short term:")
    print("{:<20s} {:<15s} {:<15s} {:<15s} {:<10s} {:<15s}".format(
        "stock", "avg.price", "quantity", "cur.price", "gain", "value"))
    for stock in holdings["short_term"]:
        item = holdings["short_term"][stock]
        quantity = item["quantity"]
        avg_price = item["avg_price"]
        cur_price = item["current_price"]
        gain = cur_price * 100 / avg_price - 100
        value = cur_price * quantity

        print("{:<20s} {:<15f} {:<15d} {:<15f} {:<10f} {:<15f}".format(
            stock, avg_price, quantity, cur_price, gain, value))

        returns += (quantity * cur_price)

    print("")

    gain = 0
    if invested:
        gain = returns * 100 / invested - 100
    print("Total Invested: {}, Total Returns: {}, Gain: {}".format(invested, returns, gain))
    print("")
    print("")
    input()



def generate_report():
    db = load_db()

    status = {
            "long_term": 0,
            "short_term": 0
        }
    booking = 0
    invested = 0
    holdings = {
            "long_term": {},
            "short_term": {}
        }

    for item in db:
        if item["action"] == "load":
            status["long_term"] += item["long_term"]
            status["short_term"] += item["short_term"]
            invested += item["long_term"] + item["short_term"]

        elif item["action"] == "withdraw":
            amount = item["amount"]
            booking += amount
            if item["pool"] == "long_term":
                status["long_term"] -= amount
            elif item["pool"] == "short_term":
                status["short_term"] -= amount

        elif item["action"] == "buy_stock":
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            amount = price * quantity
            pool = item["pool"]
            status[pool] -= amount
            holding = holdings[pool]

            try:
                holding[name]["avg_price"] = (holding[name]["avg_price"] * holding[name]["quantity"] +
                        amount) / (holding[name]["quantity"] + quantity)
                holding[name]["quantity"] += quantity
            except:
                holding[name] = {
                        "quantity": item["quantity"],
                        "avg_price": item["price"]
                    }

        elif item["action"] == "sell_stock":
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            amount = price * quantity
            pool = item["pool"]
            status[pool] += amount
            holding = holdings[pool]

            holding[name]["quantity"] -= quantity
            status[item["pool"]] += amount

    show_report(status, holdings, booking, invested)



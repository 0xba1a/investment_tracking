import json
from util import get_date, get_item_from_list, get_integer, get_float


DB = "db/db.json"
GOALS = ["short_term", "long_term"]


def insert_into_db(obj):
    # TODO: Backup db file before operation to avoid corruption
    with open(DB, "r") as db_file:
        old_data = json.load(db_file)
        old_data.append(obj)

    with open(DB, "w") as db_file:
        json.dump(old_data, db_file)

    return 0


# TODO
# amount should be positive
# split value
# default split
def load_money():
    date = get_date()
    amount = get_integer("How much?")
    split = get_integer("What is the percent for long-term?. Remaining will go to short-term.")

    long_term = amount * split / 100
    short_term = amount - long_term

    obj = {
            "date": date,
            "action": "load",
            "amount": amount,
            "split": split,
            "long_term": long_term,
            "short_term": short_term
          }

    insert_into_db(obj)


# TODO
# amount should be less than cash in hand
def withdraw_money():
    date = get_date()
    amount = get_integer("How much?")
    pool = get_item_from_list(GOALS)

    obj = {
            "date": date,
            "action": "withdraw",
            "amount": amount,
            "pool": pool
        }

    insert_into_db(obj)


# TODO: Implement this function
def migrate_money():
    pass


# TODO
# amount should be available in pool
def buy_stock():
    date = get_date()
    stock = input("Which stock? [symbl]: ").upper()
    quantity = get_integer("How many stocks?")
    price = get_float("Price of one stock")
    pool = get_item_from_list(GOALS)

    obj = {
            "date": date,
            "action": "buy_stock",
            "name": stock,
            "quantity": quantity,
            "price": price,
            "pool": pool
        }

    insert_into_db(obj)


# TODO
# should hold that many stocks in that pool
def sell_stock():
    date = get_date()
    stock = input("Which stock? [symbl]: ").upper()
    quantity = get_integer("How many stocks?")
    price = get_float("Price of once stock")
    pool = get_item_from_list(GOALS)

    obj = {
            "date": date,
            "name": stock,
            "action": "sell_stock",
            "quantity": quantity,
            "price": price,
            "pool": pool
        }

    insert_into_db(obj)


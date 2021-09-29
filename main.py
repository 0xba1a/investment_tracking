#!/usr/bin/python3

from transact import load_money, withdraw_money, buy_stock, sell_stock, migrate_money
from report import generate_report
from util import is_integer


OPERATIONS = [
        {
            "name": "Buy stocks",
            "function": buy_stock
        },
        {
            "name": "Sell stocks",
            "function": sell_stock
        },
        {
            "name": "Load money",
            "function": load_money
        },
        {
            "name": "Withdraw money",
            "function": withdraw_money
        },
        {
            "name": "Migrate money",
            "function": migrate_money
        },
        {
            "name": "Report",
            "function": generate_report
        }
    ]


def main():
    print("*** MENU ***")

    while 1:
        index = 1
        for item in OPERATIONS:
            print("{}. {}".format(index, item["name"]))
            index += 1

        print("{}. Exit".format(index))

        choice = input("\nChoose your operation: ")

        if not is_integer(choice):
            print("ERROR: Invalid input. Please try again")
            continue

        choice = int(choice)

        if choice < 1 or choice > index:
            print("ERROR: Invalid input. Please try again")
            continue

        if choice == index:
            print("BYE...")
            return

        OPERATIONS[choice-1]["function"]()



if __name__ == "__main__":
    main()

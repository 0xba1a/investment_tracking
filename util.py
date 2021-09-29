import json
from datetime import date as date_obj
from dateutil import parser as date_parser


db = "db/db.json"

def load_db():
    with open(db, "r") as db_file:
        db_data = json.load(db_file)

    return db_data


class IllegalOptionChosenError(Exception):
    pass

class ImproperInputError(Exception):
    pass


def is_integer(data):
    try:
        int(data)
        return True
    except:
        return False

def is_float(data):
    try:
        float(data)
        return True
    except:
        return False


def get_date():
    date = input("enter date in format dd-mm-yyyy [default: today]: ")

    if not date:
        date = date_obj.today().strftime("%d-%m-%Y")

    # throws exception for wrong date
    date_parser.parse(date)
    return date


def get_item_from_list(options):
    print("\nChoose action")
    index = 1

    for option in options:
        print("{}.{}".format(index, option))
        index += 1

    chosen = input("your action: ")
    chosen = int(chosen)

    if chosen < 0 or chosen >= index:
        raise IllegalOptionChosenError

    return options[chosen-1]


def get_integer(prompt):
    data = input("\n{}: ".format(prompt))

    if not is_integer(data):
        raise ImproperInputError

    return int(data)

def get_float(prompt):
    data = input("\n{}: ".format(prompt))

    if not is_float(data):
        raise ImproperInputError

    return float(data)

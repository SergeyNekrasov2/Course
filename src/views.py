import json

from dotenv import load_dotenv
import os

from utils import *

load_dotenv()


def main_list_func(path, user_date):
    """Main list function"""
    greeting = get_greeting(user_date)
    py_file = xlsx_converting(path)
    card_info = get_card_info(py_file)
    with open(os.path.abspath("user_settings.json")) as user_setts:
        setts = json.load(user_setts)
    currencies_info = get_currencies_info(setts["user_currencies"])
    stocks_info = get_stocks(setts["user_stocks"])
    response = {
        "greeting": greeting,
        "cards": card_info,
        "currency_rates": currencies_info,
        "stock_prices": stocks_info,
    }
    return response


def events_list(user_date, date_coverage="M"):
    """Function for events-page"""
    date_diapason = time_reach_identify(user_date, date_coverage)
    df_file = xlsx_converting(os.path.abspath("operations.xlsx"))
    operations_info = operations_exp_sum(df_file, user_date, date_diapason)
    with open(os.path.abspath("user_settings.json")) as user_setts:
        setts = json.load(user_setts)
    currencies_info = get_currencies_info(setts["user_currencies"])
    stocks_info = get_stocks(setts["user_stocks"])
    response = {
        "expenses": operations_info,
        "currency_rates": currencies_info,
        "stock_prices": stocks_info,
    }
    return response

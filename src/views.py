from utils import (operations_exp_sum,time_reach_identify, get_greeting, get_card_info, get_currencies_info, get_stocks,
                   xlsx_converting)
from datetime import datetime, timedelta, date
import pandas as pd
import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()


def main_list_func(path):
    """Main list function"""
    greeting = get_greeting()
    py_file = xlsx_converting(path)
    card_info = get_card_info(py_file)
    with open ("/Users/rafaelmanasyan/PycharmProjects/Module3_Course_Work/user_settings.json") as user_setts:
        setts = json.load(user_setts)
    currencies_info = get_currencies_info(setts["user_currencies"])
    stocks_info = get_stocks(setts["user_stocks"], "2024-08-27")
    # response = {"greeting": greeting,
    #             "cards": card_info,
    #             "currency_rates": currencies_info,
    #             "stock_prices": }
    return stocks_info


print(main_list_func("/Users/rafaelmanasyan/PycharmProjects/Module3_Course_Work/data/operations.xlsx"))


def events_list():
    pass

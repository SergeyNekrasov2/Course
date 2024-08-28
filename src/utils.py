from datetime import datetime, timedelta, date
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# functions for main_page
def xlsx_converting(path):
    """Function for converting excel-file to dataframe"""
    try:
        py_from_xlsx = pd.read_excel(path)
        return py_from_xlsx
    except FileNotFoundError:
        return ["Path is not correct"]


def get_greeting():
    """Function for identify part of day"""
    current_datetime = str(datetime.now())
    hour_of_day = int(current_datetime[11:13])
    greeting = ""
    if 4 <= hour_of_day <= 10:
        greeting = "Доброе утро"
    elif 11 <= hour_of_day <= 16:
        greeting = "Добрый день"
    elif 17 <= hour_of_day <= 22:
        greeting = "Добрый вечер"
    elif 23 <= hour_of_day or hour_of_day <= 3:
        greeting = "Доброй ночи"
    return greeting


def get_card_info(operations_df):
    """Function for getting info about cards"""
    cards_list = operations_df["Номер карты"].unique()
    cards_dict = {}
    for card in cards_list:
        card_sum = operations_df.loc[operations_df["Номер карты"] == card, "Сумма платежа"].sum()
        cards_dict[f"{card}"] = {"last_digits": f"{card}",
                                 "total_spent": round(float(card_sum), 2),
                                 "cashback": round((float(card_sum) / 100), 2)}
    highest_five_operas = operations_df.sort_values(by="Сумма платежа", ascending=False).head()
    highest_five_list = []
    for i, column in highest_five_operas.iterrows():
        highest_five_list.append({
            "date": column["Дата платежа"],
            "amount": column["Сумма платежа"],
            "category": column["Категория"],
            "description": column["Описание"]
        })
    result_list = [value for key, value in cards_dict.items()] + [*highest_five_list]
    return result_list


def get_currencies_info(currencies_list):
    """Function for getting currencies information"""
    currency_info = []
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    courses = response.json()
    for valute in currencies_list:
        if courses['Valute'][valute]:
            currency_info.append({
                "currency": valute,
                "rate": courses['Valute'][valute]['Value']
            })
    return currency_info


def get_stocks(stocks_list, date):
    """Function for getting stocks information"""
    stocks_prices = []
    api_key = os.getenv("STOCKS_API_KEY")
    for stock in stocks_list:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&interval=5min&apikey={api_key}'
        r = requests.get(url).json()
        stock_price = r["Time Series (Daily)"][date]["1. open"]
        stocks_prices.append({
            "stock": f"{stock}",
            "price": f"{stock_price}"
        })
    return stocks_prices


# functions for events_page
def time_reach_identify(date_current, reach="M"):
    """Function for identify first coverage day"""
    cur_date = datetime.strptime(date_current, "%d.%m.%Y %H:%M:%S")
    first_date = None
    if reach == "W":
        days_reach = cur_date.weekday()
        first_date = cur_date - timedelta(days=days_reach)
    elif reach == "M":
        days_reach = cur_date.day
        first_date = cur_date - timedelta(days=days_reach-1)
    elif reach == "Y":
        first_date = date(cur_date.year, 1, 1)
    elif reach == "ALL":
        first_date = None
    return first_date


def operations_exp_sum(file, time_reach):
    """Filter function for transactions by date reach"""
    reach_time = pd.to_datetime(time_reach)
    list_index = []
    for i, column in file.iterrows():
        x = pd.to_datetime(column["Дата платежа"], dayfirst=True, )
        if x > reach_time:
            list_index.append(i)
    file_filtered = file[file.index.isin(list_index)]
    exp_sum = sum(file_filtered["Сумма платежа"])
    category_list = file_filtered["Категория"].unique()
    category_dict = {}
    cash_trans_dict = {}
    sorted_cat_dict = {}
    first_seven_dict = {}
    for category in category_list:
        if category not in ["Переводы", "Наличные", "Пополнения"]:
            category_sum = file_filtered.loc[file_filtered["Категория"] == category, "Сумма платежа"].sum()
            category_dict[f"{category}"] = float(category_sum)
            sorted_cat_dict = dict(sorted(category_dict.items(), key=lambda value: value[1]))
        elif category in ["Переводы", "Наличные"]:
            category_sum = file_filtered.loc[file_filtered["Категория"] == category, "Сумма платежа"].sum()
            cash_trans_dict[f"{category}"] = float(category_sum)
    count = 0
    for k, v in sorted_cat_dict.items():
        count += 1
        others_sum = 0
        if count < 8:
            first_seven_dict[f"{k}"] = v
        elif count >= 8:
            others_sum += v
            first_seven_dict["Остальное"] = others_sum
    return round(exp_sum,  2), first_seven_dict, cash_trans_dict

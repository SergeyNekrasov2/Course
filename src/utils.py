import datetime
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def xlsx_converting(path):
    """Function for converting excel-file to dataframe"""
    try:
        py_from_xlsx = pd.read_excel(path)
        return py_from_xlsx
    except FileNotFoundError:
        return ["Path is not correct"]


def get_greeting():
    """Function for identify part of day"""
    current_datetime = str(datetime.datetime.now())
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
                                 "cashback": round((float(card_sum)/100), 2)}
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



# df = xlsx_converting("/Users/rafaelmanasyan/PycharmProjects/Module3_Course_Work/data/operations.xlsx")

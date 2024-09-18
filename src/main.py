import json
import logging
from pathlib import Path
from src.utils import (get_currency_rates,get_expenses_cards,top_transaction,get_greeting,get_stock_price)
from src.views import main
from src.read_excel import read_excel


ROOT_PATH = Path(__file__).resolve().parent.parent

# logger = logging.getLogger("utils.log")
# file_handler = logging.FileHandler("main.log", "w")
# file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)


def mains(date: str, file_path: str, stocks: list, currency: list):
    """Функция создающая JSON ответ для страницы главная"""

    logger = file_path.parent.joinpath("logs", "main.log")
    logger.info("Начало работы главной функции (main)")
    greeting = get_greeting()
    my_list_trans = read_excel(file_path)
    final_list = main(date, my_list_trans)
    cards = get_expenses_cards(final_list)
    top_trans = top_transaction(final_list)
    stocks_prices = get_stock_price(stocks)
    currency_r = get_currency_rates(currency)
    logger.info("Создание JSON ответа")
    date_json = json.dumps(
        {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_trans,
            "currency_rates": currency_r,
            "stock_prices": stocks_prices,
        },
        indent=4,
        ensure_ascii=False,
    )
    logger.info("Завершение работы главной функции (main)")
    return date_json
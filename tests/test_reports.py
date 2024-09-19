import pytest

from src.reports import spending_by_category
from src.services import investment_bank
import pandas as pd


# def test_spending_by_category(get_operations_df):
#     actual = spending_by_category(get_operations_df, 'Фастфуд', '07.06.2020 14:10:18')
#     expected = pd.DataFrame({'Дата операции': ['2020-04-07 19:41:58'],
#                        'Дата платежа': ['07.04.2020'],
#                        'Номер карты': ['*7197'],
#                        'Статус': ['OK'],
#                        'Сумма операции': [-100.00],
#                        'Валюта операции': ['RUB'],
#                        'Сумма платежа': [-100.00],
#                        'Валюта платежа': ['RUB'],
#                        'Кэшбэк': [0],
#                        'Категория': ['Фастфуд'],
#                        'MCC': ['5814'],
#                        'Описание': ['IP Yakubovskaya M. V.'],
#                        'Бонусы (включая кэшбэк)': [2.00],
#                        'Округление на инвесткопилку': [0.00],
#                        'Сумма операции с округлением': [100.00]}, index=[1])
#     assert actual == expected


@pytest.mark.parametrize(
    "month, trans_list, limit, expected",
    [('2020-04', [{'2020-04-07 19:41:58': 1342}, {'2021-12-31 16:42:04': 451}], 100, 58),
     ('2021-12', [{'2020-04-07 19:41:58': 1342}, {'2021-12-31 16:42:04': 451}], 10, 9)])
def test_investment_bank(month, trans_list, limit, expected):
    assert investment_bank(month, trans_list, limit) == expected




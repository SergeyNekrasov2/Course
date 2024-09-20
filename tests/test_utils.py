import json
from unittest.mock import patch
from src.utils import get_greeting, get_currencies_info, get_stocks, get_card_info


def test_get_greeting():
    assert get_greeting('2021-12-31 16:42:04') == 'Добрый день'
    assert get_greeting('2021-12-31 10:42:04') == 'Доброе утро'
    assert get_greeting('2021-12-31 23:42:04') == 'Доброй ночи'
    assert get_greeting('2021-12-31 20:42:04') == 'Добрый вечер'


def test_get_card_info(get_operations_df):
    assert get_card_info(get_operations_df) == [
        {'cashback': -1.64, 'last_digits': '*7197', 'total_spent': -164.0},
        {'amount': -64.0,
         'category': 'Супермаркеты',
         'date': '31.12.2021',
         'description': 'Колхоз'},
        {'amount': -100.0,
         'category': 'Фастфуд',
         'date': '07.04.2020',
         'description': 'IP Yakubovskaya M. V.'}]


@patch('requests.get')
def test_get_currencies_info(mock_get):
    mock_get.return_value.json.return_value = {
        'Valute': {
            'USD': {'Value': 92.6962},
            'EUR': {'Value': 103.249}
        }
    }
    assert get_currencies_info(["USD", "EUR"]) == [{'currency': 'USD', 'rate': 92.6962},
                                                   {'currency': 'EUR', 'rate': 103.249}]
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch('os.getenv')
@patch('src.utils.urlopen')
def test_get_stocks(mock_urlopen, mock_getenv):
    mock_getenv.return_value = 'fake_api'
    mock_urlopen.return_value.read.return_value = json.dumps([{"price": 100.0}]).encode('utf-8')
    assert get_stocks(["AAPL", "AMZN"]) == [{"stock": "AAPL", "price": '100.0'}, {"stock": "AMZN", "price": '100.0'}]

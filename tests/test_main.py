from src.main import main
from unittest.mock import Mock, patch
from datetime import datetime


@patch('requests.get')
def test_mine_main(mock_read_excel):
    """Тест проверяет работу функции mine_main"""
    data_string = "01.05.2023 12:34:56"
    format = "%d.%m.%Y %H:%M:%S"
    try:
        datetime.strptime(data_string, format)
    except ValueError as e:
        print(f"Ошибка при преобразовании даты: {e}")


if __name__ == "__main__":
    test_mine_main()

    mock_get.return_value.json.return_value = {
        "greeting": "Добрый день",
        "cards": [
            {
                "last_digits": "4556",
                "total_spent": 30862.13,
                "cashback": 308.62
            },
            {
                "last_digits": "7197",
                "total_spent": 26890.62,
                "cashback": 268.91
            },
            {
                "last_digits": "5091",
                "total_spent": 1974.17,
                "cashback": 19.74
            }
        ],
        "top_transactions": [
            {
                "date": "25.11.2021",
                "amount": 4451.0,
                "category": "Другое",
                "description": "Федеральная Налоговая Служба"
            },
            {
                "date": "23.11.2021",
                "amount": 126105.03,
                "category": "Переводы",
                "description": "Перевод Кредитная карта. ТП 10.2 RUR"
            },
            {
                "date": "16.11.2021",
                "amount": 65.0,
                "category": "Бонусы",
                "description": "Вознаграждение за операции покупок"
            }
        ],
        "currency_rates": [
            {
                "currency": "USD",
                "rate": 91.38
            },
            {
                "currency": "EUR",
                "rate": 102.1
            }
        ],
        "stock_prices": [
            {
                "stock": "AAPL",
                "price": 228.03
            }]}
    res = main("2021.11.30", "data/operations.xlsx", ["AAPL"],
               ["USD", "EUR"])

    assert res == {
        "greeting": "Добрый день",
        "cards": [
            {
                "last_digits": "4556",
                "total_spent": 30862.13,
                "cashback": 308.62
            },
            {
                "last_digits": "7197",
                "total_spent": 26890.62,
                "cashback": 268.91
            },
            {
                "last_digits": "5091",
                "total_spent": 1974.17,
                "cashback": 19.74
            }
        ],
        "top_transactions": [
            {
                "date": "25.11.2021",
                "amount": 4451.0,
                "category": "Другое",
                "description": "Федеральная Налоговая Служба"
            },
            {
                "date": "23.11.2021",
                "amount": 126105.03,
                "category": "Переводы",
                "description": "Перевод Кредитная карта. ТП 10.2 RUR"
            },
            {
                "date": "16.11.2021",
                "amount": 65.0,
                "category": "Бонусы",
                "description": "Вознаграждение за операции покупок"
            }
        ],
        "currency_rates": [
            {
                "currency": "USD",
                "rate": 91.38
            },
            {
                "currency": "EUR",
                "rate": 102.1
            }
        ],
        "stock_prices": [
            {
                "stock": "AAPL",
                "price": 228.03
            }]}
    print(res)
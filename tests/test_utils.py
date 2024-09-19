from src.utils import get_greeting


def test_get_greeting():
    assert get_greeting('2021-12-31 16:42:04') == 'Добрый день'



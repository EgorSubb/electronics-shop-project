import pytest
from src import item
from src import phone
from src import keyboard


@pytest.fixture
def test_item():
    item1 = item.Item("iphone", 20000.0, 2)
    return item1


@pytest.fixture
def test_phone():
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    return phone1

@pytest.fixture
def test_keyboard():
    keyboard1 = keyboard.Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard1

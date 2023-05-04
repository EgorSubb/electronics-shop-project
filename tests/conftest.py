import pytest
from src import item
from src import phone


@pytest.fixture
def test_item():
    item1 = item.Item("iphone", 20000.0, 2)
    return item1


@pytest.fixture
def test_phone():
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    return phone1

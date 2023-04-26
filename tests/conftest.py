import pytest
from src import item


@pytest.fixture
def test_item():
    item1 = item.Item("iphone", 20000.0, 2)
    return item1

import pytest
from src import item


@pytest.fixture
def test_item():
    item1 = item.Item("honey", 2.5, 2)
    return item1

import pytest
from src import phone

def test__repr__(test_phone):
    """Проверяет вывод объекта для разработчика"""
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test__str__(test_phone):
    """Проверяет вывод объекта для пользователя"""
    assert str(test_phone) == "iPhone 14"


def test__add__():
    """Проверяет сумму количества товаров у объектов"""
    phone2 = phone.Phone("Смартфон", 10000, 20, 2)
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert phone2 + phone1 == 25

def test_number_of_sim(test_phone):
    """Проверяет количество симкарт у объекта"""
    assert test_phone.number_of_sim == 2
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0


def test_name(test_phone):
    """Проверяет соответствие имени"""
    assert test_phone.name == "iPhone 14"
    with pytest.raises(Exception):
        test_phone.name = "iphoneProMax"

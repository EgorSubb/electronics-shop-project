import pytest
import os
from src.item import Item, InstantiateCSVError
from src import phone

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test__repr__(test_item):
    """Проверяет вывод объекта для разработчика"""
    assert repr(test_item) == "Item('iphone', 20000.0, 2)"


def test__str__(test_item):
    """Проверяет вывод объекта для пользователя"""
    assert str(test_item) == "iphone"

def test__add__():
    """Проверяет сумму количества товаров у объектов"""
    item2 = Item("Смартфон", 10000, 20)
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert item2 + phone1 == 25
    with pytest.raises(ValueError):
        assert item2 + 3 == 23

def test_calculate_total_price(test_item):
    """Проверяет общую стоимость товара"""
    assert test_item.calculate_total_price() == 40000.0


def test_apply_discount(test_item):
    """Проверяет стоимость товара с учетом скидки"""
    assert test_item.apply_discount() == 20000.0


def test_name(test_item):
    """Проверяет соответствие имени"""
    assert test_item.name == "iphone"
    with pytest.raises(Exception):
        test_item.name = "iphoneProMax"


def test_string_to_number(test_item):
    """Возвращает число из числа-строки"""
    assert test_item.string_to_number('20000.0') == 20000


def test_instantiate_from_csv():

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path_to_csv=r"../src/item.csv")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_to_csv=r"../src/items.csv")
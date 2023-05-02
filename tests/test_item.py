import pytest

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test__repr__(test_item):
    """Проверяет вывод объекта для разработчика"""
    assert repr(test_item) == "Item('iphone', 20000.0, 2)"


def test__str__(test_item):
    """Проверяет вывод объекта для пользователя"""
    assert str(test_item) == "iphone"


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

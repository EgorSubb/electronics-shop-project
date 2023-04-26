
"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_calculate_total_price(test_item):
    """Проверяет общую стоимость товара"""
    assert test_item.calculate_total_price() == 40000.0


def test_apply_discount(test_item):
    """Проверяет стоимость товара с учетом скидки"""
    assert test_item.apply_discount() == 20000.0


def test_name(test_item):
    """Проверяет соответствие имени"""
    assert test_item.name == "iphone"


def test_name_len(test_item):
    """Проверяет соответствие длине имени не больше 10 символов"""
    test_item.name = "iphoneProMax"
    if len(test_item.name) <= 10:
        assert test_item.name == "iphone"
    else:
        assert print("Длина наименования товара превышает 10 символов")


def test_string_to_number(test_item):
    """Возвращает число из числа-строки"""
    assert test_item.string_to_number('20000.0') == 20000

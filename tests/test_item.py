
"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_calculate_total_price(test_item):
    """Проверяет общую стоимость товара"""
    assert test_item.calculate_total_price() == 5.0


def test_apply_discount(test_item):
    """Проверяет стоимость товара с учетом скидки"""
    assert test_item.apply_discount() == 2.5

import pytest


def test__str__(test_keyboard):
    """Проверяет вывод объекта для пользователя"""
    assert str(test_keyboard) == "Dark Project KD87A"


def test_language(test_keyboard):
    """Проверяет язык объекта класса keyboard"""
    assert test_keyboard.language == "EN"


def test_change_lang(test_keyboard):
    """Проверяет смену языка объекта класса keyboard"""
    assert test_keyboard.change_lang().language == "RU"
    assert test_keyboard.change_lang().change_lang().change_lang().language == "EN"

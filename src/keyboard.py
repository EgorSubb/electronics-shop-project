from src.item import Item


class ChangeLang:
    """
    Класс-миксин, который “подмешивается” в цепочку наследования класса `Keyboard`
    и реализует дополнительный функционал по хранению и изменению раскладки клавиатур.
    """

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        """Изменяет язык клавитуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, ChangeLang):
    """Подкласс класса Item для товара 'клавиатура', у него есть атрибут `language` и метод для изменения языка"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name

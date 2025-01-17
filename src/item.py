import csv
import os


# from src.phone import Phone
class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл items.csv поврежден'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        """Выводит объект для разработчика"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Выводит объект для пользователя"""
        return self.__name

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            total_quantity = self.quantity + other.quantity
            return total_quantity
        raise ValueError('Складывать можно только объекты Item и Phone.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path_to_csv=r"../src/items.csv"):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""

        try:
            with open(path_to_csv, newline='', encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                try:
                    for row in data:
                        name = row['name']
                        price = row['price']
                        quantity = int(row['quantity'])
                        item = cls(name, price, quantity)
                        cls.all.append(item)
                except ValueError:
                    raise InstantiateCSVError("Файл items.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")



    @staticmethod
    def string_to_number(number):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(number))

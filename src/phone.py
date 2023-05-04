from src.item import Item


class Phone(Item):
    """`Phone` содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Выводит объект для разработчика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if isinstance(self, Phone) and isinstance(other, Phone):
            total_quantity = self.quantity + other.quantity
            return total_quantity

        raise ValueError('Складывать можно только объекты Item и Phone.')


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

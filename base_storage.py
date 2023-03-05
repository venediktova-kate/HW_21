from abstract_storage import AbstractStorage
from exceptions import NotEnoughProduct, NotEnoughSpace, UnknownProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, quantity: int) -> None:
        if self.get_free_space() < quantity:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity

    def remove(self, name: str, quantity: int) -> None:
        if name not in self.__items:
            raise UnknownProduct
        if self.__items[name] < quantity:
            raise NotEnoughProduct

        self.__items[name] -= quantity
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

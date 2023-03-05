from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, name: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self):
        pass

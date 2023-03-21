from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, qnt):
        pass

    @abstractmethod
    def remove(self, name, qnt):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

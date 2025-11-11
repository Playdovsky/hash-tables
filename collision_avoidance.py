from abc import ABC, abstractmethod

class CollisionAvoidance(ABC):

    def h(self, x, table_len):
        return x % table_len

    @abstractmethod
    def insert(self, number):
        pass

    @abstractmethod
    def find(self, number):
        pass

    @abstractmethod
    def delete(self, number):
        pass

    @abstractmethod
    def rehash(self, new_length):
        pass
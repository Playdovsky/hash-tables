from abc import ABC, abstractmethod

class CollisionAvoidance(ABC):

    def h(self, x, table_len):
        return x % table_len

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def delete(self):
        pass
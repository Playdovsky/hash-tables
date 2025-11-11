from collision_avoidance import CollisionAvoidance
from marker import Marker

class OpenAddressing(CollisionAvoidance):
    def __init__(self, length=10):
        self._hash_table = [Marker.Empty] * length
        self.comparisons = 0

    def display(self):
        i = 0
        result = ""
        while i < len(self._hash_table):
            result += f"{i} | {self._hash_table[i]}\n"
            i += 1
        
        return result

    def insert(self, number):
        if self.find(number) is not None:
            return False
        
        modulo = super().h(number, len(self._hash_table))
        i = 0
        while i < len(self._hash_table):
            index = (modulo + i) % len(self._hash_table)
            if self._hash_table[index] in (Marker.Empty, Marker.Deleted):
                self._hash_table[index] = number
                return True
            
            i += 1

        return False
    
    def find(self, number):
        modulo = super().h(number, len(self._hash_table))
        i = 0
        while i < len(self._hash_table):
            index = (modulo + i) % len(self._hash_table)
            self.comparisons += 1
            if self._hash_table[index] == Marker.Empty:
                return None
            
            if self._hash_table[index] == number:
                return index

            i += 1
        
        return None
    
    def delete(self, number):
        index = self.find(number)
        if index is None:
            return False
        
        self._hash_table[index] = Marker.Deleted
        return True
    
    def rehash(self, new_length):
        empty_and_deleted = self._hash_table.count(Marker.Deleted) + self._hash_table.count(Marker.Empty)
        if new_length < len(self._hash_table) - empty_and_deleted:
            raise Exception("New length too small to accommodate existing elements")
        
        old_hash_table = self._hash_table
        self._hash_table = [Marker.Empty] * new_length

        for item in old_hash_table:
            if item not in (Marker.Empty, Marker.Deleted):
                self.insert(item)
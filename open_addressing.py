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
                return False
            
            if self._hash_table[index] == number:
                return True

            i += 1
        
        return False
    
    def delete(self, number):
        modulo = super().h(number, len(self._hash_table))
        i = 0
        while i < len(self._hash_table):
            index = (modulo + i) % len(self._hash_table)
            self.comparisons += 1
            if self._hash_table[index] == Marker.Empty:
                return False
            
            if self._hash_table[index] == number:
                self._hash_table[index] = Marker.Deleted
                return True

            i += 1
        
        return False
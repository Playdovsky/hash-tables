from collision_avoidance import CollisionAvoidance
from marker import Marker

class OpenAddressing(CollisionAvoidance):
    def __init__(self, length=10):
        self._hash_table = [Marker.Empty] * length
        self.comparisons = 0
        self._is_rehashing = False

    def _load_factor(self):
        total_elements = 0
        for item in self._hash_table:
            if item not in (Marker.Empty, Marker.Deleted):
                total_elements += 1
        
        return total_elements / len(self._hash_table)

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
                
                self._auto_rehash()
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

        self._auto_rehash()
        return True

    def _auto_rehash(self):
        if self._is_rehashing:
            return
        
        load_factor = self._load_factor()

        if load_factor > 0.75:
            new_length = len(self._hash_table) * 2
            self.rehash(new_length)
        
        if load_factor < 0.25 and len(self._hash_table) > 5:
            new_length = len(self._hash_table) // 2
            self.rehash(new_length)
    
    def rehash(self, new_length):
        self._is_rehashing = True
        empty_and_deleted = self._hash_table.count(Marker.Deleted) + self._hash_table.count(Marker.Empty)
        if new_length < len(self._hash_table) - empty_and_deleted:
            raise Exception("New length too small to accommodate existing elements")
        
        old_hash_table = self._hash_table
        self._hash_table = [Marker.Empty] * new_length

        for item in old_hash_table:
            if item not in (Marker.Empty, Marker.Deleted):
                self.insert(item)
        
        self._is_rehashing = False
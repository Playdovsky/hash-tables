from collision_avoidance import CollisionAvoidance

class Chaining(CollisionAvoidance):
    def __init__(self, length=10):
        i = 0
        self._hash_table = []
        self.comparisons = 0
        while i < length:
            self._hash_table.append([])
            i += 1

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
        self._hash_table[modulo].append(number)
        return True
        
    def find(self, number):    
        modulo = super().h(number, len(self._hash_table))
        checked_array = self._hash_table[modulo]
        
        for item in checked_array:
            self.comparisons += 1
            if item == number:
                return checked_array
        
        return None

    def delete(self, number):
        checked_array = self.find(number)
        if checked_array is None:
            return False
        
        checked_array.remove(number)
        return True
    
    def rehash(self, new_length):
        i = 0
        while i < new_length:
            self._hash_table.append([])
            i += 1

        for tab in self._hash_table:
            for e in tab:
                self.insert(e)
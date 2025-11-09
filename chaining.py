from collision_avoidance import CollisionAvoidance

class Chaining(CollisionAvoidance):    
    def __init__(self, length=10):
        i = 0
        self._hash_table = []
        while i < length:
            self._hash_table.append([])
            i += 1
        
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
        self._hash_table[modulo].append(number)
        return True
        
    def find(self, number):    
        modulo = super().h(number, len(self._hash_table))
        checked_array = self._hash_table[modulo]
        
        for item in checked_array:
            if item == number:
                return True
        
        return False

    def delete(self, number):
        modulo = super().h(number, len(self._hash_table))
        checked_array = self._hash_table[modulo]
        
        for item in checked_array:
            if item == number:
                checked_array.remove(number)
                return True
        
        return False
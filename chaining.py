from collision_avoidance import CollisionAvoidance

class Chaining(CollisionAvoidance):
    def __init__(self, length=10):
        self.initialize_hash_table(length)
        self.comparisons = 0
        self.total_elements = 0
        self._is_rehashing = False

    def initialize_hash_table(self, length):
        self._hash_table = []
        i = 0
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
        self.total_elements += 1
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
        self.total_elements -= 1
        return True

    def rehash(self, new_length):
        self._is_rehashing = True
        old_hash_table = self._hash_table
        self.initialize_hash_table(new_length)

        for checked_array in old_hash_table:
            for number in checked_array:
                self.insert(number)
        
        self._is_rehashing = False

hash_table = {}

class Chaining:
    def __init__(self):
        self.hash_table_init()
    
    def hash_table_init(self):
        global hash_table
        i = 0
        
        while i < 10:
            hash_table.update({i:[]})
            i += 1

    def hash_operations(self):
        print("What do you want to do?")
        print("1. Display dictionary\n2. Insert new element\n3. Find existing element\n4. Delete element\n5. Exit to menu\n6. Exit")
        option = int(input())
        print()
        
        match option:
            case 1:
                self.display()
            case 2:
                self.insert_new_elem()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                exit()
            case _:
                print("Please select valid option from the list")
                self.hash_operations()

    def display(self):
        for k, v in hash_table.items():
            print(f"{k} | {v}")
        
        self.hash_operations()
    
    def insert_new_elem(self):
        global hash_table
        
        print("Enter number for insertion")
        number = int(input())
        v = hash_table.get(number % len(hash_table))
        v.append(number)
        hash_table.update({number % len(hash_table):v})
        print(f"Number {number} added")
        
        self.hash_operations()
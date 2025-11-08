class Chaining:
    __hash_table = []
    
    def __init__(self):

        if not self.__hash_table:
            self.hash_table_init()
    
    def hash_table_init(self):
        i = 0
        
        while i < 10:
            self.__hash_table.append([])
            i += 1

    def hash_operations(self):
        print("\nCHAINING METHOD")
        print("What do you want to do?")
        print("   1. Display all hash tables\n   2. Insert new element\n   3. Find existing element\n   4. Delete element\n   5. Exit to menu\n   6. Exit\n")
        option = int(input())
        print()
        
        match option:
            case 1:
                self.display()
            case 2:
                self.insert()
            case 3:
                self.find()
            case 4:
                self.delete()
            case 5:
                return
            case 6:
                exit()
            case _:
                print("Please select valid option from the list")
                self.hash_operations()

    def display(self):
        i = 0
        while i < len(self.__hash_table):
            print(f"{i} | {self.__hash_table[i]}")
            i += 1
        
        input("Press any key to continue...\n")
        self.hash_operations()
    
    def insert(self):        
        print("Enter number for insertion")
        number = int(input())
        modulo = number % len(self.__hash_table)
        self.__hash_table[modulo].append(number)
        
        input("Press any key to continue...\n")
        self.hash_operations()
        
    def find(self):        
        print("What number to search for?")
        number = int(input())
        modulo = number % len(self.__hash_table)
        checked_array = self.__hash_table[modulo]
        
        for item in checked_array:
            if item == number:
                print(f"Number has been found under hash table index: {modulo}")
                break
        else:
            print("Number has not been found")
        
        input("Press any key to continue...\n")
        self.hash_operations()
    
    def delete(self):        
        print("What number do you want to delete?")
        number = int(input())
        modulo = number % len(self.__hash_table)
        checked_array = self.__hash_table[modulo]
        
        for item in checked_array:
            if item == number:
                checked_array.remove(number)
                print(f"Number has been deleted from hash table index: {modulo}")
                break
        else:
            print("Number has not been found, therefore can't be deleted")
        
        input("Press any key to continue...\n")
        self.hash_operations()
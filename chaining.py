class Chaining:
    __hash_table = []
    
    def __init__(self):
        try:
            if not self.__hash_table:
                self.hash_table_init()
        except Exception as e:
            print(f"An error occurred during initialization: {e}")
    
    def hash_table_init(self):
        try:
            i = 0
            while i < 10:
                self.__hash_table.append([])
                i += 1
        except Exception as e:
            print(f"An error occurred during hash table initialization: {e}")

    def hash_operations(self):
        try:
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
        
        except ValueError:
            print("Please select valid option from the list")
            self.hash_operations()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.hash_operations()

    def display(self):
        try:
            i = 0
            while i < len(self.__hash_table):
                print(f"{i} | {self.__hash_table[i]}")
                i += 1
            
            input("Press any key to continue...\n")
            self.hash_operations()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.display()
    
    def insert(self):
        try:
            print("Enter number for insertion")
            number = int(input())
            modulo = number % len(self.__hash_table)
            self.__hash_table[modulo].append(number)
            
            input("Press any key to continue...\n")
            self.hash_operations()
        
        except ValueError:
            print("Please enter valid integer number")
            self.insert()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.insert()
        
    def find(self):    
        try:    
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

        except ValueError:
            print("Please enter valid integer number")
            self.find()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.find()

    def delete(self):
        try:
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
        
        except ValueError:
            print("Please enter valid integer number")
            self.delete()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.delete()
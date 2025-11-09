from collision_avoidance import CollisionAvoidance
from marker import Marker

class OpenAddressing(CollisionAvoidance):
    __hash_table = []

    def __init__(self):
        try:
            if not self.__hash_table:
                self.__hash_table = [Marker.Empty] * 10
        except Exception as e:
            print(f"An error occurred during initialization: {e}")
    
    def hash_operations(self):
        try:
            print("\nOPEN ADDRESSING METHOD")
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
            modulo = super().h(number, len(self.__hash_table))
            i = 0

            while i < len(self.__hash_table):
                index = (modulo + i) % len(self.__hash_table)
                if self.__hash_table[index] in (Marker.Empty, Marker.Deleted):
                    self.__hash_table[index] = number
                    print(f"Number inserted at index: {index}")
                    break

                i += 1

            if i == len(self.__hash_table):
                print("Hash table is full, cannot insert new element")
                
            input("Press any key to continue...\n")
            self.hash_operations()

        except ValueError:
            print("Please enter a valid integer")
            self.insert()
        except Exception as e: 
            print(f"An error occurred: {e}")
            self.insert()
    
    def find(self):
        try:
            print("What number to search for?")
            number = int(input())
            modulo = super().h(number, len(self.__hash_table))
            i = 0

            while i < len(self.__hash_table):
                index = (modulo + i) % len(self.__hash_table)
                if self.__hash_table[index] == Marker.Empty:
                    print("Number has not been found")
                    break
                
                if self.__hash_table[index] == number:
                    print(f"Number found at index: {index}")
                    break

                i += 1
            
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
            modulo = super().h(number, len(self.__hash_table))
            i = 0

            while i < len(self.__hash_table):
                index = (modulo + i) % len(self.__hash_table)
                if self.__hash_table[index] == Marker.Empty:
                    print("Number has not been found, therefore can't be deleted")
                    break
                
                if self.__hash_table[index] == number:
                    self.__hash_table[index] = Marker.Deleted
                    print(f"Number deleted from index: {index}")
                    break

                i += 1
            
            input("Press any key to continue...\n")
            self.hash_operations()

        except ValueError:
            print("Please enter valid integer number")
            self.delete()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.delete()
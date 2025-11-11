from chaining import Chaining
from open_addressing import OpenAddressing
from complexity import Complexity

class Start:
    def __init__(self):
        self.menu()

    def menu(self):
        try:
            while True:
                print("\n===== MAIN MENU =====")
                print("Please select type of hash tables")
                print(" 1. Chaining\n 2. Open addressing\n 3. Draw complexity chart\n 4. Exit\n")
                option = int(input())
                
                match option:
                    case 1:
                        print("\n===== CHAINING METHOD =====")
                        self.run_demonstration(Chaining())
                    case 2:
                        print("\n===== OPEN ADDRESSING METHOD =====")
                        self.run_demonstration(OpenAddressing())
                    case 3:
                        length = int(input("Enter hash table length: "))
                        num_trials = int(input("Enter number of search trials: "))
                        Complexity.draw_chart(length, num_trials)
                    case 4:
                        exit()
                    case _:
                        print("Please select valid option from the list\n")
                        self.menu()

        except ValueError:
            print("Please select valid option from the list\n")
            self.menu()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.menu()
    
    def run_demonstration(self, hashing_type):
        try:
            while True:
                print(" 1. Display table\n 2. Insert\n 3. Find\n 4. Delete\n 5. Back to menu\n")
                option = int(input())

                match option:
                    case 1:
                        print(f"\n{hashing_type.display()}")
                    case 2:
                        number = int(input("Enter number to insert: "))
                        if hashing_type.insert(number):
                            print(f"Number {number} has been inserted successfully\n")
                        else:
                            print(f"Duplicate or hash table full. Number {number} could not be inserted\n")
                    case 3:
                        number = int(input("Enter number to find: "))
                        if hashing_type.find(number):
                            print(f"Number {number} found\n")
                        else:
                            print(f"Number {number} not found\n")
                    case 4:
                        number = int(input("Enter number to delete: "))
                        if hashing_type.delete(number):
                            print(f"Number {number} deleted successfully\n")
                        else:
                            print(f"Number {number} not found, therefore cannot be deleted\n")
                    case 5:
                        return
                    case _:
                        print("Please select valid option from the list\n")
                        self.run_demonstration()

        except ValueError:
            print("[ERROR] Please select valid option from the list\n")
            self.run_demonstration()
        except Exception as e:
            print(f"[ERROR] {e}")
            self.run_demonstration()

self_start = Start()
import chaining
import open_addressing

class Start:
    def __init__(self):
        self.menu()

    def menu(self):
        try:
            print("\nMAIN MENU")
            print("Please select type of hash tables")
            print("   1. Chaining\n   2. Open addressing\n   3. Exit\n")
            option = int(input())
            
            match option:
                case 1:
                    chain = chaining.Chaining()
                    chain.hash_operations()
                    self.menu()
                case 2:
                    open_addr = open_addressing.OpenAddressing()
                    open_addr.hash_operations()
                    self.menu()
                case 3:
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

self_start = Start()
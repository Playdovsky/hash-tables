import chaining
import open_addressing

def menu():
    print("\nMAIN MENU")
    print("Please select type of hash tables")
    print("   1. Chaining\n   2. Open addressing\n   3. Exit\n")
    option = int(input())
    
    match option:
        case 1:
            chain = chaining.Chaining()
            chain.hash_operations()
            menu()
        case 2:
            open_addr = open_addressing.OpenAddressing()
            open_addr.hash_operations()
            menu()
        case 3:
            exit()
        case _:
            print("Please select valid option from the list\n")
            menu()

menu()
import chaining

def menu():
    print("Please select type of hash tables")
    print("1. Chaining\n2. Open addressing\n3. Exit")
    option = int(input())
    
    match option:
        case 1:
            chain = chaining.Chaining()
            chain.hash_operations()
            menu()
        case 2:
            pass
        case 3:
            exit()
        case _:
            print("Please select valid option from the list")
            menu()

menu()
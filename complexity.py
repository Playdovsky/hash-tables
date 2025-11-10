import random
import matplotlib.pyplot as plt
from open_addressing import OpenAddressing
from chaining import Chaining
from marker import Marker

class Complexity:
    def calculate(method, length, num_trials):
        X = []
        Y = []
        hash_table = method(length)
        inserted_numbers = set()

        i = 0
        while i < length:
            while True:
                number = random.randint(1, 1000000)
                if number not in inserted_numbers:
                    hash_table.insert(number)
                    inserted_numbers.add(number)
                    X.append(i + 1)
                    break
            
            total_comparisons = 0
            j = 0
            while j < num_trials:
                searched_number = random.randint(1, 1000000)
                hash_table.comparisons = 0
                hash_table.find(searched_number)
                total_comparisons += hash_table.comparisons
                j += 1


            avg_comparisons = total_comparisons / num_trials
            Y.append(avg_comparisons)
            
            i += 1

        return X, Y

    def draw_chart(length, num_trials):
        x1, y1 = Complexity.calculate(OpenAddressing, length, num_trials)
        x2, y2 = Complexity.calculate(Chaining, length, num_trials)
        plt.plot(x1, y1, label="Open Addressing")
        plt.plot(x2, y2, label="Chaining")
        plt.xlabel("Hash Table Length")
        plt.ylabel("Average comparisons")
        plt.title("Hash Table Length against Comparisons")
        plt.legend()
        plt.grid(True)
        plt.show()
        input("Press Enter to return to the menu...")

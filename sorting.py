import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



def selection_sort(values):
    for j in range(len(values)):
        min_index = j
        min_values = values[min_index]
        for i in range(j +1,len(values)):
            if values[i] < min_values:
                min_index = i
                min_values = values[i]

        values[j], values[min_index] = values[min_index],values[j]
    return values



def bubble_sort(values):
    numbers = values.copy()
    n = len(numbers)
    plt.ion()
    plt.show()
    for i in range(n):
        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    plt.ioff()
    plt.show()
    return numbers






if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    selection = selection_sort(values)
    print(selection)
    buble = bubble_sort(values)
    print(buble)

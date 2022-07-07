# Anthony Flores 1792816

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        l = i
        for j in range(i + 1, len(numbers)):
            if numbers[l] < numbers[j]:
                l = j
        numbers[i], numbers[l] = numbers[l], numbers[i]
        for value in numbers:
            print(value,end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = []

    numbers = [int(k) for k in input("").split()]
    selection_sort_descend_trace(numbers)
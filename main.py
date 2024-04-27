def min_n(numbers):
    if not numbers:
        raise ValueError("Список чисел порожній")

    minimum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num

    return minimum

def max_n(numbers):
    if not numbers:
        raise ValueError("Список чисел порожній")

    maximum = numbers[0]

    for num in numbers[1:]:
        if num > maximum:
            maximum = num

    return maximum

numbers_list = [5, 3, 9, 1, 7, 2]
min_value = min_n(numbers_list)
max_value = max_n(numbers_list)

print(f"Мінімальне значення: {min_value}")
print(f"Максимальне значення: {max_value}")

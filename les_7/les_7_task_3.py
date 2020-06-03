# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.


import random


def median_quick_search(arr, middle):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[random.randint(0, len(arr) - 1)]

    left_buffer = [item for item in arr if item < pivot]
    right_buffer = [item for item in arr if item > pivot]
    pivots = [item for item in arr if item == pivot]

    if middle < len(left_buffer):
        return median_quick_search(left_buffer, middle)
    elif middle < len(left_buffer) + len(pivots):
        return pivots[0]
    else:
        return median_quick_search(right_buffer, middle - len(left_buffer) - len(pivots))


M = 5
SIZE = 2 * M + 1
LEFT = 1
RIGHT = 5

array = [random.randint(LEFT, RIGHT) for _ in range(SIZE)]
print(array)

print(f'Медиана - {median_quick_search(array, len(array) / 2)}')
print(sorted(array)[len(array) // 2])

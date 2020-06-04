# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import pdb


def merge_sorting(arr):
    if len(arr) < 2:
        return arr
    left = merge_sorting(arr[:len(arr) // 2])
    right = merge_sorting(arr[len(arr) // 2:])

    i = 0
    j = 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


SIZE = 10
RIGHT = 49
LEFT = 0

array = [random.uniform(LEFT, RIGHT) for _ in range(SIZE)]
print(f'Исходный массив {array}')
print(f'Отсортированный массив {merge_sorting(array)}')

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

pos_max = 0
pos_min = 0
for i in range(len(array)):
    if array[i] > array[pos_max]:
        pos_max = i
    elif array[i] < array[pos_min]:
        pos_min = i
array[pos_max], array[pos_min] = array[pos_min], array[pos_max]

print(f'Массив с поменянными местами максимального и минимального элементов: {array}')

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 2
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

pos_max = 0
pos_min = 0
for i in range(len(array)):
    if array[i] > array[pos_max]:
        pos_max = i
    elif array[i] < array[pos_min]:
        pos_min = i
sum_ = 0

for i in (range(pos_min + 1, pos_max) if pos_min < pos_max else range(pos_max + 1, pos_min)):
    sum_ += array[i]

print(f'Сумма элементов между минимальным и максимальным элементом = {sum_}')

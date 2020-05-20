# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 1000
MIN_ITEM = -10000
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
even_pos = []

for i in enumerate(array):
    if i[1] % 2 == 0:
        even_pos.append(i[0])
print(f'Позиции четных чисел в массиве: {even_pos}')

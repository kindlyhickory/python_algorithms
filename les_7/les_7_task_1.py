# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random


def bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):  # Заменил область прохода функции, чтобы она не смотрела последние элементы,
            # т.к. с каждым циклом максимальный/минимальный элемент вспылывает в конец
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


SIZE = 10
LEFT = -100
RIGHT = 99
array = [random.randint(LEFT, RIGHT) for i in range(SIZE)]

print(bubble(array))

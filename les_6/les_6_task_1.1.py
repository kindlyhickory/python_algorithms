# Выбрал задание 1 с 3-го урока

import sys


def my_show(list_of_objects):
    total_memory = 0
    for object_ in list_of_objects:
        temp = sys.getsizeof(object_)
        if hasattr(object_, '__iter__'):
            if hasattr(object_, 'items'):
                for key, value in object_.items():
                    temp += my_show([key]) + my_show([value])
            elif not isinstance(object_, str):
                for item in object_:
                    temp += my_show([item])
        total_memory += temp
    return total_memory


for i in range(2, 10):
    counter = 0
    for j in range(2, 100):
        if j % i == 0:
            counter += 1
    print(f'{i} - {counter}')

variables = []
for k in dir():
    if not hasattr(locals()[k], '__name__') and k[0] != '_':
        variables.append(locals()[k])
variables.pop()
print(f'Всего памяти использовано: {my_show(variables)}')  # 42

# Операционная система 64-х разрядная. Windows 10.
# PyCharm 2019.2.4 (Community Edition)
# Build #PC-192.7142.42, built on October 31, 2019
# Runtime version: 11.0.4+10-b304.77 amd64
# VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
#
#
# Таким образом видим, что в первом варианте, при минимальном использовании объектов, а именно использовалось только три
# переменных типа int, видим, что затраченная память равна 42, что является самым оптимальным из трёх решений
#
# Во втором варианте, при использовании словаря dict использованная память равна 456, что является максимальным из трёх
# решений, т.к. помимо самих значений количества кратных чисел, мы храним числа, на кратность которым мы проверяли
#
# В третьем варианте затраченная память равна 208 и это средний показатель из трёх решений, т.к. мы храним значения
# количества кратных чисел в списке, который сам по себе ещё занимает память в куче.
#
# Вывод: оптимальнее всего использовать меньшее количество переменных, а так же если не получается обойтись без
# коллекций, то стараться использовать те виды коллекций, которые сами по себе занимают меньшее количество памяти.

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите целое число: '))
element = 1
dig_sum = 1
for i in range(1, n):
    if i % 2 == 0:
        dig_sum += element / 2
        element = element / 2
    else:
        dig_sum -= element / 2
        element = element / 2
print(dig_sum)

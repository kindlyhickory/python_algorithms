# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

dig_sum = 0
n = int(input('Введите натуральное число: '))
for i in range(1, n + 1):
    dig_sum += i

if dig_sum == n * (n + 1) / 2:
    print('Равнество выполняется')
else:
    print('Равентсво не выполняется')

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

maximum = 0
digit = 0
max_dig_number = 0
while True:
    dig_sum = 0
    number = int(input('Введите число: '))
    if number <= 0:
        break
    else:
        n = number
        for i in range(len(str(number))):
            digit = n % 10
            n = n // 10
            dig_sum += digit
        if dig_sum > maximum:
            maximum = dig_sum
            max_dig_number = number
print(f'Максимальная сумма цифр {maximum} у числа {max_dig_number}')

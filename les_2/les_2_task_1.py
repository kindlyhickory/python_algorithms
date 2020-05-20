# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1qNZ1Pl6-LFag8aX5utdpjH4duS-8HDNf/view?usp=sharing

def even_odd(n):
    global count_even, count_odd
    n = str(n)
    if len(n) == 1:
        if int(n) % 2 == 0:
            return f'Количество четных цифр = {count_even + 1}, количество нечетных цифр = {count_odd}'
        else:
            return f'Количество четных цифр = {count_even}, количество нечетных цифр = {count_odd + 1}'
    else:
        a = int(n) // 10
        b = int(n) % 10
        if b % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return even_odd(a)


count_even = 0
count_odd = 0
digit = input('Введите натуральное число: ')
count = even_odd(digit)
print(count)

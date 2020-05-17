# https://drive.google.com/file/d/1P7nnAu6HCzQN0a66funglZXK5mh1d78k/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число: '))

b = a // 100
c = (a // 10) % 10
d = a % 10

dig_sum = b + c + d
dig_product = b * c * d

print(f'Сумма цифр: {dig_sum}, произведение цифр: {dig_product}')

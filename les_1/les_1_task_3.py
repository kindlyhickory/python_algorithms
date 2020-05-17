# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Введите две буквы латинского алфавита')
letter_1 = str(input('Первая буква: '))
letter_2 = str(input('Вторая буква: '))

count = abs(ord(letter_2) - ord(letter_1)) - 1
position_1 = ord(letter_1) - 96
position_2 = ord(letter_2) - 96

print(f'Позиция символа "{letter_1}": {position_1}\n'
      f'Позиция символа "{letter_2}": {position_2}\n'
      f'Количество символов между: {count}')
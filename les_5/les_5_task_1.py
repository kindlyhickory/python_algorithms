# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

QUARTERS = 4
total_companies = int(input('Введите количество предприятий: '))
info = defaultdict(list)
average = 0
for i in range(total_companies):
    name = input('Введите название предприятия: ')
    for j in range(QUARTERS):
        info[name].append(int(input(f'Введите количество прибыли за {j + 1}-й квартал: ')))
    info[name] = sum(info[name])
    average += info[name]
average = average / total_companies

statistic = defaultdict(list)
for name in info:
    if info[name] > average:
        statistic['Прибыльные предприятия'].append(name)
    elif info[name] < average:
        statistic['Убыточные предприятия'].append(name)
    else:
        statistic['Прибыль равна средней'].append(name)
print(statistic)

# for name in info:
#         info[name] = 'Прибыльное'
#     elif info[name] < average:
#         info[name] = 'Убыточное'
#     else:
#         info[name] = 'Средняя'
# print(info)

# Этот вариант, если не создавать новый объект statistic, но вывод будет меннее приятный на глаз

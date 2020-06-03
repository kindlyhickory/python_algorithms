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


info = {}
for i in range(2, 10):
    info[i] = 0
    for j in range(2, 100):
        if j % i == 0:
            info[i] += 1
print(info)

variables = []
for k in dir():
    if not hasattr(locals()[k], '__name__') and k[0] != '_':
        variables.append(locals()[k])
variables.pop()
print(f'Всего памяти использовано: {my_show(variables)}')  # 456

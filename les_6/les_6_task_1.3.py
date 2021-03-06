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


array = [0 for _ in range(8)]
for i in range(2, 10):
    for j in range(2, 100):
        if j % i == 0:
            array[i - 2] += 1
    print(f'{i} - {array[i-2]} ')

variables = []
for k in dir():
    if not hasattr(locals()[k], '__name__') and k[0] != '_':
        variables.append(locals()[k])
variables.pop()
print(f'Всего памяти использовано: {my_show(variables)}')

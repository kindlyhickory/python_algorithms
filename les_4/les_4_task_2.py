import math
import timeit
import cProfile


def sieve_eratosthenes(n):
    limit = 2
    count = 0
    while count <= n:
        count = limit / math.log(limit)
        limit += 1
    sieve = [i for i in range(limit)]
    sieve[1] = 0

    if n > 2:
        for i in range(0, limit):
            if sieve[i] != 0:
                j = i + i
                while j < limit:
                    sieve[j] = 0
                    j += i
        res = [i for i in sieve if i != 0]
        return f'{n}-е по счёту простое число = {res[n - 1]}'
    elif n == 2:
        return f'{n}-е по счёту простое число - {3}'
    elif n == 1:
        return f'{n}-е по счёту простое число - {2}'


print(timeit.timeit('sieve_eratosthenes(40)', number=1000, globals=globals()))  # 0.1877059
print(timeit.timeit('sieve_eratosthenes(80)', number=1000, globals=globals()))  # 0.4685319
print(timeit.timeit('sieve_eratosthenes(160)', number=1000, globals=globals()))  # 1.0832893000000001
print(timeit.timeit('sieve_eratosthenes(320)', number=1000, globals=globals()))  # 2.4366521
print(timeit.timeit('sieve_eratosthenes(640)', number=1000, globals=globals()))  # 5.507454499999999

cProfile.run('sieve_eratosthenes(40)')
#   1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:12(<listcomp>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:6(sieve_eratosthenes)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 214    0.000    0.000    0.000    0.000 {built-in method math.log}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_eratosthenes(80)')
#   1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:12(<listcomp>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
#   1    0.000    0.000    0.001    0.001 les_4_task_2.py:6(sieve_eratosthenes)
#   1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 496    0.000    0.000    0.000    0.000 {built-in method math.log}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_eratosthenes(160)')
#    1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:12(<listcomp>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
#    1    0.001    0.001    0.001    0.001 les_4_task_2.py:6(sieve_eratosthenes)
#    1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 1123    0.000    0.000    0.000    0.000 {built-in method math.log}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_eratosthenes(320)')
#    1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:12(<listcomp>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
#    1    0.002    0.002    0.003    0.003 les_4_task_2.py:6(sieve_eratosthenes)
#    1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
# 2504    0.001    0.000    0.001    0.000 {built-in method math.log}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve_eratosthenes(640)')
#    1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:12(<listcomp>)
#    1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
#    1    0.005    0.005    0.007    0.007 les_4_task_2.py:6(sieve_eratosthenes)
#    1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
# 5513    0.001    0.000    0.001    0.000 {built-in method math.log}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(sieve_eratosthenes(168))


def prime(n):
    limit = 2
    count = 0
    while count <= n:
        count = limit / math.log(limit)
        limit += 1
    array = [2]
    for i in range(2, limit + 1):
        for j in array:
            if i % j == 0:
                break
        else:
            array.append(i)
    return f'{n}-е по счёту простое число - {array[n - 1]}'


print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.0322773
print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 0.0886716
print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 0.24382
print(timeit.timeit('prime(80)', number=1000, globals=globals()))  # 0.7058994999999999
print(timeit.timeit('prime(160)', number=1000, globals=globals()))  # 2.2777342

cProfile.run('prime(10)')
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:80(prime)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 35    0.000    0.000    0.000    0.000 {built-in method math.log}
# 11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(20)')
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:80(prime)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 89    0.000    0.000    0.000    0.000 {built-in method math.log}
# 23    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(40)')
#   1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   1    0.000    0.000    0.000    0.000 les_4_task_2.py:80(prime)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 214    0.000    0.000    0.000    0.000 {built-in method math.log}
#  46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(80)')
#   1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   1    0.001    0.001    0.001    0.001 les_4_task_2.py:80(prime)
#   1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 496    0.000    0.000    0.000    0.000 {built-in method math.log}
#  93    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(160)')
#    1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#    1    0.002    0.002    0.002    0.002 les_4_task_2.py:80(prime)
#    1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
# 1123    0.000    0.000    0.000    0.000 {built-in method math.log}
#  187    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Можно сделать вывод, что решето Эратосфена ищет быстрее, чем примитивный перебор чисел и поиск их делителей,
# т.к. сложность алогритма Эратосфена будет около логарифмической, и, возможно, быстрее, т.к. алгоритм изначально
# убирает из количества элементов, которые нужно просмотреть половину элементов, а сложность перебора - O(n^2),
# что является медленной по сравнению с лографимической

# Выбрал 4-ю задачу из второго урока

import timeit
import cProfile


# 1 вариант
def devil(n):
    element = 1
    dig_sum = 1
    for i in range(1, n):
        if i % 2 == 0:
            dig_sum += element / 2
            element = element / 2
        else:
            dig_sum -= element / 2
            element = element / 2
    return dig_sum


print(timeit.timeit('devil(10)', number=1000, globals=globals()))  # 0.0031597999999999973
print(timeit.timeit('devil(20)', number=1000, globals=globals()))  # 0.006360299999999999
print(timeit.timeit('devil(40)', number=1000, globals=globals()))  # 0.011622899999999999
print(timeit.timeit('devil(80)', number=1000, globals=globals()))  # 0.025075900000000005
print(timeit.timeit('devil(160)', number=1000, globals=globals()))  # 0.046624
print(timeit.timeit('devil(320)', number=1000, globals=globals()))  # 0.0909713

cProfile.run('devil(10)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil(20)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil(40)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil(80)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil(160)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil(320)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(devil)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('=' * 50)


# вариант 2
def devil_2(n):
    sum_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return sum_2


print(timeit.timeit('devil_2(10)', number=1000, globals=globals()))  # 0.0005941999999999892
print(timeit.timeit('devil_2(20)', number=1000, globals=globals()))  # 0.0005739000000000022
print(timeit.timeit('devil_2(40)', number=1000, globals=globals()))  # 0.0005751999999999979
print(timeit.timeit('devil_2(80)', number=1000, globals=globals()))  # 0.0005687999999999943
print(timeit.timeit('devil_2(160)', number=1000, globals=globals()))  # 0.0005427000000000071
print(timeit.timeit('devil_2(320)', number=1000, globals=globals()))  # 0.0005773999999999779

cProfile.run('devil_2(10)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_2(20)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_2(40)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_2(80)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_2(160)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_2(320)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:39(devil_2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('=' * 50)


# вариант 3
def devil_3(n):
    global sum_
    if n == 1:
        return sum_ + 1
    if n % 2 == 0:
        sum_ -= 1 / pow(2, n - 1)
    else:
        sum_ += 1 / pow(2, n - 1)
    n -= 1
    return devil_3(n)


sum_ = 0
sum_n = devil_2(40)

print(timeit.timeit('devil_3(10)', number=1000, globals=globals()))  # 0.0082087
print(timeit.timeit('devil_3(20)', number=1000, globals=globals()))  # 0.01817590000000001
print(timeit.timeit('devil_3(40)', number=1000, globals=globals()))  # 0.03767630000000001
print(timeit.timeit('devil_3(80)', number=1000, globals=globals()))  # 0.08734950000000002
print(timeit.timeit('devil_3(160)', number=1000, globals=globals()))  # 0.20980160000000003
print(timeit.timeit('devil_3(320)', number=1000, globals=globals()))  # 0.5081296000000001
print(timeit.timeit('devil_3(640)', number=1000, globals=globals()))  # 1.3090024999999998

cProfile.run('devil_3(10)')
#    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(devil_3)
#    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    9    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_3(20)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      20/1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(devil_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        19    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_3(40)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      40/1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(devil_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        39    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_3(80)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      80/1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(devil_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        79    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_3(160)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     160/1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(devil_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       159    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('devil_3(320)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     320/1    0.000    0.000    0.001    0.001 les_4_task_1.py:61(devil_3)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       319    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Замеры проводил для N = 10, 20, 40, 80, 160, 320, 640
# В первом варианте зависимость линейная, т.к. при увеличении N в два раза, время так же увеличивается в два раза
# Во втором варианте зависимость O(const), т.к. используется формула и соответсвенно время одинаково при разных N
# В третьем решил задачу через и рекурсию и видно, что зависимость не линейная и не квадратичная. Как вы сказали на
# уроке  -  в рекурсии зависимость O(n!)
# Таким образом самый оптимальный вариант через формулу, т.к. даже при больших значениях N время будет таким
# же, как и при малых значениях

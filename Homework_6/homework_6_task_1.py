# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.


from memory_profiler import profile


@profile
def primary_with_sieve(indx):
    max_n = 1000000
    n = 100
    primary_num_index = 1
    a = []
    for i in range(n + 1):
        a.append(i)
    primary_set = set()
    a[1] = 0
    while True:
        i = 2
        while i <= n:
            if a[i] != 0:
                if indx == primary_num_index:
                    return a[i]
                else:
                    if a[i] not in primary_set:
                        primary_num_index += 1
                        primary_set.add(a[i])
                j = i + i
                while j <= n:
                    a[j] = 0
                    j = j + i
            i += 1
        for i in range(n + 1, n + 101):
            a.append(i)
        n += 100
        if n > max_n:
            break
    return 0


@profile
def primary_without_sieve(indx):
    prim_indx = 1
    stop_c = 0
    number_in_step = 2
    while True:
        if stop_c == 1000000:
            return 0
        stop_c += 1
        is_primary = True
        for i in range(2, number_in_step):
            if number_in_step % i == 0:
                is_primary = False
        if is_primary and prim_indx == indx:
            return number_in_step
        elif is_primary:
            prim_indx += 1
            number_in_step += 1
        else:
            number_in_step += 1


primary_with_sieve(100)
primary_without_sieve(100)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10     17.1 MiB     17.1 MiB   @profile
#     11                             def primary_with_sieve(indx):
#     12     17.1 MiB      0.0 MiB       max_n = 1000000
#     13     17.1 MiB      0.0 MiB       n = 100
#     14     17.1 MiB      0.0 MiB       primary_num_index = 1
#     15     17.1 MiB      0.0 MiB       a = []
#     16     17.1 MiB      0.0 MiB       for i in range(n + 1):
#     17     17.1 MiB      0.0 MiB           a.append(i)
#     18     17.1 MiB      0.0 MiB       primary_set = set()
#     19     17.1 MiB      0.0 MiB       a[1] = 0
#     20     17.1 MiB      0.0 MiB       while True:
#     21     17.2 MiB      0.0 MiB           i = 2
#     22     17.2 MiB      0.0 MiB           while i <= n:
#     23     17.2 MiB      0.0 MiB               if a[i] != 0:
#     24     17.2 MiB      0.0 MiB                   if indx == primary_num_index:
#     25     17.2 MiB      0.0 MiB                       return a[i]
#     26                                             else:
#     27     17.2 MiB      0.0 MiB                       if a[i] not in primary_set:
#     28     17.2 MiB      0.0 MiB                           primary_num_index += 1
#     29     17.2 MiB      0.0 MiB                           primary_set.add(a[i])
#     30     17.2 MiB      0.0 MiB                   j = i + i
#     31     17.2 MiB      0.0 MiB                   while j <= n:
#     32     17.2 MiB      0.0 MiB                       a[j] = 0
#     33     17.2 MiB      0.0 MiB                       j = j + i
#     34     17.2 MiB      0.0 MiB               i += 1
#     35     17.2 MiB      0.0 MiB           for i in range(n + 1, n + 101):
#     36     17.2 MiB      0.0 MiB               a.append(i)
#     37     17.2 MiB      0.0 MiB           n += 100
#     38     17.2 MiB      0.0 MiB           if n > max_n:
#     39                                         break
#     40                                 return 0
#
#
# Filename: C:/Users/shoku/PycharmProjects/algorithms/Homework_6/homework_6_task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     43     17.2 MiB     17.2 MiB   @profile
#     44                             def primary_without_sieve(indx):
#     45     17.2 MiB      0.0 MiB       prim_indx = 1
#     46     17.2 MiB      0.0 MiB       stop_c = 0
#     47     17.2 MiB      0.0 MiB       number_in_step = 2
#     48     17.2 MiB      0.0 MiB       while True:
#     49     17.2 MiB      0.0 MiB           if stop_c == 1000000:
#     50                                         return 0
#     51     17.2 MiB      0.0 MiB           stop_c += 1
#     52     17.2 MiB      0.0 MiB           is_primary = True
#     53     17.2 MiB      0.0 MiB           for i in range(2, number_in_step):
#     54     17.2 MiB      0.0 MiB               if number_in_step % i == 0:
#     55     17.2 MiB      0.0 MiB                   is_primary = False
#     56     17.2 MiB      0.0 MiB           if is_primary and prim_indx == indx:
#     57     17.2 MiB      0.0 MiB               return number_in_step
#     58     17.2 MiB      0.0 MiB           elif is_primary:
#     59     17.2 MiB      0.0 MiB               prim_indx += 1
#     60     17.2 MiB      0.0 MiB               number_in_step += 1
#     61                                     else:
#     62     17.2 MiB      0.0 MiB               number_in_step += 1
#
# В соответствии с полученными данными, решето Эратосфена использует меньше памяти, чем алгоритм без использования
# решета. Однако на выполнение решета ушло ощутимо больше времени.
# Windows 10 x64, python 3.6
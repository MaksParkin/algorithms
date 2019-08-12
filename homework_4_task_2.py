# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


import timeit


indx = 30


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


print(primary_without_sieve(indx))

print(timeit.timeit("primary_without_sieve(indx)", setup="from __main__ import primary_without_sieve; indx=50", number=100))
print(timeit.timeit("primary_without_sieve;(indx)", setup="from __main__ import primary_without_sieve; indx=200", number=100))


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


print(primary_with_sieve(indx - 1))
print(timeit.timeit("primary_with_sieve(indx)", setup="from __main__ import primary_with_sieve; indx=50", number=100))
print(timeit.timeit("primary_with_sieve(indx)", setup="from __main__ import primary_with_sieve; indx=200", number=100))


#  -------------------------------------------------|-------------------------------------------------
# |Без алгоритма Эратосфена (primary_without_sieve) | С алгоритмом Эратосфена (primary_with_sieve)    |
# |-------------------------------------------------|-------------------------------------------------|
# |                   0.1198478                     |                   0.0157056                     |
# |-------------------------------------------------|-------------------------------------------------|
# |                   1.799999999996249             |                   0.2819844                     |
#  -------------------------------------------------|-------------------------------------------------
from random import random

# 4. Определить, какое число в массиве встречается чаще всего.


elem_num = 15
array = [0] * elem_num
for i in range(elem_num):
    array[i] = int(random() * 20)
print(array)

num = array[0]
max_freq = 1
for i in range(elem_num - 1):
    freq = 1
    for k in range(i + 1, elem_num):
        if array[i] == array[k]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = array[i]

if max_freq > 1:
    print(f"{max_freq} раз(а) встречается число {num}")
else:
    print("Все элементы уникальны")

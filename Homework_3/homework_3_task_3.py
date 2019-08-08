from random import random

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


elem_num = 15
array = [0] * elem_num
for i in range(elem_num):
    array[i] = int(random() * 100)
    print(array[i], end=' ')
print()

min_num = min(array)
max_num = max(array)
min_id = array.index(min_num)
max_id = array.index(max_num)
print(f"Минимальный элемент: [{min_id+1}] = {min_num}\nМаксимальный элемент: [{max_id+1}] = {max_num}")

for i in range(15):
    print(array[i], end=" ")
print()
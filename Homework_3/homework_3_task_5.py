from random import random



elem_num = 15
array = []
for i in range(elem_num):
    array.append(int(random() * 100) - 50)
print(array)

i = 0
index = -1
while i < elem_num:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

print(f"Максимальный отрицательный элемент: {array[index]}\nМесто элемента в массиве: {index + 1}")

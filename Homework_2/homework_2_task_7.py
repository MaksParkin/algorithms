# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# # 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


n = int(input("Введите переменную для проверки:"))
a = 0

for i in range(1, n+1):
    a += i
m = n * (n + 1) // 2
print(a)
print(m)

if a == m:
    print("Значения равны. Ч.т.д.!")
else:
    print("Значения не равны.")
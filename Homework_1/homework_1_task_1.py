#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


a = int(input("Введите трехзначное число: "))

b1 = a % 10
b2 = a % 100 // 10
b3 = a // 100

print(f'Сумма цифр числа {a}:', b1 + b2 + b3)
print(f'Произведение цифр числа {a}:', b1 * b2 * b3)
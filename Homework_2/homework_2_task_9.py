# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


n_num = int(input("Какое количество чисел будет?"))
max_sum = 0
max_sum_num = 0

while n_num != 0:
    n = n_num
    sum = 0
    while n_num > 0:
        sum += n_num % 10
        n_num //= 10
        if sum > max_sum:
            max_sum = sum
            max_sum_num = n
        n_num = int(input("Введите число:"))

print(f"Число {max_sum_num}, имеет максимальную сумму цифр:, {max_sum}")
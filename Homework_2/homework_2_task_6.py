import random

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# # После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# # Если за 10 попыток число не отгадано, то вывести загаданное число.


secret_num = random.randint(0, 101)
attempt = 1
print("Отгадайте число от 0 до 100")

while attempt <= 10:
    user_num = int(input(f"Введите число.\nПопытка {str(attempt)}."))
    if user_num > secret_num and 0 < user_num < 100:
        print(f"Введенное число больше загаданного.\nОсталось попыток: {10 - attempt}.")
    elif user_num < secret_num and 0 < user_num < 100:
        print(f"Введенное число меньше загаданного.\nОсталось попыток: {10 - attempt}.")
    elif user_num == secret_num:
        print("Вы угадали!")
        break
    elif 100 < user_num or user_num < 0:
        print("Ошибка ввода. Введите число от 0 до 100")
    attempt += 1
else:
    print(f"Вы использовали {str(attempt - 1)} попыток. Загаданное число- {str(secret_num)} ")
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


a = ord(input('Начальная буква: '))
b = ord(input('Конечная буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'Позиции: {a} и {b}')
print('Расстояние между буквами:', abs(a - b) - 1)

c = int(input('Позиция буквы в алфавите: '))
c = ord('a') + c - 1
print('Это буква', chr(c))
# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


input_str = input("Введите строку: ")

print(f"Строка '{input_str}' имеет длину {len(input_str)} символов.")

result = {}
for i in range(len(input_str)):
    for j in range(len(input_str)-1 if i == 0 else len(input_str), i, -1):
        result[input_str[i:j]] = hash(input_str[i:j])

print(f"Количество подстрок: {len(result)}")

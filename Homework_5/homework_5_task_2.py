# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


class HexOperation:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]


first_hex_num = list(input("Первое шеснадцатиричное число: "))
second_hex_num = list(input("Второе шеснадцатиричное число: "))

sum_result = HexOperation(first_hex_num, second_hex_num) + HexOperation(first_hex_num, second_hex_num)
mul_result = HexOperation(first_hex_num, second_hex_num) * HexOperation(first_hex_num, second_hex_num)
print(f"Сумма чисел = {sum_result}\nПроизведение чисел = {mul_result}")

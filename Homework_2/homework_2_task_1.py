# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


print("НАжмите 0 для  завершения программы")
while True:
        a = input("Знак (+,-,*,/): ")
        if a == '0': break
        if a in ('+','-','*','/'):
                x = float(input("x="))
                y = float(input("y="))
                if a == '+':
                        print(x+y)
                elif a == '-':
                        print(x-y)
                elif a == '*':
                        print(x*y)
                elif a == '/':
                        if y != 0:
                                print(x/y)
                        else:
                                print("Деление на ноль невозможно.")
        else:
                print("Введенный символ не является символом операции.")
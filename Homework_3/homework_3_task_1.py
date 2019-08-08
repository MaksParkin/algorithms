# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


mult_range = [0] * 8
for i in range(2, 100):
    for k in range(2, 10):
        if i % k == 0:
            mult_range[k - 2] += 1
i = 0

while i < len(mult_range):
    print(f"{i + 2}  -  {mult_range[i]}")
    i += 1

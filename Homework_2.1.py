# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

float_num = float(input(f'Введите число: '))
res = 0
if float_num < 0:
    float_num *= -1
float_str = str(float_num)
for i in float_str:
    if i != '.':
        res += int(i)
print(res)


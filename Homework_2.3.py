# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

a =  int(input('Введите число: '))
count = 0
sum_n = 1
print('{', end='')

while count < a:
    count += 1
    sum_n = sum_n + 3
    if count == a:
        print(f'{count}: {sum_n}', end='')
        print('}', end='')
    else:
        print(f'{count}: {sum_n}, ', end='')



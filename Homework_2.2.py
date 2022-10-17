# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


from itertools import product


n = int(input(f'Vvedite chislo N: '))
product_numbers = 1
result_product_numbers = []

for i in range(1, n+1):
    product_numbers *= i
    result_product_numbers.append(product_numbers)
print(f'N = {n} -> {result_product_numbers}')
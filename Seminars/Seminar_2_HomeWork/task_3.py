#  Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

#  Пример:

#  - Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }

digit = int(input('Введите число n: '))
result = {}

for i in range(1, digit + 1):
    result[i] = (1 + 1 / i) ** i
        
print(result)
print(f'{sum(result.values()):.2f}')
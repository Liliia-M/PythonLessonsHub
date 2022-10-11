# Задача 11.
# Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# решения с помощью функции

N = (int(input('Введите целое число N: ')))

def sequence(n):
    for i in range(n):
        print((-3) ** i, end = ' ')

sequence(N)        

# решение через список с помощью функции

N = (int(input('Введите целое число N: ')))

def sequence(n):
    result = []
    for i in range(n):
        result.append((-3) ** i)
    return result

r = sequence(N)  
print(r)




















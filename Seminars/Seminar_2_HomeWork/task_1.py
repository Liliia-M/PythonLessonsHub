#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#  Пример:

#  - 6782 -> 23
#  - 0,56 -> 11

number = float(input('Введите вещественное число: '))

sum = 0

if (number * 10) % 10 == 0: 
    
    while not number % 10 == 0:
        rest = number % 10 
        sum = sum + rest
        number = number // 10
        if number == 10: 
            number = 1
    sum = sum + number
    print(int(sum))

else:
    while (number * 10) % 10 != 0:
        number = number * 10
        
    while not number % 10 == 0:
        rest = number % 10 
        sum = sum + rest
        number = number // 10
        if number == 10: 
            number = 1
    sum = sum + number
    print(int(sum))



# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти от 1 до 4: ')
x = int(input())

if x == 1:
    print('x > 0, y > 0')
if x == 2:
    print('x < 0, y > 0')
if x == 3:
    print('x < 0, y < 0')
if x == 4:
    print('x > 0, y < 0')
if x < 1 or x > 4: 
    print('Повторите попытку и введите корректный номер четверти от 1 до 4')    
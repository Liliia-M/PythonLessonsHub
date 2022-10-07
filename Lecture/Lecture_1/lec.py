# #print('Hello world')

# # типы данных и переменная
# # int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# value = 12345
# print(value)
# print(type(value))

# # 123
# # <class 'int'>
# # 1.23
# # <class 'float'>
# # 12345
# # <class 'int'>

# # строки
# s = 'hello world'
# print(s)

# # s = "hello 'world"
# # print(s)

# # s = 'hello "world'
# # print(s)

# # s = 'hello \'world'
# # print(s)

# # s = 'hello \nworld' # \n - переход на новую строку
# # print(s)

# print(a, b, s)

# print(a, '-',b, '-',s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s)) # меняем порядок вывода 
# print(f'{a} - {b} - {s}') # интерполяция

# f = True
# print(f)

# f = False
# print(f)

# Списки

# list = []
# print(list)

# list = [1, 2, 3]
# print(list)

# list = ['1', '2', '3', 'hello world', 1, 2, 4.5, True] # динамическая типизация - но! так делать не надо
# print(list)

# # в языке Python нужно быть внимательными с пробелами - поставленные не там могут поломать код

# Ввод и вывод данных
# print, input

# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print(a, '+', b, '=', a + b)

# Введите a
# 10
# Введите b
# 10
# # 10 + 10 = 1010

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+', b, '=', a + b)

# Введите a
# 10
# Введите b
# 20
# 10 + 20 = 30

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+', b, '=', a + b)

# Введите a
# 1.23
# Введите b
# 2.35
# 1.23 + 2.35 = 3.58

# / - деление вещественных чисел, // - деление целых чисел, ** - возведение в степень

# a = 1.3
# b = 3
# c = a * b
# print(c)

# 3.9000000000000004

# a = 1.3123
# b = 3
# c = round(a * b, 5)
# print(c)

# 3.9369

# Сокращенные операции присваивания

# a = 3
# a = a + 5 # можнр записать короче:
# a+=5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать c &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# print(a)

# True

# a = [1,2]
# b = [1,2]
# print(a == b)

# True

# a = 1 < 3 < 5 < 10
# print(a)

# True


# func = 1
# T = 4
# x = 123

# print(func<T>(x))

# False

# f = 1 > 2 or 4 < 6
# print(f)

# True


# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# [1, 2, 3, 4]
# False
# False

# Управляющие конструкции: if, else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)    

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)
# 32

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит')    
# print(inverted)

# 2
# 0
# Пожалуй
# хватит
# 32

# Управляющие конструкции: for

# for i in 1,2,3,4,5:
#     print(i**2)

# 1
# 4
# 9
# 16
# 25    

# list = [1,2,3,10,4,5]
# for i in list:
#     print(i)

# 1
# 2
# 3
# 10
# 4
# 5

# r = range(10)
# for i in r:
#     print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9    

# for i in range(5):
#     print(i)

# 0
# 1
# 2
# 3
# 4    

# for i in range(1, 10, 2):
#     print(i)

# 1
# 3
# 5
# 7
# 9   
 

# for i in 'qwe - rty':
#     print(i) 

# q
# w
# e

# -

# r
# t
# y

# Немного о строках 

# Списки

# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran) # приведение типа рендж к типу лист
# print(type(numbers))

# <class 'range'>
# <class 'list'>
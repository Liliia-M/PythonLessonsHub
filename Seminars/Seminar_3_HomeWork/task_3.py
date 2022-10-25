# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dif_max_min_fractional_part(lst):
    result = 0
    max_fractional_part = float((lst[0] * 100) % 100)
    min_fractional_part = float((lst[0] * 100) % 100)
    fractional_part = 0
    for i in range(len(lst)):
        fractional_part = float((lst[i] * 100) % 100)
        if max_fractional_part < fractional_part:
            max_fractional_part = fractional_part
            
        if min_fractional_part > fractional_part:
            min_fractional_part = fractional_part
            
        result = float(max_fractional_part - min_fractional_part)
    print(max_fractional_part)   
    print(min_fractional_part)
    return result / 100   

list1 = [1.1, 1.2, 3.1, 10.01]
print(dif_max_min_fractional_part(list1))
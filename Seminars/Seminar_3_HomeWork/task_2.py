# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_pairs_digit(lst):
    pairs = []
    multiply_digit = 0
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
            multiply_digit = lst[i] * lst[len(lst) - 1 - i]
            pairs.append(multiply_digit)
    else:
        for i in range(len(lst)//2 + 1):
            multiply_digit = lst[i] * lst[len(lst) - 1 - i]        
            pairs.append(multiply_digit)
    return pairs

list1 = [2, 3, 5, 6]
print(list1)
print(f'Произведение пар чисел списка: {multiply_pairs_digit(list1)}')


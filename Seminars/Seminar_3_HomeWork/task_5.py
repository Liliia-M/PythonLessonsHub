# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

print('Введите k ');
k = int(input())

def generate_list(digit):
    result = []
    for i in range(-digit, digit+1):
        result.append(i)
    return result


def fibonacci_list(lst_1):
    
    for i in range(len(lst_1)):
        lst_1[len(lst_1) // 2] = 0
        lst_1[len(lst_1) // 2 + 1] = 1
        lst_1[len(lst_1) // 2 + 2] = 1
        if i > len(lst_1) // 2:
            lst_1[i] = lst_1[i-1] + lst_1[i-2]
    for i in range(len(lst_1)):
        lst_1[0] = - lst_1[-1]
        lst_1[1] = lst_1[-2]
        #lst_1[len(lst_1) // 2 + 2] = 1
        if i < len(lst_1) // 2:
            lst_1[i] = lst_1[i-1] + lst_1[i-2]
    
    print(lst_1)


lst = generate_list(k)

fibonacci_list(lst)

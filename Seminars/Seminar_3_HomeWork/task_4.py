# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10



def convert_decimal_to_binary(number):
    rest = 0
    result = 0
    i = 0
    while number > 0:
        rest = number % 2
        result += rest * (10 ** i)
        number = number // 2
        i += 1
    return result

decimal_number = int(input("Введите двоичное число: "))
print(convert_decimal_to_binary(decimal_number))    
        

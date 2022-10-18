# Задача 20
# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Пример:
# ["qwe", "asd", "12", "qwe", "2"], 2 -> True
# ["qwe", "asd", "qwe", "681"], 7 -> False
# ["qwe", "asd", "qwe", "0"], 0 -> True

# def find_num(number, my_list):
#     result = False
#     for i in my_list:
#         if i == number:
#             result = True
#     return result


# print(find_num('2', ['bag', 'car', 'phone', 'table', '2']))


# def find_num(number, my_list):
#     for item in my_list:
#         if number in item:
#             return True
#     return False


# print(find_num('car', ['bag', 'car', 'phone', 'table', '2']))



# "2" in "".join(['bag', 'car', 'phone', 'table', '2'])

def is_num_present (l, n):
    if str(n) in l:
        return True

    return False

print(is_num_present(["kjhkj", "kjshd", "3"], 2))

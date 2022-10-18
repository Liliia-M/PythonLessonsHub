# Задача 21
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# def find_num(number, my_list):
#     #result = 
#     for i in my_list:
#         if i == number:
#             del i
#     #return result


# print(find_num("qwe", ["qwe", "asd", "zxc", "qwe", "ertqwe"]))

def is_index(lst, t):
    count = -1
    for i in range(0, len(lst)):
        if lst[i] in t:
            count = i
            count += 1
            if count == 2:
                return i
    return count



my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
text = "йцу"
print(is_index(my_list, text))

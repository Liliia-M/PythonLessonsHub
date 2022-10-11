# Задача 13
# Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять 
# количество вхождений одной строки в другой.
# Пример:
# "hello or world", "or" -> 2

# text = "hello or world"
# find = "or"

# count = 0
# for i in range(len(text)):
#     if text[i:i + len(find)] == find:
#         count += 1

# print(f'"{text}", "{find}" -> {count}')

def count_substr(text, find):
    count = 0
    for i in range(len(text)):
        if text[i:i + len(find)] == find:
            count += 1
    return count


# assert count_substr("hello or world", "or") == 2


data_table = [
    ["hello or world", "or", 2],
    #["aaaaaaaa", "aa", 5],
    ["abababa", "aba", 3]
]

for txt, sub_str, expected in data_table:
    assert count_substr(txt, sub_str) == expected
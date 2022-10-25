# Задача 38.
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
 

# test_data = [
#     [["привет абв как абвышные дела?", "абв"], "привет как дела?"]
# ]
# for args, exp in test_data:
#     assert remove_substr(*args) == exp
#     #assert remove_substr_func(*args) == exp


test_data = "привет абв как абвышные дела?"
remove_set = "абв"

# test_list = test_data.split()
# res_data = []
# for i in test_list:
#     if remove_set not in i:
#         res_data.append(i)

# print(' '.join(res_data))

test_list = test_data.split()

print(" ". join(filter(lambda word: "абв" not in word, test_list)))

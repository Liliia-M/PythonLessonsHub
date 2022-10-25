# Задача 36.
# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]


# test_data = [
#     [[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
#     [[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
# ]

# for nums, exp in test_data:
#     assert inc_sequence(nums) == exp
 
# [1, 5, 6, 7]
# [1, 2, 3, 4, 6, 7]

# test_data = [1, 5, 2, 3, 4, 6, 1, 7]
# res_data = [test_data[0]]
# for i in test_data[1:]:
#     if i > res_data[-1]:
#         res_data.append(i)
# print(res_data)


# def inc_sequence(num):
#     num_n=[]
#     k=0
#     num_n.append(num[0])
#     for i in range(1,len(num)):
#         if num_n[k]<num[i]:
#             num_n.append(num[i])
#             k+=1
#     print(num_n)
#     return num_n

from functools import reduce


# print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 0)) #(((1+2)+3)+4)


test_data = [1, 5, 2, 3, 4, 6, 1, 7]

def cmp(acc, cur):
    if acc[-1] < cur:
        acc.append(cur)
    return acc

print(reduce(cmp, test_data[1:], test_data[:1]))


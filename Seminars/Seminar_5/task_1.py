# Задача 35.
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


# test_data = [
#     ["3 4 5 6 7 9 10 11 12", 8],
#     ["3 4 6 7 8 9 10 11 12", 5],
#     ["1 3", 2]
# ]

# for sequence, exp in test_data:
#     find_missing(sequence) == exp
    # find_missing_func(sequence) == exp

def find_missing(n_list):
    A=n_list.split()
    A[0]=int(A[0])
    for i in range(1,len(A)):
        A[i]=int(A[i])
        if A[i]-1!=A[i-1]:
            num=A[i-1]+1
            print(num)
            break
    return num


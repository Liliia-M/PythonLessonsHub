# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.



N = 3
result = 1
lst = list(range(-N, N+1))
print(lst)
print()
data = open('file.txt', 'r', encoding = "utf-8")
for line in data:
    result *= lst[int(line) - 1] 
print(result)
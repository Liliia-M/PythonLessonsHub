# Реализуйте алгоритм перемешивания списка.
import random
random.seed(10)
for i in range(10):
    print(round(random.random() * 100), end=" ")
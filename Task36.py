# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint
lst = [randint(1, 10) for i in range(20)]
print (lst)
my_set = set(lst)
print (len(my_set))

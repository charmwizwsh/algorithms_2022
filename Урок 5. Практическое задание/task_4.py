"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict


def fill_dict(n):
    dict = {}
    for i in range(n):
        dict[i] = i
    return dict

def fill_ord_dict(n):
    dict = OrderedDict()
    for i in range(n):
        dict[i] = i
    return dict

def elem_dict(dict, n):
    return dict.get(n)

n = 50
dict1 = fill_dict(n)
dict2 = fill_ord_dict(n)

print('Сравнение заполнения словарей')
print(timeit('fill_dict(n)', globals=globals(), number=1000))
print(timeit('fill_ord_dict(n)', globals=globals(), number=1000))

n = 10
print('Сравнение получение элемента словаря')
print(timeit('elem_dict(dict1, n)', globals=globals(), number=1000))
print(timeit('elem_dict(dict2, n)', globals=globals(), number=1000))



#При операции заполнения упорядоченный словарь явно проигрывает обычному, получение значения по ключу по времени у обоих словарей сопоставимо.
#Применять OrderedDict не имеет смысла в более поздних версиях, т.к. обычный словарь уже упорядочен, а работает быстрее

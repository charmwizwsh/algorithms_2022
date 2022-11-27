"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time

def decorator(function):
    def calc_time(*args, **kwargs):
        start_val = time.time()
        function(*args, **kwargs)
        end_val = time.time()
        print(f"Функция '{function.__name__}' выполнилась за {end_val - start_val:.18f} сек")   
    return calc_time


@decorator
#O(n)
def fill_list(lst, n):
    for i in range(n): #O(n)
        lst.append(i)  #O(1)
    return lst



@decorator
#O(n)
def fill_dict(n):
    dict = {}
    for i in range(n): #O(n)
        dict[i] = i    #O(1)
    return dict



@decorator
#O(n)
def list_get_el(lst, el):
    for i in range(len(lst)): #O(n)
        if lst[i] == el:      #O(1)
            return i
        
@decorator
#O(n)
def dict_get_el(dict, el): 
    dict = {}
    for i in dict.keys():  #O(n)
        if dict[i] == el:  #O(1)
            return i

@decorator
#O(n^2)
def list_del_el(lst, el):
    for i in range(len(lst)): #O(n)
        if lst[i] == el:      #O(1)
            lst.remove(i)     #O(n)
            return lst
        
@decorator
#O(n)
def dict_del_el(dict, el): 
    dict = {}
    for i in dict.keys():  #O(n)
        if dict[i] == el:  #O(1)
            dict.pop(i)
            return dict        
        
        
list=[]
n = 1000000
lst = fill_list(list, n)
dict = fill_dict(n)
#Словарь заполняется дольше, т.к. в словарях используется хэширование данных 
list_get_el(list, n)
dict_get_el(dict, n)
#Из списка удаляется медленнее, потому что проходится по всем 
list_del_el(list, n)
dict_del_el(dict, n)
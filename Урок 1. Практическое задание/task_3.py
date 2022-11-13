"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
#Сложность O(N log N)
def find_year_val1(mp_dict):
    c = []                            #O(1)
    if len(mp_dict) > 0:              #O(n)
        d = mp_dict                   #O(1)
        a = sorted(list(d.values()))  #O(N log N)
        b = a[-3:len(a)]              #O(n)
        for key in d.keys():          #O(n)
            if d[key] in b:           #O(1) (у нас же всегда будет именно 3 элемента)
                c.append(key)         #O(1)
    return c

#Сложность О(n)
def find_year_val2(mp_dict):
    c = []                          #O(1)
    a = []                          #O(1)
    if len(mp_dict) > 0:            #O(n)
        d = mp_dict                 #O(1)
        for i in range(3):          #O(1)
            x = max(d.values())     #O(n)
            for key in d.keys():    #O(n)
                if d[key] == x:     #O(1)
                    c.append(key)   #O(1)
            d.pop(c[i])             #O(1)
    return c

company_val1 = {'comp1': 601, 'comp2': 800, 'comp3': 603, 'comp4': 604, 'comp5': 605, 'comp6': 606, 'comp7': 607 }
print(find_year_val1(company_val1))

company_val2 = {'comp1': 800, 'comp2': 400, 'comp3': 500, 'comp4': 904, 'comp5': 6005, 'comp6': 606, 'comp7': 607 }
print(find_year_val2(company_val2))
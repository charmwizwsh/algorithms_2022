"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

def lst_deq(n):
    lst_deq = []
    for i in range(n):
        lst_deq.append(i)
    return lst_deq

n = 10000
lst = lst_deq(n)
deq = deque(lst_deq(n))



def app_lst_deq(lst_deq):
    for i in range(100):
        lst_deq.append(i)
    return lst_deq


def pop_lst_deq(lst_deq):
    for i in range(100):
        lst_deq.pop()
    return lst_deq


def ex_lst_deq(lst_deq):
    for i in range(100):
        lst_deq.extend([0, 0, 0, 0])
    return lst_deq


def appleft_lst(lst):
    for i in range(100):
        lst.insert(0, i)
    return lst

def appleft_deq(deq):
    for i in range(100):
        deq.appendleft(i)
    return deq


def popleft_lst(lst):
    for i in range(100):
        lst.pop()
    return lst

def popleft_deq(deq):
    for i in range(100):
        deq.popleft()
    return deq


def exleft_lst(lst):
    for i in range(100):
        lst.insert(0, [0, 0, 0, 0])
    return lst

def exleft_deq(deq):
    for i in range(100):
        deq.extendleft([0, 0, 0, 0])
    return deq


def elem_lst_deq(lst_deq):
    for i in range(100):
        lst_deq[i] = i
    return lst_deq

#1) Время выполнения приблизительно одинаковое, иногда у дека хуже.
print('Сравнение append')
print(timeit('app_lst_deq(lst)', globals=globals(), number=1000))
print(timeit('app_lst_deq(deq)', globals=globals(), number=1000))
print('Сравнение pop')
print(timeit('pop_lst_deq(lst)', globals=globals(), number=1000))
print(timeit('pop_lst_deq(deq)', globals=globals(), number=1000))
print('Сравнение extend')
print(timeit('ex_lst_deq(lst)', globals=globals(), number=1000))
print(timeit('ex_lst_deq(deq)', globals=globals(), number=1000))

#2) Операции с деком работают в разы быстрее, чем со списком.
print('Сравнение appendleft')
print(timeit('appleft_lst(lst)', globals=globals(), number=100))
print(timeit('appleft_deq(deq)', globals=globals(), number=100))
print('Сравнение popleft')
print(timeit('popleft_lst(lst)', globals=globals(), number=100))
print(timeit('popleft_deq(deq)', globals=globals(), number=100))
print('Сравнение exleft')
print(timeit('exleft_lst(lst)', globals=globals(), number=100))
print(timeit('exleft_deq(deq)', globals=globals(), number=100))

#3) Получение элемента по индексу в списке быстрее чем в деке.
print('Сравнение get elem')
print(timeit('elem_lst_deq(lst)', globals=globals(), number=100))
print(timeit('elem_lst_deq(deq)', globals=globals(), number=100))
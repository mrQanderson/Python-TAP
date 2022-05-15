"""1.	List filtering.
Дан объект типа list():

l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

Релизуйте функцию которая отфильтрует только integer (int) значения из этого списка.

Напишите несколько вариантов решения:
•	используя цикл for
•	используя list comprehensions
•	используя filter() + lambda

Пример:
def filter_list(l):
    return  # [1, 2, 4, 10, 33]

Check yourself:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


def filter_list_first(sequent):
    lst = []
    for i in sequent:
        if isinstance(i, int):
            lst.append(i)
    return lst


def filter_list_second(sequent):
    return [i for i in sequent if isinstance(i, int)]


def filter_list_third(sequent):
    return list(filter(lambda i: isinstance(i, int), sequent))

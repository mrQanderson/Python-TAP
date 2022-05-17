"""2.	Multiprocessing library.
Для решения задачи #5 (Multiples of 3 and 5) было реализовано множество различных алгоритмов.
В файле multiples_of_three_and_five.py перечислены наиболее популярные из них.

Давайте выясним какой из предложенных алгоритмов является самым эффективным.

Используйте библиотеку multiprocessing, чтобы запустить параллельное выполнение всех 4-х функций.
Вам также понадобится контекстный менеджер timer

Ответьте на вопрос:
•	почему мы не используем библиотеку threading для решения этой задачи?

Check yourself:

bash$ python multiples_of_three_and_five.py

Output:

math_formula() -> 0.0 sec
several_for_loops() -> 28.89 sec
iterate_over_fifteen() -> 41.32 sec
simple_iteration() -> 66.87 sec
"""

"""5.	Multiples of 3 and 5. Find the best algorithm.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 100000000.
source: https://projecteuler.net/problem=1
"""

n = 100000000


def find_sum_of_multiple():
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

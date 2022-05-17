"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""
import time
from multiprocessing import Process

N = 300000000


def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


def run_all_calculations_in_parallel():
    functions = [math_formula, iterate_over_fifteen, several_for_loops, simple_iteration]
    for func in functions:
        p = FuncProcessor(func)
        p.start()


class Timer:
    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.length_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.func()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.length_time = time.time() - self.start_time
        print("{}() -> {:.2f} sec".format(self.func.__name__, self.length_time))


class FuncProcessor(Process):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        with Timer(self.func):
            pass


if __name__ == "__main__":
    run_all_calculations_in_parallel()



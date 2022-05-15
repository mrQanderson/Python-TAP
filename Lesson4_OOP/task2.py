"""2.	Context manager.
Реализуйте контекстный менеджер timer, используя __enter__ и __exit__

Check yourself:

with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)

Output:
timer: block 'doing some sleeps' executed in 6.013 sec
"""
import time


class Timer:
    def __init__(self, block_name):
        self.block_name = block_name
        self.start_time = None
        self.length_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.length_time = time.time() - self.start_time
        print("block {} executed in {:.3f} sec".format(self.block_name, self.length_time))


if __name__ == "__main__":

    with Timer('doing some sleeps'):
        time.sleep(1)
        time.sleep(2)
        time.sleep(3)
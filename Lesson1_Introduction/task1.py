""" 1.	FizzBuzz task.
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом, если число кратно 3-м, вместо него программа должна вывести слово Fizz,
а если кратно 5 — слово Buzz.
Если число кратно и 3 и 5, то программа должна выводить слово FizzBuzz"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizz_buzz()

"""1.	Multiply numbers with regex.
Дан текст:
Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний
показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных

Напишите функцию которая умножает каждую цифру в тексте на 2, и возвращает изменённый текст

Example:
def my_function(text, multiplier=2):
    # implement me
    return text

my_function('I am 10 years old')
  'I am 20 years old'

my_function('I am 10 years old', multiplier=25)
 'I am 250 years old'

Примечания:
•	используйте re.sub https://docs.python.org/3/library/re.html#re.sub
•	обратите внимание на параметр repl (repl can be a string or a function)
"""
import re
import os

path = os.getcwd()

with open(path + '/text1.txt') as file_data:
    data = file_data.read()


def override_digits(text, multiplier=2):
    return re.sub(r"\d+", lambda x: str(int(x.group()) * multiplier), text)


if __name__ == "__main__":
    result = override_digits(data, multiplier=25)
    print(result)

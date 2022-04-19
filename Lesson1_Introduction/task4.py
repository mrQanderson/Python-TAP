"""4.	File size conversion.
Релизуйте функцию которая принимает размер файла в байтах (Byte) и преобразует его в удобный для чтения формат: Byte,
Kilobyte, Megabyte, Gigabyte.

Пример:

def file_size(size_in_bytes):
    # implement me
    return '12.6Mb'

Примечания:
•	Стоит ограничиться Гигабайтами
•	String Format examples:
https://docs.python.org/3/library/string.html#format-examples
•	это очень плохая реализация: https://stackoverflow.com/a/14822210

Ответьте на вопрос:
•	Сколько гигабайт (Gigabyte) в sys.maxsize ?

Check yourself:

assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
"""


def convert_size(file_size):
    for i in ["B", "Kb", "Mb", "Gb"]:
        if file_size < 1024.0:
            return "{:.1f}{}".format(file_size, i)
        elif file_size >= 1024.0 and i == "Gb":
            raise ValueError("Convert function is limited for input no more than 1024 Gigabytes")
        file_size /= 1024.0


def convert_another_size(file_size):
    i = 0
    lst = ["B", "Kb", "Mb", "Gb"]
    while file_size >= 1024.0:
        file_size /= 1024.0
        i += 1
        if i == len(lst):
            raise ValueError("Convert function is limited for input no more than 1024 Gigabytes")
    return "{:.1f}{}".format(file_size, lst[i])

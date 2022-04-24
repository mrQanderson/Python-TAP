"""5.	Unix 'ls -lh' on Python.
По аналогии с командой ls -lh для Unix систем, реализуйте модуль на Python который отображает содержимое директории

Примечания:
•	Чтобы получить содержимое директории используйте os.listdir
•	Используйте os.stat чтобы получить информацию о каждом файле
•	Используйте библиотеку prettytable
1.	pip install prettytable
2.	Имена столбцов: Mode, Owner, Group, Size, File name
•	Используйте библиотеки pwd и grp чтобы получить имя пользователя и группу
"""
import os
import stat
import pwd
import grp
from prettytable import PrettyTable


def unix_ls():
    unix_table = PrettyTable(field_names=["Mode", "Owner", "Group", "Size", "File name"])
    cwd_files = os.listdir(os.getcwd())

    for file_name in cwd_files:
        file = os.stat(file_name)
        unix_table.add_row(
            [stat.filemode(file.st_mode),
             pwd.getpwuid(file.st_uid).pw_name,
             grp.getgrgid(file.st_gid).gr_name,
             file.st_size,
             file_name]
        )

    print("total", len(cwd_files))
    print(unix_table)


if __name__ == "__main__":
    unix_ls()

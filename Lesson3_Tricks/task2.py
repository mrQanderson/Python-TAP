"""2.	importlib.
Используя библиотеку importlib, реализуйте функцию, которая будет возвращать путь к пакету,
если он установлен, и строку “Package not found” – если нет.
"""
import importlib.util


def get_package_path(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec and (module_path := spec.submodule_search_locations):
        return module_path[0]
    else:
        return "Package not found"


if __name__ == "__main__":
    result = get_package_path("prettytable")
    print(result)

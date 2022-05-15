"""3.	logging & argparse.
Для задания importlib, реализуйте логирование в консоль и файл одновременно.

Примечания:
•	если пакет не найден, логгер должен записать строку “Package not found” в ERROR level.
•	для найденного пакета, логгер должен записать описание пакета (метод __doc__) в WARNING,
путь к пакету в INFO и версию пакета в DEBUG.
•	уровень логирования задается отдельно для консоли и отдельно для файла через параметры командной строки,
используя библиотеку argparse.
"""
import sys
import importlib.util
from loguru import logger


logger.add("get_package_info_{time}.log", level="WARNING", rotation="10 MB")


def get_package_path(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec and (module_path := spec.submodule_search_locations):
        logger.warning(sys.modules[package_name].__doc__)
        logger.info(module_path[0])
        logger.debug(f"Package version: {sys.modules[package_name].__version__}")
        return module_path[0]
    else:
        logger.error("Package not found")
        return "Package not found"


if __name__ == "__main__":
    result = get_package_path("loguru")
    print(result)

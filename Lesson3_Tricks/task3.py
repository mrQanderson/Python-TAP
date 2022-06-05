"""3.	logging & argparse.
Для задания importlib, реализуйте логирование в консоль и файл одновременно.

Примечания:
•	если пакет не найден, логгер должен записать строку “Package not found” в ERROR level.
•	для найденного пакета, логгер должен записать описание пакета (метод __doc__) в WARNING,
путь к пакету в INFO и версию пакета в DEBUG.
•	уровень логирования задается отдельно для консоли и отдельно для файла через параметры командной строки,
используя библиотеку argparse.

---->
example to check:
1) python task3.py -type f -l info
2) python task3.py -type c -l info
"""

import argparse
import importlib.util
import sys

from loguru import logger


def parse_cmd_args():
    type_help = "logging type - console or file"
    level_help = "logging level - 'debug', 'info', 'warning', 'error' or 'critical'"

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-type", nargs="?", default=None, choices=["c", "f"], help=type_help
    )
    parser.add_argument(
        "-l",
        "--level",
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help=level_help,
    )

    if len(sys.argv) <= 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    cmd, _ = parser.parse_known_args()

    console, file = True, True
    if cmd.type == "c":
        file = False
    if cmd.type == "f":
        console = False
    return console, file, cmd.level.upper()


def set_logging(console=True, file=True, level=None):
    if console:
        logger.add(
            sys.stderr,
            level=level,
            format="<red>[{level}]</red> Message : <green>{message}</green> @ {time}",
            colorize=True,
        )
    if file:
        logger.add(sink="get_package_info_{time}.log", level=level, rotation="10 MB")


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
    args = parse_cmd_args()
    set_logging(*args)
    result = get_package_path("loguru")
    print(result)

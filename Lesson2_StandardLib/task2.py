"""2.	IP validation.
Напишите функцию для валидации IP-адреса.

Пример:
def check_ip(ip_address):
    return True/False

Напишите несколько вариантов решения:
•	используя библиотеку re
•	используя socket.inet_aton

Check yourself
assert check_ip('') is False
assert check_ip('192.168.0.1') is True
assert check_ip('0.0.0.1') is True
assert check_ip('10.100.500.32') is False
assert check_ip(700) is False
assert check_ip('127.0.0.1') is True
"""
import re
import socket


def check_ip_first(ip_address):
    if isinstance(ip_address, str):
        ip4 = r"(([0-9]|[1-9][0-9]|1[0-9][0-9]|" \
              "2[0-4][0-9]|25[0-5])\\.){3}" \
              "([0-9]|[1-9][0-9]|1[0-9][0-9]|" \
              "2[0-4][0-9]|25[0-5])"

        ip6 = r"((([0-9a-fA-F]){1,4})\\:){7}" \
              "([0-9a-fA-F]){1,4}"

        pattern_ip4 = re.compile(ip4)
        pattern_ip6 = re.compile(ip6)

        if pattern_ip4.search(ip_address):
            return True
        elif re.search(pattern_ip6, ip_address):
            return True
    return False


def check_ip_second(ip_address):
    if isinstance(ip_address, str):
        try:
            return bool(socket.inet_aton(ip_address))
        except OSError:
            return False
    return False

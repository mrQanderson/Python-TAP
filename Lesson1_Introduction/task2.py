"""2.	Find min. and max. value.
Имеется список:
numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
Преобразуйте элементы списка в тип int(). Найдите минимальное и максимальное значение."""

numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

numbers_new = []
for i in numbers:
    try:
        numbers_new.append(int(i))
    except Exception:
        continue
print("New list:", numbers_new)
print("Max value in list:", max(numbers_new))
print("Min value in list:", min(numbers_new))


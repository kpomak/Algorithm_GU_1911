"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
Определить, является ли год, который ввел пользователь, високосным или не високосным.
год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
остальные годы, номер которых кратен 4, — високосные.
все остальные годы — невисокосные.
"""

year = int(input('Введите год '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Год високосный')
else:
    print('Год невисокосный')

from Functions import *

print('Введите размерность трехмерного массива')
y = int(input('Y: '))
x = int(input('X: '))
z = int(input('Z: '))
arr = []
for i in range(y):
    new_st = []
    for j in range(x):
        new_el = list(map(int, input(f'Введите массив элементов строки №{i + 1}, столбца №{i + 1} через пробел: ').split()))
        while len(new_el) != z:
            print(f'Ошибка! Указанное количество элементов не соответствует данному (Z = {z})')
            new_el = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
        new_st.append(new_el)
    arr.append(new_st)

i = int(input('Введите i для вывода среза по второму индексу: '))
while i > y:
    print('Ошибка! - i > y')
    i = int(input('Введите i для вывода среза: '))
for j in arr:
    print(j[i:])
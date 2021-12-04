# Прямоугольная целочисленная матрица удалить все столбцы содержащие хотя бы 1 нулевой элемент

def del_column(arr, index):
    for i in range(len(arr)):
        del arr[i][index]
    #return arr

arr = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

for i in range(n):
    new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
    while len(new) > m:
        print('Ошибка! - Строка, больше заданной размерности')
        new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
    arr.append(new)

for j in range(m - 1, -1, -1):
    flag = False
    for i in range(n):
        if arr[i][j] == 0:
            flag = True
            break
    if flag:
        del_column(arr, j)

for i in arr:
    for j in i:
        print(f'{j:^10}', end='')
    print()
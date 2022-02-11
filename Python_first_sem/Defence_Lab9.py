# Сортировка по среднему арифметическому в столбце

def get_column_average(arr, index) -> float:
    sum = 0
    counter = 0
    for i in range(len(arr)):
        sum += arr[i][index]
        counter += 1
    avg = sum / counter
    return avg

def swap_columns(arr, first, second) -> None:
    for i in range(len(arr)):
        arr[i][first], arr[i][second] = arr[i][second], arr[i][first]
    return arr

arr = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

for i in range(n):
    new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
    while len(new) > m:
        print('Ошибка! - Строка, больше заданной размерности')
        new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
    arr.append(new)

for i in range(m):
    for j in range(m - i - 1):
        if get_column_average(arr, j) > get_column_average(arr, j + 1):
            arr = swap_columns(arr, j, j + 1)

for i in arr:
    for j in i:
        print(f'{j:^10}', end='')
    print()
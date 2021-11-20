from math import sin

def create_matrix(D, F) -> list:
    a = []
    for d in D:
        new = []
        for f in F:
            new.append(sin(d + f))
        a.append(new)
    return a

def matrix_init(n=0, m=0, type=float) -> list:
    if not n:
        n = int(input('Введите количество строк: '))
    if not m:
        m = int(input('Введите количество столбцов: '))
    arr = []
    if type != str:
        for i in range(n):
            new = list(map(type, input(f'Введите строку №{i + 1} через пробел: ').split()))
            while len(new) != m:
                print('Ошибка! Указанное количество элементов не соответствует данному')
                new = list(map(type, input(f'Введите строку №{i + 1} через пробел: ').split()))
            arr.append(new)
    else:
        for i in range(n):
            new = []
            for j in range(m):
                element = input(f'Введите {j} элемент {i} строки: ')
                new.append(element)
            arr.append(new)
    return arr

def print_matrix(matrix, type=float) -> None:
    for i in matrix:
        for e in i:
            if type == float:
                print(f'{e:>10.5f}', end=' ')
            elif type == str:
                print(f'{e:>10}', end=' ')
        print()

def get_average(arr) -> float:
    if len(arr) > 0:
        return abs(sum(arr)/len(arr))
    else:
        print('Ошибка: нет элементов!')

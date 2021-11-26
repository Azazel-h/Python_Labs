from math import sin

# Функция для создания матрицы по формуле
def create_matrix(D, F) -> list:
    a = []
    for d in D:
        new = []
        for f in F:
            new.append(sin(d + f))
        a.append(new)
    return a

# Функция валидации значения
def validation(inp, type):
    validated_inp = str(inp)
    if type == float: # Проверка на Float
        # Сюда лучше не смотреть, без регулярных выражений слишком страшно
        if validated_inp.isdigit():
            return float(validated_inp)
        elif '.' in validated_inp or 'e-' in validated_inp or 'e+' in validated_inp or '-' in validated_inp:
            if "." in validated_inp and validated_inp[0:validated_inp.index(".")].isdigit() \
                    and validated_inp[validated_inp.index(".") + 1:].isdigit():
                return float(validated_inp)
            elif validated_inp[0] == "-" and "." in validated_inp \
                    and validated_inp[1:validated_inp.index(".")].isdigit() \
                    and validated_inp[validated_inp.index(".") + 1::].isdigit():
                return float(validated_inp)
            elif validated_inp[0] == "-" and validated_inp[1::].isdigit():
                return float(validated_inp)
            elif ("e-" in validated_inp or "e+" in validated_inp) and \
                    validated_inp[validated_inp.index("e") + 2::].isdigit():
                return float(validated_inp)
            else:
                return False
        else:
            return False
    if type == int: # Проверка на Int
        if len(validated_inp) >= 1:
            if (validated_inp[0] in ('-', '+') and validated_inp[1:].isdigit()) or validated_inp.isdigit():
                return int(validated_inp)
            else:
                return False
        else:
            return False
    if type == str:
        return validated_inp

# Проверка массива
def array_validation(arr, type):
    for i in arr:
        if not validation(i, type) and str(validation(i, type))[0] != '0':
            print(f'Ошибка! - Все значения должны быть типа {type}')
            return False
    return list(map(type, arr))

# Ввод матрицы
def matrix_init(n=0, m=0, type=float) -> list:
    # Была ли введена размерность
    if not n: # Если не было введено количество строк
        n = validation(input('Введите количество строк: '), int) # Вводим и проверяем на Int
        while not n or n < 0: # Пока не проходит проверку или ноль
            if str(n) == '0' or n < 0: # Если ноль
                print(f'Введите значение > 0')
            else:
                print(f'Ошибка! - Введите значение типа {int}')
            n = validation(input('Введите количество строк: '), int) # Повторный ввод

    if not m: # Если не было введено количество столбцов
        m = validation(input('Введите количество столбцов: '), int) # Вводим и проверяем на Int
        while not m or m < 0: # Пока не проходит проверку или ноль
            if str(m) == '0' or m < 0: # Если ноль
                print(f'Введите значение > 0')
            else:
                print(f'Ошибка! - Введите значение типа {int}')
            m = validation(input('Введите количество столбцов: '), int) # Повторный ввод

    arr = [] # Пустой массив для строк матрицы
    if type != str: # Если тип матрицы не строковый
        for i in range(n):
            new = array_validation(input(f'Введите строку №{i + 1} через пробел: ').split(), type) # Вводим и проверяем строку
            while not new: # Пока проверка не проходит
                new = array_validation(input(f'Введите строку №{i + 1} через пробел: ').split(), type) # Повторный ввод
            while len(new) != m: # Если длинна строки не соответствует размерности
                new = []
                while not new: # Проверяем строку
                    print('Ошибка! - Указанное количество элементов не соответствует данному')
                    new = array_validation(input(f'Введите строку №{i + 1} через пробел: ').split(), type) # Вводим и проверяем строку
            arr.append(new) # Добавляем в массив
    else: # Если тип строковый то просто используем другой тип ввода
        for i in range(n):
            new = []
            for j in range(m):
                element = input(f'Введите {j} элемент {i} строки: ')
                new.append(element)
            arr.append(new)
    return arr

# Вывод матрицы
def print_matrix(matrix, type=float) -> None:
    for i in matrix:
        for e in i:
            if type == float:
                print(f'{e:>10.5f}', end=' ')
            elif type == str:
                print(f'{e:>10}', end=' ')
        print()




from math import sin

from math import inf


def int_proof(s):
    """
    проверяет строку на принадлежность целым числам
    :param s: str: строка на проверку
    :return: bool: является ли строка целым числом
    """
    return s.lstrip('-').isdecimal()


def float_proof(s):
    """
    проверяет строку на принадлежность float
    :param s: str: строка на проверку
    :return: bool: является ли строка float
    """
    try:
        float(s)
        return True
    except:
        return False


def input_proof(inpt: str, left_limit=-inf, right_limit=+inf, amount_of_numbers=1, type_proof='float'):
    """
    проверяет ввод на корректность
    :param inpt: str: строка на проверку
    :param left_limit: float: левая граница чисел
    :param right_limit: float: правая граница чисел
    :param amount_of_numbers: int: количество чисел (0 для любого количества)
    :param type_proof: str: тип проверки
    :return: bool: является ли ввод корректным
    """
    def proof(num: str):
        if type_proof == 'float':
            return float_proof(num)
        elif type_proof == 'char':
            return len(num) == 1
        else:
            return int_proof(num)

    inputs = inpt.split()
    if len(inputs) != amount_of_numbers and amount_of_numbers != 0:
        return False
    if False in list(map(proof, inputs)):
        return False
    if type_proof != 'char':
        inputs = list(map(float, inputs))
        if False in list(map(lambda x: left_limit <= x <= right_limit, inputs)):
            return False

    return True

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

def get_average(arr) -> float:
    if len(arr) > 0:
        return abs(sum(arr)/len(arr))
    else:
        print('Ошибка: нет элементов!')


# Написать программу, которая позволит с использованием меню обеспечить работу с
# целочисленными матрицами:
# 1. Ввести матрицу
# 2. Добавить строку
# 3. Удалить строку
# 4. Добавить столбец
# 5. Удалить столбец
# 6. Найти строку, имеющую наибольшее среднее арифметическое
# 7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
# 8. Найти столбец, имеющий наибольшее количество нулевых элементов
# 9. Переставить местами столбцы с максимальной и минимальной суммой элементов
# 10. Вывести текущую матрицу
# Булгаков Арсений Сергеевич ИУ7-16Б
from statistics import mean


# Вывод матрицы
def matrix_print(arr) -> None:
    for i in arr:
        print(*i)


# Ввод матрицы
def matrix_init() -> list:
    print('Введите размерность матрицы')
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))
    arr = []
    for i in range(n):
        new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
        while len(new) != m:
            print('Ошибка! Указанное количество элементов не соответсвует данному')
            new = list(map(int, input(f'Введите строку №{i + 1} через пробел: ').split()))
        arr.append(new)
    return arr


# Добавление строки
def add_string(arr, var) -> list:
    index = int(input('Введите индекс для вставки строки: '))
    if 0 <= index <= len(arr):  # Проверка на некорректный индекс
        new = []
        new = list(map(int, input(f'Введите новую строку через пробел: ').split()))
        while len(new) != len(arr[0]):
            print('Ошибка! Указанное количество элементов не соответсвует данному')
            new = list(map(int, input(f'Введите строку №{index + 1} через пробел: ').split()))
        if var == 1:
            arr += [0] * len(arr[0])
            for i in range(len(arr) - 1, index, -1):
                arr[i] = arr[i - 1]
            arr[index] = new
            return arr
        elif var == 2:
            arr.insert(index, new)
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Добавление столбца
def add_column(arr, var) -> list:
    index = int(input('Введите индекс для вставки строки: '))
    if 0 <= index <= len(arr):  # Проверка на некорректный индекс
        new = []
        for j in range(len(arr)):
            new.append(int(input(f'Введите элемент столбца №{j + 1}: ')))
        if var == 1:
            for i in range(len(arr)):
                arr[i] += [0]
                for j in range(len(arr[0]) - 1, index, -1):
                    arr[i][j] = arr[i][j - 1]
                arr[i][index] = new[i]
            return arr
        elif var == 2:
            for i in range(len(arr)):
                arr[i].insert(index, new[i])
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Удаление столбца
def del_column(arr, var) -> list:
    index = int(input('Введите индекс удаляемого столбца: '))
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        if var == 1:
            for i in range(len(arr)):
                for j in range(index, len(arr[0]) - 1):
                    arr[i][j] = arr[i][j + 1]
                del arr[i][-1]
            return arr
        elif var == 2:
            for i in range(len(arr)):
                del arr[i][index]
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Удаление строки
def del_string(arr, var) -> list:
    index = int(input('Введите индекс удаляемой строки: '))
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        if var == 1:
            for i in range(index, len(arr) - 1):
                arr[i] = arr[i + 1]
            del arr[-1]
            return arr
        elif var == 2:
            del arr[index]
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Поиск строки с максимальным средне арифмитическим
def max_avarage_search(arr) -> list:
    max_avg = arr[0]
    for i in arr:
        if mean(i) > mean(max_avg):
            max_avg = i
    return max_avg


# Свап строк с максимальным и минимальным количеством нулей
def under_zero_min_max_strings_swap(arr) -> list:
    max = sum(k for k in arr[0] if k < 0)
    max_index = 0
    min = sum(k for k in arr[0] if k < 0)
    min_index = 0
    for i, v in enumerate(arr):
        new = sum(k for k in v if k < 0)
        if new > max:
            max = new
            max_index = i
        if new < min:
            min = new
            min_index = i
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
    return arr


# Свап столбцов с максимальной и минимальной суммой элементов
def max_min_element_sum_column_swap(arr):
    columns = dict.fromkeys(range(len(arr[0])), 0)
    for i in arr:
        for j, v in enumerate(i):
            columns[j] += v
    max_column = max(columns, key=columns.get)
    min_column = min(columns, key=columns.get)
    for i in arr:
        i[max_column], i[min_column] = i[min_column], i[max_column]
    return arr


# Поиск столбца с максимальным количеством нулей
def max_zero_column(arr) -> int:
    columns = dict.fromkeys(range(len(arr[0])), 0)
    for i in arr:
        for j, v in enumerate(i):
            if v == 0:
                columns[j] += 1
    return max(columns, key=columns.get)


# Меню
def menu_print() -> None:
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Ввести матрицу')
    print('2 - Добавить строку')
    print('3 - Удалить строку')
    print('4 - Добавить столбец')
    print('5 - Удалить столбец')
    print('6 - Найти строку, имеющую наибольшее среднее арифметическое')
    print('7 - Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов')
    print('8 - Найти столбец, имеющий наибольшее количество нулевых элементов')
    print('9 - Переставить местами столбцы с максимальной и минимальной суммой элементов')
    print('10 - Вывести текущую матрицу')


counter = 0  # Счетчик операций
# Первая инициализация списка
print('- Введите матрицу -')
arr = matrix_init()

# Бесконечный цикл воода команд
while True:
    # Вывод меню
    if counter % 5 == 0:
        menu_print()

    command = int(input('Введите номер команды: '))  # Приглашение ввода
    counter += 1  # Счетчик количества введеных команд

    if command == 0:  # Выйти из программы
        exit(0)
    elif command == 1:  # Ввод матрицы
        arr = matrix_init()
    elif command == 2:  # Добавление строки
        print('1 - Алгоритмическая реализация')
        print('2 - Реализация средствами языка')
        num = int(input('>>> '))
        if 0 < num <= 2:
            add_string(arr, num)
        else:
            print('Ошибка! Нет такого варианта')
    elif command == 3:  # Удаление строки
        print('1 - Алгоритмическая реализация')
        print('2 - Реализация средствами языка')
        num = int(input('>>> '))
        if 0 < num <= 2:
            del_string(arr, num)
        else:
            print('Ошибка! Нет такого варианта')
    elif command == 4:  # Добавление столбца
        print('1 - Алгоритмическая реализация')
        print('2 - Реализация средствами языка')
        num = int(input('>>> '))
        if 0 < num <= 2:
            add_column(arr, num)
        else:
            print('Ошибка! Нет такого варианта')
    elif command == 5:  # Удаление столбца
        print('1 - Алгоритмическая реализация')
        print('2 - Реализация средствами языка')
        num = int(input('>>> '))
        if 0 < num <= 2:
            del_column(arr, num)
        else:
            print('Ошибка! Нет такого варианта')
    elif command == 6:  # Поиска строки с максимальным средне арифметическим
        print(f'Максимальное среднее арифметическое {max_avarage_search(arr)}')
    elif command == 7:  # Свап строк с максимальным и минимальным количеством отриц. элементов
        arr = under_zero_min_max_strings_swap(arr)
        print('Теперь ваша матрица:')
        matrix_print(arr)
    elif command == 8:  # Вывод номера столбца с максимальным количеством нулей
        print(f'Столбец с максимальным количеством нулей: {max_zero_column(arr) + 1}')
    elif command == 9:  # Свап столбцов с максимальной и минимальной суммой элементов
        arr = max_min_element_sum_column_swap(arr)
        print('Теперь ваша матрица:')
        matrix_print(arr)
    elif command == 10:  # Вывод матрицы
        print('Теперь ваша матрица:')
        matrix_print(arr)

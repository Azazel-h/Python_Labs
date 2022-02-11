# Написать программу, которая позволит с использованием меню:
# 1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
# 2. Очистить список и ввести его с клавиатуры
# 3. Добавить элемент в произвольное место списка
# 4. Удалить произвольный элемент из списка (по номеру)
# 5. Очистить список
# 6. Найти значение K-го экстремума в списке
# 7. Найти наиболее длинную последовательность по варианту
# Булгаков Арсений Сергеевич ИУ7-16Б
import re


# Валидация ввода
def validate(inp):
    validated_inp = str(inp)
    if re.search(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', validated_inp) is None:
        print('Введи нормальное число...')
        return False
    else:
        return float(validated_inp)


# Проверка на простоту
def is_prime(n) -> bool:
    if float(n).is_integer():
        if n <= 1:
            return False
        for divisor in range(2, int(n)):
            if n % divisor == 0:
                return False
        return True
    return False


# Функция для инициализации через бесконечный ряд
def inf_init() -> list:
    n = int(input('Введите количество элементов: '))
    arr = [(1 / ((2 ** i) - i)) for i in range(1, n + 1)]
    print('Теперь список: ' + str(arr))
    return arr


# Функция для инициализации через ввод с клавиатуры
def keyboard_init() -> list:
    arr = []
    n = int(input('Введите количество элементов: '))
    for i in range(1, n + 1):
        inp = validate(input(f'Ввведите {i} элемент списка: '))
        while not inp:
            inp = validate(input(f'Ввведите {i} элемент списка: '))
        arr.append(inp)
    print('Теперь список: ' + str(arr))
    return arr


# Поиск экстремумов
def maxima_minima_search(arr) -> list:
    extremas = []
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            extremas.append(arr[i])
        elif arr[i - 1] > arr[i] < arr[i + 1]:
            extremas.append(arr[i])
    return extremas


# Поиск подпоследовательности
def subsequence_search(arr):
    max_start, start = 0, 0
    max_end, end = 0, 0
    for i in range(len(arr) - 1):
        if is_prime(arr[i]) and arr[i] - arr[i + 1] > 1e-5:
            end = i + 1
        else:
            start += i + 1
            end += i + 1
        if end - start > max_end - max_start:
            max_end = end
            max_start = start
    return arr[max_start:max_end + (1 if is_prime(arr[max_end]) else 0)]


# Вывод меню
def menu_print() -> None:
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Инициализировать список первыми N элементами бесконечного ряда')
    print('2 - Очистить список и ввести его с клавиатуры')
    print('3 - Добавить элемент в произвольное место списка')
    print('4 - Удалить произвольный элемент из списка (по номеру)')
    print('5 - Очистить список')
    print('6 - Найти значение K-го экстремума в списке')
    print('7 - Найти наиболее длинную убывающую последовательность простых чисел.')


counter = 0  # Счетчик операций
# Первая инициализация списка
print('Инициализировать список первыми N элементами бесконечного ряда? Y / N')
c = str(input()).strip()
if c == 'Y' or c == 'y':
    arr = inf_init()
else:
    print('Введите список с клавиатуры')
    arr = keyboard_init()

# Бесконечный цикл воода команд
while True:
    # Вывод меню
    if counter % 3 == 0:
        menu_print()

    command = int(input('>>> '))  # Приглашение ввода
    counter += 1

    if command == 0:  # Выход из программы
        exit()
    elif command == 1:  # Инициализация через бесконечный ряд
        arr_type = 'float'
        arr = inf_init()
    elif command == 2:  # Инициализация через ввод с клавиатуры
        arr = keyboard_init()
    elif command == 3:  # Добавить элемент в произвольное место
        x = int(input('Введите элемент: '))
        n = int(input('Введите позицию (С нуля): '))
        arr.insert(n, x)
        print('Теперь список: ' + str(arr))
    elif command == 4:  # Удаление элемента
        n = int(input('Введите позицию (С нуля): '))
        del arr[n]
        print('Теперь список: ' + str(arr))
    elif command == 5:  # Очистка списка
        arr.clear()
        print('Список очищен')
    elif command == 6:  # Поиск экстремумов
        print('Ваш список: ' + str(arr))
        extremas = maxima_minima_search(arr)  # Получаем все экстремумы
        print('Экстремумы: ' + str(extremas))
        print('Всего экстремумов: ' + str(len(extremas)))
        if len(extremas) > 0:
            k = int(input('Введите номер K: '))
            if k <= len(extremas):
                print('Kый экстремум: ' + str(extremas[k - 1]))
            else:
                print('K - некорректно')
    elif command == 7:  # Поиск последовательности
        print('Список: ' + str(arr))
        print('Наиболее длинная убывающая последовательность простых чисел: ' + str(subsequence_search(arr)))

# Написать программу, которая позволит с использованием меню обеспечить работу со
# строковыми массивами:
# 1. Очистить список и ввести его с клавиатуры
# 2. Добавить элемент в произвольное место списка
# 3. Удалить произвольный элемент из списка (по номеру)
# 4. Очистить список
# 5. Поиск элемента с наибольшим числом английских гласных букв
# 6. Замена всех заглавных гласных английских букв на строчные в элементе
# Булгаков Арсений Сергеевич ИУ7-16Б

# Функция для инициализации через ввод с клавиатуры
def keyboard_init() -> list:
    arr = []
    n = int(input('Введите количество элементов: '))
    for i in range(1, n + 1):
        inp = str(input(f'Ввведите {i} элемент списка: '))
        while not inp:
            inp = str(input(f'Ввведите {i} элемент списка: '))
        arr.append(inp)
    print('Теперь список: ' + str(arr))
    return arr

# Функция для добавления элемента в произвольное место в списке
def add(arr, n, index) -> list:
    arr_len = len(arr)
    arr += [0]
    for i in range(arr_len, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = n
    return arr

# Функция для удаления элемента в списке
def delete(arr, index) -> list:
    arr_len = len(arr)
    for i in range(index, arr_len - 1):
        arr[i] = arr[i + 1]
    del arr[-1]
    return arr

# Подсчет гласных в строке
def vowel_counter(string) -> int:
    return sum(1 for i in string if i in 'aeiouAEIOU')

# Ищем максимум
def max_vowel_eng(arr) -> str:
    max = vowel_counter(arr[0])
    max_string = ''
    for i in arr:
        num = vowel_counter(i)
        if num > max:
            max = num
            max_string = i
    return max_string

# Видим заглавную гласную? Делаем строчной.
def vowels_to_lower(string) -> str:
    for i in string:
        if i in 'AEIOU':
            string = string.replace(i, i.lower())
    return string

# Меню
def menu_print() -> None:
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Очистить список и ввести его с клавиатуры')
    print('2 - Добавить элемент в произвольное место списка')
    print('3 - Удалить произвольный элемент из списка (по номеру)')
    print('4 - Очистить список')
    print('5 - Поиск элемента с наибольшим числом английских гласных букв')
    print('6 - Замена всех заглавных гласных английских букв на строчные в элементе')

counter = 0 # Счетчик операций
# Первая инициализация списка
print('Введите список с клавиатуры')
arr = keyboard_init()

# Бесконечный цикл воода команд
while True:
    # Вывод меню
    if counter % 3 == 0:
        menu_print()

    command = int(input('>>> ')) # Приглашение ввода
    counter += 1

    if command == 0: # Выйти из программы
        exit(0)
    elif command == 1: # Очистить список и ввести его с клавиатуры
        arr.clear()
        arr = keyboard_init()
    elif command == 2: # Добавить элемент в произвольное место списка
        print('Ваш список: ' + str(arr))
        n = str(input('Введите строку: '))
        index = int(input('Введите индекс: '))
        if 0 <= index <= len(arr): # Проверка на некорректный индекс
            arr = add(arr, n, index)
            print('Теперь список: ' + str(arr))
        else:
            print('Дурак')
    elif command == 3: # Удалить произвольный элемент из списка (по номеру)
        print('Ваш список: ' + str(arr))
        index = int(input('Введите индекс удаляемого элемента: '))
        if 0 <= index < len(arr): # Проверка на некорректный индекс
            arr = delete(arr, index)
            print('Теперь список: ' + str(arr))
        else:
            print('Дурак')
    elif command == 4: # Очистить список
        arr.clear()
    elif command == 5: # Поиск элемента с наибольшим числом английских гласных букв
        print('Ваш список: ' + str(arr))
        print('Элемент с наибольшим числом английских гласных букв: ' + max_vowel_eng(arr))
    elif command == 6: # Замена всех заглавных гласных английских букв на строчные в элементе
        print('Ваш список: ' + str(arr))
        index = int(input('Введите индекс изменяемого элемента: '))
        arr[index] = vowels_to_lower(arr[index])
        print('Теперь список: ' + str(arr))

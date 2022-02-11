# Булгаков Арсений Сергеевич ИУ7-16Б, ну +- сам

from Functions import validation

def drawing_head():
    print('┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓\n'
          '┃ Язык программирования ┃         Категория          ┃ Популярность (1-5) ┃\n'
          '┣━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━┫')


def drawing_footer():
    print('┗━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┛')


def drawing_table(file):
    drawing_head()
    for line in file:
        list_line = line.strip().split(';')
        print(f'┃{list_line[0]:^23}┃{list_line[1]:^28}┃{list_line[2]:^20}┃')
    drawing_footer()


# Подфункция функции view_all_strings, ищущая строки, подходящие условию.
def strings_finder(line, find_fields):
    finded_string = ''
    prev_line = line
    line = prev_line.split(';')
    if len(find_fields) > 1:
        if line[0] == find_fields[0] and line[1] == find_fields[1]:
            finded_string = prev_line
    elif len(find_fields) == 1:
        if line[0] == find_fields[0]:
            finded_string = prev_line
    return finded_string


# Просмотр всех строк и вызов функции strings_finder.
def view_all_strings(find_fields, file):
    strings = []
    for line in file:
        if strings_finder(line, find_fields) != '':
            strings.append(strings_finder(line, find_fields))
    if len(strings) == 0:
        print('Нет записей, содержащие заданные поля.')
    else:
        print('Записи с заданными полями:')

    return strings


# Ввод и обработка искомых полей.
def choice_search_field(string_input, max_len):
    while True:
        find_fields = list(map(str, input('\nВведите ' + string_input + ' Вы хотите искать: ').split(';')))
        if len(find_fields) != max_len:
            print('Вы ввели недопустимое количество полей.')
        else:
            break

    return find_fields


# Ввод и оработка кол-ва записей очищаемых и/или добавления записей.
def count_strings():
    while True:
        try:
            count = int(input('\nВведите количество записей: '))
        except ValueError:
            print('Некорректный ввод.')
            continue
        if count < 1:
            print('Некорректное число записей.')
        else:
            return count


# Пункт меню 1: Выбор файла.
def choice_file():
    while True:
        file_name = input('\nВведите название файла: ')
        if len(file_name.split('.')) > 1:
            if file_name.split('.')[1] == 'txt':
                try:
                    open(file_name)
                    return file_name
                except:
                    print('В дирректории нет такого файла. Хотите его создать?')
                    answ = input('Y / N ?: ')
                    if answ == 'Y':
                        f = open(file_name, 'w+')
                        f.write('')
                        return file_name
                    else:
                        return None
        print('Ошибка! - Файл должен быть текстовым')


# Пункт меню 2 и 3: Очищение и/или добавление записей.
def records_change(file_name, argument_file):
    if argument_file != 'a':
        count_strings_add = count_strings()
    else:
        count_strings_add = 1
    file = open(file_name, argument_file)
    if count_strings_add > 1:
        print('Введите', count_strings_add, 'записией (построчно, через ";"): ')
    else:
        print('Введите запись (через ";"): ')
    for i in range(count_strings_add):
        while True:
            line = input()
            args = line.split(';')
            if len(args) != 3:
                print('Некорректный ввод. Должно быть 3 аргумента: название ЯП, категория и оценка популярности.')
            else:
                flag = True
                if str(validation(args[0], str))[0] == 'F' or \
                        str(validation(args[1], str))[0] == 'F' \
                        or str(validation(args[2], int))[0] == 'F':
                    flag = False
                if flag:
                    file.write(line + '\n')
                    break
                else:
                    print('Некорректный ввод. Должно быть 3 аргумента формата: str;str;int')
    file.close()
    return menu(file_name)


# Пункт меню 4: Вывод всех записей.
def print_all_set(file_name):
    file = open(file_name)
    drawing_table(file)
    file.close()
    return menu(file_name)


# Пункт меню 5: Поиск по одному заданному полю.
def single_field_search(file_name):
    file = open(file_name)
    need_find_fields = choice_search_field('поле, по которому', 1)
    drawing_table(view_all_strings(need_find_fields, file))
    file.close()
    return menu(file_name)


# Пункт меню 6: Поиск по двум заданным полям.
def two_field_search(file_name):
    file = open(file_name)
    need_find_fields = choice_search_field('поля, по которым', 2)
    drawing_table(view_all_strings(need_find_fields, file))
    file.close()
    return menu(file_name)


def commands_menu(choice, file_name):
    if choice > 1 and file_name is None:
        print('\nОшибка! - Вы не выбрали файл для работы.')
        return menu(file_name)
    if choice == 0:
        exit()
    elif choice == 1:
        menu(choice_file())
    elif choice == 2:
        records_change(file_name, 'w')
    elif choice == 3:
        print_all_set(file_name)
    elif choice == 4:
        records_change(file_name, 'a')
    elif choice == 5:
        single_field_search(file_name)
    else:
        two_field_search(file_name)


def menu(file_name=None):
    print('0. Выход из программы\n1. Выбрать файл для работы\n2. Инициализировать базу данных\n3. Вывести содержимое '
          'базы данных\n4. Добавить запись в базу данных\n5. Поиск по одному полю\n6. Поиск по двум полям')
    while True:
        try:
            key = int(input('\nВведите пункт из меню: '))
        except ValueError:
            print('Некорректный ввод.')
            continue
        if key > 6 or key < 0:
            print('Вы ввели некорректный пункт.')
        else:
            commands_menu(key, file_name)

menu()

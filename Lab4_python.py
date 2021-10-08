# Построить график функции
# Булгаков Арсений Сергеевич ИУ7-16Б

# Функция графика
def func(x) -> float:
    return x ** 7 - x ** 6 + 8 * (x ** 5) - 4 * (x ** 4) + 6 * (x ** 3) + 2 * (x ** 2) - 5 * x + 1

# Ввод данных
x_first = float(input('Введите начальное значение: ')) # Ввод начального значения
h = float(input('Введите шаг: ')) # Ввод шага
x_last = float(input('Введите конечное значение: ')) # Ввод конечного значения
# Заводим переменные максимума и минимума, приравниваем к первым полученным значениям
max_f = func(x_first)
min_f = func(x_first)
EPS = 1e-5 # Берем эпсилон для вычислений
GRAPH_W = 80 # Ширина графика в пробелах

# Проверка начального и конечного значения
if x_first > x_last:
    print('Начальное значение должно быть всегда меньше конечного')
    exit(-1)

# Считаем количество шагов
num_of_h = int((x_last - x_first + EPS) // h)

# Выводим таблицу значений
print('-------------------------\n|     x     |     y     |\n|-----------------------|')
for i in range(num_of_h + 1):
    x = x_first + h * i # Считаем новый x
    if (x - x_last > EPS): break # Проверка на выход за границы заданной области
    y = func(x) # Считаем y
    # Ищем минимум и максимум
    min_f = min(y, min_f)
    max_f = max(y, max_f)
    print(f'|{x:>10.5f}|  {y:>10.5f}|') # Выводим таблицу
print('-' * 25) # Закрываем таблицу
print('Разница максимума и минимума:', max_f - min_f) # Выполняем доп. задание

num_of_cuts = int(input('Введите количество засечек (от 4 до 8): ')) # Вводим количество засечек
if not 4 <= num_of_cuts <= 8: # Проверяем, что их количество от 4 и до 8
    print('Количество засечек должно быть строго от 4 до 8')
    exit(-1)

# Считаем количество пробелов и шаг для засечек
second_h = (max_f - min_f) / (num_of_cuts - 1)
spaces = GRAPH_W // (num_of_cuts - 1)

print(' ' * 4, end='')
for i in range(num_of_cuts):
    y = min_f + second_h * i # Считаем y на засечках, начиная с минимума
    if (y - max_f > EPS): y = max_f # Приравниваем к максимуму, если вышли за границу
    cut = f'{y:.2f}'
    print(cut, end=' ' * (spaces - len(cut) + 1)) # Пытаемся ровно вывести
print()

# Выводим ось оординат
print(' ' * 7, end ='')
for i in range(GRAPH_W + 1):
    if i % spaces == 0: # Вывод засечек
        print('|', end='')
    else:
        print('-', end='')
print('>') # Стрелочка

# Смотрим, где находиться ось абцисс в заданном масштабе
normalized_axis = (0 - min_f) / (max_f - min_f)
axis_position = int(normalized_axis * GRAPH_W)

for i in range(num_of_h + 1):
    x = x_first + h * i # Считаем x
    y = func(x) # Считаем y
    # Смотрим, где находится точка в заданном масштабе
    normalized_y = (y - min_f) / (max_f - min_f)
    y_position = int(normalized_y * GRAPH_W)
    # Очень заумно выводим график
    if y_position == axis_position: # Если на оси
        print(f'{x:>5.2f} |' + (axis_position - 1) * ' ' + '*')
    elif y_position < axis_position: # Если слева от оси
        print(f'{x:>5.2f} |' + (y_position - 1) * ' ' + '*' + (axis_position - y_position - (1 if y_position != 0 else 2)) * ' ' + '|')
    else: # Если справа от оси
        print(f'{x:>5.2f} |' + (axis_position - 1) * ' ' + '|' + (y_position  - axis_position - 1) * ' ' + '*')
print(' ' * 6 + 'v') # Стрелочка



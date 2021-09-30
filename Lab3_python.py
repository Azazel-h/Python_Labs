# Написать программу, которая по введенным целочисленным координатам трех точек на плоскости вычисляет стороны
# образованного треугольника и длину биссектрисы, проведенной из наименьшего угла. Определить, является ли
# треугольник прямоугольным. Далее вводятся координаты точки. Определить, находится ли точка внутри треугольника.
# Если да, то найти расстояние от точки до ближайшей стороны треугольника или ее продолжения.
# Булгаков Арсений Сергеевич ИУ7-16Б

# Эпсилон для сравнения чисел с плавающей точкой
EPS = 1e-10

# Сообщения об ошибках
error = 'Ошибка: Точки должны быть различны!'
error_2 = 'Ошибка: Точки не образуют треугольник!'

# Функция для рассчета расттояния от точки до точки
# Принимает кортежи координат точек
def calc_distance(first_point, second_point) -> float:
    distance = abs((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2) ** (1 / 2)
    return distance

# Функция для рассчета длинны бисектрисы
# Принимает стороны угла, а затем оставшуюся
def calc_bisector(first_angle_side, second_angle_side, third_side) -> float:
    length = (((first_angle_side * second_angle_side * (first_angle_side + second_angle_side - third_side)
                * abs(third_side + second_angle_side + first_angle_side)) ** (1 / 2))
                / (first_angle_side + second_angle_side))
    return length

# Функция для проверки на прямоугольный треугольник
# Принимает сначала наибольшую сторону треугольника, а затем две другие
def right_triangle_checking(greatest_side, second_side, third_side) -> bool:
    print(greatest_side, second_side, third_side, greatest_side ** 2, second_side ** 2, third_side ** 2)
    if abs(greatest_side ** 2 - (second_side ** 2 + third_side ** 2)) <= EPS:
        return True
    return False

# Функция для рассчета площади треугольника
# Принимает просто стороны треугольника
def calc_S(first_side, second_side, third_side) -> float:
    p = (first_side + second_side + third_side) / 2
    S = abs(p * (p - first_side) * (p - second_side) * (p - third_side)) ** (1 / 2)
    return S

# Функция для рассчета высот
# Принимает просто стороны треугольника
def calc_height(first_side, second_side, third_side) -> float:
    p = (first_side + second_side + third_side) / 2
    height = (2 * (abs(p * (p - first_side) * (p - second_side) * (p - third_side)) ** (1 / 2))) / first_side
    return height

print('Все вводимые точки должны быть различны!')
points = [] # Массив точек
for i in range(3): # Ввод входных данных
     points.append(tuple(map(float, input('Введите координаты точки X, Y: ').split(','))))
     if points.count(points[i]) > 1:
         print(error)
         exit(1)

# Массив сторон треугольника
triangle = []
for i in range(3): # Рассчет сторон треугольника
    triangle.append(calc_distance(points[i], points[(i + 1) % 3]))

S = calc_S(triangle[0], triangle[1], triangle[2]) # Считаем площадь треугольника
if S == 0: # Проверяем образуют ли точки треугольник (Сравнение с константным нулем без eps корректно)
    print(error_2)
    exit(-1)

a, b, c = triangle[0], triangle[1], triangle[2] # Создаем копию сторон перед сортировкой
triangle.sort() # Сортируем, чтобы найти наименьший угол напротив наименьшей стороны

# Вывод треугольника с координатами для наглядности
# print(f'\n          {points[1]}\n              /  \\\n             /    \\\n            /      \\\n  {points[0]} ------ {points[2]}\n')

print(f'Стороны треугольника: {a:.5f} {b:.5f} {c:.5f}')
print(f'Длинна биссектрисы: {calc_bisector(triangle[1], triangle[2], triangle[0]):.5f}') # Выводит длинну бисектриссы
print('Это прямоугольный треугольник' if right_triangle_checking(triangle[2], triangle[1], triangle[0])
      else 'Это непрямоугольный треугольник') # Проверяет на прямоугольный треугольник

# Вввод новой точки
new_point = tuple(map(float, input('Введите координаты новой точки X, Y: ').split(',')))

arr = [calc_distance(new_point, i) for i in points] # Проводим отрезки до точки
sum_S = calc_S(a, arr[0], arr[1]) + calc_S(b, arr[1], arr[2]) + calc_S(c, arr[0], arr[2]) # Считаем площади появившехся треугольников

# Проверяем внутри ли точка
if abs(S - sum_S) <= EPS:
    print('Точка внутри треугольника')
    # Считаем расстояние до сторон треугольника и берем минимальное
    min_distance = min(calc_height(a, arr[0], arr[1]), calc_height(b, arr[1], arr[2]), calc_height(c, arr[0], arr[2]))
    print(f'Минимальное расстояние до ближайшей стороны: {min_distance:.5f}')
else:
    print('Точка снаружи треугольника')

# Задан треугольник (целочисл. координаты всех вершин, а ввод всегда корректный) требуется найти высоту из наименьшего угла
points = []
for i in range(3):
     points.append(tuple(map(int, input('Введите координаты точки X, Y: ').split(','))))

a = abs((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2) ** (1 / 2)
b = abs((points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2) ** (1 / 2)
c = abs((points[2][0] - points[0][0]) ** 2 + (points[2][1] - points[0][1]) ** 2) ** (1 / 2)

triangle = [a, b, c]
triangle.sort()

p = (a + b + c) / 2
height = (2 * (abs(p * (p - triangle[0]) * (p - triangle[1]) * (p - triangle[2])) ** (1 / 2))) / triangle[0]

print(f'Высота из наименьшего угла: {height:.5f}')

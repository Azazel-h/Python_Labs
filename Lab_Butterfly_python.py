# Определение принадлежности точек графику функций или области ограниченной ими
# Булгаков Арсений Сергеевич ИУ7-16Б

def check(x, y):
    if -9 <= x <= -1:
        print((-1 / 8) * (x + 9) ** 2 + 8, 7 * (x + 8) ** 2 + 1, (1 / 49) * (x + 1) ** 2)
        if y <= (-1 / 8) * (x + 9) ** 2 + 8 and y >= 7 * (x + 8) ** 2 + 1 and y >= (1 / 49) * (x + 1) ** 2:
            return 'Left Wing'
    if 1 <= x <= 9:
        if y <= (-1 / 8) * (x - 9) ** 2 + 8 and y >= 7 * (x - 8) ** 2 + 1 and y >= (1 / 49) * (x - 1) ** 2:
            return 'Right Wing'
    return 'Outside'

x = float(input())
y = float(input())
print(check(x, y))
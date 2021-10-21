# ВВОДИТСЯ МАССИВ СТРОК сделать частотный анализ латинских букв для каждого элемента
import string

def analyse(i) -> list:
    d = {}
    for c in i:
        if c.lower() in string.ascii_lowercase:
            if not d.get(c.lower()):
                d[(c.lower())] = 1
            else:
                d[(c.lower())] += 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

n = int(input('Введите количество элементов: '))
arr = []
for i in range(n):
    arr.append(str(input(f'Введите {i} элемент: ')))
for i in arr:
    print(f'Анализируемая строка: {i}')
    data = analyse(i)
    for i in data:
        print(i[0], ':', i[1])



# 1 ТЕКСТОВЫЙ ФАЙЛ int поле
f = open('123.txt')
new_f = open('new.txt', 'w+')
n = 0
for j in f.read():
    n += 1
f.seek(0)

ignore = []
for k in range(n):
    counter = 0
    max_i = -1
    max = -float('inf')
    for i in f:
        if counter not in ignore:
            if int(i) > max:
                max = int(i)
                max_i = counter
        counter += 1

    print(max)
    new_f.write(str(max) + '\n')
    if max_i != -1:
        ignore.append(max_i)
    f.seek(0)
f.close()
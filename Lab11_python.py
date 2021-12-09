text = ['kek 5 + 5 82823 -312 + 5 5',
        'lol 2-2, 25 +3+4 +5, 2-23, 2-+2, asf131kna, gi2 + 3 -4fgaig1ga+akfh1+2',
        'одетый в летнюю серенькую пару, был маленького роста, упитан,',
        'лыс, свою приличную шляпу пирожком нес в руке, а на хорошо выбритом Lol',
        'лице его помещались сверхъестественных размеров очки в черной роговой',
        'оправе. Второй – плечистый, рыжеватый, вихрастый молодой человек в заломленной',
        'на затылок клетчатой кепке – был в ковбойке, жеваных белых брюках и в черных тапочках.']
max_len = max([len(i) for i in text])

def left_alignment() -> None:
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
        text[i] = text[i] + ' ' * (max_len - len(text[i]))
        print(text[i])

def right_alignment() -> None:
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
        text[i] = (max_len - len(text[i])) * ' ' + text[i]
        print(text[i])

def center_alignment() -> None:
    for i in range(len(text)):
        string = list(' '.join(text[i].split()))
        counter = 0
        while len(string) < 86:
            if string[counter] == ' ':
                counter += 1
                string.insert(counter, ' ')

            if counter < len(string) - 1:
                counter += 1
            else:
                counter = 0
        text[i] = ''.join(string)
        print(text[i])

def delete(word: str) -> int:
    flag = False
    if len(word.split()) > 1:
        print('Ошибка! - Введено некорректное слово или оно является словосочетанием.')
        return -1
    for i in range(len(text)):
        if text[i].find(' ' + word + ' ') != -1 or text[i].find(' ' + word) != -1 or text[i].find(word + ' ') != -1:
            text[i] = ' '.join(list(filter(lambda x: x != word, text[i].split())))
            flag = True
        print(text[i])
    if not flag:
        print('Ошибка! - такого слова нет в тексте. Текст выведен без изменений.')
        return -1

def replace_word(word_1: str, word_2: str) -> int:
    flag = False
    if len(word_1.split()) > 1 or len(word_2.split()) > 1:
        print('Ошибка! - Введено некорректное слово или оно является словосочетанием.')
        return -1
    for i in range(len(text)):
        if text[i].find(' ' + word_1 + ' ') != -1 or text[i].find(' ' + word_1) != -1 or text[i].find(word_1 + ' ') != -1:
            text[i] = ' '.join([(s if s != word_1 else word_2) for s in text[i].split()])
            flag = True
        print(text[i])
    if not flag:
        print('Ошибка! - такого слова нет в тексте. Текст выведен без изменений.')
        return -1

def translate(enc: str) -> int:
    enc += '+'
    result = 0
    number = 0
    number_cont = False
    sign = 1
    for char in enc:
        if char == '+':
            if number_cont:
                result += sign * number
                number_cont = False
                number = 0
                sign = 1
        elif char == '-':
            if number_cont:
                result += sign * number
                number_cont = False
                number = 0
                sign = 1
            sign *= -1
        elif char in '1234567890':
            number_cont = True
            number = number * 10 + int(char)
    return result

def menu_print() -> None:
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Выровнять текст по левому краю')
    print('2 - Выровнять текст по правому краю')
    print('3 - Выровнять текст по ширине')
    print('4 - Удаление всех вхождений заданного слова')
    print('5 - Замена одного слова другим во всём тексте')
    print('6 - Вычисление арифметических выражений внутри текста (Сложение / Вычитание)')
    print('7 - Определить, сколько имеется слов из 2, 3, 4 букв в каждом предложении')

def solve() -> None:
    last_was_space = False
    was_it_num = False
    arr = []
    answ = ''
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == ' ':
                answ += text[i][j]
                last_was_space = True
            elif text[i][j] in '1234567890':
                if last_was_space and was_it_num :
                    arr.append(answ)
                    answ = ''
                answ += text[i][j]
                was_it_num = True
                last_was_space = False
            elif text[i][j] in '+-':
                was_it_num = False
                last_was_space = False
                answ += text[i][j]
            else:
                arr.append(answ)
                was_it_num = False
                last_was_space = False
                answ = ''

    arr = [i for i in arr if i and i != ' ']
    results = [translate(i) for i in arr]
    for i in range(len(text)):
        for j in range(len(text[i])):
            for k in range(len(arr)):
                text[i] = text[i].replace(arr[k].strip(), str(results[k]), 1).lstrip('0')
        print(text[i])

def count() -> None:
    for i in text:
        counter = 0
        for j in i.split():
            if len(j) == 2 or len(j) == 3 or len(j) == 4:
                counter += 1
        print(counter, end=' ')
    print()

counter = 0
while True:
    if counter % 5 == 0:
        menu_print()

    command = int(input('Введите номер команды: '))
    counter += 1

    if command == 0:
        exit(0)
    elif command == 1:
        left_alignment()
    elif command == 2:
        right_alignment()
    elif command == 3:
        center_alignment()
    elif command == 4:
        delete(input('Введите удаляемое слово: '))
    elif command == 5:
        replace_word(input('Введите заменяемое слово: '), input('Введите замену: '))
    elif command == 6:
        solve()
    elif command == 7:
        count()


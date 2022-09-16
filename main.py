import csv

f = open('output.txt', 'w')
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    duck = csv.reader(csvfile, delimiter=';')
    author = input('Введите автора: ')
    search = input('Введите 1, если хотите ввести 20 ID книг, 0 — случайный выбор: ')
    books = 20
    i = -1
    k = 0
    dog = 0
    id_array = []
    tags_array = []
    flag = 0
    numbers = []
    if search == '1':
        for v in range(books):
            id_array.append(input('Введите ID нужной книги: '))
    else:
        flag = 1

    for row in duck:
        i += 1
        if len(row[1]) > 30:
            dog += 1

        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]

        surname = row[3].split()
        surname = surname[-1:]
        if len(surname) > 0:
            if (author == str(surname[0])) and int(row[7]) < 150:
                print(row[1])

        # дополнительноезадание
        tags = row[12].split('#')
        for tag in tags:
            if not (tag in tags_array):
                tags_array.append(tag)

        if flag == 0:
            if row[0] in id_array:
                f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')
        elif (flag == 1) and (i < 22) and (i > 1):
            f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')

        if i > 0:
            numbers.append(int(row[8]))

    print('Всего записей:', i)
    print('Количество записей длиной > 30:', dog)
    tags_array.pop(0)
    tags_array.pop(0)
    print(tags_array)

    numbers.sort(reverse=True)

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    duck = csv.reader(csvfile, delimiter=';')
    c = -1
    k = 0
    books_array = []
    for row in duck:
        c += 1
        book = row[1]
        if (c > 0) and (int(row[8]) == numbers[k]) and (k < 20) and not(book in books_array):
            print(book)
            k += 1

f.close()

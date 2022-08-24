# Импортируем модуль для работы с CSV
import csv

# Константа с именем файла
FILENAME = 'test.csv'

users = [
    ['User1', 1],
    ['User2', 2],
    ['User3', 3]
]

# Записывваем несколько строк в файл
with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)

# Дописываем одну строку в файл
with open(FILENAME, 'a', newline='') as file:
    user = ['User4', 4]
    writer = csv.writer(file)
    writer.writerow(user)

# Читаем данные из файла
with open(FILENAME, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], '-', row[1])

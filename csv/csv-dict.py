# Импортируем модуль для работы с CSV
import csv

# Константа с именем файла
FILENAME = 'test.csv'

users = [
    {'name': 'User1', 'age': 1},
    {'name': 'User2', 'age': 2},
    {'name': 'User3', 'age': 3}
]

# Записывваем несколько строк в файл
with open(FILENAME, 'w', newline='') as file:
    columns = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    writer.writerows(users)

    # Дописываем одну строку в файл
    user = {'name': 'User4', 'age': 4}
    writer.writerow(user)

# Читаем данные из файла
with open(FILENAME, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], '-', row['age'])

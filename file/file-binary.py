# Импортируем модуль для работы с CSV
import pickle

# Константа с именем файла
FILENAME = 'test.dat'

name = 'User'
age = 1

# Записывваем несколько строк в файл
with open(FILENAME, 'wb') as file:
    # С помощью dump происходит последовательная запись объъектов
    pickle.dump(name, file)
    pickle.dump(age, file)

# Читаем данные из файла
with open(FILENAME, 'rb') as file:
    # Поэтому при чтении используем load, для последовательного чтения объектов
    name = pickle.load(file)
    age = pickle.load(file)
    print('Name:', name, '\nAge:', age)

# Версия с записью и чтением набора объектов
users = [
    ["User1", 1, True],
    ["User2", 2, False],
    ["User3", 3, False]
]

# Записывваем объект в файл
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

# Читаем объект из файла
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Name:", user[0], "\nAge:", user[1], "\nPython developer:", user[2])

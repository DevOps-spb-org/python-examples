# Импортируем модуль для работы с CSV
import pickle

# Константа с именем файла
FILNAME = 'test.dat'

name = 'User'
age = 1

# Записывваем несколько строк в файл
with open(FILNAME, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

# Читаем данные из файла
with open(FILNAME, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print('Name:', name, '\nAge:', age)

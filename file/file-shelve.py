# Импортируем модуль для работы с бинарными файлами при помощи модуля shelve
import shelve

# Константа с именем файла
FILENAME = 'test.shelve'

# Записывваем несколько строк в файл
with shelve.open(FILENAME) as file:
    file['User1'] = 'First user'
    file['User2'] = 'Second user'

# Читаем данные из файла
with shelve.open(FILENAME) as file:
    print(file['User1'])
    print(file['User2'])

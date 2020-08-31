# Импортируем модуль для работы с файловой системой
import os

# Создание папки с путем относительно текущего скрипта
os.mkdir('test')

# Создание папки с абсолютным путем
os.mkdir('c://test')

# Удаление папки с путем относительно текущего скрипта
os.rmdir('test')

# Удаление папки с абсолютным путем
os.rmdir('c://test')

# Переименование файла
os.rename('somefile1', 'somefile2')

# Удаление файла
os.remove('somefile')

# Проверка на существование файла
filename=input('Enter path: ')
if os.path.exists(filename):
    print('File exist')
else:
    print('File does not exist')

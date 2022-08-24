# Константа с именем файла
FILENAME = 'test.txt'

messages = list()

# Выводим 4 запроса на ввод данных от пользователя
for i in range(4):
    message = input('Введите строку ' + str(i + 1) + ': ')
    messages.append(message + '\n')

# Записываем введенные данные в файл
with open(FILENAME, 'a') as file:
    for message in messages:
        file.write(message)

print('Читаем файл')
# Читаем все строки из файла
with open(FILENAME, 'r') as file:
    for message in file:
        print(message, end='')

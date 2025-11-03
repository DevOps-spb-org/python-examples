string = "hello world"

# Получение подстроки
sub_string1 = string[:5]
print(sub_string1)  # hello

sub_string2 = string[2:5]
print(sub_string2)  # llo

sub_string3 = string[2:9:2]
print(sub_string3)  # lowr

# Длина строки
length = len(string)
print(length)  # 11

# Поиск в строке
exist = "hello" in string
print(exist)  # True

exist = "sword" in string
print(exist)  # False

exist = string.find("or")
print(exist)  # 7

# Перебор строки
for char in string:
    print(char)

# перебор строки по словам
for worlds in string.split():
    # print(worlds) # построчно
    print(worlds, end=" ") # по пробелам

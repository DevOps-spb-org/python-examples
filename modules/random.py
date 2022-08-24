import random

number = random.random()  # значение от 0.0 до 1.0
print(number)

number = random.randint(20, 35)  # значение от 20 до 35
print(number)

number = random.randrange(10)  # значение от 0 до 10
print(number)

number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9, 10
print(number)

number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8, 10
print(number)

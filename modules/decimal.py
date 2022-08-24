# При работе с числами с плавающей точкой (то есть float) мы сталкиваемся с тем,
# что в результате вычислений мы получаем не совсем верный результат
number = 0.1 + 0.1 + 0.1
print(number)  # 0.30000000000000004

from decimal import Decimal

number = Decimal("0.1")
number = number + number + number
print(number)  # 0.3

# В операциях с Decimal можно использовать целые числа:
number = Decimal("0.1")
number = number + 2

# Однако нельзя смешивать в операциях дробные числа float и Decimal:
number = Decimal("0.1")
number = number + 0.1  # здесь возникнет ошибка

# С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:
number = Decimal("0.10")
number = 3 * number
print(number)  # 0.30

# англосаксонская система
# 1,234.567
# европейская система
# 1.234,567

import locale

locale.setlocale(locale.LC_ALL, "de")  # для  Windows
# locale.setlocale(locale.LC_ALL, "de_DE")   # для MacOS

number = 12345.6789
formatted = locale.format("%f", number)
print(formatted)  # 12345,678900

formatted = locale.format("%.2f", number)
print(formatted)  # 12345,68

formatted = locale.format("%d", number)
print(formatted)  # 12345

formatted = locale.format("%e", number)
print(formatted)  # 1,234568e+04

money = 234.678
formatted = locale.currency(money)
print(formatted)  # 234,68 €

# программа конвертирует секунды в часы

total_second = float(input('Введите количество секунд: '))  # получаем от пользователя кол-во сек.
# получаем количество часов (// выполняем целочисленное деление - выдает в результате целое число)
hours = total_second // 3600

# получить количество оставшихся минут(% делит одно число на другое и выдает остаток от него
# например 17 % 3 = 2)
minutes = (total_second // 60) % 60
# получить количество оставшихся секунд
seconds = total_second % 60
# показать результат
print('Часы', hours)
print('Минуты', minutes)
print('Секунды', seconds)

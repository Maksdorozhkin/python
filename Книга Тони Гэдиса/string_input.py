# Получить имя пользователя
first_name = input('Введите свое имя: ')
last_name = input('Введите фамилию: ')  # получить фамилию пользователя
print('Привет', first_name, last_name)

string_value = input('Сколько часов Вы отработали? ')
hours = int(string_value)  # преобразование строкового значение в числовое
print(hours)

# более оптимальный подход
hours = int(input('Сколько часов Вы отработали? '))
print(hours)

# Похожий пример
pay_rate = float(input('Сколько ты зарабатываешь в час? '))

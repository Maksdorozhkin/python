# оператор распаковки словаря **
button = {
    'width': 200,
    'text': 'Buy'
}

# создает новый словарь и добавляет новый ключ и значение к словарю кнопка
red_button = {
    **button,
    'color': 'red'
}

print(red_button)
print(button)

# объединение словарей
button_info = {
    'text': 'buy',
}
button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
}
new_button = {
    **button_info,
    **button_style
}

print(new_button)

# более простой способ объединение словарей с помощью |

cool_button = button_info | button_style
print(cool_button)

# задача объединить три разных словаря

dict1 = {
    'nastay': 'tits',
    'nadya': 'ass',
    'katya': 'brain out',
}

dict2 = {
    'andrew': 'lol',
}

dict3 = {
    'maks': 'bad man',
}

# all_dict = dict1 | dict2 | dict3
all_dict = {
    **dict1,
    **dict2,
    **dict3,
}
print(all_dict)

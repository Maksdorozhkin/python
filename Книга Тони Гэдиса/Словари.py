# простой словарь
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])

# сохранение значения из словаря в переменную
alien_0 = {'color': 'green', 'point': 5}
new_points = alien_0['point']
print(f"Ты получил {new_points} очков")

# добавление новых пар ключ значение
alien_0 = {'color': 'green', 'point': 5}
alien_0['x_poz'] = 10
alien_0['y_poz'] = 15
print(alien_0)

# создание пустого словаря
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# изменение значений в словаре
alien_0 = {'color': 'green'}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

# задача чем больше скорость пришельца тем сильнее он будет смещаться по оси х
alien_0 = {'x_position': 0, 'y_posit': 25, 'speed': 'medium'}
print(f"Изначальное местоположение пришельца: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Новая позиция пришельца {alien_0['x_position']}")

# удаление пар в словаре
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
del alien_0['point']
print(alien_0)

# обращение к словарю методом get
alien_0 = {'color': 'green', 'point': 5}
speed_value = alien_0.get('speed', 'Значение скорости не задано')
print(speed_value)
# если ключ 'speed' существует в словаре то получим его значение /
# если нет то сообшение после запятой

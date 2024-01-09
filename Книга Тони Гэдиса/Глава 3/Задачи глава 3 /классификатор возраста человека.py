age = int(input('Введите возраст человека: '))
if age <= 1:
    print('Младенец')
if age > 1 and age <= 13:
    print('Ребенок')
if age > 13 and age <= 20:
    print('Подросток')
if age > 20:
    print('Взрослый')

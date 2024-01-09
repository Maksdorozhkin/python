SOSIGES_P = 10
BUNS_P = 8

people = int(input('Введите количество гостей на пикнике: '))
hotdogs = int(input('Введите количество хотдогов для одного гостя: '))

# определяем сколько нужно хотдогов
food = people * hotdogs

# определяем сколько нужно пачек сосисок

sosiges_tmp = SOSIGES_P

sosiges = SOSIGES_P / food

if sosiges < 0:
    SOSIGES_P += 1,
print(f"Необходимо купить {sosiges} пачек сосисок")

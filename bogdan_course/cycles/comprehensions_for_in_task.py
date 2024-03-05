# Задача 1 создать из словаря с значениями ключей типа строка новый словарь с теми же значениями только в верхнем регистре используя dict comprehensions
my_dict = {
    'a': 'maksim',
    'c': 'mikhailovich',
    'b': 'dorozhkin'
}

new_dict = {k: v.upper() for k, v in my_dict.items()}
print(new_dict)

# создать список из списка с элементами типа строка длинна который более 3 символов используем list comprehension
my_list = ['abs', 'a', 'sos', 'wark']
new_list = [elem for elem in my_list if len(elem) > 3]
print(new_list)

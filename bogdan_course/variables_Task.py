# Задание: переменные разных типов

my_int = 10
my_string = 'Maks'
my_list = [1, 2, 'Maks', True]
my_dikt = {'my_name': 'Maks',
           'my_age': 43,
           'my_child_name': 'Denis'}

print(my_int, my_string, my_list, my_dikt)

my_number = 8
my_name = 'Maks'
print(id(my_number))

other_number = my_number
print(id(other_number))

print(id(my_name))

print(type(my_name))

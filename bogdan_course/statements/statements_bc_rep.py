# Пример if с оператором отрицания not
person_info = {
    'age': 20
}
if not person_info.get('name'):
    print("Имя отсутствует")

num_one = 10
num_two = 5
if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Both numbers are ints and positive")

# инструкция if else, выполняется если условие if ложно
my_number = 21
if type(my_number) is int:
    print("My number is integer")
else:
    print("My number is not integer")

my_phone = {
    'price': 200,
    'brand': 'apple',
}
if my_phone.get('brand'):
    print("My phone brand is", my_phone['brand'])
else:
    print("There is no phone brand")

# Инструкция if elif
my_nums = 0
if my_nums > 0:
    print("Число положительное")
elif my_nums < 0:
    print("Число отрицательное")
else:
    print("zero")

# использование if в функциях


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов целое число"
    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a} меньше {b}"


print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))

# тоже самое только с использованием одной лишней переменной


def nums_info2(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов целое число"
    elif a >= b:
        info = f"{a} больше или равно {b}"
    else:
        info = f"{a} меньше {b}"
    return info


print(nums_info2(True, 10))
print(nums_info2(10, 2))
print(nums_info2(4, 15))

# task statements создать функцию route_info в которую будет передаваться словарь если в словаре есть ключ distance и его значение целое число, верните строку "Distance to your destination is "distance"" иначе если в словаре есть ключи speed and time, верните строку "distance to your destination is <speed * time>" иначе верните строку "no distance info is available"


def route_info(route_dict):
    if route_dict.get('distance') and type(route_dict['distance']) is int:
        return f"Distance to your destination is {route_dict['distance']}"
    if (route_dict.get('speed') and type(route_dict['speed']) is int) and (route_dict.get('time') and type(route_dict['time']) is int):
        return f"Distance to your destination is {route_dict['speed'] * route_dict['time']}"
    return "No distance info is available"


route_dict1 = {
    'distance': 100,
    'speed': 20,
    'time': 2,
}

route_dict2 = {
    # 'distance': 100.1,
    'speed': 20,
    'time': 2,
}

route_dict3 = {
    'distance': 100.1,
    'my_time': 2,
}
print(route_info(route_dict=route_dict1))
print(route_info(route_dict=route_dict2))
print(route_info(route_dict=route_dict3))

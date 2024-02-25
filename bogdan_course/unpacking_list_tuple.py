# распаковка списков

my_fruits = ['apple', 'banana', 'lime']

my_apple, my_banana, my_lime = my_fruits
print(my_apple)

# распаковка с помощью *

apple, *list_fruits = my_fruits
print(apple)
print(list_fruits)
print(type(apple))
print(type(list_fruits))

# распаковка словаря в аргументы с ключевыми словами
# в данном примере словарь распаковывается в параметры функции с помощью **

user_profile = {
    'name': 'Maks',
    'comments_qty': 25,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))

# можно передать значения ключей словаря без распаковки

print(user_info(user_profile['name'], user_profile['comments_qty']))

# тоже самое с ключевыми словами

print(user_info(name=user_profile['name'],
                comments_qty=user_profile['comments_qty']))

# распаковка списка в позиционные аргументы

user_data = ['Maks', 43]


def maks_data(name, com_qty):
    if not com_qty:
        return f"{name} has no comments"
    return f"{name} has {com_qty} comments"


print(maks_data(*user_data))

# task создать список словарей (3 словаря по 2 ключа) с помощью оператора распаковки
# списков создать три переменные каждая из которых будет содержать один словарь далее.
# Cоздайте функцию, которая будет принимать два аргумента в вызове функции распаковать словарь функцию вызвать три раза

my_list_dikt = [
    {'bike': 'kawasaki',
     'color': 'black'},
    {'bike': 'ducati',
     'color': 'red'},
    {'bike': 'honda',
     'color': 'blue'}]

bike1, bike2, bike3 = my_list_dikt


def love_bikes(bike, color):
    return f"{bike}, most be {color} color"


print(bike1)
print(love_bikes(**bike1))
print(love_bikes(**bike2))
print(love_bikes(**bike3))

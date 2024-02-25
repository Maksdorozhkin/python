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

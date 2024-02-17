# аргументы и параметры функции
# ошибка отсутствия аргументов
def sum_nums(a, b):
    c = a + b
    return c


print(sum_nums(2, 2))


# объединение аргументов в кортеж


def sum_nums1(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)


print(sum_nums1(2, 3, 4, 2))


# использование позиционных аргументов

def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info('Maks', 25)
print(info)

# объединение аргументов в словарь
# нельзя использовать позиционные аргументы

def get_post_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['post_qty']} posts"
    )
    return info
info = get_post_info(name='Maks', post_qty=32, id=1388)
print(info)

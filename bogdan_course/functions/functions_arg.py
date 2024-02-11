# аргументы с ключевыми словами

def get_post_info(name, post_qty):
    info = f"{name} wrote {post_qty} posts"
    return info


info = get_post_info(name='Maks', post_qty=25)
print(info)


# объединение аргументов с ключевыми словами в словарь

def post_info(**person):
    print(person)
    # print(type(person))
    # info_ = (f"{person['name']} wrote "
    #          f"{person['posts_qty']} posts")

    info_ = f"{person['name']} wrote, {person['posts_qty']} posts"
    return info_


info = post_info(name='Maksim', posts_qty=100)
print(info)

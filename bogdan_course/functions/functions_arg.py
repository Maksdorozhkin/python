# аргументы с ключевыми словами

def get_post_info(name, post_qty):
    info = f"{name} wrote {post_qty} posts"
    return info


info = get_post_info(name='Maks', post_qty=25)
print(info)

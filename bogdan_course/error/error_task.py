# Задача на генерацию ошибок
# мое решение

def image_info(dict):
    if dict.get('image_id') and dict.get('image_title'):
        print(f"Image {dict['image_title']} has id {dict['image_id']}")
    elif not dict.get('image_id'):
        raise TypeError("В словаре нет необходимого ключа")
    elif not dict.get('image_title'):
        raise TypeError("В словаре нет необходимого ключа")
    return dict

my_dict = {
    'image_id': 5136,
    # 'image_title': 'my cat',
}
# image_info(my_dict)

# правильное решение (задачу решил правильно, это просто более красивое решение)


def image_info2(image):
    if ('image_id' not in image) or ('image_title' not in image):
        raise TypeError("Нет необходимых ключей")
    return f"Image {image['image_title']} has id {image['image_id']}"

try:
    print(image_info2(my_dict))
except TypeError as e:
    print(e)
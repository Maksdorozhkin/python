#Объединение двух списков с помощью функции с аргументами с ключевыми словами
def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


res = merge_lists_to_dict(list_one=[1, 2, 3], list_two=[True, 'abc', False])
print(res)

res2 = merge_lists_to_dict([1, 2, 3], list_two=[True, 'abc', False])
print(res2)

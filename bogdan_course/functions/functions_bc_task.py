def merge_lists_to_dict(list_one, list_two):
    merge_lists = zip(list_one, list_two)
    convert_merge_list_to_dict = dict(merge_lists)
    return convert_merge_list_to_dict


list1 = ['Andrew', 'Maks', 'Nastya', 'Yuriy']
list2 = [100, 200, 300, 400, 500]

print(merge_lists_to_dict(list1, list2))


res_two = merge_lists_to_dict(['abc'], [{}, True, 100])
print(res_two)

# функция объединяет два списка, конвертирует их в словарь

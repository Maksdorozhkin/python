

# функция которая принимает словарь, конвертирует его в список кортежей и если в нем есть значение ключа целое число то умножает его на 2
def dict_to_list(dict_to_convert):
    list_for_conversion = []
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_conversion.append((k, v))
    return list_for_conversion


print(dict_to_list({'a': 2, 'b': True}))


# Задача функция фильтрует список и возвращает новый список с данными определенного типа

def filter_list(data, type_data):
    new_list = []
    for item in data:
        if type(item) == type_data:
            new_list.append(item)
    return new_list


print(filter_list(data=[True, 1, 2, 3, 1, 2,
      'abc', 'xyz', False], type_data=str))

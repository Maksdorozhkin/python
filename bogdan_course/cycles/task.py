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
print(filter_list(data=[True, 1, 2, 3, 1, 2,
      'abc', 'xyz', False], type_data=bool))
print(filter_list(data=[True, 1, 2, 3, 1, 2,
      'abc', 'xyz', False], type_data=int))

# тоже решение только с помощью isinstance данное решение не рекомендуется т.к. вернет еще и bool т.к. true в python это единица а false 0


def filter_list1(data1, type_data1):
    new_list1 = []
    for item1 in data1:
        if isinstance(item1, type_data1):
            new_list1.append(item1)
    return new_list1


print(filter_list1(data1=[True, 1, 2, 3, 1, 2,
      'abc', 'xyz', False], type_data1=int))

# решение с помощью встроенной функции filterlist


def filter_list2(data2, type_data2):
    def check_element_type(elem):
        return type(elem) is type_data2

    return list(filter(check_element_type, data2))


res = filter_list2(data2=[1, 2, 3, 4, 3.1, True, 'abc', False], type_data2=int)
print(res)


# тоже самое только с помощью lambda функции
def filter_list3(data3, type_data3):
    return list(filter(lambda elem2: type(elem2) is type_data3, data3))


res = filter_list3(data3=[1, 2, 3, 4, 3.1, True, 'abc', False], type_data3=int)
print(res)

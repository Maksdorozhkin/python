# структура и синтаксис
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

# Чтобы сравнить два словаря можно использовать оператор ==

# изменение и получения значений в словарях
print(my_motorbike['brand'])
my_motorbike['brand'] = 'KTM'
print(my_motorbike)
# print(dir(my_motorbike))

# добавление элементов

my_motorbike['is new'] = True
print(my_motorbike)

# del elements
del my_motorbike['is new']
print(my_motorbike)

# use variable in the dict
new_key_name = 'brand'
my_motorbike[new_key_name] = 'ducati'
print(my_motorbike)

# вложенные словари
my_motorbike = {
    'brand': 'Ducati',
    'price_info': {
        'price': 25000,
        'is_available': True
    },
    'engine_vol': 1.2
}
print(my_motorbike['price_info']['price'])
print(my_motorbike['price_info']['is_available'])

# use variable for create dict
brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2
my_new_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_volume': engine_volume,
}
print(my_new_motorbike)

# длинна словаря
print(len(my_new_motorbike))

# использование метода get для получения ключа в словаре возвращает none если ключа нет
print(my_new_motorbike.get('model'))
print(my_new_motorbike.get('model', 0)) # если ключ отсутствует можно указать какое значение возвращать

# резюме по словарям
my_dict = {}
print(my_dict.__doc__)

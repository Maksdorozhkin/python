import json  # импорт модуля json

json_str = '{"id":235, "brand": "Nike", "qty":84}'
# если json выполнен как массив
json_array = '[{"a":1}, {"b":2}]'

sneakers = json.loads(json_str)  # конвертация json в словарь

print(type(sneakers))
print(sneakers)
print(sneakers['brand'])

my_list = json.loads(json_array)  # конвертация json массива в список
print(my_list)


# обратная конвертация
json_from_dict = json.dumps(sneakers)
print(json_from_dict)

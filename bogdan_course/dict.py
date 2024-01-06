# пример словаря
my_bike = {
    "brand": "Ducati",
    "model": "Monster s4r",
    "price": 420000,
    "engine_vol": 1.0,
}
print(my_bike)

print(my_bike["engine_vol"])

# изменение значений
my_bike["price"] = 320000
print(my_bike["price"])
print(my_bike)

# добавление элементов
my_bike["year"] = 2004
print(my_bike)

# удаление элементов
del my_bike["engine_vol"]
print(my_bike)

# сипользование переменных в словаре
key_name = "my_next_bike"
my_bike[key_name] = "Harley Davidson"
print(my_bike)
my_bike[key_name] = "Only Ducati"
print(my_bike)

# вложенные словари
my_bike["price info"] = {
    "currency": "RUB",
    "is_avalilable": False,
}
print(my_bike)
print(my_bike["price info"]["is_avalilable"])

# использование переменных для создания словарей
name = "Marusya"
hear = "blondine"
tits = "size 4"

my_favorite_gerl = {
    "name": name,
    "hear": hear,
    "tits": tits,
}
print(my_favorite_gerl)

# длинна словаря
print(len(my_favorite_gerl))

# метод get для получения для получения значений ключа (этот метод следует использовать всегда)
# если уверены, что ключ есть в словаре можно использовать вместо get квадратные скобки
print(my_favorite_gerl.get("tits"))
print(my_favorite_gerl.get("status", 0))

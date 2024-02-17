# Объединение двух списков с помощью функции с аргументами с ключевыми словами
def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


res = merge_lists_to_dict(list_one=[1, 2, 3], list_two=[True, 'abc', False])
print(res)

res2 = merge_lists_to_dict([1, 2, 3], list_two=[True, 'abc', False])
print(res2)


# функция в которой все именованные аргументы объединены в словарь

def update_car_info(**car):
    car['color'] = 'red'
    print(car)
    print(f"Эта машина марки {car['brand']} , стоит {car['price']} рублей, она в продаже {car['is_available']}")


update_car_info(brand='BMW', price=3000000, is_available=True)

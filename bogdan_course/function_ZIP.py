# пример объединения (слияния)

fruits = ['apple', 'lime', 'banana', 'coconut']
quantities = [100, 30, 4, 40]
availability = [True, False, True, True]
fruit_quant_zip = zip(fruits, quantities, availability)
print(fruit_quant_zip)
print(list(fruit_quant_zip))

# объединяем в словарь можно объединить только два значения
fruits_2 = ['apple', 'lime', 'banana', 'coconut']
quantities_2 = [100, 30, 4, 40]

zip_dict = dict(zip(fruits_2, quantities_2))
print(zip_dict)

# task
motorbike_shop_goods = ['backpack', 'pant', 'glower', 'helmet']
prices = [120, 80, 15, 400]

current_list = []
zip_shop = zip(motorbike_shop_goods, prices)
list_zip_shop = list(zip_shop)
for i in list_zip_shop:
    lists_in_i = list(i)
    current_list.append(lists_in_i)
print(current_list)

print(dict(current_list))

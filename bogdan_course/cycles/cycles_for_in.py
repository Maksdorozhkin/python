# цикл for in для списка для кортежа тоже самое что и для списка
my_list = [True, 10, 'abc', {}]
for elem in my_list:
    print(type(elem))


# for in for dict

my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for key in my_dict:
    # print(key)
    print(key, my_dict[key])  # если нужно получить значения ключей

for item in my_dict.items():
    key, value = item
    print(key, value)

for k, v in my_dict.items():
    print(k, v)


# цикл for in для наборов
video_id = {123, 457, 1456, 456}
for sets in video_id:
    print(sets)


# цикл for in для строк
my_name = 'Maksim Dorozhkin'
for symbol in my_name:
    print(symbol.upper())


# for in для диапазонов
for num in range(5):
    print(num)

for nums in range(3, 10, 2):
    print(nums)

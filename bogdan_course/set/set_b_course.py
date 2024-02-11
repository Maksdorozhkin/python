# структура и синтаксис набора
my_fruit = {'apple', 'banana', 'lime'}
post_ids = {151, 258, 6458, 457}
user_inputs = {True, 'hi', '😜😜😜', 10.5}
print(dir(post_ids))

# добавление кортежа в набор
# my_set = {(10, 10), 15, 25, 103}
# print(my_set)
# print(len(my_set))

# create empy set
my_empy_set = set()
print(my_empy_set)
print(type(my_empy_set))

# методы в наборах
photo_sizes = {'1920x1080', '800x600'}
photo_sizes.add('1024x768')
print(photo_sizes)

# объединение
other_sizes = {'800x600', '2100x1534'}
# all_sizes = photo_sizes.union(other_sizes)
all_sizes = photo_sizes | other_sizes
print(all_sizes)

# пересечение наборов
# common_sizes = photo_sizes.intersection(other_sizes)
common_sizes = photo_sizes & other_sizes
print(common_sizes)

# элементы набора внутри другого большого набора
# в данном примере одно множество является подмножеством другого множества
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset((other_nums))
print(res)

### поиск одинаковых элементов
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection('d'))
print(my_set.intersection('f'))
print(my_set.intersection('abcd'))

# объединение
print(my_set.union(other_set))
print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))

# разница
print(my_set.difference(other_set))

# удаление
print(my_set.discard('d'))
print(my_set)
my_set.discard('dei') # если нет элемента метод не выдаст ошибку
# my_set.remove('def') # если нет элемента в наборе метод выдаст ошибку

# копирование
copied_set = my_set.copy()
my_set.add('t')
copied_set.add('xep')
print(my_set)
print(copied_set)

print(my_set & copied_set)

# поиск уникальных элементов набора
print(my_set.symmetric_difference(other_set))
print((my_set | other_set) - (my_set & other_set)) # объединили два набора и отняли пересечение


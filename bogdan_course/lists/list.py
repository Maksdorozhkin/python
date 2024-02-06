maks_input = [False, 'Hello', '8', '[]']
print(maks_input)
del maks_input[-1]
print(len(maks_input))

users = [
    {
        'user_id': 100,
        'user_name': 'Maks'
    },
    {
        'user_id': 101,
        'user_name': 'Andrew'
    }
]
print(users[-1]['user_name'])

# использование переменных в списках

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'
all_fruite = [my_fruit, other_fruit, new_fruit]
print(all_fruite)

# сравнение списков
print(users == all_fruite)

# получение значений из списка 
post_ids = [151, 245, 762, 167]
print(post_ids[-1])
print(post_ids[0])

# изменение значений по индексу
post_ids[1] = 8 
print(post_ids)

# удаление элементов списка 
del post_ids[-2] 
print(post_ids)

# количество элементов в списке
print(len(post_ids))

# методы в списках 
# добавление элементов в конец списка
favorite_gerl = []
favorite_gerl.append('Галя')
favorite_gerl.append('Люда')
favorite_gerl.append('Оля')
favorite_gerl.append('Надя')
print(len(favorite_gerl))
print(favorite_gerl)

# удаление элементов из списка 
favorite_gerl.pop() # удаляет последний элемент
print(favorite_gerl)
favorite_gerl.pop(0)
print(favorite_gerl)
removed_element = favorite_gerl.pop() #присваивает удаленный элемент переменной removed_element
print(removed_element)

# сортировка элементов в списке
post_ids.sort() # по возрастанию 
print(post_ids)
post_ids.sort(reverse=True)
print(post_ids)

# Конвертация в список 
greeting = "Hello Maks"
greeting_letters = list(greeting)
# print(greeting_letters)
print(list(greeting))

# встроенные функции в python(арифметические операции)
raitings = [2.5, 5.0, 3, 3.7]
print(min(raitings))
print(max(raitings))
print(sum(raitings))
print(sum(raitings)*len(raitings))

#объединение списков 
other_raitings = [0.8, 0.8, 1980]
print((raitings)+(other_raitings))

# расширить список элементами второго списка
raitings.extend(other_raitings)

# нарезка списков
first_two_ratings = raitings[:2]
print(first_two_ratings)
print(raitings[1:-1])
print(raitings[-2:])

# копирование списка вариант 1
my_cars = ['BMW', 'Lotus']
copied_cars = my_cars[:]
copied_cars.append("Audi")
print(copied_cars)
print(my_cars)
# копирование списка вариант 2
copied_cars_2 = my_cars.copy()
copied_cars_2.append('UAZ')
print(copied_cars_2)
# вариант 3 
copied_cars_3 = list(my_cars)
copied_cars_3.append('Tatra')
print(copied_cars_3)


my_nums = [10, 50, 0, 5,]
print(dir(my_nums))
my_nums.insert(2, -5) # вставляем третий элемент
print(my_nums)

my_nums.clear() # очистить список
print(my_nums)
my_nums.extend('abc')
print(my_nums)

other_nums = my_nums.copy()
print(other_nums)


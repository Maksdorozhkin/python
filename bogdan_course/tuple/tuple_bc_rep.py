# структура и синтаксис кортежей - неизменяемый тип
my_fruits = ('apple', 'banana', 'lime')
post_id = (151, 245, 762, 167)
user_inputs = (True, 'hi', 10.5, '😊😊😊')
print(user_inputs)

# кортеж словарей (словари изменять можно внутри кортежа удалить и добавить нельзя)
roomate = (
    {
        'user_id': 831,
        'user_name': 'Andrew'
    },
    {
        'user_id': 832,
        'user_name': 'Katya'
    }
)

print(roomate[0]['user_name'])

roomate[1]['user_name'] = 'Nastya'
print(roomate[1]['user_name'])

# формирование с помощью переменных
first_fruit = 'apple'
second_fruit = 'lime'
last_fruit = 'pineapple'

all_fruit = (first_fruit, second_fruit, last_fruit)
print(all_fruit)

print(len(all_fruit))
# print(all_fruit[4]) - выдаст ошибку тк всего три элемента в кортеже
if 3 > (len(all_fruit) -1):
    print('Длинна кортежа равна 3')

# кортежи можно объединить с помощью оператора +
# методы кортежей
print(post_id.count(245))
print(post_id.index(151))
# конвертация кортежа в список изменение его и конвертация обратно
post_id_list = list(post_id)
post_id_list.insert(0,100) # добавление по индексу
print(post_id_list)
post_id_tuple = tuple(post_id_list)
print(post_id_tuple)

# методы кортежей
# пример как узнать индекс элемента в кортеже если таких элементов несколько
my_nums = (10, 5, 5, 100, 0)
print(my_nums.count(5))
print(my_nums.index(5))
index_one = my_nums.index(5)
print(my_nums.index(5, index_one + 1))
my_list = list(my_nums)

# формирование кортежа из строки
my_tuple_string = tuple('abcd')
print(my_tuple_string)

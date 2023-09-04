my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('banana', 'lime', 'apple')
print(my_fruits == other_fruits)
print(len(my_fruits))
print(my_fruits[-1])

# кортежи словарей
users = (
        {
            'user_id': 134,
            'user_name': 'Maks',
            },
        {
            'user_id': 831,
            'user_name': 'Andrew',
            }
        )
print(users)
# обращение к определенному элементу кортежа
print(users[0]['user_name'])

# изменение значения словаря внутри кортежа
users[0]['user_id'] = 100
print(users)

#использование переменных
favorite_position = 'dogy'
love_in_sex = 'minet'
excites_in_sex = 'domination'

sex = (favorite_position, love_in_sex, excites_in_sex)
print(sex)

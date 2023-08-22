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

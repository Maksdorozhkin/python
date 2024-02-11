my_bike = ['ducati', 'kawasaki']
my_first_last_bike = ['kawasaki', 'ducati']
print(my_bike == my_first_last_bike)

print(len(my_bike))

print(my_bike[0])
print(my_bike[0].capitalize())
del my_bike[-1]
print(my_bike)

bikes = [
    {
        'first_bike': 'kawasaki',
        'hors_power': 72
    },
    {
        'last_bike': 'ducati',
        'hors_power': 112
    }
]
print(len(bikes))
print(bikes[-1]['hors_power'])
print(bikes.__len__())

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'pineapple'
all_fruit = ['my_fruit', 'other_fruit', 'new_fruit']
print(all_fruit)

# Копирование списков

all_fruit_copy = all_fruit[:]
print(all_fruit_copy)
all_fruit_copy2 = all_fruit.copy()
print(all_fruit)

# списки практика
res = my_bike.count('ducati')
print(res)

my_bike.append(5)

my_bike.insert(2, -5)
print(my_bike)
my_bike.clear()
print(my_bike)
my_bike.extend('abs')
print(my_bike)

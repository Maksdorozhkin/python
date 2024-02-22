# операторы

a = 10

b = a
c = a + b

print(a is b)
print(c is a)


my_car = {
    'brand': 'BMW',
    'price': 10000
}

print('brand' in my_car)
print('year' not in my_car)

# task

set_one = {True, 'hi', '😜😜😜', 10.5}
set_two = {True, 'hi', '😜😜😜', 10.5}

print(set_one == set_two)
print(set_one.__eq__(set_two))
print({True, 'hi', '😜😜😜', 10.5} is set_two)
print(set_one is set_two)
print('hi' in set_two)


# функции структура и синтаксис

a = 5
b = 3
c = a + b
print(c)

a = 8
b = 12
c = a + b
print(c)


def sum(a, b):
    c = a + b
    print(c)


a = 20
b = 10

sum(a, b)

a = 9
b = 10

sum(a, b)

print(type(sum(a, b)))


def my_fn(a1, b1):
    a1 = a1 + 1
    c1 = a1 + b1
    return c1  # функция прекращает свою работу


res = my_fn(10, 20)
print(res)


# самая короткая функция pass делает функцию не пустой чтоб python не ругался
def my_pass_function():
    pass


print(my_pass_function())


# передача неизменяемых объектов в функцию

def my_fn2(a, b):
    a2 = a + 1
    c2 = a + b
    return c2


num_one = 10
num_two = 5

res2 = my_fn2(num_one, num_two)
print(res2)
print(num_one)


# передача изменяемых объектов

def increase_person_age(person):
    print(id(person))
    person['age'] += 1
    return person


person_one = {
    'name': 'Maks',
    'age': 42
}

increase_person_age(person_one)
print(person_one['age'])
print(id(person_one))


# создание копии объекта внутри функции

def increase_person_age_copy(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Maks',
    'age': 42
}

new_person = increase_person_age_copy(person_one)

print(new_person['age'])
print(person_one['age'])

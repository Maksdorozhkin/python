from copy import deepcopy

# глубокое копирование объектов

info = {
    'name': 'Maks',
    'is learning': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Bogdan course')

print(info)
print(info_deepcopy)

print(id(info))
print(id(info_deepcopy))

# поверхностная копия

info1 = {
    'name': 'Maks',
    'is learning': True,
    'reviews': []
}

info_shallow_copy = info1.copy()

info_shallow_copy['reviews'].append('Bogdan course')

print(info1)
print(info_shallow_copy)

print(id(info1))
print(id(info_shallow_copy))

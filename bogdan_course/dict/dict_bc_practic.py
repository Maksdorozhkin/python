my_disk = {}

my_disk['brand'] = 'Kingston'
my_disk['volume'] = '1 tb.'
print(id(my_disk))
print(type(my_disk))
# print(my_disk.__doc__)
print(my_disk.items())
print(type(my_disk.items()))
print(list(my_disk.keys())) # конвертация в список
print(my_disk.popitem()) # not use this method, use del operator
print(my_disk)

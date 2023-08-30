from typing import List


my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'sumsung'
my_disk['price'] = 80
# print(my_disk)
# print(my_disk.__doc__)
# print(my_disk.items())
# print(type(my_disk.items()))
print(list(my_disk.keys()))


print(my_disk.get('type', 'hdd'))







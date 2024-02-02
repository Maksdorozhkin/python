my_disk = {}

my_disk["brand"] = "sumsung"
my_disk["price"] = 80
# print(my_disk)
# print(my_disk.__doc__)
# print(my_disk.items())
# print(type(my_disk.items()))
print(len(my_disk))


new_disc = my_disk.copy()
new_disc["type"] = "ssd"
print(my_disk)
print(new_disc)
print(id(my_disk))
print(id(new_disc))

# конвертация других элементов в словарь
# из списка списков
my_list = [["first", 0], ["second", True]]
my_dict = dict(my_list)
print(my_dict)

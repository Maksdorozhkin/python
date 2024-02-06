my_set = {1, 2, 3, 4}
my_set.add(5)
new_set = {1, 5, 6, 7, 8, 9}
common_elements = my_set & new_set
print(common_elements)
common_elements_list = list(common_elements)
print(common_elements_list)
my_list = [10, 'Maks', 2.5, True, [1,2,3]]
print(my_list)
del my_list[2]
print(my_list)
print(len(my_list))
my_list.reverse()
print(my_list)
# my_list2 = [False, -5]
# big_list = my_list + my_list2
# print(my_list + my_list2)
# print(len(big_list))


# расширить список вторым списком 
oher_list = [True, {'a':10}]
my_list.extend(oher_list)
print(my_list)
print(len(my_list))

# примеры слияния списков 
list_1 = [1, 2, 3]
list_2 = ['abc', True]
merged_list = list_1 + list_2
print(merged_list)

other_merged_list = list_1.__add__(list_2)
print(other_merged_list)





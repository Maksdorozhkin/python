my_list = [1, 'abc', 2.3, True, [1, 2, 3]]
print(my_list)
del my_list[2]
print(my_list)
print(len(my_list))
my_list.reverse()
print(my_list)
new_list = ['Maksim', 'Denis']
my_list.extend(new_list)
print(my_list)

nums = [1, 2, 3, 4, 5, 6]
text = ['a', 'b', 'c']
result = nums + text
print(result)

if hasattr(type(nums), '__add__'):
    print("Магический метод __add__ используется.")
else:
    print("Магический метод __add__ не найден.")

result2 = nums.__add__(text)
print(result2)


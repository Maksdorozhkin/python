# инструкция del

my_dict = {'a': True, 'b': 10}

del my_dict['b']
print(my_dict)

my_dict.__delitem__('a')

print(my_dict)
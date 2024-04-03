# 7.1
# ears_list = [ear for ear in range(1980, 1986)]
# print(ears_list)
# print(ears_list[3])
# print(ears_list[-1])
# things = []
# things.append("mozzarella")
# things.append('cinderella')
# things.append('salmonella')
# print(things)
# print(things[1].capitalize())
# print(things[0].upper(), things[1], things[-1].upper())
# print(things)
# del things[-1]
# print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
# print(surprise[2].capitalize())
res = surprise[2:3]
print(len(res[0]))
print(res[0][5::-1])  # перевернуть строку списка


even = [even for even in range(1, 11) if not even % 2 == 1]
print(even)

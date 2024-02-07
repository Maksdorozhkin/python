# структура и синтаксис

# my_range = range(7)
# print(type(my_range))
# print(my_range)
# print(list(my_range))

# начинаем с 10 до 1000 с шагом 3
my_range = range(10, 100, 3)
print(my_range)
print(list(my_range))
print(my_range[0])

# использование диапазонов в циклах
for n in range(10, 100, 10):
    print(n)

for l in my_range:
    print(l)

####
my_new_range = range(5)
print(my_new_range)
print(my_new_range[0])

for r in my_new_range:
    print(r)

for z in range(12, 25, 5):
    print(z)

print(list(range(12, 25, 5)))
print(set(range(12, 25, 5)))

print(dir(my_new_range))
print(my_new_range.start)
print(my_new_range.stop)
print(my_new_range.step)
print(my_new_range.index(4))
print(my_new_range.count(10))

## передать элементы из цикла for диапазона в ранее созданный список

my_range_for_task = range(10, 20, 2)
my_list_for_range = []
for m in my_range_for_task:
  my_list_for_range.append(m)
print(my_list_for_range)





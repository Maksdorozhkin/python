import copy
numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]

numbers[1:3] = "Wat?"
print(numbers)

# оператор del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes)

# function remove()
marxes.remove('Groucho')
print(marxes)

# получаем и удаляем с помощью pop() function

print(marxes.pop(-1))
print(marxes)

# clear() function удаляет все элементы списка

# index()
print(marxes.index("Chico"))

# проверяем на наличие
print("Bob" in marxes)

# count('Chico') показывает количество элементов в списке
# join()
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = '*'
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

# sorted() создает копию списка сортированного если строки то по алфавиту если цифры то по порядку
# sort() изменит список

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)


# способы копирования списков
numbers = [2, 1, 4, [8, 9]]
a = numbers.copy()
print(a)
b = list(numbers)
print(b)
c = numbers[:]
print(c)

d = copy.deepcopy(numbers)
print(d)


# итерируем по спискам с помощью for in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)

cheeses = ['brie', 'gjetost', 'havarti']
my_chose = []
for cheese in cheeses:
    if cheese.startswith('g'):
        my_chose.append(cheese)
        print("Я хочу съесть что нибудь начинающиеся на g")
        break
    else:
        print(cheese)


cheeses = ['brie', 'gjetost', 'havarti']
my_chose = []
for cheese in cheeses:
    if cheese.startswith('x'):
        my_chose.append(cheese)
        print("Я хочу съесть что нибудь начинающиеся на g")
        break
    else:
        print(cheese)
else:
    print("На х ничего не находится")


# zip() functions
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, ": drink", drink, "eat", fruit)


english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list(zip(english, french)))
print(dict(zip(english, french)))

# создаем список с помощью range

my_list = []
for number in range(1, 6):
    my_list.append(number)
print(my_list)

number_list = list(range(1, 6))
print(number_list)

# по пайтеновски
num_list = [number for number in range(1, 6)]
print(num_list)


num_list = [number-1 for number in range(1, 6)]
print(num_list)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)


rows = range(1, 4)
cows = range(1, 3)
for row in rows:
    for cow in cows:
        print(row, cow)

cells = [(row, cow) for row in rows for cow in cows]
for cell in cells:
    print(cell)

for row, cow in cells:
    print(row, cow)

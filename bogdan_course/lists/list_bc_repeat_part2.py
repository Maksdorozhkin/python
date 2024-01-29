inputs = [True, 'Hi!', '😎', 10.5]
removed_element = inputs.pop(-2)
print(removed_element)

post_ids = [1, 2, 3, 4, 7, 6]
post_ids.sort()
print(post_ids)

post_ids.sort(reverse=True)
print(post_ids)

# конвертация в список

greeting = 'Hi from madhouse'
greeting_letters = list(greeting)
print(greeting_letters)

my_dict = {'a': 10, 'b': 20}
my_dict_key = list(my_dict)
print(my_dict_key)

# арифметические операции в списках

ratings = [2.1, 2.4, 3.1, 4.5]
print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(sum(ratings) / len(ratings))

# объединение списков

my_ratings = [2, 3, 5]
all_ratings = ratings + my_ratings
print(all_ratings)

# нарезка списков

first_two_ratings = ratings[1:-1]
print(first_two_ratings)

# создаем новый список с теми же объектами

list_clone = ratings[:]
print(list_clone)

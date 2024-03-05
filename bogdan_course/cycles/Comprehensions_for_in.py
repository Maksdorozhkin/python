# сокращенный for in
# обычный цикл перебирает список и добавляет в новый список только положительные цифры
my_list = [-1, 2, 3, -4, -6, 9, 0]
absolute_nums_list = []
for nums in my_list:
    absolute_nums_list.append(abs(nums))
print(absolute_nums_list)

# пример решения данного цикла с помощью сокращенного цикла for in
absolute_nums_list2 = [abs(nums2) for nums2 in my_list]
print(absolute_nums_list2)

# пример обычного цикла но с фильтрацией
positive_nums_list = []
for nums3 in my_list:
    if nums3 > 0:
        positive_nums_list.append(nums3)
print(positive_nums_list)

# пример решения данного цикла с помощью сокращенного цикла for in
positive_nums_list2 = [nums4 for nums4 in my_list if nums4 > 0]
print(positive_nums_list2)

# пример формирования нового набора с элементами старого умноженного на себя с помощью цикла for in
my_set = {1, 10, 15}
new_set = set()
for n in my_set:
    new_set.add(n * n)
    print(new_set)

# пример решения данного цикла с помощью сокращенного цикла for in
new_set2 = set(n1 * n1 for n1 in my_set)
print(new_set2)

# пример формирования нового словаря значение ключей которого умножается на 100 с помощью цикла for in
my_score = {
    'a': 10,
    'b': 15,
    'c': 25,
}
new_score = {}

for key, value in my_score.items():
    new_score[key] = value * 100
print(new_score)

# пример решения данного цикла с помощью сокращенного цикла for in
new_score2 = {k: v * 100 for k, v in my_score.items()}
print(new_score2)

# set
new_score3 = {v1 * 10 for k1, v1 in my_score.items()}
print(new_score3)
print(type(new_score3))
# list
new_score4 = [v2 * 10 for k2, v2 in my_score.items()]
print(new_score4)
print(type(new_score4))

# формирование словаря из списка используя сокращенный цикл for in
m_list = [1, 5, 7, 9]
# тут создаем две переменные k - ключ будет индексом списка v - будет элементом из списка используем встроенную функцию enumerate
m_dict = {k: v for k, v in enumerate(m_list)}
print(m_dict)

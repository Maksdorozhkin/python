# модуль re регулярные выражения
import re

my_string = "My name is Maksim."

res = re.search('M....m$', my_string)
res = re.search('M....m\.', my_string)
print(res)
print(type(res))

# используем заранее заготовленный патерн для поиска
my_pattern1 = re.compile(r'M....m\.$')
print(my_pattern1)
print(my_pattern1.search(my_string))

my_pattern2 = re.compile(r'^My.*\.$')
print(my_pattern2.search(my_string))
print(my_pattern2.match(my_string))

my_string2 = "My name is Maks. Maks is learning"

my_pattern3 = re.compile(r'M..s')
print(my_pattern3.findall(my_string2))

# модуль re регулярные выражения
import re

my_string = "My name is Maksim."

res = re.search('M....m$', my_string)
res = re.search('M....m\.', my_string)
print(res)
print(type(res))

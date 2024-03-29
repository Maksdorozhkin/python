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


# проверка email c помощью регулярного выражения, паттерн для поиска email


email_regexp = r"^[a-zA-z0-9_.]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$"

email_check_pattern = re.compile(email_regexp)
print(email_check_pattern.fullmatch('maksdorozhkin@gmail.com'))


# функция проверки email на основе паттерна

def check_email(email):
    email_regexp = r"^[a-zA-z0-9_.]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(
        email) else "not valid"
    return (email, validation_result)


print(check_email('maksdorozhkin@gmail.com'))

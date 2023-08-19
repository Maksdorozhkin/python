# многострочные строки

info_msg = """You are
learning the easiest
programing language
Python!"""

print(info_msg)

print(type(info_msg))
print(type(str))
print(id(info_msg))

print(len(info_msg))  # len показывает длинну строки

print(info_msg[0])  # выводит первый символ строки
print(info_msg[0:4])  # выводит с первого по четвертый включая пробелы символ

print(info_msg.upper())  # метод строк делает все символы заглавными

print(info_msg.replace('language', 'язык'))

print(info_msg.count('e'))

# многострочные строки

# info_msg = """You are
# learning the easiest
# programing language
# Python!"""
#
# print(info_msg)
#
# print(type(info_msg))
# print(type(str))
# print(id(info_msg))
#
# print(len(info_msg))  # len показывает длинну строки
#
# print(info_msg[0])  # выводит первый символ строки
# print(info_msg[0:4])  # выводит с первого по четвертый включая пробелы символ
#
# print(info_msg.upper())  # метод строк делает все символы заглавными
#
# print(info_msg.replace('language', 'язык'))
#
# print(info_msg.count('e'))
long_string = ("This"
               " is long string")
long_str = """This is long 
string"""
print(long_str)
print(type(long_str))
print(type(str))
print(id(long_str))
print(long_string)
# методы строк и функции
print(len(long_string))
print(long_string[0])
print(long_string[-1])
print(long_string[0:4])  # первый индекс включительно второй не включительно
my_son = "Denis"
print(len(my_son))
print(my_son.replace('Denis', 'DENIS'))
print(my_son.count('D'))

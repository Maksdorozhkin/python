# импортирование из другого модуля (файла)
import module_practice  # as first_module чтобы переименовать модуль при импорте
# from module_practice import my_name, print_sum так делаем если нужно импортировать что то одно а не весь файл (модуль)
# from module_practice import * импортирует все из файла
# что бы переименовать переменную при импорте, from module_practice import my_name as name

print(module_practice)
print(type(module_practice))
print(dir(module_practice))
print(module_practice.my_name)

module_practice.print_sum(5, 7)

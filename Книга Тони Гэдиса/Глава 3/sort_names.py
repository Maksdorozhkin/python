# эта программа сравнивает строковые значения оператором <
# поскольку строковые данные это в илтоге цивры в ASCII то их можно сравнить
#  в итоге эта программа выстраевает имена в алфовитном порядке т.л. в ASCII цифры тоже попорядку

name1 = input('Введите имя и фамилию: ')
name2 = input('Введите еще одну фамилию и имя: ')
# показать имена в алфавитном порядке
print('Вот имена ранжированные по алфавиту: ')
if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)


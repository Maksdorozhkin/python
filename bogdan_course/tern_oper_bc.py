# тернарный оператор
# Переменная = Выражение 1 if условие else Выражение 2
my_number = 21.9
print("is int") if type(my_number) is int else print("is not int")
# напечатать текст is int если число целое иначе напечатать is not int

# тоже самое
if type(my_number) is int:
    print("Is int")
else:
    print("is not int")

# пример 2
product_qty = 10
print("in stock" if product_qty > 0 else "out of stock")

# пример 3
temp = 24
weather = "hot" if temp > 18 else "cold"
print(weather)


# практика
my_image = ('1920', '1080', True)
print(
    f"{my_image[0]}*{my_image[1]}") if len(my_image) == 2 else print("incorrect image")

# тоже самое с переменной
my_image = ('1920', '1080')
a = f"{my_image[0]}*{my_image[1]}" if len(my_image) == 2 else "incorrect image"
print(a)

# задача, переписать это с использованием if else
my_image = ('1920', '1080')
if len(my_image) == 2:
    print(f"{my_image[0]}x{my_image[1]}")
else:
    print('incorrect image')

# задача 2 проверка длинны строки с помощью тернарного оператора
my_string = "На поле танки грохотали, солдаты шли в последний бой"
print("String is short" if len(my_string) <= 79 else "String is long")
print(len(my_string))

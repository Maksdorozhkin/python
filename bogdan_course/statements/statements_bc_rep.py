# Пример if с оператором отрицания not
person_info = {
    'age': 20
}
if not person_info.get('name'):
    print("Имя отсутствует")

num_one = 10
num_two = 5
if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Both numbers are ints and positive")

# инструкция if else, выполняется если условие if ложно
my_number = 21
if type(my_number) is int:
    print("My number is integer")
else:
    print("My number is not integer")

my_phone = {
    'price': 200,
    'brand': 'apple',
}
if my_phone.get('brand'):
    print("My phone brand is", my_phone['brand'])
else:
    print("There is no phone brand")

# Инструкция if elif
my_nums = 0
if my_nums > 0:
    print("Число положительное")
elif my_nums < 0:
    print("Число отрицательное")
else:
    print("zero")

# использование if в функциях


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов целое число"
    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a} меньше {b}"


print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))

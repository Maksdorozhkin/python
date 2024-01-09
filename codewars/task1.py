# def convert_to_string(number):
#     return str(number)
# m_number = 123
# my_string = convert_to_string(m_number)
# print(my_string)

# if isinstance(my_string, str):
#     print("Переменная является строкой.")
# else:
#     print("Переменная не является строкой.")


def convert_to_string(number):
    return str(number)


number = input("введите число: ")
# m_number = 123, 999, -100
my_string = convert_to_string(number)
print(my_string)

if isinstance(my_string, str):
    print("Переменная является строкой.")
else:
    print("Переменная не является строкой.")

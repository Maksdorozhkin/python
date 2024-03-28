# Чтение и запись файлов
# test_file = open('test.txt', 'w')  # создание файла test.txt в папке python

# запись в файл \n добавляет переход на новую строку
# test_file.write("First string\n")
# test_file.write("Second string\n")

# создание и запись с помощью with это тоже самое, что и три строки выше но при использовании with метод close вызовется автоматически и вам не нужно самостоятельно закрывать файл
with open('test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    test_file.write("My string\n")

# закрываем файл чтобы его прочесть
# test_file.close()

# теперь открываем для чтения
# test_file = open('test.txt')

# чтение файла, после чтения файла его необходимо закрыть
# print(test_file.read())
# test_file.close()

# можно иначе
# with open('test.txt') as test_file:
#     print(test_file.read())
# в данном случае закрывать файл не надо

# Запись в файл в режиме "a" каждый раз будет добавлять строки
# with open('test.txt', 'a') as test_file:
#     test_file.write("First string\n")
#     test_file.write("Second string\n")
#     test_file.write("My string\n")

# with open('test.txt') as test_file:
#     print(test_file.read())
# получаем список по строкам
# with open('test.txt') as test_file:
#     print(test_file.readlines())

# # делаем итерацию по списку
# with open('test.txt') as test_file:
#     for line in test_file:
#         print(line)

# используем метод readline работает по одной строке как курсор
with open('test.txt') as test_file:
    #     print(test_file.readline())
    #     print(test_file.readline())
    #     print(test_file.readline())
    #     res = test_file.readline()
    #     print(res)
    # print(type(res))
    # используем бесконечный цикл чтобы читать построчно
    while True:
        line = test_file.readline()
        if not line:
            break
        print(line)

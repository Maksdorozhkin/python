# удаление файла


from pathlib import Path

# Создаем файл
file = open('test.txt', 'w')
file.close()  # закрываем его

my_file = Path('test.txt')
if my_file.exists():  # проверяем есть ли такой файл
    my_file.unlink()  # удаляем

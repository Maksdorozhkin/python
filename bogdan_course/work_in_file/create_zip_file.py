# модуль zipfile

from zipfile import ZipFile
from pathlib import Path

# # создаем папку и файл
# Path('my-files').mkdir()

# with open("my-files/first.txt", 'w') as my_file:
#     my_file.write("This is first file")

# with open("my-files/second.txt", 'w') as my_file:
#     my_file.write("This is second file")
# создаем файл архива zip
# with ZipFile('my-files.zip', mode='w')as my_zip_file:
#     for file in Path('my-files').iterdir():
#         print(file)
#         my_zip_file.write(file)


# Читаем архив и распаковываем
with ZipFile('my-files.zip') as my_zip_file:
    my_zip_file.extractall('my-files-unzipped')
    # print(my_zip_file.infolist())
    # print(my_zip_file.filename)

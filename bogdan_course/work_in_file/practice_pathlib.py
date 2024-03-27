# практика работы с путями и файлами
# from os import path

# print(path.curdir)
# print(path.abspath('.'))
from pathlib import Path
print(type(Path))

cwd = Path('.')

print(cwd)
# проверим является ли cwd экземпляром класса path
print(isinstance(cwd, Path))
print(type(cwd))
print(Path.__subclasses__())
print(cwd.absolute())
# создаем папку
cwd = Path(
    '/home').joinpath('md').joinpath('Documents').joinpath('python').joinpath('Django')
if not cwd.exists():  # проверяем есть ли папка и если нет создаем
    cwd.mkdir()

#  удаляем папки
if cwd.exists():  # если папка существует то удаляем
    cwd.rmdir()

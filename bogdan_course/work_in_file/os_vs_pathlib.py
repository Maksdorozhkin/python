from pathlib import Path  # из модуля pathlib импортируем класс Path
# from os import path  # из модуля os импортируем path

# используем модуль os атрибут abspath а . это текущая директория в которой лежит данный файл
# print(path.abspath('.'))
# print(type(path))


# используем pathlib, тут объектно ориентированный подход
# тут мы вызываем экземпляр класса Path и в нем передаем строку с точкой как аргумент далее используем метод absolute()
print(Path('.').absolute())

# методы класса Path

# найти путь к текущей директории
print(Path.cwd())

# формирование путей на mac и unix
print(Path('usr').joinpath('local').joinpath('bin'))
print(Path('usr')/'local'/'bin')

# формирование путей на windows
print(Path('C:/').joinpath('Users').joinpath('maks'))
print(Path('C:/') / 'Users'/'Maks')

# проверка присутствия директории или файла
print(Path('os_vs_pathlib.py').exists())

# посмотреть список файлов и папок
for f in Path('.').iterdir():
    print(f)

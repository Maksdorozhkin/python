from pathlib import Path  # из модуля pathlib импортируем класс Path
from os import path  # из модуля os импортируем path

# используем модуль os атрибут abspath а . это текущая директория в которой лежит данный файл
print(path.abspath('.'))
print(type(path))


# используем pathlib, тут объектно ориентированный подход
# тут мы вызываем экземпляр класса Path и в нем передаем строку с точкой как аргумент далее используем метод absolute()
print(Path('.').absolute())

# классы это шаблоны для объектов
# на основании шаблонов создаются экземпляры объектов их может быть много
# экземпляры могут иметь собственные атрибуты
# экземпляры наследуют атрибуты классов
# Пример класса
class Bike:  # название класса начинается с заглавной буквы
    def move(self):  # методы класса добавляют как обычные функции
        print("Мот прет")

    def stop(self):
        print("Мот заглох")


# создаем экземпляр класса и присваиваем его переменной my_bike
my_bike = Bike()
# проверяем является ли эта переменная экземпляром класса bike
print(isinstance(my_bike, Bike))  # True

# вызываем методы move и stop для конкретного экземпляра класса можно вызывать многократно
my_bike.move()  # Мот прет
my_bike.stop()  # Мот заглох
# проверим какие атрибуты доступны для экземпляра класса my_bike
print(dir(my_bike))  # в списке есть move и stop
# проверяем что атрибуты move и stop наследуются из класса bike а не являются собственными атрибутами экземпляра класса my_bike
# выводит пустой словарь это означает что собственных атрибутов у my_bike нет
print(my_bike.__dict__)
# создаем еще один экземпляр класса
my_new_bike = Bike()
# сравниваем два объекта
# False потому что это два разных экземпляра класса Bike
print(my_bike == my_new_bike)
# Добавляем собственные атрибуты для экземпляров класса, создание класса с методом __init__


class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


my_comment = Comment("Меня чуть не наебали")
my_comment.upvote()

second_comment = Comment("Я заблокировал карту")
second_comment.upvote()
print(second_comment.votes_qty)


class Image:
    def __init__(self, resolutions, title, extension):
        self.resolutions = resolutions
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolutions = new_resolution

    def ch_extensions(self, new_extensions):
        self.extension = new_extensions

    def result(self):
        return print(f"{self.resolutions} + {self.title} + {self.extension}")

    def text_upper(self):
        self.title = self.title.upper()

    def __str__(self):
        return self.title + self.extension


image1 = Image('1920x1080', 'My_photo', '.jpg')
print(image1.resolutions)
print(image1.title)

image1.resize('800x600')
print(image1.resolutions)
image1.ch_extensions('.png')
print(image1.extension)
image1.result()
image1.text_upper()
print(image1.title)
print(image1)

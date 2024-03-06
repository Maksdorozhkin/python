# преимущество генераторов их маленький размер, пример создания синтаксис
# импортируем библиотеку которая считает размер
from sys import getsizeof
# создаем генератор

squares_gen = (num * num for num in range(1000000))
print(getsizeof(squares_gen))

print(type(squares_gen))
# в генераторе нельзя получить доступ к элементу по индексу но можно провести перебор
for elem in squares_gen:
    print(elem)
    if elem == 100:
        break

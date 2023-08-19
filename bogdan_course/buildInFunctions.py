# print(10, 'Maksim', True)
# print(dir(__builtins__))

print(-5 > 0)
print('Long string' > 'Long')  # строки сравниваются посимвольно
print([1, 2, 3] == [1, 2, 3])

# конвертация в логический тип

db_is_avaible = False
print(db_is_avaible)
print(type(db_is_avaible))

db_is_avaible = True
print(db_is_avaible)
print(type(db_is_avaible))

print(bool(10))
print(bool('abc'))
print(bool([]))
print(bool([1, 3]))
print(bool(None))

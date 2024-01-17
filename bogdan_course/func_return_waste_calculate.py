# функция подсчета дробленки по формуле umt
# a - количество изделий
# b - средний вес
# c - сработано ленты
def returnable_waste_calculate(a, b, c):
    waste = ((a * b) / 1000) - c
    return waste


print(returnable_waste_calculate(208000, 6.84, 2008))


# другой пример

def waste_calc():
    a_str = input("Введи кол-во изделий: ")
    a_int = int(a_str)
    b_str = input("Введи ср.вес: ")
    b_int = float(b_str)
    c_str = input("Кол-во сработанной ленты: ")
    c_int = int(c_str)
    waste = ((a_int * b_int) / 1000) - c_int
    return waste


print(waste_calc())

print(returnable_waste_calculate(int(input("Веди количество изделий:")),
                                 float(input("Средний вес:")),
                                 int(input("Кол-во сработанной ленты: "))))

weight = float(input('Введите массу тела в килограммах: '))
weight_n = weight * 9.8
if weight_n > 500:
    print('Масса тела слишком тяжелая!')
if weight_n < 100:
    print('Масса теля слишком легкая!')
print(f'{weight_n} ньютонов')

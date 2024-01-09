fuel_consumption = 6
distance_tpm = input('Введите пройденное расстояние: ')
distance = int(distance_tpm)
gass = distance / fuel_consumption
print(f'Расход топлива составил: {gass:.1f} ')
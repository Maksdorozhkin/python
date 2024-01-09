length_ridge_tmp = input('Введите длинну гряды в метрах: ')
length_support_tmp = input('Введите длянну опоры в метрах: ')
distance_vines_tmp = input('Введите растояние между виноградными лозами в метрах: ')
length_support = float(length_support_tmp)
length_ridge = float(length_ridge_tmp)
distance_vines = float(distance_vines_tmp)
print(f"На данной гряде поместится не более:\n\t"
      f"{(length_ridge - 2 * length_support) / distance_vines:.0f} виноградных лоз")

sugar = 1.5 / 48
buter = 1 / 48
flour = 2.75 / 48
bun_tmp = input('Введите желаемое количество булочек: ')
bun = int(bun_tmp)
sugar_1 = bun * sugar
flour_1 = bun * flour
buter_1 = bun * buter
print(f"Для приготовления данного количества булочек необщодимо\n"
      f" {sugar_1:.1f} сахара\n {buter_1:.1f} масла\n {flour_1:.1f} "
      f"муки")

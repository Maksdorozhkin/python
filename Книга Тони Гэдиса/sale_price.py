# эта програма получает исходное значение и вычитает из него 20%

original_price = float(input('Введите исходное значение '))

# вычисление 20% от исходного значения

discount = original_price * 0.2

# отнимаем 20 % от исходного значения

sale_price = original_price - discount

print("Отпускная цена состовляет", sale_price)

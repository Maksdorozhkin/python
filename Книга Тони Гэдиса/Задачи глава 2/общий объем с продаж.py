# определяем цену пяти товаров
price_1 = input('Введите цену первого товара: ')
price_2 = input('Введите цену второго товара: ')
price_3 = input('Введите цену третьего товара: ')
price_4 = input('Введите цену четвертого товара: ')
price_5 = input('Введите цену пятого товара ')
# преобразуем строки в числа
price_1_1 = float(price_1)
price_2_1 = float(price_2)
price_3_1 = float(price_3)
price_4_1 = float(price_4)
price_5_1 = float(price_5)
# Складываем
full_price = price_1_1 + price_2_1 + price_3_1 + price_4_1 + price_5_1
# вычисляем процент от сложенного
tax = full_price / 100 * 7
# складываем налог с процентом
f_and_tax = full_price + tax
print(f" Налог составил {tax}")
print(f" Сумма покупок составила {full_price:}")
print(f'Итого {f_and_tax:}')

sales_volum = input('Ввведите плановую сумму общего объема продаж: ')
sales_volum_1 = float(sales_volum)
full_profit = sales_volum_1 / 100 * 23
full_profit_1 = sales_volum_1 + full_profit
print(f"Сумма процентов составила: {full_profit}")
print(f'Итого: {full_profit_1}')

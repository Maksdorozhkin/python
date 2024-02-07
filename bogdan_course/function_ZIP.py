# пример объединения (слияния)

fruits = ['apple', 'lime', 'banana', 'coconut']
quantities = [100, 30, 4, 40]
availability = [ True, False, True, True]
fruit_quant_zip = zip(fruits, quantities, availability)
print(fruit_quant_zip)
print(list(fruit_quant_zip))



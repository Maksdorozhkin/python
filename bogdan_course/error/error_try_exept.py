try:
    print('10'/0)
except ZeroDivisionError as e:
    print(e)
    print(type(e))
    # print(dir(e))
except TypeError as e:
    print(type(e))
else:
    print("Нет ошибок")
finally:
    print('Continue ...')

# любые ошибки

try:
    print(10/0)
except Exception as e:
    print(e)

# или

try:
    print(10/0)
except:
    print("Some error occurred")

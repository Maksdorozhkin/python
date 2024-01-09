x = int(input("введи x"))
y = int(input("введи у"))
if y > 0:
    if x > 0:
        print(1)
    if x == 0:
        print('Меня не наебешь, если сраный ноль ты щас введешь!')
    else:
        print(2)
else:
    if x < 0:
        print(3)
    if x == 0:
        print('Меня не наебешь, если сраный ноль ты щас введешь!')
    else:
        print(4)

def greet(name, owner):
    if name.lower() == owner.lower():
        return 'Hello Boss!'
    else:
        return 'Hello guest'

name = ('Maks')
owner = 'Maks'

print(greet(name, owner))

# def greet(name, owner):
#     return "Hello boss" if name == owner else "Hello guest"

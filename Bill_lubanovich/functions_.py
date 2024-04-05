def agree():
    return True


agree()
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')


# функция показывает является ли ее аргумент None True False
def whatis(thing):
    if thing is None:
        return None
    elif thing:
        return True
    else:
        return False


print(whatis(0.0001))

# ошибки с аргументами по умолчанию, ставить аргументом по умолчанию изменяемый объект в данном случае список


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')

# корректно


def works(arg):
    result = []
    result.append(arg)
    print(result)


works('a')
works('b')


# можно по другому решить проблему
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')
nonbuggy('b')

# аргумент *args пример использования


def print_more(req1, req2, *args):
    print('Need this one: ', req1)
    print('Need this one two: ', req2)
    print('All the rest: ', args)


print_more('cap', 'glovers', 'scarf', 'monocle', 'mustache wax')

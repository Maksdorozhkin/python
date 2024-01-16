def func1():
    result = True
    return result


def func2():
    nums = 1
    return nums


def func3():
    return 1 == 1 > 0 and 10 < 11 and 4 < 5 or 1 > 0 or 4 > 4


def func4():
    my_bike = {
        'brand': 'Ducati',
        'model': 'Monster s4r',
        'price': 420000,
        'engine_vol': 1.0,
    }
    return my_bike


def func5():
    maks_input = []
    return maks_input


if __name__ == "__main__":
    assert func1() is True
    assert isinstance(func2(), int)
    assert func3() is True
    assert isinstance(func4(), dict) and func4()
    assert isinstance(func5(), list) and not func5()

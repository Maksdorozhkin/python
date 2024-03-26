# создание функции декоратора которая проверяет аргументы основной функции
def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:  # распаковываем аргументы в список
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All argument must be int or float!")

        return fn(*args, **kwargs)
    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums(a=10.5, b='2.0'))
    print(sum_nums([1, 2, 3], '2.0'))
except ValueError as e:
    print(e)

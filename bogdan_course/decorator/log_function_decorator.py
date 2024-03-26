# пример декоратора фикция логирования

def log_function_call(fn):
    def wrapper(*args, **kwargs):
        # исполняется перед основной функцией
        print(f"Function name is {fn.__name__.upper()}")
        print(f"Function arguments is {args}, {kwargs}")
        result = fn(*args, **kwargs)
        # выполняется после основной функции
        print(f"Function result is {result}")
        return result

    return wrapper


@log_function_call  # использование декоратора
def mult(a, b):
    return a * b


print(mult(5, 2))
print("")  # просто разделил строку в выводе


@log_function_call  # применение того же декоратора к новой функции
def sum(a, b):
    return a + b


print(sum(a=10, b=10))

# пример создание декоратора
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):  # универсальные параметры
        # выполняется до функции my_function
        print("Executed before function")
        # универсальные параметры позволяют передавать в функцию любые аргументы в том числе именованные
        result = original_fn(*args, **kwargs)
        # выполняется после функции my_function
        print("Executed after function")
        return result
    return wrapper_function


@decorator_function  # применение декоратора
def my_function(a, b):
    print("This is my function!")
    return (a, b)


result = my_function(100, 50)
print(result)

# Функция декоратор проверки авторизации пользователя
def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")  # ошибка

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Выполняем действия если пользователь авторизован
    print("Result of some sensitive tasks")


try:
    do_sensitive_job()
except Exception as e:
    print(e)

import re


def check_password(password):
    password_pattern = re.compile(
        r"""^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|:"<>?`~\-=[\]\\;',./]).{8,20}$""")
    if len(password) < 8:
        return (False, "Пароль должен содержать минимум 8 символов")
    if not re.fullmatch(password_pattern, password):
        return (False, "Пароль должен содержать заглавные и строчные цифры и спецсимволы")
    return (True, "Password is valid")


while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    # проверка если в в последнем return True выводит password is valid
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])


# решение задачи на основе паттерна который создал chatgpt)

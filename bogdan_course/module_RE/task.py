import re


def check_password(password):
    password_pattern1 = r"/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}/g"
    # password_pattern2 = r"""^[!@#$%^&*()-_=+{}[]|\;:"<>,.?/]"""
    if re.search(password_pattern1, password):
        print("yes!")
    else:
        print("no!")


def get_password_from_user():
    while True:
        password = input(
            "Введите пароль состоящий минимум из 8 символов содержащий заглавные и прописные буквы и специальные символы: ")
        if len(password) < 8:
            print("Пароль должен содержать 8 символов! ")
            continue
        check_password(password)
        break


get_password_from_user()

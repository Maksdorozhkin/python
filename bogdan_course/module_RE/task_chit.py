import re


def check_password(password):
    # паттерн проверяет что в строке 8 символов при этом пробелы не считаются
    length_regexp = r"\S{8,}"
    length_pattern = re.compile(length_regexp)
    # можно одной строкой length_pattern = re.compile(r"\S{8,}")
    # паттерн проверяет буквы в нижнем регистре + означает что должна быть хоть одна буква в нижнем регистре
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    # паттерн проверяет буквы в верхнем регистре
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")  # цифры
    special_symbol_pattern = re.compile(
        r"^.*[~!@#$%^&*(){}\.]+.*$")  # спецсимволы
    no_whitespace_pattern = re.compile(r"^\S*$")  # пробелы
    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespace allowed in the password")
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol ~!@#$%^&*(){}\.")
    return (True, "Password is valid")


# print(check_password('rdf34ds   gWOW()'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('1234567A'))
# print(check_password('absdADCK'))
# print(check_password('32155ajsksHDJHJD'))
# print(check_password('32155ajsksHDJHJD)(%)'))
while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    # проверка если в в последнем return True выводит password is valid
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])

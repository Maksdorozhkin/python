# secrets модуль для генерации паролей
import secrets
import string


print(string.ascii_letters)
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)

dictionary = string.ascii_letters + string.digits + string.punctuation
print(dictionary)
print(''.join(secrets.choice(dictionary)
      for i in range(20)))  # генерация надежного пароля

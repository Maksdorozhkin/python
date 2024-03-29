# модуль random

import random
print(random.random())
print(random.randint(1, 100))
print(random.choice('abcd'))

print(random.choices([1, 2, 3, 7, 8, 9, 10, 12, 54], k=3))

# перемешивает элементы последовательности в произвольном порядке
my_list = [1, 2, 3, 7, 8, 9, 10, 12, 54]
random.shuffle(my_list)
print(my_list)

# сгенерируем пароль из 12 символов псевдо случайный пароль не надежный пароль
print(''.join(random.choices('fdjlkdfjslshjdjkhbercjhkbcz541658473zs54sa', k=12)))

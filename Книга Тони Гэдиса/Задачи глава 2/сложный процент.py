deposite = float(input('Введите депозит:'))
a_i_r = float(input('Введите годовую процентную ставку: '))
accrual_of_interest = float(input('Введи частоту начисления процентов в месяцах: '))
deposite_term = float(input('Введите срок депозита в годах: '))

result = (deposite * (1 + (a_i_r / 100) / accrual_of_interest) ** (accrual_of_interest * deposite_term))

print(f'{result:.2f}')

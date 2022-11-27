# Эта программа определяет, удовлетворяет ли клиент требованиям банка на получение ссуды

MIN_SALARY = 30000.0
MIN_YEARS = 2
salary = float(input('Введите свой годовой доход: '))
years_on_job = int(input('Введите количество лет' + 'рабочего стажа: '))
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Ваша ссуда одобрена')
    else:
        print(f'Вы должны отработать',
              f'не менее {MIN_YEARS}',
              f'лет, чтобы получить одобрение.')
else:
    print(f'Вы должны зарабатыать не менее $'
          f'{MIN_SALARY:,.2f}'
          f' чтобы получить одобрение.')

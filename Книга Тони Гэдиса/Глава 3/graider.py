# программа получает от пользователя количество балов,
# в результате назначает буквенный уровень знаний


A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

you_score = int(input('Введите свой бал: '))

if you_score >= A_SCORE:
    print(f'Твой уровень - А.')
else:
    if you_score >= B_SCORE:
        print('Твой уровень - В.')
    else:
        if you_score >= C_SCORE:
            print('Твой уровень - С.')
        else:
            if you_score >= C_SCORE:
                print('Твой уровень - D.')
            else:
                print('Твой уровень - ДАУН!')

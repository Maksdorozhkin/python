# программа расчета зароботной платы со сверхурочными или без 
# именованные константы содержат базовое количество часов и кофициэнт сверхурочного времени

BASE_HOURSE = 40
OT_MULTIPLEYER = 1.5

hourse = float(input('Введите количество отработанных часов: '))
standsrt_pay = float(input('Введите стандартную ставку сотрудника: '))

if hourse <= BASE_HOURSE:
    print(f'Ваша зп до вычетов составила: \n\t{hourse * standsrt_pay}')
else:
    overtime_hourse = hourse - BASE_HOURSE
    overtime_pay = overtime_hourse * standsrt_pay * OT_MULTIPLEYER
    gros_pay = BASE_HOURSE * standsrt_pay + overtime_pay
    print('Ваша зп до вычетом с учетом сверрхурочных составила: '
          f'\n\t{gros_pay:,.2f}')

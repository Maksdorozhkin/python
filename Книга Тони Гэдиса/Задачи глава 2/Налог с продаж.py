purchese_tmp = input('Введите сумму покупки: ')
purchese = float(purchese_tmp)
# высчитываем налоги (федеральный и региональный)
fed_tax = purchese / 100 * 5
reg_tax = purchese / 100 * 2.5
# вычисляем общий налог
oll_tax = fed_tax + reg_tax
# вычисляем общую сумму покупки
oll_price = purchese + fed_tax + reg_tax
# выводим полученные данные
print(
    f'Покупка: {purchese},\n\tФедеральный налог состатвил: {fed_tax:.2f}'
    f'\n\tРегиональный налог составил: {reg_tax:.2f}'
    f'\n\tИтого налог: {oll_tax:.2f}'
    f'\n\tИтого к оплате: {oll_price:.2f}'
)

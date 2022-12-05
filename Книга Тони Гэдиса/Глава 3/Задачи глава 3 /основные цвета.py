MAIN_COLOR_1 = 'красный'
MAIN_COLOR_2 = 'желтый'
MAIN_COLOR_3 = 'синий'
ERROR = 'Вы ввели не основной цвет. Основными являются красный, синий, желтый!'

user_color_1 = input('Введите первый основной цвет для смешивания: ')
user_color_2 = input('Введите второй основной цвет для смешивания: ')

if user_color_1 == MAIN_COLOR_1 and user_color_2 == MAIN_COLOR_2:
    print('При смешивании желтого и красного вы получите оранжевый.')
elif user_color_1 == MAIN_COLOR_2 and user_color_2 == MAIN_COLOR_1:
    print('При смешивании желтого и красного вы получите оранжевый.')

elif user_color_1 == MAIN_COLOR_1 and user_color_2 == MAIN_COLOR_3:
    print('При смешивания красного и синего вы получите фиолетовый.')
elif user_color_1 == MAIN_COLOR_3 and user_color_2 == MAIN_COLOR_1:
    print('При смешивания красного и синего вы получите фиолетовый.')

elif user_color_1 == MAIN_COLOR_2 and user_color_2 == MAIN_COLOR_3:
    print('При смешивании желтого и синего вы получите зеленый.')
elif user_color_1 == MAIN_COLOR_3 and user_color_2 == MAIN_COLOR_2:
    print('При смешивании желтого и синего вы получите зеленый.')
else:
    print(ERROR)

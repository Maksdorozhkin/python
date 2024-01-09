triangle1_length = float(input('Введите длину первого треугольника: '))
triangle1_width = float(input('Введите ширину первого треугольника: '))
triangle2_length = float(input('Введите длину второго треугольника: '))
triangle2_width = float(input('Введите ширину второго треугольника: '))
area_triangle1 = triangle1_length * triangle1_width
area_triangle2 = triangle2_length * triangle2_width
if area_triangle1 > area_triangle2:
    print(f'Площадь первого дреугольника равна {area_triangle1:,.2f}, /'
          f'она больше второго!')
if area_triangle2 > area_triangle1:
    print(f'Площадь второго треугольника равна {area_triangle2:,.2f}, /'
          f'она больше площади первого!')
if area_triangle1 == area_triangle2:
    print('Треугольники равны')
# else:
#     print('Че за хуйню ты ввел?')

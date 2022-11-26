man_tmp = input('Ведите количество юношей в вашей группе: ')
woman_tmp = input('Введите количество девушек в вашей группе: ')
man = int(man_tmp)
woman = int(woman_tmp)
oll_people = man + woman

man_p = man / oll_people * 100
woman_p = woman / oll_people * 100
print(
    f'Соотношение студентов в вашей группе составило:\nюношей {man_p:.1f}%\n'
    f'девушек {woman_p:.1f}%'
)

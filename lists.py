b = ['ducati', 'kawasaki', 'honda', 'harley']
print(b)
popped_b = b.pop()
print(b)
print(popped_b)


b = ['ducati', 'kawasaki', 'honda', 'harley']
l_o = b.pop(0)
print(f"The last bike i ownet was a {l_o.title()}.")



b = ['ducati', 'kawasaki', 'honda', 'harley']
f_b = b.pop(1) #вырезает из списка элемент
print(f"My first bike was a {f_b.title()}.")
print(b)


b = ['ducati', 'kawasaki', 'honda', 'harley']
b.remove('honda') #удаляет из списка элемент
print(b)

b = ['ducati', 'kawasaki', 'honda', 'harley']
print(b)
exp = 'harley'
b.remove(exp) #удаляет переменную exp
print(b)
print(f"\nA {exp.title()} is too expensive for me.") # выводит сообщение + заначение переменной exp

g = ['куба', 'андрей', 'alex']
print(f"\n {g[0].title()}, приходи ко мне на обед")
print(f"\n {g[1].title()}, приходи ко мне на обед")
print(f"\n {g[-1].title()}, приходи ко мне на обед")
print(f"\n к сожалению {g[0].title()}, прийти не сможет")
g[0] = 'Славик'
print(f"\n {g[0].title()}, приходи ко мне на обед")
print(f"\n {g[1].title()}, приходи ко мне на обед")
print(f"\n {g[-1].title()}, приходи ко мне на обед")
g.insert(0, 'жанна')
g.insert(2, 'виталя')
g.append('никита')
print(f"\n {g[0].title()}, приходи ко мне на обед")
print(f"\n {g[1].title()}, приходи ко мне на обед")
print(f"\n {g[2].title()}, приходи ко мне на обед")
print(f"\n {g[3].title()}, приходи ко мне на обед")
print(f"\n {g[4].title()}, приходи ко мне на обед")
print(f"\n {g[-1].title()}, приходи ко мне на обед")
mes = "\n на обед приглошаются только два гостя"
print(mes)
pos = g.pop(1)
print(f"\n {pos.title()}, я тебя кинул")
pos1 = g.pop(2)
pos2 = g.pop(3)
pos4 = g.pop(-2)
print(f"\n {pos1.title()}, я тебя кинул")
print(f"\n {pos2.title()}, я тебя кинул")
print(f"\n {pos4.title()}, я тебя кинул")
print(f"\n {g[-1].title()}, приглошение остается в силе!")

print(f"\n {g[-2].title()}, приглошение остается в силе!")
del g[-2]
del g[-1]
print(g)

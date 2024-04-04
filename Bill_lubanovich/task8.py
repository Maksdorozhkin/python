# 8.1
english = 'dog', 'cat', 'walrus'
french = 'chien', 'chat', 'morse'
e2f = dict(zip(english, french))
print(e2f)
# 8.2
print(e2f['walrus'])
# 8.3 поменять местами ключи и значения в словаре
f2e = {v: k for k, v in e2f.items()}
print(f2e)
# 8.4
print(f2e['chien'])
# 8.5
print(set(e2f))
# 8.6
life = {
    'animals': {'cats': {}, 'octopi': {}, 'emus': {}},
    'plants': {},
    'other': {},
}
print()
print(life['animals'].keys())

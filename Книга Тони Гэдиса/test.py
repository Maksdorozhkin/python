sec = float(input('сек: '))
hours = sec // 3600

minutes = (sec // 60) % 60

seconds = sec % 60

print(hours, minutes, seconds)

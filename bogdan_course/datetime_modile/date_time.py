# модуль datetime
from datetime import date
from datetime import time
from datetime import datetime
# my_date = date(2100, 6, 5)
# print(my_date)
# print(my_date.day)

# print(my_date.isocalendar())

# my_time = time(18, 10, 45)
# print(my_time)
# print(my_time.hour)
# print(my_time.minute)
# print(my_time.second)

my_datetime = datetime(2024, 3, 29, 12, 29, 00)
# print(my_datetime)
# print(my_datetime.isoformat())
# print(my_datetime.now().microsecond)

print(my_datetime.strftime('%d-%b-%Y'))  # отображение даты в читаемом формате
# отображение времени в читаемом формате
print(my_datetime.strftime('%d-%b-%Y %H:%M:%S'))

# конвертация из строки
date_str = '29-Mar-2024'
convert_str = datetime.strptime(date_str, '%d-%b-%Y')
print(convert_str)

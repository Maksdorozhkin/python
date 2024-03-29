from datetime import datetime, timedelta

my_datetime = datetime(2024, 3, 29, 12, 29, 00)

print(timedelta)
# к нашей дате добавляем 100 дней, можно использовать минус и отнимать от нашей даты время и дату
print(my_datetime + timedelta(days=100, minutes=120, hours=2))

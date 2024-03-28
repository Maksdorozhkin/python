# работа с csv файлами
# создание
import csv
# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5234, 'Maks', 1352])
#     writer.writerow([5264, 'Nyc', 12])
#     writer.writerow([5224, 'Lol', 13])
#     writer.writerow([5236, 'Chikas', 52])


# чтение csv файла
with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
    for line in reader:
        print(line)
    print(reader.line_num)

# пример цикла while
i = 10
while i <= 100:  # цикл работает пока i < 100
    print(i)
    i += 10  # прибавляем к i 10

# выход из цикла с помощью brake

while True:
    answer = input("Enter yes or no: ")
    if answer == 'no':
        break

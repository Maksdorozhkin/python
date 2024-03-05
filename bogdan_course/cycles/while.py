import random
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

# использование continue
random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print("Try again")
        continue
    print("Congratulation!", random_num)
    break

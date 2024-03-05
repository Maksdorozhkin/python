while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter last number: "))
    print(f"{num1 / num2}")
    answer = input("You wont begin? Answer yes or no: ")
    if answer == 'no':
        break

# задача просит ввести 2 числа делит одно на другое спрашивает хочу повторить если нет цикл повторяется

while True:  # запускает бесконечный цикл
    try:  # если вводим не число выдает ошибку и просит ввести число
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter last number: "))
    except ValueError as e:
        print(e)
        print("Enter number!")
        continue  # завершает эту часть если ошибка
    print(num1 / num2)
    answer = input("You wont begin? Answer yes or no: ")
    if answer == 'no':
        break

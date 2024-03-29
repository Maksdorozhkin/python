# колбэк функции
# пример использования
# добавление описания к функции

def print_number_info(num):
    """Функция выясняет четное ли число"""
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):
    print("Square num is", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number: '))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)


# пример 2

def send_data(data):
    # sending data to the remote server
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated data
    send_data_fn(updated_data)


process_data({'name': 'Maks'}, send_data)

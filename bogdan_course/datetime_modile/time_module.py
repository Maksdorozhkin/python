# модуль time позволяет замерять время
import time
print(time.time())  # показывает текущее время в секундах с начала unix эпохи
print(time.ctime(1711705973.7401152))  # конвертирует в читаемый формат

# как остановить время
time.sleep(2.5)
print(time.time())  # ожидаем 2,5 секунды и получаем еще один вывод

# как замерить время выполнения определенной программы или задачи

start_time = time.time()
my_range = (range(1000000))
print(my_range[1000])
end_time = time.time()
print("Total durations of the operations: ", end_time - start_time)

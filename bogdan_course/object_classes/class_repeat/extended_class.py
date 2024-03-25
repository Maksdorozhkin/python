# наследование из других классов
class ExtendedList(list):
    def print_list_info(self):
        print(f"Список содержит {len(self)} элементов")


custom_list = ExtendedList([3, 5, 1])

custom_list.print_list_info()
# создание подклассов
# добавляем новый элемент в custom_list
custom_list.append(7)
custom_list.print_list_info()

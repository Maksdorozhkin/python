from pathlib import Path
# создаем папку Files в директории python
file_dir = Path('files')
file_dir.mkdir(exist_ok=True)  # если папка уже есть ошибки не будет

# создаем экземпляры класса path
first_file = Path(file_dir / 'first.txt')
second_file = Path(file_dir / 'second.txt')

with open(first_file, 'w') as f:  # создаем файл с двумя строками
    f.write("First line \n")
    f.write("Second Line \n")

with open(second_file, 'w') as f:  # создаем второй файл с двумя строками
    lines = [
        "First line in the second file",
        "Second line in the second file",
        "Last line in the second file"
    ]
    for line in lines:
        f.write(line + '\n')
# прочтем первый файл
with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    for line in f.readlines():
        print(line)

# удаляем файлы
first_file.unlink()
second_file.unlink()

# удаляем папку
file_dir.rmdir()

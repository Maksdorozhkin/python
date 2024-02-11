def my_name(name):
    print(name.capitalize())


my_name("maks")


def my_name(name):
    print(name.capitalize())
    my_name(name)


my_name("maks")

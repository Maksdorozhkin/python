class Image:
    def __init__(self, resolution, title, extension):
        self.resolutions = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolutions):
        self.resolutions = new_resolutions

    def __str__(self):
        return f"{self.title.upper()}.{self.extension}"


my_image = Image('1920x1080', "My face", 'jpj')
print(my_image.resolutions)
print(my_image.title)
print(my_image.extension)


my_image.resize('4000x3000')

print(my_image.resolutions)


second_image = Image('800x600', 'my bike', 'png')
print(my_image)
print(second_image)

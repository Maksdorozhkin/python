class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
# print(my_car)
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(dir(my_car))
my_car.move()
my_car.stop()
my_second_car = Car()
print(my_car == my_second_car)
print(id(my_car), id(my_second_car))


class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def sum(self):
        self.votes_qty += self.votes_qty


my_comment = Comment("My comment")

my_comment.upvote()
my_comment.upvote()
my_comment.upvote()
my_comment.upvote()
my_comment.upvote()
my_comment.upvote()
my_comment.sum()

print(my_comment.votes_qty)
print(isinstance(my_comment, Comment))
print(type(my_comment) == Comment)

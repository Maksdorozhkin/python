# магические методы в классах, создание

class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):  # добавили магический метод __add__
        return [f"{self.text} {other.text}", self.votes_qty + other.votes_qty]


f_comment = Comment("First comment")
f_comment.upvote()
s_comment = Comment("Second comment")
s_comment.upvote()
s_comment.upvote()

print(f_comment + s_comment)

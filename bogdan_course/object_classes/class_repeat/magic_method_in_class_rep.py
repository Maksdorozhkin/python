# магические методы классов создание
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    # добавление магического метода с описанием сложения, можно заменить на список добавив [], можно словарь тогда код будет {'text':f"{self.text} {other.text}", 'total_votes_qty': self.votes_qty + other.votes_qty}
    def __add__(self, other):
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)

    def __eq__(self, other):  # добавил магический метод сравнения двух комментариев
        return self.text == other.text and self.votes_qty == other.votes_qty


one_comment = Comment("Первый комментарий")
one_comment.upvote()
new_comment = Comment("Второй коммент")
new_comment.upvote()
# new_comment.upvote()

# как можно сложить два комментария, для этого нужно добавить в класс магический метод __add__ и в нем описать как мы хотим суммировать два комментария
# теперь при использовании оператора + python найдет магический метод и сложит два комментария
print(one_comment + new_comment)  # ('Первый коммент Второй коммент', 2)
print(one_comment == new_comment)  # False

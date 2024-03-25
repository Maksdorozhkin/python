# атрибуты класса

class Comment:
    total_comment = 0  # собственный атрибут

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        # изменяем значение атрибута класса, каждый раз когда будет создаваться новый экземпляр класса значение будет изменяться на 1
        Comment.total_comment += 1

    def upvote(self):
        self.votes_qty += 1


my_comment = Comment("Меня чуть не наебали")
print(Comment.total_comment)
new_comment = Comment("Я вовремя понял")
print(Comment.total_comment)
# собственные атрибуты классов наследуются экземплярами класса
print(my_comment.total_comment)
# изменяем значение унаследованного собственного атрибута
my_comment.total_comment = 10
print(Comment.total_comment)  # значение атрибута класса не изменилось
print(my_comment.total_comment)  # значение изменилось на 10
Comment.total_comment = 10  # меняем значение собственного атрибута класса
print(Comment.total_comment)

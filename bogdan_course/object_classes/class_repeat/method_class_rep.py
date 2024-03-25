# методы экземпляров и классов
# в данном случае text это атрибут, а upvote метод
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


my_comment = Comment("Меня чуть не наебали")
# привязанные методы bound method, метод считается привязанным если у него первый параметр self

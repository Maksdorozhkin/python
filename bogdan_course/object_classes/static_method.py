class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod  # статический метод
    def merge_comment(first, second):
        return f"{first} {second}"

    @staticmethod
    def sum_nums(one, two):
        return one + two


my_comment = Comment("My comment")

m_1 = Comment.merge_comment("Thanks!", "Excellent.")
print(m_1)
m_2 = Comment.merge_comment("Great", "OK")
print(m_2)

m_3 = Comment.sum_nums(5, 6)
print(m_3)


# атрибуты класса

class Mycomment:
    total_comment = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Mycomment.total_comment += 1


f_comment = Mycomment("First comment")
print(Mycomment.total_comment)
s_comment = Mycomment("Second comment")
print(Mycomment.total_comment)
print(f_comment.total_comment)
f_comment.total_comment = 10
print(Mycomment.total_comment)
print(f_comment.total_comment)

class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comment(first, second):
        return f"{first} {second}"


my_comment = Comment("My comment")

m_1 = Comment.merge_comment("Thanks!", "Excellent.")
print(m_1)
m_2 = Comment.merge_comment("Great", "OK")
print(m_2)

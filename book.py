
class book:
    def __init__(self, title, author, ISBN, is_available ):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available

    def __str__(self):
        return f"name of book : {self.title} name of author : {self.author}"
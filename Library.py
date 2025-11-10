class Library:

    def __init__(self):
        self.list_of_book=[]
        self.list_of_users=[]

    def add_book(self,book):
        self.list_of_book.append(book)

    def add_user(self,user):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        user = None
        for u in self.list_of_users:
            if u.id == user_id:
                user = u
        return user    
        

        




















# if __name__ == '__main__':
#     lib = Library()
#     lib.list_of_users.append({"id": 12})
#     print(lib.borrow_book(152, None))
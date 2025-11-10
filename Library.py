import json

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
        book = None
         
        for u in self.list_of_users:
            if u.id == user_id:
                user = u
                for b in self.list_of_book:
                    if b.ISBN == book_isbn:
                        book=b
                        book.is_available=False
                        user.borrowed_books.append(book)
        return f"{user},{book}"
    

    def return_book(self,user_id, book_isbn):
        user = None
        book = None
         
        for u in self.list_of_users:
            if u.id == user_id:
                user = u
                for b in self.list_of_book:
                    if b.ISBN == book_isbn:
                        book=b
                        book.is_available=True
                        user.borrowed_books.remove(book)
        return f"{user},{book}"


    def list_available_books(self):
        return self.list_of_book

    @staticmethod
    def read_data_json(data_json):
        with open(data_json) as data:
            data_string = json.load(data)
        return data_string
    
    @staticmethod
    def add_data_to_json(data_json):
        pass


        




















# if __name__ == '__main__':
#     lib = Library()
#     lib.list_of_users.append({"id": 12})
#     print(lib.borrow_book(152, None))
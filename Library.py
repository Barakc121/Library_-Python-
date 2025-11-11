import json

BOOKS_PATH_JSON = "data/data_books.json"



class Library:

    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def add_book(self,book):
        self.list_of_books.append(book)

    def add_user(self,user):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        user = ""
        for i in self.list_of_users:
            if i.id == user_id:
                user = i
        if user == "":
            return "the user is not exist"
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if book.is_available:
                    book.is_available=False
                    user.borrowed_books.append(book)
                else:
                    return "The book is not available"
            return "The book is not found"
    

    def return_book(self,user_id, book_isbn):
        user=None
        book=None

        for u in self.list_of_users:
            if u.id ==user_id:
                user=u

        if user == None:
                return "user anavilable"
        for book in self.list_of_books:
            if book.ISBN == book_isbn and book.is_available == False:
                book.is_available=True
                user.borrowed_books.remove(book)
                return "the book is back"
            else:
                return "where is the book"



    def list_available_books(self):
        list_available=[]
        for i in self.list_of_books:
            if i.is_available == True:
                 list_available.append(vars(i))
        return list_available

    def search_book(self, input):
        for book in self.list_of_books:
            if book.title == input or book.author == input:
                return vars(book)
        return "book not found"
        
    
    @staticmethod
    def read_data_json(data_json):
        print(data_json)
        with open(data_json) as data:
            return json.load(data)
    
    @staticmethod
    def add_data_to_json(data_json,data):
        with open(data_json,"w") as f:
            json.dump(data, f, indent=4)
    




# print(Library.read_data_json(BOOKS_PATH_JSON))

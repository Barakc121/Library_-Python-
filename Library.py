import json

class Library:

    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def add_book(self,book):
        self.list_of_books.append(book)

    def add_user(self,user):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        pass
    

    def return_book(self,user_id, book_isbn):
        pass


    def list_available_books(self):
        pass

        list_available=[]
        for i in self.list_of_books:
            if i.is_available == True:
                 list_available.append(i.ISBN)
        return list_available

    def search_book(self,input):
        for i in [b for b in self.list_of_books if b.is_available == True]:
            if i.title==input or i.author==input:
                return f" the book here"        
            
    @staticmethod
    def read_data_json(data_json):
        with open(data_json)as data:
            data_string=json.load(data)
        return data_string
    
    @staticmethod
    def add_data_to_json(data_json):
        pass

    @staticmethod
    def add_data_of_json(data_json,data):
        print(data)
        with open(data_json,"w")as f:
            json.dump(data, f, indent=4)


# if __name__ == '__main__':
#     name_libar=Library()

#     barak=User("barak",11911)
#     tora=Book("tiire","bkaa",911)
#     name_libar.add_book(tora)
#     print(name_libar.borrow_book(111,11))
#     print(name_libar.list_available_books())

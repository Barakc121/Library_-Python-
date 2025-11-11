class User:
    id=1
    def __init__(self,name):
        self.name=name
        self.id=User.id
        self.borrowed_books=[]
        User.id +=1

    def __str__(self):
        return f"name of user :{self.name}"
# class BookShelf:
#     def __init__(self,quantity):
#         self.quantity=quantity

#     def __str__(self):
#         return f"BookShelf with {self.quantity} books"
    
# shelf=BookShelf(300)

# print(shelf)

class Bookshelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"Book: {self.name}"
    
book =Book("Harry Potter")
book2=Book("Python ")
shelf=Bookshelf(book,book2)

print(shelf)
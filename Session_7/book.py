class Book:

    def __init__(self, title, author, page, current_page):
        self.title = title # the name can be the same
        self.author = author
        self.current_page = current_page
        self.bookmark = 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def bookmark_page(self):
        self.bookmakr - self.current_page

    def turn_page(self):
        self.current_page += 1
    
my_book = Book("A great book", "me")
print(my_book)

# The way you initialise an object is up to you
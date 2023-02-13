class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    
b1=Book(150)
b2=Book(200)
b3=Book(220)
b4=Book(110)
b5=b1 + b2
b6=b3 + b4
b7=b5 + b6
print("Total number of pages in the book: ",b7)


class Book:
    title=""
    pages=0
    def __init__(self,t,p):
        self.title=t
        self.pages=p
    def __add__(self,other):
        return(Book(self.title,self.pages+other.pages))

a= Book("B",30)
b=Book("A",40)
c= a+b
print(c.pages)
class Book:
    title=""
    pages=0
    def __init__(self,t,p):
        self.title=t
        self.pages=p
    def __add__(self,other):
        return(Book(self.title,self.pages+other.pages))
a=Book("fairytail",60)
b=Book("one piece",70)
c=b+a
print(c.pages)
print(c.title)
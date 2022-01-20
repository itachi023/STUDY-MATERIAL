class complex:
    def read(self):
        print("a+ib and x+iy")
        self.a=int(input("Enter a="))
        self.b=int(input("Enter b="))
        self.x=int(input("Enter x="))
        self.y=int(input("Enter y="))
        self.ch=input("Enter - or *")
    def comp(self):
        if(self.ch=='-'):
            print(f"(a+ib)-(x+iy) = {self.a-self.x}+{self.b-self.y} ")
        elif(self.ch=='*'):
            print(f"(a+ib)*(x-iy)= {(self.a*self.x)-(self.b*self.y)}+i{self.a*self.y+self.b*self.x} ")
        else:
            print("invalid")
ob=complex()
ob.read()
ob.comp()

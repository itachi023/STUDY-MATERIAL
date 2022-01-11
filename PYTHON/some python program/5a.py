class complex:
    def read(self):
        print("a+ib and x+iy")
        self.a=int(input(" Enter a=:"))
        self.b=int(input(" Enter b=:"))
        self.x=int(input(" Enter x=:"))
        self.y=int(input(" Enter y=:"))
        self.ch=input(" Enter-or *")

    def comp(self):
        if(self.ch=='-'):
            print(" a+ib - x+iy = %d + i %d"%(self.a-self.x,self.b-self.y))
        elif(self.ch=='*'):
            print(" a+ib * x+iy = %d + i %d"%(self.a*self.x-self.b*self.y,self.a*self.y+self.b*self.x))
        else:
            print("INVALID")

ob=complex()
ob.read()
ob.comp()

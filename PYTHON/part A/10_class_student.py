class student:
    nm=""
    usn=""
    def read(self):
        self.nm=input("enter the name\n")
        self.usn=input("enter the usn\n")
    def display(self):
        print(f"name is {self.nm}\nusn is {self.usn}")

s=student()
s.read()
s.display()

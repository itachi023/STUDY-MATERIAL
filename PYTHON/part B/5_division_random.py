import random

try:
    a=random.randint(0,5)
    b=random.randint(0,5)
    c=a/b
    f=open("res.txt","w")
    f.write(f" {a}/{b} = {c} ")
    f.close()
    r=open("res.txt").read()
    print("content of files are: ",r)
except:
    print("Error! denominator is zero")
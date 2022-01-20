with open("text.txt","r") as f:
    r= f.read()

with open("copy.txt","w") as f:
    f.write(r)
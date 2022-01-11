f= open("text.txt","r")
i=0
while(f.readline()!=""):
    i+=1
print("no. of lines ",i)
f.close()
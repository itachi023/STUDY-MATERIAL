with open("prime.txt","w") as f:
    for i in range(2,1001):
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            f.write(str(i)+"\n")

with open("count.txt","w") as f:
    for i in range(1001):
        f.write(str(i)+"\n")
r1=open("prime.txt").read()
r2=open("count.txt").read()

for i,j in ((x,y) for x in r1.split() for y in r2.split()):
    if(i==j):
        print(i,end="  ")
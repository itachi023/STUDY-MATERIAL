for i in range(2,int(input("enter the range\n"))+1):
    for x in range(2,i):
        if(i%x==0):
            break
    else:
        print(i,end=",")

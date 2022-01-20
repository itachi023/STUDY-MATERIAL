#find number which divisible 7 and not a multiple of 5

for i in range(2000,3200+1):
    if i%7==0:
        if i%5!=0:
            print(i,end=",")
        else:
            pass
    else:
        pass
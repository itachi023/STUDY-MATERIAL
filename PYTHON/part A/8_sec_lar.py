l=[]
for i in range(0,int(input("Enter the no. item in list\n"))):
    l.append(int(input("Enter item: ")))
l.sort()
print(f"second largest is {l[-2]} and second smallest is {l[1]} ")
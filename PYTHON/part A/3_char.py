# length and no. of character in given string
sentence=input("enter the string\n")
# l=0
a=sentence.split()

print("No. words is ",len(a))

for i in a:
    print(f"length of {i} is {len(i)}")
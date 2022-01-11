st=input("enter the string\n")
d={}
for i in st.split():
    if(i[0] in d.keys()):
        d[i[0]].append(i)
    else:
        d.update({i[0]:[i]})
print(d)
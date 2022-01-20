from tkinter import * # import all the functions of ktinter 

def comp(): #function invoked from submit button
    x=op.get()
    if(x==1): # addition a+b
        res=(var1.get()+var2.get())
    elif x==2: # difference a-b
        res=(var1.get()-var2.get())
    else:
        res=(var1.get()+var2.get())/2 # average of a & b
    var.set(res)
    if(res<0):
        l1.config(fg="red") # changes color of text in result if <0

root=Tk() # master window
root.title(" Compute")# change title from tk to compute
var1=IntVar()
var2=IntVar()
var=StringVar()
op=IntVar()
Label(master=root,font=4,text="a=").grid(row=0,column=0)#Label & grid to together 
e1=Entry(root,bd=4,text=var1)# variable for Entry to use get function
e1.grid(row=0,column=1)
Label(master=root,font=4,text="b=").grid(row=1,column=0)
e2=Entry(root,bd=4,text=var2)
e2.grid(row=1,column=1)
# Radiobutton
Radiobutton(root,text="sum",variable=op,value=1).grid(row=2,column=0)# for addition
Radiobutton(root,text="diff",variable=op,value=2).grid(row=3,column=0)# for differnce
Radiobutton(root,text="avg",variable=op,value=3).grid(row=4,column=0)# for average

Button(root,text="Submit",font=4,bd=3,command=comp).grid(row=5,column=0)# submit button to invoke comp function
Label(root, font=4,text="Result=").grid(row=6,column=0)
l1=Label(root,textvariable=var)
l1.grid(row=6,column=1)
root.mainloop()

from tkinter import *
from tkinter import messagebox

def comp():
    tot= (m1.get()+m2.get())
    avg= tot/2
    messagebox.showinfo("marks",avg)
root=Tk()
m1=IntVar()
m2=IntVar()

Label(root,text="Name :").pack()
Entry(root).pack()

Label(root,text="Marks1 :").pack()
Entry(root,textvariable=m1).pack()
Label(root,text="Marks2 :").pack()
Entry(root,textvariable=m2).pack()

Button(root,text="SUBMIT",command=comp).pack()
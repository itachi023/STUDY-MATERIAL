from tkinter import *
from tkinter import messagebox

def comp():
    tot=(m1.get()+m2.get()+m3.get()+m4.get())
    avg=tot/4
    messagebox.showinfo("",f"average is {avg} \nsum is {tot}")
root=Tk()
root.geometry("500x500")
m1=IntVar()
m2=IntVar()
m3=IntVar()
m4=IntVar()

Label(root,text="Name :").pack()
Entry(root).pack()

Label(root,text="Marks1 :").pack()
Entry(root,textvariable=m1).pack()
Label(root,text="Marks2 :").pack()
Entry(root,textvariable=m2).pack()
Label(root,text="Marks3 :").pack()
Entry(root,textvariable=m3).pack()
Label(root,text="Marks4 :").pack()
Entry(root,textvariable=m4).pack()

Button(root,text="SUBMIT",command=comp).pack()
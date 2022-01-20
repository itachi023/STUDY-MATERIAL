from tkinter import *
from tkinter import filedialog
root = Tk()
root.fn=filedialog.askopenfilename(initialdir="/",filetypes=(("Python files",".py"),("All files","*.*")))

print(root.fn)
root.title=root.fn
t=open(root.fn).read()
T=Text(root,height=100,width=100)
T.pack()
T.insert(END,t)
root.mainloop()

#collecting data
from tkinter import *

class gui:
    def __init__(self, parent): 
        Label(parent,text="name").grid()
        gui.name = Entry (parent,width=20)
        gui.name.grid()
        Label(parent,text="age").grid()
        gui.age = Entry (parent,width=20)
        gui.age.grid()  
        self.select=StringVar()
        self.select.set(0)
        self.ans = ['Yes','No']
        for item in self.ans:
            gui.input=Radiobutton(text=item,value=item,variable = self.select)
            gui.input.grid()
        enter=Button(parent,text="save",command=self.save)
        enter.grid()
        self.info = []

    def save(self):
        self.info.append([gui.name,gui.age,gui.input])

root = Tk()
gui(root)
root.mainloop()
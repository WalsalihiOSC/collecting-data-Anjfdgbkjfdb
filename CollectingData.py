#collecting data
from tkinter import *

class gui:
    def __init__(self, parent): 
        self.f1=Frame(parent)
        self.f1.grid()
        Label(self.f1,text="name").grid()
        gui.name = Entry (self.f1,width=20)
        gui.name.grid()

        Label(self.f1,text="age").grid()
        gui.age = Entry (self.f1,width=20)
        gui.age.grid()  

        self.select=StringVar()
        self.select.set(0)
        self.ans = ['Yes','No']
        for item in self.ans:
            gui.input=Radiobutton(self.f1,text=item,value=item,variable = self.select)
            gui.input.grid()

        enter=Button(self.f1,text="save",command=self.save)
        enter.grid()
        Button(self.f1,text="show", command=self.show).grid()
        self.info = []

        
        self.f2=Frame(parent)
        self.f2.grid()
        self.f2.grid_forget()
        Label(self.f2,text="name").grid()
        Button(self.f2,text="Enter data", command=self.enter_data).grid()


    def save(self):
        self.info.append([gui.name,gui.age,gui.input])
        Label(self.f1,text=self.info).grid()

    def show(self):
        self.f1.grid_forget()
        self.f2.grid()

    def enter_data(self):
        self.f2.grid_forget()
        self.f1.grid()

    



root = Tk()
gui(root)
root.mainloop()
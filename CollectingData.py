#collecting data
from tkinter import *

class gui:
    def __init__(self, parent): 
        data.setup(self)
    # Frame 1 =====================================================================================================
        gui.f1=Frame(parent)
        self.f1.grid()
        Label(gui.f1,text="name").grid()
        gui.name = Entry (gui.f1,width=20)
        gui.name.grid()
        Label(gui.f1,text="age").grid()
        gui.age = Entry (gui.f1,width=20)
        gui.age.grid()  
        for item in data.ans:
            gui.input=Radiobutton(gui.f1,text=item,value=item,variable = data.select)
            gui.input.grid()
        enter=Button(gui.f1,text="save",command=data.save)
        enter.grid()
        Button(gui.f1,text="show", command=data.show).grid()
        gui.info = [""""""]

        # Frame 2 ========================================================================================================
        
        gui.f2=Frame(parent)
        gui.f2.grid()
        gui.f2.grid_forget()
        Button(gui.f2,text="Enter data", command=data.enter_data).grid()
        gui.info_text=Label(gui.f2, text="")
        gui.info_text.grid()
        Button(gui.f2,text="next", command=data.next).grid()
        Button(gui.f2,text="prev", command=data.prev).grid()



class data:
    def setup(self): 
        data.i=0
        data.select=StringVar()
        data.select.set(0)
        data.ans = ['Yes','No']

    def save():
        gui.info.append([gui.name.get(), gui.age.get()  ,data.select.get()]) 
        gui.name.delete(0, END) 
        gui.age.delete(0, END) 
        data.select.set(0)

    def show():
        gui.f1.grid_forget()
        gui.f2.grid()

    def enter_data():
        gui.f2.grid_forget()
        gui.f1.grid()


    def next():
        data.i=data.i + 1
        gui.info_text.configure(text=gui.info[data.i])
    
    def prev():
        data.i=data.i - 1
        gui.info_text.configure(text=gui.info[data.i])

root = Tk()
gui(root)
root.mainloop()
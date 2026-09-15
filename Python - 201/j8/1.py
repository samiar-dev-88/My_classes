from tkinter import *
from tkinter import ttk , messagebox 

root = Tk()

#Checkbutton
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
checkbu = Checkbutton(root , text="Option 1" , bg="gray" , font=("Arial" , 10) , variable=check1)
checkbu.pack()
checkbu = Checkbutton(root , text="Option 2" , bg="gray" , font=("Arial" , 10) , variable=check2)
checkbu.pack()
checkbu = Checkbutton(root , text="Option 3" , bg="gray" , font=("Arial" , 10) , variable=check3)
checkbu.pack()

#Radiobutton
radio = IntVar()
radiobu = Radiobutton(root , text="Option 1" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=1)
radiobu.pack()
radiobu = Radiobutton(root , text="Option 2" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=2)
radiobu.pack()
radiobu = Radiobutton(root , text="Option 3" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=3)
radiobu.pack()

#Combobox
combo = ttk.Combobox(root , text="Option 3" , font=("Arial" , 10) , value=["Option 1" , "Option 2" , "Option 3"])
combo.current(0)
print(combo.get())
combo.pack()

#Listbox
lis = Listbox(root , width=30 , height=5 , bg="lightgray" , fg="gray" , font=("Arial" , 13))
lis.insert(0,"Option 1")
lis.insert(1,"Option 2")
lis.insert(2,"Option 3")
lis.pack()

def butt():
    messagebox.askyesno("Button","Thanks for clicking me!")

but = Button(root , command=butt , text="Click").pack()

root.mainloop()
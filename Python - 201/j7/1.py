from tkinter import *

root = Tk()

root.config(bg="gray")
root.title("App")
root.geometry("500x500")
root.resizable(False,False)

a = Label(root, text="سلام جهان" , bg="gray" , fg="white" , font=("Arial",20))
a.pack()

b = Entry(root, width=10 ,bg="gray" , fg="white" , font=("Arial",20) , borderwidth=10 , relief="groove")
b.pack()
c = b.get()

d = Text(root, width=10 , height=5 ,bg="white" , fg="black" , font=("Arial",20) , borderwidth=0 , relief="flat")
d.pack()

def butt():
    print("Hello")

d = Button(root, text="Click me", width=10 , height=5 , command=butt , activebackground="blue", activeforeground="red")
d.place(x=-20 , y = 30)

root.mainloop()
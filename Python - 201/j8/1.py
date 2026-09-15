from tkinter import *

root = Tk()
root.config(bg="#3ae124")
root.title("Notepad")
root.geometry("600x600")
root.resizable(False, False)

text = Text(root,width=10 , height=5 ,bg="white" , fg="#2024e6" , font=("Arial",20) , borderwidth=10 , relief="sunken")
text.pack()

root.mainloop()
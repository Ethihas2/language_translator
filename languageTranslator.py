from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root = Tk()
root.geometry("900x400")
root.title("Translator")
root.config(bg="cyan")

label_head = Label(root,text="Language Translator",bg="cyan",font=("black",18,"bold","italic"))
label_head.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="Enter Text",bg="cyan",font=("black",18,"bold"))
label1.place(relx=0.1,rely=0.2,anchor=CENTER)

text_area = Text(root,bg="white",height=10,width=40,wrap=WORD,padx=10,pady=10,bd=0)
text_area.place(relx=0.22,rely=0.5,anchor=CENTER)
root.mainloop()
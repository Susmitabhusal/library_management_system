from tkinter import *
#from tkinter import BOTH
from turtle import Canvas
from AddBook import *
from ViewBook import *
from DeleteBook import *
from IssueBook import *
from PIL import Image, ImageTk

obj1 = AddDetails()
obj2 = ViewDetails()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
photo = ImageTk.PhotoImage(file="libicon.png")
root.iconphoto(False,photo)
#root.mainloop()
same = True
n = 0.25

# Adding a background image
canvas = Canvas(root)
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "lib.jpg")
canvas.create_image(10, 10, image = image, anchor = NW)
#Adding a header
headingFrame1 = Frame(root,bg="#FFFFFF",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n the Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=obj1.addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
#btn2 = Button(root, text="View Book List", bg='black', fg='white', command=Delete)
#btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
btn3 = Button(root, text="View Book List", bg='black', fg='white', command=obj2.View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

root.mainloop()
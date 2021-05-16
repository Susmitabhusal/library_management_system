from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from AddBook import *
from ConnectDatabase import DB_FILE



# List To store all Book IDs
allBid = []


def issue():
    DB_FILE = "Library.db"
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    #issueBtn.destroy()
    #labelFrame.destroy()
    #lb1.destroy()
    #inf1.destroy()
    #inf2.destroy()

    extractBid = """select bid from  tbl_Books"""
    try:
        cursor.execute(extractBid)
        conn.commit()
        for i in cursor:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = """select status from tbl_Books  where bid = bid  """
            cursor.execute(checkAvail)
            conn.commit()
            for i in cursor:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    sql = """INSERT INTO books_issued(bid, issueto) values(?,?)"""
    values = (bid,issueto)
    show = """select * from books_issued"""


    updatesql = """UPDATE  tbl_Books set status=? where bid =?"""
    updatevalues = ('issued',bid)
    try:
        if bid in allBid and status == True:
            cursor.execute(sql,values)
            conn.commit()
            cursor.execute(updatesql,updatevalues)
            conn.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(bid)
    print(issueto)

    allBid.clear()


def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
    sql = """
                   CREATE TABLE IF NOT EXISTS books_issued(
                       bid INTEGER PRIMARY KEY,
                       issueto Text NOT NULL 
                   );
               """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
#from ConnectDatabase import DB_FILE

class ViewDetails():
    def View(self):
        DB_FILE = 'Library.db'

        root = Tk()
        root.title("View Records")
        root.minsize(width=400 ,height=400)
        root.geometry("600x500")



        Canvas1 = Canvas(root)
        Canvas1.config(bg="#12a4d9")
        Canvas1.pack(expand=True ,fill=BOTH)


        headingFrame1 = Frame(root ,bg="#FFFFFF" ,bd=5)
        headingFrame1.place(relx=0.25 ,rely=0.1 ,relwidth=0.5 ,relheight=0.13)

        headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier' ,15))
        headingLabel.place(relx=0 ,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(root ,bg='black')
        labelFrame.place(relx=0.1 ,rely=0.3 ,relwidth=0.8 ,relheight=0.5)
        y = 0.25

        Label(labelFrame, text="%-10s%-30s%-30s%-20s " %('BID' ,'Title' ,'Author' ,'Status') ,bg='black' ,fg='white').place \
            (relx=0.07 ,rely=0.1)
        Label(labelFrame, text="----------------------------------------------------------------------------" ,bg='black'
              ,fg='white').place(relx=0.05 ,rely=0.2)
        sql = """SELECT * FROM tbl_Books"""
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            for i in cursor:
                Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                    relx=0.07, rely=y)
                y += 0.1
        except:
            print("Error : ", sys.exc_info()[0])
        finally:
            cursor.close()
            conn.close()

        quitBtn = Button(root ,text="Quit" ,bg='#f7f1e3', fg='black', command=root.destroy)
        quitBtn.place(relx=0.4 ,rely=0.9, relwidth=0.18 ,relheight=0.08)

        root.mainloop()
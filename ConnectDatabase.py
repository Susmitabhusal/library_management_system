import sqlite3
import sys

DB_FILE = 'Library.db'


def connectDB():
    try:
        conn = sqlite3.connect(DB_FILE)
        print(sqlite3.version)
        print("Connection database sucessfully")
    except:
        print("Error :", sys.exc_info()[1])
    finally:
        conn.close()

def create_table1():
    sql = """
        CREATE TABLE IF NOT EXISTS tbl_Books(
            bid INTEGER PRIMARY KEY,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,
            Status TEXT NOT NULL 
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

#connectDB()

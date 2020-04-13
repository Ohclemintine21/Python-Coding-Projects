
import sqlite3

conn = sqlite3.connect('drill2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_text( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        

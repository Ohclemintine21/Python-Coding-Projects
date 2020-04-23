


import tkinter as tk

import os

dir_list = os.listdir()
print("Files and directories in current working directory :")

print(dir_list)

import sqlite3

def create_db(self):
    conn = sqlite3.connect('filetxt.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_file( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_time-stamp TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()


def findTxt():
    path = './files'
    files = os.listdir(path)
    for file in files:
        if (".txt" in file):
            fullPath = os.path.join(path, file)
            mtime = os.path.getmtime(fullPath)
            print("{} - {}".format(file, mtime))

import shutil

path = 'C:/Python-Coding-Projects/test.txt'
print("before moving file:")
print(os.listdir(path))

source = 'C:/Python-Coding-Projects/test.txt/source'

destination = 'C:/Python-Coding-Projects/test.txt/destination'

dest = shutil.move(source, destination)
print("After moving file:")
print(os.listdir(path))

print("Destination path:", dest)





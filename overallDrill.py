
from tkinter import filedialog
from tkinter import *
from os import *
import sqlite3
import shutil


class BrowseFiles(Frame):
    def __init__(self, parent):
        super(BrowseFiles, self).__init__(parent)
        
        self.parent = parent
        self.parent.resizable(width=False, height=False)
        self.parent.geometry('{}x{}'.format(400,250))
        self.conn = self.create_db()
        self.label = Label(self, text="Hello, World!")
        self.label.pack(padx=20, pady=20)

        self.input_dir = Entry(self)
        self.input_dir_button = Button(self, text="BROWSE", command=self.getInputPath)
        self.input_dir.pack()
        self.input_dir_button.pack()

        self.output_dir = Entry(self)
        self.output_dir_button = Button(self, text="BROWSE", command=self.getOutputPath)
        self.output_dir.pack()
        self.output_dir_button.pack()

        self.exec_button = Button(self, text="GO!", command=self.findTxt)
        self.exec_button.pack()
        
    def getInputPath(self):
        fdVal = filedialog.askdirectory() 
        self.input_dir.delete(0, END)
        self.input_dir.insert(0, fdVal)

    def getOutputPath(self):
        fdVal = filedialog.askdirectory()
        self.output_dir.delete(0, END)
        self.output_dir.insert(0, fdVal)

    def findTxt(self):
        input_path = self.input_dir.get()
        output_path = self.output_dir.get()
        files = listdir(input_path)
        conn = self.conn
        for file in files:
            fullPath = path.join(input_path, file)
            if ('.txt' in file):
                mtime = path.getmtime(fullPath)
                self.move(fullPath)
                print("{} - {}".format(file, mtime))
                self.addFileToDb(file, mtime)
        self.getTextDb()
        
    def create_db(self):
        conn = sqlite3.connect('testFind.db')

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_mtxt  TEXT  \
            )")
            conn.execute("DELETE FROM tbl_txtfiles WHERE true")
        return conn
        
    def addFileToDb(self, fname, mtime):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tbl_txtfiles(col_fname, col_mtxt) VALUES (?,?)", (fname, mtime))
        self.conn.commit()       
        
    def getTextDb(self):
        conn = self.conn

        with conn:
            cur = self.conn.cursor()
            cur.execute("SELECT col_fname, col_mtxt FROM tbl_txtfiles")
            varFile= cur.fetchall()
            for item in varFile:
                msg = "Filename: {}".format(item[0], item[1])
                print(msg)

    def move(self,source):
        shutil.move(source,self.output_dir.get())



                
if __name__ == "__main__":
    root = Tk()

    main = BrowseFiles(root)
    main.pack(fill="both", expand=True)

    root.mainloop()
    













from tkinter import *



class Application(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400,250))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.txtBrowse = Entry(self.master,text="browse" , font =("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse.grid(row=0, column=1, pady=30, padx=10)

        self.txtBrowse2 = Entry(self.master,text="browse", font =("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=1, column=1)

        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=2, command=self.browse)
        self.btnBrowse.grid(row=0, column=0, padx=10)
        
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=2, command=self.browse)
        self.btnBrowse2.grid(row=1, column=0)

        self.btnCheckforfiles = Button(self.master, text="Check for files...", width=12, height=3, command=self.checkForFiles)
        self.btnCheckforfiles.grid(row=2, column=0, pady=10)

        self.btnCloseProgram = Button(self.master, text="Close Program", width=12, height=3, command=self.CloseProgram)
        self.btnCloseProgram.grid(row=2, column=1, pady=10, sticky=E)


    def browse(arg):
        return true

    def checkForFiles(arg):
        return true

    def CloseProgram(arg):
        return true


root = Tk()
app = Application(root)
root.mainloop()              


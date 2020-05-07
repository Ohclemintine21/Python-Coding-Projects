import sqlite3


conn = sqlite3.connect('textFiles.db')
#create and clear db
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('textFiles.db')

fileList = ('information.docx','Hello.txt','myImage.png', 'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for file in fileList:
    if ('.txt' in file):
        print(file)
    conn.commit()
conn.close()




import os

def findTxt():
    path = './files'
    files = os.listdir(path)
    for file in files:
        if (".txt" in file):
            fullPath = os.path.join(path, file)
            mtime = os.path.getmtime(fullPath)
            print("{} - {}".format(file, mtime))


findTxt()

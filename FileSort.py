import os
import datetime
import shutil

def MoveByDate():
    print(r"An example: C:\Users\Name\OneDrive\Pictures\Screenshots")
    directory = input("Enter directory of files to be sorted: ").replace("\\","\\\\")
    folder = os.listdir(directory)
    for counter in range(len(folder)):
        if os.path.isfile(directory+"\\"+folder[counter]):
            time = os.path.getctime(directory+"\\"+folder[counter])
            date = str(datetime.datetime.fromtimestamp(time))
            try:
                os.mkdir(directory+"\\"+date[:4])
            except FileExistsError:
                pass
            shutil.move(directory+"\\"+folder[counter],directory+"\\"+date[:4])

MoveByDate()
print("Files sorted by date.")
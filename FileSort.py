import os
import datetime
import shutil

def SortByDate():
    print(r"An example: C:\Users\John\OneDrive\Pictures\Screenshots")
    directory = input("Enter directory of files to be sorted: ").replace("\\","\\\\")
    folder = os.listdir(directory)
    for counter in range(len(folder)):
        file = directory+"\\"+folder[counter]
        if os.path.isfile(file):
            time = os.path.getctime(file)
            date = str(datetime.datetime.fromtimestamp(time))
            try:
                os.mkdir(directory+"\\"+date[:4])
            except FileExistsError:
                pass
            shutil.move(file,directory+"\\"+date[:4])

def sortByType():
    print(r"An example: C:\Users\John\OneDrive\Downloads")
    directory = input("Enter directory of files to be sorted: ").replace("\\","\\\\")
    folder = os.listdir(directory)
    for counter in range(len(folder)):
        file = directory+"\\"+folder[counter]
        if os.path.isfile(file):
            extension = os.path.splitext(file)[1]
            try:
                os.mkdir(directory+"\\"+extension)
            except FileExistsError:
                pass
            shutil.move(file,directory+"\\"+extension)


print("""Options:
    [1]By date
    [2]By extension""")
mode = input("What do you want to sort by: ")
print("")
if mode == "1":
    SortByDate()
    print("Files sorted by date.")
elif mode == "2":
    sortByType()
    print("Files sorted by extension.")

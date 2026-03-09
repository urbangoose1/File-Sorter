import os
import datetime
import shutil

def SortByDate():
    print(r"An example: C:\Users\John\OneDrive\Pictures\Screenshots")
    directory = input("Enter directory of files to be sorted: ").replace("\\","\\\\")
    print("")
    print("    [1]Sort by year")
    print("    [2]Sort by month(EXCLUDES YEARS, recommended to use inside year folders)")
    sortType = ""
    while sortType != "1" and sortType != "2": #Validates input
        sortType = input("Sort into: ")
    folder = os.listdir(directory)
    monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    for counter in range(len(folder)):
        file = directory+"\\"+folder[counter]
        if os.path.isfile(file):
            time = os.path.getctime(file)
            date = str(datetime.datetime.fromtimestamp(time)) #format: 2025-04-18 14:30:00
            if sortType == "1":
                try:
                    os.mkdir(directory+"\\"+date[:4])
                except FileExistsError:
                    pass
                shutil.move(file,directory+"\\"+date[:4])
            elif sortType == "2":
                month = monthList[int(date[5:7])-1]
                try:
                    os.mkdir(directory+"\\"+month)
                except FileExistsError:
                    pass
                shutil.move(file,directory+"\\"+month)


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
    [2]By file type(extension)""")
mode = input("What do you want to sort by: ")
print("")
if mode == "1":
    SortByDate()
    print("Files sorted by date.")
elif mode == "2":
    sortByType()
    print("Files sorted by extension.")

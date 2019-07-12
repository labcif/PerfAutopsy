#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import time
import getpass
import sys
import tkinter
from datetime import datetime
from tkinter import filedialog
from tkinter import *
from tkinter import ttk


log_file = ""

print("Current system: " + platform.system() + "\n")


def __run_scripts(test):

    test = test[:2].strip()
    print("Running module " + test + "\n")
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("/usr/bin/actexec Linux/Script-m" + test + ".ascr")
    else:
        os.system("actexec.exe Windows/Script-m" + test + ".ascr")


def popup_error(msg):
    popup = tkinter.Tk()
    popup.wm_title("Error")
    label = ttk.Label(popup, text=msg, font="helvetica 16")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="OK", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def printOptions():
    tests = []

    tests.insert(0, tkvar.get())
    tests.insert(1, tkvar2.get())
    tests.insert(2, tkvar3.get())
    tests.insert(3, tkvar4.get())
    tests.insert(4, tkvar5.get())
    tests.insert(5, tkvar6.get())
    tests.insert(6, tkvar7.get())
    tests.insert(7, tkvar8.get())
    tests.insert(8, tkvar9.get())
    tests.insert(9, tkvar10.get())
    tests.insert(10, tkvar11.get())
    tests.insert(11, tkvar12.get())

    #remove todos os 'None' do array
    tests = list(filter(lambda a: a != 'None', tests))

    if len(log_file) == 0:
        popup_error("You must choose a log file!")

    for test in tests:

        startArray = []
        finishArray = []

        start_date = []
        end_date = []

        print("Module " + test)

        resultsFile = open("resultados.txt", "a+")
        resultsFile.write("Module " + str(test) + ":\n")
        resultsFile.close()

        __run_scripts(test)

        while True:
            for line in open(log_file, "r"):
                if "IngestManager startIngestJob" in line:
                    if line not in startArray:
                        print("START: " + line)
                        startArray.append(line)

            if len(startArray) == (tests.index(test) + 1):
                open("resultados.txt", "a+").write("Start: " + str(startArray[-1]))
                start_date = datetime.strptime(startArray[-1][:18], "%Y-%m-%d %H:%M:%S")

            if len(startArray) != (tests.index(test) + 1):
                print("startArray:" + str(len(startArray)) + "; index:" + str((tests.index(test) + 1)))
                time.sleep(60)
            else:
                break

        while True:
            for line in open(log_file, "r"):
                if "IngestManager finishIngestJob" in line:
                    if line not in finishArray:
                        print("FINISH: " + line)
                        finishArray.append(line)

            if len(finishArray) == (tests.index(test) + 1):
                open("resultados.txt", "a+").write("Finish: " + str(finishArray[-1]))
                end_date = datetime.strptime(finishArray[-1][:18], "%Y-%m-%d %H:%M:%S")
                result = end_date - start_date
                print(result)
                open("resultados.txt", "a+").write("Time: " + str(result) + "\n\n")


            if len(finishArray) != (tests.index(test) + 1):
                print("finishArray:" + str(len(finishArray)) + "; index:" + str((tests.index(test) + 1)))
                time.sleep(300)
            else:
                break


def fileBrowse():
    window.filename = filedialog.askopenfilename(initialdir="~", title="Select LOG file",
                                                 filetypes=(("Log File", "*.log.0"), ("all files", "*.*")))
    global log_file
    log_file = window.filename
    showBrowse.configure(text=window.filename)


window = Tk()
window.title("Monitor Interact")

topFrame = Frame(window)
topFrame.pack()
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)


#dropdown var
tkvar = StringVar(window)
tkvar2 = StringVar(window)
tkvar3 = StringVar(window)
tkvar4 = StringVar(window)
tkvar5 = StringVar(window)
tkvar6 = StringVar(window)
tkvar7 = StringVar(window)
tkvar8 = StringVar(window)
tkvar9 = StringVar(window)
tkvar10 = StringVar(window)
tkvar11 = StringVar(window)
tkvar12 = StringVar(window)


# Dictionary with options
choices = ["0 - Recent Activity",
           "1 - Hash Lookup",
           "2 - File Type Identification",
           "3 - Extension Mismatch Detector",
           "4 - Embedded File Extractor",
           "5 - Exif Parser",
           "6 - Keyword Search",
           "7 - Email Parser",
           "8 - Encryption Detection",
           "9 - Interesting Files Identifier",
           "10 - Correlation Engine",
           "11 - PhotoRec Carver",
           "12 - Virtual Machine Extractor",
           "13 - Data Source Integrity",
           "14 - Android Analyzer",
           "None"]


#  preciso todo este codigo repetido porque senao os dropdown mudam todos ao selecionar cada um deles
tkvar.set('None') # set the default option
tkvar2.set('None')
tkvar3.set('None')
tkvar4.set('None')
tkvar5.set('None')
tkvar6.set('None')
tkvar7.set('None')
tkvar8.set('None')
tkvar9.set('None')
tkvar10.set('None')
tkvar11.set('None')
tkvar12.set('None')



popupMenu = OptionMenu(topFrame, tkvar, *choices)
popupMenu2 = OptionMenu(topFrame, tkvar2, *choices)
popupMenu3 = OptionMenu(topFrame, tkvar3, *choices)
popupMenu4 = OptionMenu(topFrame, tkvar4, *choices)
popupMenu5 = OptionMenu(topFrame, tkvar5, *choices)
popupMenu6 = OptionMenu(topFrame, tkvar6, *choices)
popupMenu7 = OptionMenu(topFrame, tkvar7, *choices)
popupMenu8 = OptionMenu(topFrame, tkvar8, *choices)
popupMenu9 = OptionMenu(topFrame, tkvar9, *choices)
popupMenu10 = OptionMenu(topFrame, tkvar10, *choices)
popupMenu11 = OptionMenu(topFrame, tkvar11, *choices)
popupMenu12 = OptionMenu(topFrame, tkvar12, *choices)


Label(topFrame, text="Choose the Ingest Modules you want to run in order.", font="helvetica 15").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
popupMenu2.grid(row = 3, column =1)
popupMenu3.grid(row = 4, column =1)
popupMenu4.grid(row = 5, column =1)
popupMenu5.grid(row = 6, column =1)
popupMenu6.grid(row = 7, column =1)
popupMenu7.grid(row = 8, column =1)
popupMenu8.grid(row = 9, column =1)
popupMenu9.grid(row = 10, column =1)
popupMenu10.grid(row = 11, column =1)
popupMenu11.grid(row = 12, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
# on change dropdown value
def change_dropdown2(*args):
    print( tkvar2.get() )
# on change dropdown value
def change_dropdown3(*args):
    print( tkvar3.get() )
# on change dropdown value
def change_dropdown4(*args):
    print( tkvar4.get() )
# on change dropdown value
def change_dropdown5(*args):
    print( tkvar5.get() )
# on change dropdown value
def change_dropdown6(*args):
    print( tkvar6.get() )
# on change dropdown value
def change_dropdown7(*args):
    print( tkvar7.get() )
# on change dropdown value
def change_dropdown8(*args):
    print( tkvar8.get() )
# on change dropdown value
def change_dropdown9(*args):
    print( tkvar9.get() )
# on change dropdown value
def change_dropdown10(*args):
    print( tkvar10.get() )
# on change dropdown value
def change_dropdown11(*args):
    print( tkvar11.get() )
# on change dropdown value
def change_dropdown12(*args):
    print( tkvar12.get() )
# link function to change dropdown
tkvar.trace('w', change_dropdown)
tkvar2.trace('w', change_dropdown2)
tkvar3.trace('w', change_dropdown3)
tkvar4.trace('w', change_dropdown4)
tkvar5.trace('w', change_dropdown5)
tkvar6.trace('w', change_dropdown6)
tkvar7.trace('w', change_dropdown7)
tkvar8.trace('w', change_dropdown8)
tkvar9.trace('w', change_dropdown9)
tkvar10.trace('w', change_dropdown10)
tkvar11.trace('w', change_dropdown11)
tkvar12.trace('w', change_dropdown12)





# end of dropdown
showBrowse = Label(window)
showBrowse.pack(side=BOTTOM)

v = StringVar()

buttonBrowse = Button(bottomframe, text="Browse Log", fg="blue", command=fileBrowse)
buttonBrowse.pack(side=LEFT)


buttonSubmit = Button(bottomframe, text="Submit", fg="blue", command=printOptions)
buttonSubmit.pack(side=LEFT)

window.mainloop()

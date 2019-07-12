#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import filedialog
from tkinter import *

def printOptions():
        print(v.get())
        print([x for x in v.get()])

def fileBrowse():
        window.filename =  filedialog.askopenfilename(initialdir = "~",title = "Select LOG file",filetypes = (("Log File","*.log.0"),("all files","*.*")))
        print (window.filename)
        showBrowse.configure(text = window.filename)

window = Tk()
window.title("Monitor Autopsy")

topFrame = Frame(window)
topFrame.pack()
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

title = Label(window, text="Choose the Ingests you want to run, the order counts", font="helvetica 15", padx=50, pady=20)
label = Label(window, text="A - Hash Lookup\nB - File Tyle Identification\nC - Extension Mismatch Detector\nD - Embedded File Extractor\nE - Exif Parser\nF - Keyword Search\nG - Email Parser\nH - Encryption Detection\nI - Interesting Files Identifier\nJ - Correlation Engine\nK - PhotoRec Carver\nL - Virtual Machine Extractor\nM - Data Source Integrity\nN - Android Analyzer", justify=LEFT, font="helvetica 12", padx=50)

showBrowse = Label(window)
showBrowse.pack(side=BOTTOM)
label_text = Label(window, text="options")
v = StringVar()
entry_text = Entry(window, textvariable=v)


title.pack(side=TOP)
label.pack(side=TOP)

buttonBrowse = Button(bottomframe, text="Browse Log", fg="blue", command=fileBrowse)
buttonBrowse.pack(side=LEFT)


label_text.pack(side=LEFT)
entry_text.pack(side=BOTTOM, fill=X)

buttonSubmit = Button(bottomframe, text="Submit", fg="blue", command=printOptions)
buttonSubmit.pack(side=LEFT)


window.mainloop()



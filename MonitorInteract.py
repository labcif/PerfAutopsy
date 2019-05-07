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


def __run_scripts(teste):
    print("A correr o módulo " + teste + "\n")
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("/usr/bin/actexec Script-m" + teste + ".ascr")
    else:
        os.system("actexec.exe Script-m" + teste + ".ascr")


def popup_error(msg):
    popup = tkinter.Tk()
    popup.wm_title("Error")
    label = ttk.Label(popup, text=msg, font="helvetica 16")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def printOptions():
    testes = [x.upper() for x in v.get()]

    if len(log_file) == 0:
        popup_error("You must choose a log file!")

    if len(v.get()) == 0:
        popup_error("Your must choose some tests to run!")

    for t in testes:
        if not ord(t) in range(ord('A'), ord('N') + 1):
            popup_error("Only letters from A to N!")

    counter = 0

    for test in testes:

        __run_scripts(test)

        time.sleep(20)

        if platform.system() == "Linux" or platform.system() == "Darwin":
            os.system(
                "grep \"IngestManager startIngestJob\" " + log_file + " > timestamp_start_module_" + str(
                    test) + ".txt")
        else:
            os.system(
                "findstr /S /c:\"IngestManager startIngestJob\" " + log_file + " > timestamp_start_module_" + str(
                    test) + ".txt")

        while counter != (testes.index(test) + 1):

            if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("grep -c \"IngestManager finishIngestJob\" " + log_file + " > counter.txt")
                with open("counter.txt") as f:
                    counter = f.read()
            else:
                os.system(
                    "findstr /S /c:\"IngestManager finishIngestJob\" " + log_file + " > counter.txt")
                counter = len(open("counter.txt", "r+").readlines())

            if platform.system() == "Linux" or platform.system() == "Darwin":
                os.system(
                    "grep \"IngestManager finishIngestJob\" " + log_file + " > timestamp_end_module_" + str(
                        test) +
                    ".txt")
            else:
                os.system(
                    "findstr /S /c:\"IngestManager finishIngestJob\" " + log_file + " > timestamp_end_module_" +
                    str(test) + ".txt")

            print("Contador: ", counter, "; Atual: ",
                  (testes.index(test) + 1))

            if counter != (testes.index(test) + 1):
                print("Em espera.\n")
                time.sleep(300)


def fileBrowse():
    window.filename = filedialog.askopenfilename(initialdir="~", title="Select LOG file",
                                                 filetypes=(("Log File", "*.log.0"), ("all files", "*.*")))
    global log_file
    log_file = window.filename
    showBrowse.configure(text=window.filename)


window = Tk()
window.title("Monitor Autopsy")

topFrame = Frame(window)
topFrame.pack()
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

title = Label(window, text="Choose the Ingests you want to run, the order counts", font="helvetica 15", padx=50,
              pady=20)
label = Label(window,
              text="A - Hash Lookup\nB - File Tyle Identification\nC - Extension Mismatch Detector\nD - Embedded File "
                   "Extractor\nE - Exif Parser\nF - Keyword Search\nG - Email Parser\nH - Encryption Detection\nI - "
                   "Interesting Files Identifier\nJ - Correlation Engine\nK - PhotoRec Carver\nL - Virtual Machine "
                   "Extractor\nM - Data Source Integrity\nN - Android Analyzer",
              justify=LEFT, font="helvetica 12", padx=50)

showBrowse = Label(window)
showBrowse.pack(side=BOTTOM)
label_text = Label(window, text="Options")
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

import VMMain as vm
import tkinter
from tkinter import *
import tkinter.messagebox as msg
import numpy as np
import VHellGui

main = tkinter.Tk()
login_window = Toplevel(main)

def config_main_window():
    #main.overrideredirect(True)
    main.withdraw() #blendet das main window aus
    main.geometry('1000x800')

def open_login_window():
    login_window.lower()
    login_window.title("Login")
    login_window.geometry("300x150")
    login_window.configure(background="lightblue")
    tkinter.Label(login_window, text="Geben Sie Ihren Namen ein:", bg="lightblue").pack(pady=10)
    name_entry = tkinter.Entry(login_window, width=25)
    name_entry.pack(pady=5)






config_main_window()
open_login_window()

VHellGui.create_heart()

main.mainloop()






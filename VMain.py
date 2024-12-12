import VMMain as vm
import tkinter as tk
from tkinter import messagebox
import VHellGui
import threading
#simon binär = 0101001101101001011011010110111101101110

main = tk.Tk()
login_window = tk.Toplevel(main)

def config_main_window():
    main.withdraw() #blendet das main window aus
    main.geometry('1000x800')
def open_login_window():
    def check_name_input():
        name = name_entry.get().strip()
        if vm.is_binary_string(name):
            if len(name) <= 24:
                messagebox.showerror('Error', 'Das ist zu kurz für einen Namen')
            elif vm.tempName != None and vm.convert_binary_to_letter(name) != vm.tempName:
                messagebox.showerror('Error', 'Das ist nicht der Name den du zuerst eingegeben hast du Schlingel')
            else:
                messagebox.showinfo("Willkommen", f"Hallo, {vm.convert_binary_to_letter(name)}")
                login_window.destroy()
                main.deiconify()
        else:
            vm.tempName = name
            messagebox.showerror('Error', 'Nur die binäre schreibweise ist erlaubt')

    login_window.lower()
    login_window.title("Login")
    login_window.geometry("300x150")
    tk.Label(login_window, text="Geben Sie Ihren Namen ein:").pack(pady=10)
    name_entry = tk.Entry(login_window, width=25)
    name_entry.pack(pady=5)
    login_button = tk.Button(login_window, text="Anmelden", command=check_name_input)
    login_button.pack(pady=10)

def btnClose_click():
    main.destroy()


def start_gui():
    config_main_window()
    open_login_window()
    VHellGui.create_heart()
    VHellGui.play_song()

    console_thread = threading.Thread(target=vm.write_to_console, daemon=True)
    console_thread.start()

    main.mainloop()

btnClose = tk.Button(main, text="Beenden", command=btnClose_click)
btnClose.place(x=1200, y=700)
lblFilialieA = tk.Label (main, text="Filialie A:")
lblFilialieA.place(x=50, y=150)
lblFilialieB = tk.Label (main, text="Filialie B:")
lblFilialieB.place(x=50, y=350)
lblFilialieC = tk.Label (main, text="Filialie C:")
lblFilialieC.place(x=50, y=550)
lblMonday = tk.Label (main, text="Montag:")
lblMonday.place(x=150, y=50)
lblTuesday = tk.Label (main, text="Dienstag:")
lblTuesday.place(x=350, y=50)
lblWednesday = tk.Label (main, text="Mittwoch:")
lblWednesday.place(x=550, y=50)
lblThursday = tk.Label (main, text="Donnerstag:")
lblThursday.place(x=750, y=50)
lblFriday = tk.Label (main, text="Freitag:")
lblFriday.place(x=950, y=50)
lblSaturday = tk.Label (main, text="Samstag:")
lblSaturday.place(x=1150, y=50)
#lblInhalt = tk.Entry(main)
#lblInhalt.place(x=200, y=150)
start_gui()

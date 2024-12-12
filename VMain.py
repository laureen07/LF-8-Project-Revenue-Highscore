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



def start_gui():
    config_main_window()
    open_login_window()
    VHellGui.create_heart()
    VHellGui.play_song()

    console_thread = threading.Thread(target=vm.write_to_console, daemon=True)
    console_thread.start()

    main.mainloop()
start_gui()

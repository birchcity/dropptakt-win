#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

# Konverteringsfunktioner

def konvertera_volym(volym, enhet):
    if enhet == "L":
        return volym * 1000  # liter -> ml
    return volym


def konvertera_tid(tid, enhet):
    if enhet == "timmar":
        return tid * 60  # timmar -> minuter
    return tid

def hämta_droppfaktor():
    # Om användaren valt "Egen", ta värdet från inputfältet
    if faktor_val.get() == "Egen":
        return float(entry_faktor.get())
    else:
        return float(faktor_val.get())


def beräkna():
    try:
        volym = float(entry_volym.get())
        tid = float(entry_tid.get())
        droppfaktor = hämta_droppfaktor()

        volym_ml = konvertera_volym(volym, volym_enhet.get())
        tid_min = konvertera_tid(tid, tid_enhet.get())

        if svar_typ.get() == "dr/min":
            resultat = (volym_ml * droppfaktor) / tid_min
            result_label.config(text=f"Dropptakt: {round(resultat)} dr/min")
        else:
            resultat = volym_ml / (tid_min / 60)
            result_label.config(text=f"Flöde: {round(resultat)} ml/timme")

    except Exception:
        messagebox.showerror("Fel", "Kontrollera dina inmatningar")



# GUI
root = tk.Tk()
root.title("Dropptakt Kalkylator")
root.geometry("600x250")

# Volym

tk.Label(root, text="Volym:").grid(row=0, column=0)
entry_volym = tk.Entry(root)
entry_volym.grid(row=0, column=1)

volym_enhet = ttk.Combobox(root, values=["ml", "L"], width=5)
volym_enhet.current(0)
volym_enhet.grid(row=0, column=2)

# Tid

tk.Label(root, text="Tid:").grid(row=1, column=0)
entry_tid = tk.Entry(root)
entry_tid.grid(row=1, column=1)

tid_enhet = ttk.Combobox(root, values=["minuter", "timmar"], width=8)
tid_enhet.current(0)
tid_enhet.grid(row=1, column=2)

# Droppfaktor (preset + egen)

tk.Label(root, text="Droppfaktor:").grid(row=2, column=0)

faktor_val = ttk.Combobox(root, values=["10", "15", "20", "60", "Egen"], width=7)
faktor_val.current(2)  # standard = 20
faktor_val.grid(row=2, column=1)

entry_faktor = tk.Entry(root)
entry_faktor.grid(row=2, column=2)
entry_faktor.insert(0, "20")

# Svarstyp

svar_typ = ttk.Combobox(root, values=["dr/min", "ml/timme"])
svar_typ.current(0)
svar_typ.grid(row=3, column=0, columnspan=3)

# Knapp

tk.Button(root, text="Beräkna", command=beräkna).grid(row=4, column=0, columnspan=3)

# Resultat

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3)

# Footer
footer = tk.Label(root, text="Github Birchcity, ssk-student på UMU, 2026", font=("Arial", 8))
footer.grid(row=6, column=0, columnspan=3, pady=(10,0))

root.mainloop()

root.mainloop()

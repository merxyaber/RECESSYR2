import tkinter as tk
from tkinter import messagebox

# FUNCTIONS

def calculate():
    try:
        bill = float(entry_bill.get())
        people = int(entry_people.get())
        tip = float(entry_tip.get())

        if bill <= 0 or people <= 0 or tip < 0:
            messagebox.showerror("Error", "Enter valid positive values")
            return

        tip_amount = (tip / 100) * bill
        total = bill + tip_amount
        per_person = total / people

        result.set(
            f"Bill: UGX {bill:.2f}\n"
            f"Tip: UGX {tip_amount:.2f}\n"
            f"Total: UGX {total:.2f}\n"
            f"Each Pays: UGX {per_person:.2f}"
        )

    except:
        messagebox.showerror("Error", "Please enter correct values")


# function to quickly set tip from buttons
def set_tip(value):
    entry_tip.delete(0, tk.END)
    entry_tip.insert(0, str(value))


def clear():
    entry_bill.delete(0, tk.END)
    entry_people.delete(0, tk.END)
    entry_tip.delete(0, tk.END)
    result.set("")


# WINDOW SETUP
window = tk.Tk()
window.title("Bill Split Calculator")
window.geometry("320x350")
window.config(bg="#1e1e2f")  # dark background

# INPUT SECTION

tk.Label(window, text="Total Bill", bg="#1e1e2f", fg="white").pack()
entry_bill = tk.Entry(window)
entry_bill.pack(pady=5)

tk.Label(window, text="Number of People", bg="#1e1e2f", fg="white").pack()
entry_people = tk.Entry(window)
entry_people.pack(pady=5)

tk.Label(window, text="Tip (%)", bg="#1e1e2f", fg="white").pack()
entry_tip = tk.Entry(window)
entry_tip.pack(pady=5)

# TIP BUTTONS
frame = tk.Frame(window, bg="#1e1e2f")
frame.pack(pady=10)

tk.Button(frame, text="10%", bg="#4CAF50", fg="white",
          command=lambda: set_tip(10)).grid(row=0, column=0, padx=5)

tk.Button(frame, text="15%", bg="#2196F3", fg="white",
          command=lambda: set_tip(15)).grid(row=0, column=1, padx=5)

tk.Button(frame, text="20%", bg="#FF9800", fg="white",
          command=lambda: set_tip(20)).grid(row=0, column=2, padx=5)

# ACTION BUTTONS

tk.Button(window, text="Calculate", bg="#9C27B0", fg="white",
          command=calculate).pack(pady=10)

tk.Button(window, text="Clear", bg="#f44336", fg="white",
          command=clear).pack()

# RESULT DISPLAY

result = tk.StringVar()
tk.Label(window, textvariable=result, bg="#1e1e2f", fg="white").pack(pady=10)

# RUN APP

window.mainloop()
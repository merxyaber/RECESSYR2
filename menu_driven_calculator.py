import tkinter as tk
from tkinter import messagebox

#/CREATE MAIN WINDOW (THE APP SCREEN)/
# This section creates the main application window and sets its size,
# title, and dark background color.
root = tk.Tk()
root.title("Mercy's Calculator")
root.geometry("320x450")
root.resizable(False, False)   # Prevents resizing to keep layout fixed
root.configure(bg="#1e1e1e")   # Dark background theme

#CREATE DISPLAY SCREEN (WHERE NUMBERS/RESULTS SHOW)
# This Entry widget acts like a calculator screen.
# Users cannot type directly (they use buttons instead).
display = tk.Entry(
    root,
    font=("Arial", 20),
    bg="#2b2b2b",
    fg="white",
    bd=0,
    insertbackground="white",
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=15, pady=10, padx=10)

#/FUNCTIONS (LOGIC OF THE CALCULATOR)/
# Adds numbers/characters to the display screen
def press(num):
    display.insert(tk.END, str(num))

# Clears everything on the display
def clear():
    display.delete(0, tk.END)

# Removes the last character (backspace feature)
def backspace():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])

# Calculates the expression typed in the display
def calculate():
    try:
        # eval() reads the full expression like "2+3*4"
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        # Shows error if input is invalid
        messagebox.showerror("Error", "Invalid Input")

#/BUTTON CREATION HELPER FUNCTION/
def create_btn(text, row, col, command, bg="#333333"):
    btn = tk.Button(
        button_frame,
        text=text,
        width=6,
        height=2,
        font=("Arial", 14),
        bg=bg,
        fg="white",
        bd=0,
        command=command
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    return btn

#/BUTTON LAYOUT SECTION/
# This section creates all calculator buttons and arranges them in a grid.

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack()

# Row 1: Clear, Backspace, Divide, Multiply
create_btn("C", 0, 0, clear, "#ff4d4d")          # Clear all input
create_btn("⌫", 0, 1, backspace, "#555555")      # Delete last character
create_btn("/", 0, 2, lambda: press("/"), "#555555")
create_btn("*", 0, 3, lambda: press("*"), "#555555")

# Row 2: Numbers 7–9 and minus
create_btn("7", 1, 0, lambda: press("7"))
create_btn("8", 1, 1, lambda: press("8"))
create_btn("9", 1, 2, lambda: press("9"))
create_btn("-", 1, 3, lambda: press("-"), "#555555")

# Row 3: Numbers 4–6 and plus
create_btn("4", 2, 0, lambda: press("4"))
create_btn("5", 2, 1, lambda: press("5"))
create_btn("6", 2, 2, lambda: press("6"))
create_btn("+", 2, 3, lambda: press("+"), "#555555")

# Row 4: Numbers 1–3 and equals
create_btn("1", 3, 0, lambda: press("1"))
create_btn("2", 3, 1, lambda: press("2"))
create_btn("3", 3, 2, lambda: press("3"))
create_btn("=", 3, 3, calculate, "#00b894")      # Calculate result

# Row 5: 0, decimal, double zero
create_btn("0", 4, 0, lambda: press("0"))
create_btn(".", 4, 1, lambda: press("."))        # Decimal point
create_btn("00", 4, 2, lambda: press("00"))      # Quick double zero

# /START THE APPLICATION/
# This keeps the program running and displays the window.
root.mainloop()
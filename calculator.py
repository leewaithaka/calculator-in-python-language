import tkinter as tk
def calculate():
    expression = entry.get()
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
app = tk.Tk()
app.title("Calculator")
entry = tk.Entry(app)
entry.grid(row=0, column=0, columnspan=4)
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
buttons = []

for label in button_labels:
    buttons.append(tk.Button(app, text=label, command=lambda label=label: entry.insert(tk.END, label)))
    buttons[-1].grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Special case for the equals button
buttons[-2].config(command=calculate)
app.mainloop()

import tkinter as tk
def click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '.', '=', '/',
    'C'
]

row = 1
col = 0
for b in buttons:
    tk.Button(root, text=b, width=5, height=2,
              command=lambda x=b: click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

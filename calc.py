import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return
        result = float(entry1.get()) / denominator
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def numpad_press(entry, value):
    entry.insert(tk.END, value)

root = tk.Tk()
root.title("Simple Calculator")

theme = tk.StringVar(value="Light")

# Button and text colors for theme
theme_colors = {
    "Light": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        "btn_bg": "#e0e0e0",
        "btn_fg": "#000000",
        "entry_bg": "#ffffff",
        "entry_fg": "#000000"
    },
    "Dark": {
        "bg": "#222222",
        "fg": "#ffffff",
        "btn_bg": "#444444",
        "btn_fg": "#ffffff",
        "entry_bg": "#333333",
        "entry_fg": "#ffffff"
    }
}

def set_theme():
    colors = theme_colors[theme.get()]
    root.configure(bg=colors["bg"])
    for widget in root.winfo_children():
        config_widget(widget, colors)
    # Numpads
    for widget in numpad_frame1.winfo_children():
        config_button(widget, colors)
    for widget in numpad_frame2.winfo_children():
        config_button(widget, colors)
    # Operation buttons
    for widget in btn_frame.winfo_children():
        config_button(widget, colors)

def config_widget(widget, colors):
    if isinstance(widget, tk.Label):
        widget.configure(bg=colors["bg"], fg=colors["fg"])
    elif isinstance(widget, tk.Entry):
        widget.configure(bg=colors["entry_bg"], fg=colors["entry_fg"], insertbackground=colors["entry_fg"])
    elif isinstance(widget, tk.Frame):
        widget.configure(bg=colors["bg"])
        for child in widget.winfo_children():
            config_widget(child, colors)
    elif isinstance(widget, tk.Radiobutton):
        widget.configure(bg=colors["bg"], fg=colors["fg"], selectcolor=colors["bg"])

def config_button(btn, colors):
    if isinstance(btn, tk.Button):
        btn.configure(bg=colors["btn_bg"], fg=colors["btn_fg"], activebackground=colors["btn_fg"], activeforeground=colors["btn_bg"])

tk.Label(root, text="First Number:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

result_var = tk.StringVar()
tk.Label(root, text="Result:").grid(row=2, column=0, padx=5, pady=5)
result_entry = tk.Entry(root, textvariable=result_var, state="readonly")
result_entry.grid(row=2, column=1, padx=5, pady=5)

# Operation buttons
btn_frame = tk.Frame(root)
btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(btn_frame, text="Add", width=8, command=add).grid(row=0, column=0, padx=2)
tk.Button(btn_frame, text="Subtract", width=8, command=subtract).grid(row=0, column=1, padx=2)
tk.Button(btn_frame, text="Multiply", width=8, command=multiply).grid(row=0, column=2, padx=2)
tk.Button(btn_frame, text="Divide", width=8, command=divide).grid(row=0, column=3, padx=2)

# Numpad for First Number
numpad_frame1 = tk.LabelFrame(root, text="Numpad (First Number)")
numpad_frame1.grid(row=4, column=0, padx=5, pady=5)
for i, num in enumerate([7,8,9,4,5,6,1,2,3,0,'.','C']):
    def cmd(x=num):
        if x == 'C':
            entry1.delete(0, tk.END)
        else:
            numpad_press(entry1, str(x))
    tk.Button(numpad_frame1, text=str(num), width=3, command=cmd).grid(row=i//3, column=i%3, padx=2, pady=2)

# Numpad for Second Number
numpad_frame2 = tk.LabelFrame(root, text="Numpad (Second Number)")
numpad_frame2.grid(row=4, column=1, padx=5, pady=5)
for i, num in enumerate([7,8,9,4,5,6,1,2,3,0,'.','C']):
    def cmd(x=num):
        if x == 'C':
            entry2.delete(0, tk.END)
        else:
            numpad_press(entry2, str(x))
    tk.Button(numpad_frame2, text=str(num), width=3, command=cmd).grid(row=i//3, column=i%3, padx=2, pady=2)

# Theme radio buttons
theme_frame = tk.Frame(root)
theme_frame.grid(row=5, column=0, columnspan=2, pady=10)
tk.Label(theme_frame, text="Theme:").grid(row=0, column=0, padx=5)
tk.Radiobutton(theme_frame, text="Light", variable=theme, value="Light", command=set_theme).grid(row=0, column=1, padx=5)
tk.Radiobutton(theme_frame, text="Dark", variable=theme, value="Dark", command=set_theme).grid(row=0, column=2, padx=5)

set_theme()
root.mainloop()
import tkinter as tk
from tkinter import Menu, Text, Scrollbar, StringVar, ttk
import tkinter.filedialog

# Placeholder functions (replace with actual compiler logic)
def abrir():
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        code_entry.delete(1.0, tk.END)  # Clear existing content
        code_entry.insert(tk.END, content)  # Insert file content into code entry widget

def on_content_change(event):
    lines = code_entry.get(1.0, tk.END).split('\n')
    line_count.set(len(lines) - 1)  # Subtract 1 to exclude the empty line at the end
    update_line_numbers()

def update_line_numbers():
    lines = code_entry.get(1.0, tk.END).split('\n')
    line_numbers.delete(1.0, tk.END)
    for i in range(len(lines) - 1):  # Subtract 1 to exclude the empty line at the end
        line_numbers.insert(tk.END, f"{i + 1}\n")

# Main program window
root = tk.Tk()
root.title("Compilador")

# Line counter variable
line_count = StringVar()
line_count.set("0")

# Menu bar
menu_bar = Menu(root)

# File menu
archivo_menu = Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Abrir", command=abrir)
# ... other file menu options ...
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

# Compilar menu
compilar_menu = Menu(menu_bar, tearoff=0)
compilar_menu.add_command(label="Compilar", command=lambda: print("Compilar"))
compilar_menu.add_command(label="Run Code", command=lambda: print("Running code"))
menu_bar.add_cascade(label="Compilar", menu=compilar_menu)

# Help menu
menu_bar.add_command(label="Ayuda", command=lambda: print("Ayuda"))

root.config(menu=menu_bar)

# Screen 1: Code entry and line numbers
screen1_frame = tk.Frame(root)
screen1_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Text widget for line numbers
line_numbers = Text(screen1_frame, width=4, bg="#f0f0f0", bd=0, padx=0, pady=0, wrap="none")
line_numbers.pack(side=tk.LEFT, fill=tk.Y)

# Text widget for code entry
code_entry = Text(screen1_frame, height=10, width=50, wrap="none")
code_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
code_entry.bind("<KeyRelease>", on_content_change)

# Scrollbar for code entry and line numbers
scrollbar = Scrollbar(screen1_frame, orient=tk.VERTICAL, command=code_entry.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Linking scrollbar to code entry and line numbers
code_entry.config(yscrollcommand=scrollbar.set)
line_numbers.config(yscrollcommand=scrollbar.set)

# Screen 2: Result of compiling or running code
screen2_frame = tk.Frame(root)
screen2_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

result_text = Text(screen2_frame, height=10, width=50)
result_text.pack(fill=tk.BOTH, expand=True)

# Screen 3: Options and buttons
screen3_frame = tk.Frame(root)
screen3_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Options frame
options_frame = tk.Frame(screen3_frame, padx=10, pady=10)
options_frame.pack(side=tk.TOP)

# Options label
options_label = ttk.Label(options_frame, text="Options:")
options_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Option listbox
options_list = tk.Listbox(options_frame, height=2)
options_list.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
options_list.insert(tk.END, "Syntactic Analyzer")
options_list.insert(tk.END, "Intermediate Code")

# Buttons frame
buttons_frame = tk.Frame(screen3_frame, padx=10, pady=10)
buttons_frame.pack(side=tk.TOP)

# Compile button
compile_button = tk.Button(buttons_frame, text="Compilar", command=lambda: print("Compilar"))
compile_button.grid(row=0, column=0, padx=5, pady=5)

# Run code button
run_button = tk.Button(buttons_frame, text="Run Code", command=lambda: print("Running code"))
run_button.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
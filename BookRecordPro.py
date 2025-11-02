from tkinter import *
from tkinter import ttk
import backend

selected_tuple = None

def get_selected_row(event):
    global selected_tuple
    selected = table.selection()
    if selected:
        index = selected[0]
        selected_tuple = table.item(index)["values"]

        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])

def view_command():
    table.delete(*table.get_children())
    for row in backend.view():
        table.insert("", END, values=row)
    status_label.config(text="All books loaded successfully!")

def search_command():
    table.delete(*table.get_children())
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        table.insert("", END, values=row)
    status_label.config(text="Search completed!")

def add_command():
    if title_text.get() and author_text.get():
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()
        clear_inputs()
        status_label.config(text="Book added successfully!")
    else:
        status_label.config(text="Error: Title and Author are required!")

def delete_command():
    if selected_tuple:
        backend.delete(selected_tuple[0])
        view_command()
        clear_inputs()
        status_label.config(text="Book deleted successfully!")
    else:
        status_label.config(text="Please select a book to delete!")

def update_command():
    if selected_tuple:
        backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()
        status_label.config(text="Book updated successfully!")
    else:
        status_label.config(text="Please select a book to update!")

def clear_command():
    global selected_tuple
    selected_tuple = None
    clear_inputs()
    # Clear table selection
    for item in table.selection():
        table.selection_remove(item)
    status_label.config(text="All fields cleared!")

def clear_inputs():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

# ---------------- Simplified Modern UI ---------------- #

window = Tk()
window.title("Book Records Pro")
window.geometry("900x600")
window.resizable(True, True)

# Modern color scheme
COLORS = {
    "primary": "#2c3e50",
    "secondary": "#34495e", 
    "accent": "#3498db",
    "success": "#27ae60",
    "danger": "#e74c3c",
    "light": "#ecf0f1",
    "dark": "#2c3e50",
    "text": "#2c3e50",
    "text_light": "#ffffff"
}

# Configure styles
style = ttk.Style()
style.theme_use("clam")

# Configure custom styles
style.configure("Primary.TButton", 
                background=COLORS["accent"],
                foreground=COLORS["text_light"],
                borderwidth=0,
                focuscolor="none",
                padding=(10, 5))

style.map("Primary.TButton",
          background=[('active', COLORS["primary"])])

style.configure("Success.TButton",
                background=COLORS["success"],
                foreground=COLORS["text_light"],
                borderwidth=0,
                padding=(10, 5))

style.configure("Danger.TButton",
                background=COLORS["danger"],
                foreground=COLORS["text_light"],
                borderwidth=0,
                padding=(10, 5))

style.configure("Custom.Treeview",
                background="white",
                fieldbackground="white",
                rowheight=25)

style.configure("Custom.Treeview.Heading",
                background=COLORS["primary"],
                foreground=COLORS["text_light"],
                relief="flat",
                font=('Arial', 10, 'bold'))

# Main container
main_container = Frame(window, bg=COLORS["light"])
main_container.pack(fill=BOTH, expand=True, padx=15, pady=15)

# Header
header_frame = Frame(main_container, bg=COLORS["primary"], height=70)
header_frame.pack(fill=X, pady=(0, 15))
header_frame.pack_propagate(False)

header_label = Label(header_frame, 
                    text="📚 Book Records Pro", 
                    bg=COLORS["primary"],
                    fg=COLORS["text_light"],
                    font=('Arial', 18, 'bold'))
header_label.pack(expand=True)

# Main content area
content_frame = Frame(main_container, bg=COLORS["light"])
content_frame.pack(fill=BOTH, expand=True)

# Left section - Inputs and Table
left_section = Frame(content_frame, bg=COLORS["light"])
left_section.pack(side=LEFT, fill=BOTH, expand=True)

# Input section
input_frame = Frame(left_section, bg=COLORS["light"])
input_frame.pack(fill=X, pady=(0, 15))

input_header = Label(input_frame, 
                    text="Book Details",
                    bg=COLORS["light"],
                    fg=COLORS["text"],
                    font=('Arial', 12, 'bold'))
input_header.pack(anchor=W, pady=(0, 10))

# Input grid
input_grid = Frame(input_frame, bg=COLORS["light"])
input_grid.pack(fill=X)

# Configure grid columns
input_grid.columnconfigure(0, weight=1)
input_grid.columnconfigure(1, weight=1)
input_grid.columnconfigure(2, weight=1)
input_grid.columnconfigure(3, weight=1)

label_opts = {"bg": COLORS["light"], "fg": COLORS["text"], "font": ('Arial', 9), "anchor": "w", "pady": 2}

# Title
Label(input_grid, text="Title *", **label_opts).grid(row=0, column=0, sticky="w")
title_text = StringVar()
e1 = ttk.Entry(input_grid, textvariable=title_text, font=('Arial', 9))
e1.grid(row=1, column=0, sticky="ew", pady=(0, 10), padx=(0, 10))

# Author
Label(input_grid, text="Author *", **label_opts).grid(row=0, column=1, sticky="w")
author_text = StringVar()
e2 = ttk.Entry(input_grid, textvariable=author_text, font=('Arial', 9))
e2.grid(row=1, column=1, sticky="ew", pady=(0, 10), padx=(0, 10))

# Year
Label(input_grid, text="Year", **label_opts).grid(row=0, column=2, sticky="w")
year_text = StringVar()
e3 = ttk.Entry(input_grid, textvariable=year_text, font=('Arial', 9))
e3.grid(row=1, column=2, sticky="ew", pady=(0, 10), padx=(0, 10))

# ISBN
Label(input_grid, text="ISBN", **label_opts).grid(row=0, column=3, sticky="w")
isbn_text = StringVar()
e4 = ttk.Entry(input_grid, textvariable=isbn_text, font=('Arial', 9))
e4.grid(row=1, column=3, sticky="ew", pady=(0, 10))

# Quick Actions
quick_actions_frame = Frame(input_frame, bg=COLORS["light"])
quick_actions_frame.pack(fill=X, pady=(5, 0))

btn_opts = {"pady": 5, "padx": 5, "sticky": "ew"}

for i in range(4):
    quick_actions_frame.columnconfigure(i, weight=1)

# Table section
table_frame = Frame(left_section, bg=COLORS["light"])
table_frame.pack(fill=BOTH, expand=True)

table_header = Label(table_frame, 
                    text="Book Collection",
                    bg=COLORS["light"],
                    fg=COLORS["text"],
                    font=('Arial', 12, 'bold'))
table_header.pack(anchor=W, pady=(0, 8))

# Table
table_container = Frame(table_frame, bg=COLORS["light"])
table_container.pack(fill=BOTH, expand=True)

columns = ("id", "title", "author", "year", "isbn")
table = ttk.Treeview(table_container, columns=columns, show="headings", height=15, style="Custom.Treeview")

# Configure columns
table.heading("id", text="ID")
table.heading("title", text="TITLE")
table.heading("author", text="AUTHOR")
table.heading("year", text="YEAR")
table.heading("isbn", text="ISBN")

table.column("id", width=50, anchor=CENTER)
table.column("title", width=200, anchor=W)
table.column("author", width=150, anchor=W)
table.column("year", width=80, anchor=CENTER)
table.column("isbn", width=150, anchor=CENTER)

table.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar
sb1 = ttk.Scrollbar(table_container, orient=VERTICAL, command=table.yview)
sb1.pack(side=RIGHT, fill=Y)
table.configure(yscrollcommand=sb1.set)

# Bind row select
table.bind("<<TreeviewSelect>>", get_selected_row)

# Right section - All Actions
right_section = Frame(content_frame, bg=COLORS["light"], width=180)
right_section.pack(side=RIGHT, fill=Y, padx=(15, 0))
right_section.pack_propagate(False)

actions_header = Label(right_section, 
                      text="Actions",
                      bg=COLORS["light"],
                      fg=COLORS["text"],
                      font=('Arial', 12, 'bold'))
actions_header.pack(anchor=W, pady=(0, 10))

# Actions buttons - all in one place
actions_frame = Frame(right_section, bg=COLORS["light"])
actions_frame.pack(fill=X)

sidebar_btn_opts = {"fill": X, "pady": 6}

ttk.Button(actions_frame, text="👁️ View All", style="Primary.TButton", command=view_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="🧹 Clear All", style="Primary.TButton", command=clear_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="➕ Add Book", style="Success.TButton", command=add_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="🔍 Search", style="Primary.TButton", command=search_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="🔄 Update", style="Primary.TButton", command=update_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="🗑️ Delete", style="Danger.TButton", command=delete_command).pack(**sidebar_btn_opts)
ttk.Button(actions_frame, text="❌ Close", style="Danger.TButton", command=window.destroy).pack(**sidebar_btn_opts)

# Status bar
status_frame = Frame(main_container, bg=COLORS["primary"], height=25)
status_frame.pack(fill=X, pady=(10, 0))
status_frame.pack_propagate(False)

status_label = Label(status_frame, 
                    text="Ready - Select a book or add a new one", 
                    bg=COLORS["primary"],
                    fg=COLORS["text_light"],
                    font=('Arial', 9))
status_label.pack(side=LEFT, padx=10)

# Load initial data
view_command()

window.mainloop()
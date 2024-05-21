import tkinter as tk
from tkinter import ttk

def load_brands():
    brands = set()
    brands.add("All") 
    with open("computer_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == "CPU":
                brands.add(data[2])
    return list(brands)

def filter_data():
    selected_brand = brand_var.get()
    table.delete(*table.get_children())
    with open("computer_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == "CPU" and (selected_brand == "All" or data[2] == selected_brand):
                table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6],data[7],data[8]))

# Create the root Tkinter window
window = tk.Tk()
window.title("Processors")

table = ttk.Treeview(window, columns=("brand", "model", "price", "socket", "speed","memory","power"), show="headings")
table.heading("brand", text="brand")
table.heading("model", text="model")
table.heading("price", text="price")
table.heading("socket", text="socket")
table.heading("speed", text="speed")
table.heading("memory", text="memory")
table.heading("power", text="power")


brands = load_brands()
brand_var = tk.StringVar()
brand_dropdown = ttk.Combobox(window, textvariable=brand_var, values=brands)
brand_dropdown.pack()
brand_dropdown.set("All")

filter_button = ttk.Button(window, text="Filter", command=filter_data)
filter_button.pack()

# Load initial data
with open("computer_parts.txt", "r") as file:
    for line in file:
        data = line.strip().split(',')
        if data[1] == "CPU":
            table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6],data[7],data[8]))

table.pack(expand=True, fill=tk.BOTH)
buy_button = tk.Button(window, text="Buy CPU",command=lambda: add_selected_cpu(table))
buy_button.pack(side=tk.LEFT, anchor=tk.SW, padx=5, pady=5)

def add_selected_cpu(table):
    selected_row = table.selection()
    if selected_row:
        values = table.item(selected_row)["values"]
        cpu_info = ", ".join(map(str, values)) 
        print("Selected CPU added to the list:", cpu_info)

        table.delete(selected_row)

        with open("bought_parts.txt", "a") as bought_file:
            bought_file.write("CPU, "+cpu_info + "\n")

        with open("computer_parts.txt", "r") as file:
            lines = file.readlines()
        with open("computer_parts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] != "CPU" or data[2:] != values:
                    file.write(line)

window.mainloop()
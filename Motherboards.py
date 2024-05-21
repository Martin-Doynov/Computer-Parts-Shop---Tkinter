import tkinter as tk
from tkinter import ttk

def add_selected_motherboard(table):
    selected_row = table.selection()
    if selected_row:
        values = table.item(selected_row)["values"]
        mb_info = ", ".join(map(str, values))
        print("Selected Motherboard added to the list:", mb_info)

        table.delete(selected_row)

        with open("bought_parts.txt", "a") as bought_file:
            bought_file.write("Motherboard, "+mb_info + "\n")

        with open("computer_parts.txt", "r") as file:
            lines = file.readlines()
        with open("computer_parts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] != "Motherboard" or data[2:] != values:
                    file.write(line)

def filter_by_socket():
    selected_socket = socket_combobox.get()
    if selected_socket == "All":
        table.delete(*table.get_children())
        with open("computer_parts.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if data[1] == "Motherboard":
                    table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6], data[7]))
    else:
        table.delete(*table.get_children())
        with open("computer_parts.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if data[1] == "Motherboard" and data[5] == selected_socket:
                    table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6], data[7]))

def get_unique_sockets():
    sockets = set()
    with open("computer_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == "Motherboard":
                sockets.add(data[5])
    return ["All"] + list(sockets)

window=tk.Tk()
window.title("Motherboards")

table=ttk.Treeview(window,columns=("brand","model","price","socket","memory","size"),show="headings")
table.heading("brand",text="Brand")
table.heading("model",text="Model")
table.heading("price",text="Price")
table.heading("socket",text="Socket")
table.heading("memory",text="Memory")
table.heading("size",text="Size")
table.pack(expand=True, fill=tk.BOTH)

with open("computer_parts.txt", "r") as file:
    for line in file:
        data = line.strip().split(',')
        if data[1] == "Motherboard":
            table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6], data[7]))

sockets = get_unique_sockets()
socket_combobox = ttk.Combobox(window, values=sockets)
socket_combobox.pack()

filter_button = tk.Button(window, text="Filter by Socket", command=filter_by_socket)
filter_button.pack()

buy_button = tk.Button(window, text="Buy Motherboard",command=lambda: add_selected_motherboard(table))
buy_button.pack(side=tk.LEFT, anchor=tk.SW, padx=5, pady=5)

window.mainloop()

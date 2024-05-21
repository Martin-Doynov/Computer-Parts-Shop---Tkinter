import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Graphics Cards")
gpu_list = []
table=ttk.Treeview(window,columns=("brand","model","price","memory","bandwidth"),show="headings")
table.heading("brand",text="brand")
table.heading("model",text="model")
table.heading("price",text="price")
table.heading("memory",text="memory")
table.heading("bandwidth",text="bandwidth")

with open("computer_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == "GPU":
                table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6]))
def sort_ascending():
        table_items = table.get_children('')
        table_items = sorted(table_items, key=lambda x: float(table.item(x)['values'][2]))
        for index, item in enumerate(table_items):
            table.move(item, '', index)

            
sort_ascending_button = tk.Button(window, text="Sort Ascending", command=sort_ascending)
sort_ascending_button.pack()

def sort_descending():
        table_items = table.get_children('')
        table_items = sorted(table_items, key=lambda x: float(table.item(x)['values'][2]), reverse=True)
        for index, item in enumerate(table_items):
            table.move(item, '', index)
            
sort_descending_button = tk.Button(window, text="Sort Descending", command=sort_descending)
sort_descending_button.pack()

table.pack(expand=True, fill=tk.BOTH)
table.pack()

buy_button = tk.Button(window, text="Buy GPU",command=lambda: add_selected_gpu(table))
buy_button.pack(side=tk.LEFT, anchor=tk.SW, padx=5, pady=5)

def add_selected_gpu(table):
    selected_row = table.selection()
    if selected_row:
        values = table.item(selected_row)["values"]
        gpu_info = ", ".join(map(str, values))
        gpu_list.append(gpu_info)
        print("Selected GPU added to the list:", gpu_info)

        table.delete(selected_row)

        with open("bought_parts.txt", "a") as bought_file:
            bought_file.write("GPU, "+gpu_info + "\n")

        with open("computer_parts.txt", "r") as file:
            lines = file.readlines()
        with open("computer_parts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] != "GPU" or data[2:] != values:
                    file.write(line)

window.mainloop()
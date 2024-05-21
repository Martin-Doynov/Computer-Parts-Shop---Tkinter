import tkinter as tk
from tkinter import ttk

def add_selected_psu(table):
    # Get the selected row from the table
    selected_row = table.selection()
    if selected_row:
        values = table.item(selected_row)["values"]
        psu_info = ", ".join(map(str, values))  # Convert the selected row values to a string
        print("Selected PSU added to the list:", psu_info)

        # Remove the selected row from the table
        table.delete(selected_row)

        # Write the PSU information to the bought_parts.txt file
        with open("bought_parts.txt", "a") as bought_file:
            bought_file.write("PSU, "+psu_info + "\n")

        # Remove the PSU from the file
        with open("computer_parts.txt", "r") as file:
            lines = file.readlines()
        with open("computer_parts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] != "PSU" or data[2:] != values:
                    file.write(line)

def filter_psu(power_range):
    table.delete(*table.get_children())  # Clear the table
    with open("computer_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == "PSU":
                power = int(data[5][:-1])
                if power_range == "below_500" and power < 500:
                    table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6]))
                elif power_range == "between_500_700" and 500 <= power <= 700:
                    table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6]))
                elif power_range == "above_700" and power > 700:
                    table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6]))

window = tk.Tk()
window.title("Power supplies")

table = ttk.Treeview(window, columns=("brand", "model", "price", "power", "certification"), show="headings")
table.heading("brand", text="Brand")
table.heading("model", text="Model")
table.heading("price", text="Price")
table.heading("power", text="Power")
table.heading("certification", text="Certification")
table.pack(expand=True, fill=tk.BOTH)

# Insertion of PSUs into the table
with open("computer_parts.txt", "r") as file:
    for line in file:
        data = line.strip().split(',')
        if data[1] == "PSU":
            table.insert("", "end", values=(data[2], data[3], data[4], data[5], data[6]))

# Radio buttons for filtering PSUs
filter_frame = tk.Frame(window)
filter_frame.pack()

power_filter_var = tk.StringVar()
power_filter_var.set("all")

below_500_radio = tk.Radiobutton(filter_frame, text="Below 500W", variable=power_filter_var, value="below_500", command=lambda: filter_psu(power_filter_var.get()))
below_500_radio.pack(side=tk.LEFT)

between_500_700_radio = tk.Radiobutton(filter_frame, text="500-700W", variable=power_filter_var, value="between_500_700", command=lambda: filter_psu(power_filter_var.get()))
between_500_700_radio.pack(side=tk.LEFT)

above_700_radio = tk.Radiobutton(filter_frame, text="Above 700W", variable=power_filter_var, value="above_700", command=lambda: filter_psu(power_filter_var.get()))
above_700_radio.pack(side=tk.LEFT)

buy_button = tk.Button(window, text="Buy PSU", command=lambda: add_selected_psu(table))
buy_button.pack(side=tk.LEFT, anchor=tk.SW, padx=5, pady=5)

window.mainloop()
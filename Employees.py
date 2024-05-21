import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def populate_table(table):
    output_dict = dict()
    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[3] != '0': # if employee is NOT fired
                output_dict.update({data[1]:data[2]})
    
    output_dict = {key: round(float(value),2) for key, value in output_dict.items()} # converts earned money into double from string
    output_dict = dict(sorted(output_dict.items(), key=lambda item: item[1], reverse=True)) # We want the employees automatically sorted in descending order

    for key, value in output_dict.items():
        table.insert("", "end", values=(key, value))

def on_row_selected(event):
    selected_items = table.selection()
    if selected_items:
        selected_item = selected_items[0]
        selected_row = table.item(selected_item)

        name, money_earned = selected_row['values']

        name_field.delete(0, tk.END)
        name_field.insert(tk.END, name)

        money_field.config(text=str("$"+money_earned))
    else: print("Row no longer selected")

def addEmployee():
    name_value = name_field.get()

    empAlreadyExists = False   

    employees = []

    with open('employees.txt','r') as file:
        for line in file:
            data = line.strip().split(",")
            if name_value == data[1]: empAlreadyExists = True
            employees.append(f"{data[0]},{data[1]},{data[2]},{data[3]}")
    
    if empAlreadyExists:
        messagebox.showinfo("Error", "The person already exists!")
    else:
        if messagebox.askyesno("Add new employee?",f"Are you sure you want to add {name_value} as a new employee?"):
            employees.append(f"{len(employees)+1},{name_value},0.00,1")
            with open('employees.txt','w') as file:
                for employee in employees:
                    file.write(f"{employee}\n")
            table.delete(*table.get_children())
            populate_table(table)
            

def fireEmployee():
    selected_item = table.selection()
    selected_row = table.item(selected_item)

    name, money_earned = selected_row['values']

    print(f"The selected name is {name}")

    with open('employees.txt','r') as file:
        data = file.readlines()
    
    for i in range(len(data)):
        line = data[i].strip().split(',')
        if line[1] == name:
            if messagebox.askyesno("Fire this employee?",f"Are you sure you want to fire {name}?"):
                line[1]="[EXPUNGED]"+line[1]
                line[-1] = '0\n'
                data[i] = ','.join(line)
                table.delete(selected_item)
                break

    with open('employees.txt', 'w') as file:
        file.writelines(''.join(data))    
        




window = tk.Tk()
window.title("Employee Details")

tk.Label(window, text="Name").grid(column=0, row=0)
name_field = tk.Entry(window)
name_field.grid(column=1, row=0)

add_button = tk.Button(window, text="Add", command=addEmployee, width=20)
add_button.grid(column=2, row=0)

tk.Label(window, text="Money earned so far").grid(column=0, row=1)
money_field = tk.Label(window, text="", anchor="w")
money_field.grid(column=1, row=1, sticky="w")

fire_button = tk.Button(window, text="Fire", command=fireEmployee, width=20)

table = ttk.Treeview(window, columns=("Name", "Money Earned"), show='headings')
table.heading("Name", text="Name")
table.heading("Money Earned", text="Money Earned")
table.grid(column=0, row=2, columnspan=3)

table.bind('<<TreeviewSelect>>', on_row_selected)

populate_table(table)

window.mainloop()

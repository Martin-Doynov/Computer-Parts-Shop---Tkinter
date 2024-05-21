import tkinter as tk
from tkinter import ttk


def filter_and_populate():

    table.delete(*table.get_children()) # clear table

    product_employee_value = product_employee_dropdown.get()
    criterion_value = criterion_dropdown.get()

    # Get entered text from text fields
    price_from_value = price_from_field.get()
    price_to_value = price_to_field.get()
    boolRangeInsteadOfCriterion = True

    if not price_from_value or not price_to_value: # if both the range variables are empty
        boolRangeInsteadOfCriterion = False
    
    sister_values = {"All":"All", "Processor":"CPU" , "Graphics Card":"GPU", "Motherboard":"Motherboard", 
                     "Power Supply":"PSU", "Memory":"RAM", "Employee":"Employee"}
    # instead of making the values in the dropbox aligned directly with their names in the files,
    # we decided to use a dictionary instead :D

    raw_data = []
    output_dict = dict()

    with open("computer_parts.txt", "r") as file, open("employees.txt","r",encoding="windows-1251") as file2:
        for line in file:
            data = line.strip().split(",")
            raw_data.append(data)
        
        for line in file2:
            data = line.strip().split(",")
            raw_data.append(data)
        # print(raw_data)

    
    for line in raw_data:
        # if raw_data[1] == sister_values.get(product_employee_value):
        #     output_dict.update({raw_data[2] + " " + raw_data[3] : raw_data[4]}) # AMD Ryzen 9 5950X : 749.99
        # else: # for employees
        isEmployee = False
        if line[1] not in sister_values.values() and line[3] != "0": # checks if it is an employee and not fired
            isEmployee = True

        if product_employee_value == "All":
            if isEmployee == True: output_dict.update({line[1]:line[2]})
            elif not line[1].startswith('[EXPUNGED]'): 
                output_dict.update({line[2]+" "+line[3]:line[4]})
        elif product_employee_value == "Employee":
            if isEmployee == True: output_dict.update({line[1]:line[2]})
            print(line[1])
        else: 
            product_value = sister_values.get(product_employee_value)
            if product_value == line[1]:
                output_dict.update({line[2]+" "+line[3]:line[4]})


    output_dict = {key: round(float(value),2) for key, value in output_dict.items()} # converts earned money into double from string

    if boolRangeInsteadOfCriterion == False:
        if criterion_value == "Highest": # Find highest value + its keyS
            temp = max(output_dict.values())
            # print("OAIEJOIEATJOEAIJTOIEAJTOAIE",temp)
            res = [key for key in output_dict if output_dict[key] == temp]
            output_dict = {key: temp for key in res}
        elif criterion_value == "Lowest": # Find lowest value + its keyS
            temp = min(output_dict.values())
            # print("gdsfgsfdgdsf",temp)
            res = [key for key in output_dict if output_dict[key] == temp]
            output_dict = {key: temp for key in res}
    
    elif boolRangeInsteadOfCriterion == True:
        output_dict = {key: val for key, val in filter(lambda sub: float(sub[1]) >= float(price_from_value) and
                                   float(sub[1]) <= float(price_to_value), output_dict.items())} # pilfered from geeksforgeeks :D
        
            
        
    print(output_dict)

    

    # Populate the table with the key and values from output_dict
    for key, value in output_dict.items():
        table.insert("", "end", values=(key, value))

window = tk.Tk()
window.title("Extracts")

tk.Label(window, text="Product/Employees").grid(column=0, row=0)
tk.Label(window, text="Criterion").grid(column=0, row=1)
tk.Label(window, text="or").grid(column=0, row=2)
tk.Label(window, text="Price from:").grid(column=0, row=3)
tk.Label(window, text="Price to:").grid(column=0, row=4)

product_employee_dropdown = ttk.Combobox(window)
product_employee_dropdown['values'] = ("All", "Processor", "Graphics Card", "Motherboard", "Power Supply", "Memory", "Employee")
product_employee_dropdown.grid(column=1, row=0)
product_employee_dropdown.current(0)

criterion_dropdown = ttk.Combobox(window)
criterion_dropdown['values'] = ("None", "Highest", "Lowest")
criterion_dropdown.grid(column=1, row=1)
criterion_dropdown.current(0)

price_from_field = tk.Entry(window)
price_from_field.grid(column=1, row=3)

price_to_field = tk.Entry(window)
price_to_field.grid(column=1, row=4)

filter_button = tk.Button(window, text="Filter", command =filter_and_populate)
filter_button.grid(column=0, row=5, columnspan=2)

table = ttk.Treeview(window, columns=("Product/Employee", "Price"), show='headings')
table.heading("Product/Employee", text="Product/Employee")
table.heading("Price", text="Price")
table.grid(column=0, row=6, columnspan=2)

window.mainloop()


            

    





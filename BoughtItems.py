import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def calculate_total_price():
    total_price = 0
    with open("bought_parts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            total_price += float(data[3])
        return total_price

def buy_item():
    hired_employees = dict()
    
    with open("employees.txt","r",encoding="windows-1251") as file:
        for line in file:
            data = line.strip().split(",")
            if data[3]=='1': hired_employees.update({data[1]:data[2]})

    res = key, val = list(random.choice(list(hired_employees.items()))) # a random employee will take the order and will be turned into a list
    
    res[1]=float(res[1])+calculate_total_price() # the employee is responsible for this order's handling and his money value is updated

    with open('employees.txt','r') as file:
        data = file.readlines()
    
    for i in range(len(data)):
        line = data[i].strip().split(',')
        if line[1] == res[0]:
            line[2] = str(res[1])
            line[3]+="\n"
            data[i] = ','.join(line)
            messagebox.showinfo("Finish order",f"Your order estimates to ${calculate_total_price()} and was serviced by {line[1]}!")
            break

    with open('employees.txt', 'w') as file:
        file.writelines(''.join(data))   

    with open('bought_parts.txt', 'w'):
        table.delete(*table.get_children())    
    


window = tk.Tk()
window.title("Bought items")

motherboard_list = []

table = ttk.Treeview(window, columns=("type", "brand", "model", "price"), show="headings")
table.heading("type", text="type")
table.heading("brand", text="brand")
table.heading("model", text="model")
table.heading("price", text="price")

with open("bought_parts.txt", "r") as file:
    for line in file:
        data = line.strip().split(',')
        table.insert("", "end", values=(data[0], data[1], data[2], data[3]))

table.pack(expand=True, fill=tk.BOTH)

total_price_label = tk.Label(window, text=f"Total Spent: ${calculate_total_price():.2f}")
total_price_label.pack()

buy_button = tk.Button(window, text="Buy", command=buy_item)
buy_button.pack()

window.mainloop()
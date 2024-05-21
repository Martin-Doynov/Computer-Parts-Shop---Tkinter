import tkinter as tk
import tkinter.font as tkFont
import subprocess
class App:
    def __init__(self, root):
        #setting title
        root.title("Computer parts shop")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_570=tk.Button(root)
        GButton_570["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Processors"
        GButton_570.place(x=50,y=70,width=100,height=25)
        GButton_570["command"] = self.GButton_570_command

        GButton_300=tk.Button(root)
        GButton_300["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_300["font"] = ft
        GButton_300["fg"] = "#000000"
        GButton_300["justify"] = "center"
        GButton_300["text"] = "Graphics cards"
        GButton_300.place(x=50,y=110,width=100,height=25)
        GButton_300["command"] = self.GButton_300_command


        GButton_352=tk.Button(root)
        GButton_352["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_352["font"] = ft
        GButton_352["fg"] = "#000000"
        GButton_352["justify"] = "center"
        GButton_352["text"] = "Motherboards"
        GButton_352.place(x=50,y=150,width=100,height=25)
        GButton_352["command"] = self.GButton_352_command


        GButton_412=tk.Button(root)
        GButton_412["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_412["font"] = ft
        GButton_412["fg"] = "#000000"
        GButton_412["justify"] = "center"
        GButton_412["text"] = "Power supplies"
        GButton_412.place(x=50,y=190,width=100,height=25)
        GButton_412["command"] = self.GButton_412_command

        GButton_777=tk.Button(root)
        GButton_777["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_777["font"] = ft
        GButton_777["fg"] = "#000000"
        GButton_777["justify"] = "center"
        GButton_777["text"] = "Memory"
        GButton_777.place(x=50,y=230,width=100,height=25)
        GButton_777["command"] = self.GButton_777_command

        GLabel_75=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_75["font"] = ft
        GLabel_75["fg"] = "#333333"
        GLabel_75["justify"] = "center"
        GLabel_75["text"] = "Categories"
        GLabel_75.place(x=60,y=30,width=70,height=25)

        def exit_app(): 
            root.destroy()

        GButton_190=tk.Button(root, command = exit_app)
        GButton_190["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_190["font"] = ft
        GButton_190["fg"] = "#000000"
        GButton_190["justify"] = "center"
        GButton_190["text"] = "Exit"
        GButton_190.place(x=60,y=440,width=70,height=25)


        GButton_580=tk.Button(root)
        GButton_580["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)  
        GButton_580["font"] = ft
        GButton_580["fg"] = "#000000"
        GButton_580["justify"] = "center"
        GButton_580["text"] = "View bought items"
        GButton_580.place(x=410,y=80,width=120,height=25)
        GButton_580["command"] = self.GButton_580_command

        EmployeesButton = tk.Button(root)
        EmployeesButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        EmployeesButton["font"] = ft
        EmployeesButton["fg"] = "#000000"
        EmployeesButton["justify"] = "center"
        EmployeesButton["text"] = "Employees"
        EmployeesButton.place(x=410,y=120,width=120,height=25)
        EmployeesButton["command"] = self.EmployeesButton_command

        ExtractButton = tk.Button(root)
        ExtractButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ExtractButton["font"] = ft
        ExtractButton["fg"] = "#000000"
        ExtractButton["justify"] = "center"
        ExtractButton["text"] = "Extracts"
        ExtractButton.place(x=410,y=160,width=120,height=25)
        ExtractButton["command"] = self.ExtractButton_command

    def GButton_570_command(self):
        subprocess.Popen(["python", "Processors.py"])

    def GButton_300_command(self):
        subprocess.Popen(["python", "GraphicsCards.py"])

    def GButton_352_command(self):
        subprocess.Popen(["python", "Motherboards.py"])

    def GButton_412_command(self):
        subprocess.Popen(["python", "Powersupplies.py"])

    def GButton_777_command(self):
        subprocess.Popen(["python", "Memory.py"])

    def GButton_580_command(self):
        subprocess.Popen(["python", "BoughtItems.py"])

    def EmployeesButton_command(self):
        subprocess.Popen(["python", "Employees.py"])

    def ExtractButton_command(self):
        subprocess.Popen(["python", "Extract.py"])        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

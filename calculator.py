import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Create Entry widget to display calculations
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        
        # Create buttons for numbers and operations
        self.buttons = [
            tk.Button(master, text="7", width=5, height=2, command=lambda: self.add_to_display("7")),
            tk.Button(master, text="8", width=5, height=2, command=lambda: self.add_to_display("8")),
            tk.Button(master, text="9", width=5, height=2, command=lambda: self.add_to_display("9")),
            tk.Button(master, text="4", width=5, height=2, command=lambda: self.add_to_display("4")),
            tk.Button(master, text="5", width=5, height=2, command=lambda: self.add_to_display("5")),
            tk.Button(master, text="6", width=5, height=2, command=lambda: self.add_to_display("6")),
            tk.Button(master, text="1", width=5, height=2, command=lambda: self.add_to_display("1")),
            tk.Button(master, text="2", width=5, height=2, command=lambda: self.add_to_display("2")),
            tk.Button(master, text="3", width=5, height=2, command=lambda: self.add_to_display("3")),
            tk.Button(master, text="0", width=5, height=2, command=lambda: self.add_to_display("0")),
            tk.Button(master, text="+", width=5, height=2, command=lambda: self.add_to_display("+")),
            tk.Button(master, text="-", width=5, height=2, command=lambda: self.add_to_display("-")),
            tk.Button(master, text="*", width=5, height=2, command=lambda: self.add_to_display("*")),
            tk.Button(master, text="/", width=5, height=2, command=lambda: self.add_to_display("/")),
            tk.Button(master, text=".", width=5, height=2, command=lambda: self.add_to_display(".")),
            tk.Button(master, text="C", width=5, height=2, command=lambda: self.clear_display()),
            tk.Button(master, text="=", width=5, height=2, command=lambda: self.calculate()),
        ]
        
        # Position buttons on the grid
        row = 1
        column = 0
        for button in self.buttons:
            button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column > 3:
                column = 0
                row += 1
                
    def add_to_display(self, text):
        self.display.insert('end', text)
        
    def clear_display(self):
        self.display.delete(0, 'end')
        
    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.add_to_display(str(result))
        except:
            self.clear_display()
            self.add_to_display("Error")
        
root = tk.Tk()
app = Calculator(root)
root.mainloop()

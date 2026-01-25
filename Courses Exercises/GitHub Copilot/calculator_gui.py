import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.configure(bg='#5e4b8a')  # Dark clear purple background

        self.current_input = ""
        self.mode = "simple"  # Default mode

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.master, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            'sin', 'cos', 'tan', 'sqrt'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == 'C':
                tk.Button(self.master, text=button, padx=20, pady=20, bg='blue', command=self.clear).grid(row=row_val, column=col_val)
            elif button == '=':
                tk.Button(self.master, text=button, padx=20, pady=20, bg='blue', command=self.calculate).grid(row=row_val, column=col_val)
            elif button in ['sin', 'cos', 'tan', 'sqrt']:
                tk.Button(self.master, text=button, padx=20, pady=20, bg='blue', command=lambda b=button: self.complex_operation(b)).grid(row=row_val, column=col_val)
            else:
                tk.Button(self.master, text=button, padx=20, pady=20, bg='blue', command=lambda b=button: self.add_to_input(b)).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Mode toggle button
        self.mode_button = tk.Button(self.master, text='Toggle Mode', padx=20, pady=20, bg='blue', command=self.toggle_mode)
        self.mode_button.grid(row=row_val, column=0, columnspan=4)

        # Message label
        self.message_label = tk.Label(self.master, text='Welcome to the Calculator!', bg='#5e4b8a', fg='white', font=('Arial', 14))
        self.message_label.grid(row=row_val + 1, column=0, columnspan=4)

    def add_to_input(self, value):
        self.current_input += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def clear(self):
        self.current_input = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.current_input)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.current_input = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    def complex_operation(self, operation):
        if self.mode == "complex":
            try:
                if operation == 'sin':
                    result = math.sin(math.radians(float(self.current_input)))
                elif operation == 'cos':
                    result = math.cos(math.radians(float(self.current_input)))
                elif operation == 'tan':
                    result = math.tan(math.radians(float(self.current_input)))
                elif operation == 'sqrt':
                    result = math.sqrt(float(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.current_input = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            messagebox.showinfo("Info", "Switch to Complex Mode to use this operation.")

    def toggle_mode(self):
        if self.mode == "simple":
            self.mode = "complex"
            self.message_label.config(text='Complex Mode Activated')
        else:
            self.mode = "simple"
            self.message_label.config(text='Simple Mode Activated')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
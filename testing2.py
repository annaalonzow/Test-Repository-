import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        elif op == '\\':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 // num2   # floor division
        elif op == '^':
            result = num1 ** num2   # exponent
        elif op == '%':             # modulus
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 % num2

        result_var.set(result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

def exit_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("200x300")

# Title
tk.Label(root, text="Simple Calculator", font=("Arial Narrow", 12, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# LEFT: Operators
left_frame = tk.Frame(frame)
left_frame.grid(row=0, column=0, padx=10)

tk.Label(left_frame, text="Operators:", font=("Arial", 10)).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)

btn_w = 5
pad = 3

# Row 1
tk.Button(left_frame, text="+", width=btn_w,
          command=lambda: calculate('+')).grid(row=1, column=0, padx=pad, pady=pad)

tk.Button(left_frame, text="-", width=btn_w,
          command=lambda: calculate('-')).grid(row=1, column=1, padx=pad, pady=pad)

# Row 2
tk.Button(left_frame, text="*", width=btn_w,
          command=lambda: calculate('*')).grid(row=2, column=0, padx=pad, pady=pad)

tk.Button(left_frame, text="/", width=btn_w,
          command=lambda: calculate('/')).grid(row=2, column=1, padx=pad, pady=pad)

# Row 3
tk.Button(left_frame, text="\\", width=btn_w,
          command=lambda: calculate('\\')).grid(row=3, column=0, padx=pad, pady=pad)

tk.Button(left_frame, text="^", width=btn_w,
          command=lambda: calculate('^')).grid(row=3, column=1, padx=pad, pady=pad)

# Row 4
tk.Button(left_frame, text="Mod", width=btn_w*2+2,
          command=lambda: calculate('%')).grid(row=4, column=0, columnspan=2, pady=pad)

# RIGHT: Inputs and Result
input_frame = tk.Frame(frame)
input_frame.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Operand 1").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1)

tk.Label(input_frame, text="Operand 2").grid(row=1, column=0, pady=5)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1)

tk.Label(input_frame, text="Result").grid(row=2, column=0, pady=5)
result_var = tk.StringVar()
tk.Entry(input_frame, textvariable=result_var, state='readonly').grid(row=2, column=1)

# Bottom buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

tk.Button(bottom_frame, text="Clear", width=10, command=clear).grid(row=0, column=0, padx=5)
tk.Button(bottom_frame, text="Exit", width=10, command=exit_app).grid(row=0, column=1, padx=5)

root.mainloop()

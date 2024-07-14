import tkinter as tk

# Function to update the expression in the entry widget
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the entry widget
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression and update the entry widget
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Initialize the main window
win = tk.Tk()
win.geometry("400x500")
win.resizable(0, 0)
win.title("Calculator")

# String variable to hold the expression
expression = ""
input_text = tk.StringVar()

# Entry widget for displaying the expression
input_frame = tk.Frame(win, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of the entry widget

# Frame for the buttons
btns_frame = tk.Frame(win, width=400, height=450, bg="grey")
btns_frame.pack()

# First row
tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# Second row
tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("7")).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("8")).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("9")).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third row
tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("4")).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("5")).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("6")).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("1")).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("2")).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("3")).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth row
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
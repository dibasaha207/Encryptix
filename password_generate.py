import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(int(length)))
    t = tk.Label(root,text=f"Generated Password\n {password}",fg="maroon",font=('arial',16,'bold'))
    t.pack(pady=20)
    return password

root = tk.Tk()
root.geometry('400x300')
root.resizable(False,True)
root.title("Generate Password")

bar = tk.Frame(root, bg="maroon", height=50)
bar.pack(fill=tk.X)

text = tk.Label(bar, text="Random Password Generator", bg='maroon', font=('arial', 16, 'bold'), fg='white')
text.pack(pady=6)

text2 = tk.Label(root, text="Enter the length of password", font=('arial', 16, 'bold'), fg='maroon')
text2.pack(pady=6)

e = tk.Entry(root, width=30, background="white", foreground="black", font=("arial", 16))
e.place(height=80)
e.pack(pady=20, padx=7)

button = tk.Button(root,bg='maroon',fg='white',command=lambda:generate_password(e.get()),font=("arial", 14),width=30,text="Generate Password")
button.pack()



root.mainloop()
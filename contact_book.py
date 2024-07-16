import tkinter as tk
from tkinter import messagebox,simpledialog

root = tk.Tk()
root.title("Contact Manager")
root.geometry('400x500')
root.resizable(False,False)
root.config(bg='lightblue')

contact = {}

def add_contact():
    name = simpledialog.askstring("Input","Enter Name:")
    phone = simpledialog.askstring("Input","Enter Phone Number:")
    email = simpledialog.askstring("Input","Enter Email Address:")
    address = simpledialog.askstring("Input","Enter Address:")
    if name and phone:
        contact[name]={"Phone":phone,"email":email,"address":address}
        messagebox.showinfo("Success",f"{name} added successfully in contact")
        view_contact()

def update_contact():
    selected_item = contact_list.get(tk.ACTIVE)
    if selected_item:
        name = selected_item.split(":")[0]
        new_phone = simpledialog.askstring("Input","Enter New Phone Number: ")
        new_email = simpledialog.askstring("Input","Enter New Email: ")
        new_address = simpledialog.askstring("Input","Enter New Address: ")
        contact[name]={"Phone":new_phone,"email":new_email,"address":new_address}
        messagebox.showinfo("Success",f"{name} updated successfully in contact")
        view_contact()

def search_contact():
    search = simpledialog.askstring("Search","Enter name or phone number")
    contact_list.delete(0, tk.END)
    for name,info in contact.items():
        if search in name or search in info['Phone']:
            contact_list.insert(tk.END,f"{name}:{info['Phone']}")
            

def view_contact():
    contact_list.delete(0, tk.END)
    for name,info in contact.items():
        contact_list.insert(tk.END,f"{name}:{info['Phone']}")
        contact_list.insert(tk.END,f"{info['email']}|{info['address']}")
        
        
    
def delete_contact():
    selected_item = contact_list.get(tk.ACTIVE)
    if selected_item:
        name = selected_item.split(":")[0]
        del contact[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        view_contact()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

bar = tk.Frame(root,bg="white",height=50)
bar.pack(fill=tk.X)

text = tk.Label(bar,text="Contact Book",bg='white',fg='black',font=('arial', 16, 'bold'))
text.pack(pady=6)

contact_list = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("arial", 16))
contact_list.pack(fill="both", expand=True, padx=7, pady=5)

buttons_frame = tk.Frame(root, bg='lightblue')
buttons_frame.pack(pady=5)

add_button = tk.Button(buttons_frame, text="Add Contact", width=15, command=add_contact, background="white", fg="black", borderwidth=3)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(buttons_frame, text="Update Contact", width=15, command=update_contact, background="white", fg="black", borderwidth=3)
update_button.grid(row=0, column=2, padx=5, pady=5)

view_button = tk.Button(buttons_frame, text="View Contact", width=15, command=view_contact, background="white", fg="black", borderwidth=3)
view_button.grid(row=1, column=0, padx=5, pady=5)

search_button = tk.Button(buttons_frame, text="Search Contact", width=15, command=search_contact, background="white", fg="black", borderwidth=3)
search_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = tk.Button(buttons_frame, text="Delete Contact", width=15, command=delete_contact, background="white", fg="black", borderwidth=3)
delete_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
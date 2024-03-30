import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 8:
        messagebox.showwarning("WARNING!", "Password length shoul dbe at least 8 characters.")
        return
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get()
    password = password_entry.get()
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website} - Password: {password}\n")
    messagebox.showinfo("Success", "Password saved successfully!")

root = tk.Tk()
root.title("Password Generator")

website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

website_entry = tk.Entry(root, width=20)
website_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = tk.Label(root, text="Password Length: ")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

password_entry = tk.Entry(root, width=50)
password_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

root.mainloop()
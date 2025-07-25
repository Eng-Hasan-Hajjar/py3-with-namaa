import json
import os
import tkinter as tk
from tkinter import messagebox

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()  # ← تم التصحيح هنا

    if not username or not password:
        messagebox.showwarning("Missing Info", "Please enter your name and password")
        return

    users = load_users()

    if username in users:
        if users[username] == password:
            messagebox.showinfo("Login Successful", f"Hello, {username}!")
        else:
            messagebox.showerror("Error", "Invalid password")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Welcome", f"Thank you, {username}, you have been registered!")

# واجهة المستخدم
window = tk.Tk()
window.title("Login System")
window.geometry("400x250")

tk.Label(window, text="Username").pack(pady=5)
entry_user = tk.Entry(window)
entry_user.pack()

tk.Label(window, text="Password").pack(pady=5)
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

tk.Button(window, text="Login", command=login).pack(pady=20)

window.mainloop()
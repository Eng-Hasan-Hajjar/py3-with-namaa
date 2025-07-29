import json
import os
import tkinter as tk
from tkinter import messagebox, ttk

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def open_dashboard(username):
    # نافذة جديدة بعد التسجيل
    dashboard = tk.Toplevel()
    dashboard.title(f"Dashboard - Welcome {username}")
    dashboard.geometry("600x400")

    # مثال: إضافة عناصر مشابهة للقائمة الأصلية (كـ GLOBALS و Graphs)
    tab_control = ttk.Notebook(dashboard)

    # تبويب GLOBALS
    globals_tab = ttk.Frame(tab_control)
    tab_control.add(globals_tab, text="GLOBALS")
    ttk.Label(globals_tab, text="Combat Settings").pack(pady=10)
    ttk.Checkbutton(globals_tab, text="Enable Combat").pack(anchor="w")
    ttk.Checkbutton(globals_tab, text="Enable Visuals").pack(anchor="w")

    # تبويب Graphs
    graphs_tab = ttk.Frame(tab_control)
    
    tab_control.add(graphs_tab, text="Graphs")
    ttk.Label(graphs_tab, text="Aimbot Settings").pack(pady=10)
    ttk.Checkbutton(graphs_tab, text="Auto-fire").pack(anchor="w")
    ttk.Checkbutton(graphs_tab, text="Auto-scope").pack(anchor="w")
    ttk.Checkbutton(graphs_tab, text="aimbot").pack(anchor="w")
    ttk.Checkbutton(graphs_tab, text="wall hack").pack(anchor="w")
    tab_control.pack(expand=1, fill="both")

def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not username or not password:
        messagebox.showwarning("Missing Info", "Please enter your name and password")
        return

    users = load_users()

    if username in users:
        if users[username] == password:
            messagebox.showinfo("Login Successful", f"Hello, {username}!")
            window.withdraw()  # إخفاء نافذة الدخول
            open_dashboard(username)  # فتح لوحة التحكم
        else:
            messagebox.showerror("Error", "Invalid password")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Welcome", f"Thank you, {username}, you have been registered!")
        window.withdraw()
        open_dashboard(username)

# واجهة الدخول الرئيسية
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
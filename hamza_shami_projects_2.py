import tkinter as tk
from tkinter import messagebox

# Fake database (you can expand it later or load from a file)
citizens = {
    "123456789": {
        "name": "Ahmed Ali",
        "birthdate": "1990-01-15",
        "address": "Riyadh, Saudi Arabia",
        "job": "Engineer"
    },
    "987654321": {
        "name": "Sara Mohammed",
        "birthdate": "1985-05-22",
        "address": "Jeddah, Saudi Arabia",
        "job": "Teacher"
    },
    "111222333": {
        "name": "Khaled Saleh",
        "birthdate": "1978-12-10",
        "address": "Dammam, Saudi Arabia",
        "job": "Doctor"
    }
}

# Search function
def search():
    citizen_id = entry_id.get()
    output_box.delete("1.0", tk.END)

    if citizen_id in citizens:
        info = citizens[citizen_id]
        result = (
            f"Name: {info['name']}\n"
            f"Birthdate: {info['birthdate']}\n"
            f"Address: {info['address']}\n"
            f"Job: {info['job']}"
        )
        output_box.insert(tk.END, result)
    else:
        messagebox.showinfo("Not Found", "No citizen found with that ID.")

# GUI setup
root = tk.Tk()
root.title("Citizen Info Lookup")
root.geometry("400x300")

# ID input
tk.Label(root, text="Enter Citizen ID:").pack(pady=10)
entry_id = tk.Entry(root, width=30)
entry_id.pack()

# Search button
tk.Button(root, text="Search", command=search).pack(pady=10)

# Output display
output_box = tk.Text(root, height=8, width=45)
output_box.pack(pady=10)

# Start the app
root.mainloop()
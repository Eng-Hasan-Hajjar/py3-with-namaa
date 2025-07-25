import tkinter as tk
from tkinter import ttk
from datetime import datetime

products = []

def add_product():
    name = entry_name.get()
    try:
        price = float(entry_price.get())
        time_added = datetime.now().strftime("%H:%M:%S")
        products.append((name, price, time_added))
        update_table()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        output_label.config(text="")
        entry_name.focus()
    except ValueError:
        output_label.config(text="أدخل سعرًا صالحًا.")

def update_table():
    for row in tree.get_children():
        tree.delete(row)
    total = 0
    for name, price, time_added in products:
        tree.insert("", tk.END, values=(name, f"{price:.2f}", time_added))
        total += price
    total_label.config(text=f"الإجمالي: {total:.2f} ₺")

def reset_all():
    products.clear()
    update_table()
    output_label.config(text=" تم حذف السلا ")

def on_name_enter(event):
    entry_price.focus()  # الانتقال إلى خانة السعر عند الضغط Enter

def on_price_delete(event):
    reset_all()  # إعادة تعيين عند ضغط Delete

# واجهة المستخدم
window = tk.Tk()
window.title("سوبر ماركت - جمع أسعار المنتجات")
window.geometry("800x600")

tk.Label(window, text="اسم المنتج:", font=("Arial", 12)).pack()
entry_name = tk.Entry(window, font=("Arial", 12))
entry_name.pack(pady=5)
entry_name.bind("<Return>", on_name_enter)  # رابط Enter

tk.Label(window, text="السعر:", font=("Arial", 12)).pack()
entry_price = tk.Entry(window, font=("Arial", 12))
entry_price.pack(pady=5)
entry_price.bind("<Delete>", on_price_delete)  # رابط Delete

tk.Button(window, text="إضافة", command=add_product, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(window, text=" حذف السلا ", command=reset_all, bg="red", fg="white", font=("Arial", 12)).pack(pady=5)

columns = ("المنتج", "السعر", "الوقت")
tree = ttk.Treeview(window, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)

total_label = tk.Label(window, text="الإجمالي: 0.00 ₺", font=("Arial", 14), fg="blue")
total_label.pack(pady=10)

output_label = tk.Label(window, text="", font=("Arial", 12), fg="red")
output_label.pack()

entry_name.focus()  # يبدأ المؤشر في خانة اسم المنتج
window.mainloop()
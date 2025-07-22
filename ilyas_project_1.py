import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import ImageGrab

# -------------------- واجهة التطبيق يجب أن تُنشأ أولاً --------------------
root = tk.Tk()
root.title("مطعم ياس - نظام الطلبات")
root.geometry("1050x620")
root.configure(bg="#ff8800")  # خلفية هادئة

# -------------------- المتغيرات الأساسية --------------------
table_number = tk.IntVar(value=1)     # رقم الطاولة
order_list = []                       # قائمة الطلبات
receipt_number = 1                    # رقم الفاتورة
selected_item = tk.StringVar()        # العنصر المحدد للحذف

# -------------------- قائمة الطعام --------------------
menu = {
    "مأكولات": {
        "🌯 شاورما": 80,
        "🍟 بطاطا": 40,
        "🌮 ماكسيكانو": 80,
        "🍔 برغر": 110,
        "🥙 كباب": 90,
        "🍕 بيتزا": 95,
        "🍘 مقرمشات": 70
    },
    "مشروبات": {
        "🟠🥤 مندرين كولا": 15,
        "🍊 عصير برتقال": 20,
        "💧 مياه معدنية": 10,
        "🍋🌿 ليمون نعنع": 25
    }
}

# -------------------- إضافة صنف إلى الطلب --------------------
def add_to_order(item, price):
    order_list.append((item, price))
    update_receipt()

# -------------------- تحديث الفاتورة --------------------
def update_receipt():
    receipt_text.delete("1.0", tk.END)
    total = 0
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    item_counts = {}

    for item, price in order_list:
        item_counts[item] = item_counts.get(item, 0) + 1

    receipt_text.insert(tk.END, f"{'🍽️ مطـ🌟ـعــم يـــاس 🍽️':^40}\n")
    receipt_text.insert(tk.END, f"{'رقم الطاولة: ' + str(table_number.get()):^40}\n")
    receipt_text.insert(tk.END, f"{'رقم الوصل: ' + str(receipt_number):^40}\n")
    receipt_text.insert(tk.END, f"{'التاريخ: ' + now:^40}\n")
    receipt_text.insert(tk.END, "-"*40 + "\n")

    for item, count in item_counts.items():
        price = menu['مأكولات'].get(item, menu['مشروبات'].get(item, 0))
        line = f"{item} × {count} = {price * count} ل.س"
        receipt_text.insert(tk.END, f"{line:^40}\n")
        total += price * count

    receipt_text.insert(tk.END, "-"*40 + "\n")
    receipt_text.insert(tk.END, f"{'عدد الأصناف: ' + str(len(order_list)) :^40}\n")
    receipt_text.insert(tk.END, f"{'🧾 المجموع النهائي: ' + str(total) + ' ل.س':^40}\n")

    update_delete_menu()

# -------------------- حذف صنف --------------------
def delete_selected_item():
    item_to_remove = selected_item.get()
    if item_to_remove:
        for i in range(len(order_list) - 1, -1, -1):
            if order_list[i][0] == item_to_remove:
                del order_list[i]
                break
        update_receipt()

# -------------------- تحديث قائمة الحذف --------------------
def update_delete_menu():
    delete_menu['menu'].delete(0, 'end')
    added_items = sorted(set([item for item, _ in order_list]))
    for item in added_items:
        delete_menu['menu'].add_command(label=item, command=tk._setit(selected_item, item))

# -------------------- مسح الطلب --------------------
def clear_order():
    global order_list, receipt_number
    order_list = []
    receipt_number += 1
    receipt_text.delete("1.0", tk.END)
    receipt_text.insert(tk.END, "الطلب فارغ حالياً.")
    table_number.set(1)
    delete_menu['menu'].delete(0, 'end')
    selected_item.set("")

# -------------------- حفظ الفاتورة كصورة --------------------
def save_receipt_as_image():
    x = root.winfo_rootx() + receipt_frame.winfo_x()
    y = root.winfo_rooty() + receipt_frame.winfo_y()
    w = x + receipt_frame.winfo_width()
    h = y + receipt_frame.winfo_height()
    img = ImageGrab.grab((x, y, w, h))
    img.save(f"فاتورة_طاولة_{table_number.get()}_{receipt_number}.png")
    messagebox.showinfo("تم الحفظ", "✅ تم حفظ الفاتورة كصورة!")

# -------------------- واجهة المستخدم --------------------

# العنوان / اللوجو
logo_label = tk.Label(root, text="🍽️ مطـ🌟ـعــم يـــاس 🍽️", font=("Tajawal", 26, "bold"), fg="#2e8b57", bg="#fff8f0")
logo_label.pack(pady=10)

# رقم الطاولة
top_frame = tk.Frame(root, bg="#000000")
top_frame.pack(pady=5)
tk.Label(top_frame, text="رقم الطاولة:", font=("Arial", 12, "bold"), bg="#fff8f0").pack(side=tk.LEFT)
tk.Entry(top_frame, textvariable=table_number, width=5, font=("Arial", 12)).pack(side=tk.LEFT)

# قسم الأزرار (يمين)
buttons_frame = tk.Frame(root, bg="#fff8f0")
buttons_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# أزرار الطعام
tk.Label(buttons_frame, text="🍔 المأكولات", font=("Arial", 14, "bold"), bg="#fff8f0", fg="#cc3300").pack(pady=5)
for item, price in menu['مأكولات'].items():
    tk.Button(buttons_frame, text=f"{item} ({price} ل.س)", width=22, bg="#fff2cc", fg="black",
              font=("Arial", 10, "bold"), command=lambda i=item, p=price: add_to_order(i, p)).pack(pady=2)

# أزرار المشروبات
tk.Label(buttons_frame, text="🥤 المشروبات", font=("Arial", 14, "bold"), bg="#fff8f0", fg="#1e90ff").pack(pady=10)
for item, price in menu['مشروبات'].items():
    tk.Button(buttons_frame, text=f"{item} ({price} ل.س)", width=22, bg="#e0f7fa", fg="black",
              font=("Arial", 10, "bold"), command=lambda i=item, p=price: add_to_order(i, p)).pack(pady=2)

# الفاتورة (يسار)
receipt_frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
receipt_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

receipt_text = tk.Text(receipt_frame, font=("Arial", 13), wrap=tk.WORD, bg="white", fg="black")
receipt_text.pack(fill=tk.BOTH, expand=True)
receipt_text.insert(tk.END, "الطلب فارغ حالياً.")

# أدوات التحكم
control_frame = tk.Frame(root, bg="#fff8f0")
control_frame.pack(pady=5)

tk.Button(control_frame, text="🔄 طلب جديد", command=clear_order, bg="#c2f0c2", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="📸 حفظ الفاتورة كصورة", command=save_receipt_as_image, bg="#fff176", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)

# قائمة حذف الأصناف
delete_menu = tk.OptionMenu(control_frame, selected_item, "")
delete_menu.config(font=("Arial", 10), bg="#ffdddd")
delete_menu.pack(side=tk.LEFT, padx=5)

tk.Button(control_frame, text="🗑️ حذف صنف", command=delete_selected_item, bg="#f28b82", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)

# تشغيل البرنامج
root.mainloop()
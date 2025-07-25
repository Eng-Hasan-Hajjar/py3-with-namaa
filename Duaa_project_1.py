import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def حساب_الوزن_المثالي():
    try:
        الطول = float(entry_الطول.get())
        الجنس = gender_var.get()

        if الطول <= 100:
            messagebox.showerror("خطأ", "يجب أن يكون الطول أكبر من 100 سم.")
            return

        if الجنس == "ذكر":
            الوزن_المثالي = (الطول - 100) - ((الطول - 100) * 0.10)
        elif الجنس == "أنثى":
            الوزن_المثالي = (الطول - 100) - ((الطول - 100) * 0.15)
        else:
            messagebox.showerror("خطأ", "الرجاء اختيار الجنس.")
            return

        label_النتيجة.config(text=f"الوزن المثالي هو: {الوزن_المثالي:.2f} كغ")
    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال الطول بشكل صحيح.")

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("حاسبة الوزن المثالي")
window.geometry("350x300")
window.resizable(False, False)

# العنوان
title = tk.Label(window, text="برنامج حساب الوزن المثالي", font=("Arial", 16, "bold"),bg="light blue")
title.pack(pady=10)

# إدخال الطول
frame_الطول = tk.Frame(window)
frame_الطول.pack(pady=5)
label_الطول = tk.Label(frame_الطول, text="الطول (سم):", font=("Arial", 12))
label_الطول.pack(side=tk.LEFT)
entry_الطول = tk.Entry(frame_الطول, font=("Arial", 12))
entry_الطول.pack(side=tk.LEFT, padx=5)

# اختيار الجنس
frame_الجنس = tk.Frame(window)
frame_الجنس.pack(pady=5)
label_الجنس = tk.Label(frame_الجنس, text="الجنس:", font=("Arial", 12))
label_الجنس.pack(side=tk.LEFT)
gender_var = tk.StringVar()
combo_الجنس = ttk.Combobox(frame_الجنس, textvariable=gender_var, state="readonly", font=("Arial", 12))
combo_الجنس['values'] = ("ذكر", "أنثى")
combo_الجنس.pack(side=tk.LEFT, padx=5)

# زر الحساب
btn_حساب = tk.Button(window, text="احسب", command=حساب_الوزن_المثالي, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_حساب.pack(pady=10)

# عرض النتيجة
label_النتيجة = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
label_النتيجة.pack(pady=10)




# تشغيل التطبيق
window.mainloop()
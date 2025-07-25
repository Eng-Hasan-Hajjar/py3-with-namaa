import tkinter as tk
from tkinter import messagebox

def calculate_macros():
    try: 
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        bulk = bulk_var.get()
        if weight <= 0 or height <= 0 or age <= 0:
            messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال قيم موجبة للطول والوزن والعمر.")
            return

        if bulk == "التضخيم":
            amr = (10 * weight) + (6.25 * height) - (5 * age) + 500

        
        else:  
            amr = (10 * weight) + (6.25 * height) - (5 * age) - 400



        
        bul = amr * 1.55

        
        protein_need = weight * 1.8

        
        fat_calories = bul * 0.25
        fat_needed = fat_calories / 9

        
        protein_calories = protein_need * 4
        carbs_calories = bul - protein_calories - fat_calories
        carbs_need = carbs_calories / 4
        result_text = f"السعرات الحرارية: {bul:.2f} \n" \
f"البروتين: {protein_need:.2f} جرام\n" \
f"الكربوهيدرات: {carbs_need:.2f} جرام\n" \
f"الدهون: {fat_needed:.2f} جرام"

        result_label.config(text=result_text,bg="gray")
        result_label.place(x=100,y=450)

    except ValueError:
        messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال أرقام صحيحة للطول والوزن والعمر.")
    

root = tk.Tk()
root.title("حسب السعرات لكمال الأجسام")
root.geometry("400x600")
root.resizable(False, False)

als=tk.Label(root,text="⬇الإحتياجات اليومي المقدرة⬇",bg="gray")
als.place(x=127,y=420)

bg_color = "#4E9EA8"
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
result_font = ("Arial", 14, "bold")

root.configure(bg=bg_color)

# الوزن
weight_label = tk.Label(root, text="الوزن (كجم):", font=label_font, bg=bg_color)
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, font=entry_font, width=30,bg="gray")
weight_entry.pack(pady=5)

# الطول
height_label = tk.Label(root, text="الطول (سم):", font=label_font, bg= bg_color)
height_label.pack(pady=5)
height_entry = tk.Entry(root, font=entry_font, width=30,bg="gray")
height_entry.pack(pady=5)

# العمر
age_label = tk.Label(root, text="العمر (سنة):", font=label_font, bg=bg_color)
age_label.pack(pady=5)
age_entry = tk.Entry(root, font=entry_font, width=30,bg="gray")
age_entry.pack(pady=5)

gender_label = tk.Label(root, text="الجنس:", font=label_font, bg=bg_color)
gender_label.pack(pady=5)
gender_var = tk.StringVar(root)
gender_var.set("ذكر") 
gender_menu = tk.OptionMenu(root, gender_var, "ذكر", "أنثى")
gender_menu.config(font=entry_font, bg="gray")
gender_menu.pack(pady=5)

# التضخيم
bulk_label = tk.Label(root, text="هدفك", font=label_font, bg=bg_color)
bulk_label.pack(pady=5)
bulk_var = tk.StringVar(root)
bulk_var.set("التنشيف") 
bulk_menu = tk.OptionMenu(root,bulk_var, "التضخيم","التنشيف")
bulk_menu.config(font=entry_font, bg="gray")
bulk_menu.pack(pady=5)

# زر الحساب
calculate_button = tk.Button(root, text="احسب السعرات", command=calculate_macros,
font=button_font, bg="#707070", fg="black",
bd=0, padx=10, pady=5)
calculate_button.pack(pady=20)


result_label = tk.Label(root, text="", font=result_font, bg=bg_color, justify="left")
result_label.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
food = {
    "تفاح": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
    "صدر دجاج": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "رز": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
    "خبز )": {"calories": 265, "protein": 9, "fat": 3.2, "carbs": 49},
    "حليب": {"calories": 61, "protein": 3.2, "fat": 3.3, "carbs": 4.8},
    "موز": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23},
    "بيض": {"calories": 155, "protein": 13, "fat": 11, "carbs": 1.1},
    "بطاطا": {"calories": 77, "protein": 2, "fat": 0.1, "carbs": 17},
    "بروكلي": {"calories": 34, "protein": 2.8, "fat": 0.4, "carbs": 7},
    "زيت زيتون": {"calories": 884, "protein": 0, "fat": 100, "carbs": 0},
    "عدس": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20}, 
    "فول سوداني": {"calories": 567, "protein": 26, "fat": 49, "carbs": 16},
    "شوفان": {"calories": 389, "protein": 17, "fat": 7, "carbs": 66}, 
    "فاصوليا": {"calories": 116, "protein": 6.7, "fat": 0.5, "carbs": 20},
    "ذرة": {"calories": 86, "protein": 3.2, "fat": 1.2, "carbs": 19},
    "طماطم": {"calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 3.9},
    "خيار": {"calories": 15, "protein": 0.7, "fat": 0.1, "carbs": 3.6},
    "جزر": {"calories": 41, "protein": 0.9, "fat": 0.2, "carbs": 9.6},
    "سلمون": {"calories": 208, "protein": 20, "fat": 13, "carbs": 0},
    "بطاطا حلوة": {"calories": 86, "protein": 1.6, "fat": 0.1, "carbs": 20},
    "سبانخ": {"calories": 23, "protein": 2.9, "fat": 0.4, "carbs": 3.6},
    "زبادي": {"calories": 59, "protein": 10, "fat": 0.4, "carbs": 3.6}, 
    "شوفان مطبوخ": {"calories": 68, "protein": 2.4, "fat": 1.4, "carbs": 12},
    "عدس مطبوخ": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20}, 
    "خس": {"calories": 15, "protein": 1.4, "fat": 0.2, "carbs": 2.9},
    "فلفل ": {"calories": 20, "protein": 0.9, "fat": 0.2, "carbs": 4.6},
    "بصل": {"calories": 40, "protein": 1.1, "fat": 0.1, "carbs": 9.3},
    "ثوم": {"calories": 149, "protein": 6.4, "fat": 0.5, "carbs": 33},
    "زيتون اسود": {"calories": 115, "protein": 0.8, "fat": 10.7, "carbs": 6.3},
    "حمص مطبوخ": {"calories": 164, "protein": 8.9, "fat": 2.6, "carbs": 27.4},
    "فاصوليا سوداء": {"calories": 132, "protein": 8.9, "fat": 0.5, "carbs": 23.7}, 
    "فاصوليا بيضاء": {"calories": 134, "protein": 9.1, "fat": 0.3, "carbs": 24.3}, 
    "بازلاء خضراء": {"calories": 81, "protein": 5.4, "fat": 0.4, "carbs": 14.4}, 
    "عدس احمر": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20}, 
    "تونا": {"calories": 116, "protein": 25.5, "fat": 1.1, "carbs": 0},
    "لوز": {"calories": 579, "protein": 21, "fat": 49.9, "carbs": 21.6},
    "بذور الشيا": {"calories": 486, "protein": 16.5, "fat": 30.7, "carbs": 42.1},
    "أفوكادو": {"calories": 160, "protein": 2, "fat": 14.7, "carbs": 8.5},
    "برتقال": {"calories": 47, "protein": 0.9, "fat": 0.1, "carbs": 11.8},
    "فراولة": {"calories": 32, "protein": 0.7, "fat": 0.3, "carbs": 7.7},
    "جبنة قريش": {"calories": 72, "protein": 12.4, "fat": 1.5, "carbs": 3.4}, 
    "لحم بقري": {"calories": 250, "protein": 26, "fat": 15, "carbs": 0}, 
    "بط": {"calories": 130, "protein": 23, "fat": 4, "carbs": 0}, 
    "قرنبيط": {"calories": 25, "protein": 1.9, "fat": 0.3, "carbs": 5},
    "فطر": {"calories": 22, "protein": 3.1, "fat": 0.3, "carbs": 3.3},
    "فاصوليا خضراء": {"calories": 31, "protein": 1.8, "fat": 0.2, "carbs": 7},
    "كاجو": {"calories": 553, "protein": 18, "fat": 44, "carbs": 30},
    "بذور اليقطين": {"calories": 574, "protein": 24.5, "fat": 49, "carbs": 10.7},
    "بذور دوار الشمس": {"calories": 584, "protein": 20.7, "fat": 51.5, "carbs": 20},
    "عنب": {"calories": 69, "protein": 0.6, "fat": 0.2, "carbs": 18},
    "كرز": {"calories": 50, "protein": 1, "fat": 0.3, "carbs": 12},
    "أناناس": {"calories": 50, "protein": 0.5, "fat": 0.1, "carbs": 13},
    "شمام": {"calories": 34, "protein": 0.8, "fat": 0.2, "carbs": 8},
    "بامية": {"calories": 33, "protein": 1.9, "fat": 0.2, "carbs": 7.5},
    "كوسة": {"calories": 17, "protein": 1.2, "fat": 0.3, "carbs": 3.1},
    "سمك ": {"calories": 82, "protein": 17.8, "fat": 0.7, "carbs": 0},
    "جمبري": {"calories": 85, "protein": 20, "fat": 0.3, "carbs": 0.2},
    "لحم بقر مفروم": {"calories": 250, "protein": 26, "fat": 15, "carbs": 0},
    "صدر دجاج ": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
    "فخذ دجاج ": {"calories": 180, "protein": 25, "fat": 8, "carbs": 0},
    "لحم خروف ": {"calories": 290, "protein": 25, "fat": 20, "carbs": 0},
    "سمك سلمون": {"calories": 208, "protein": 20, "fat": 13, "carbs": 0},
    "جمبري": {"calories": 85, "protein": 18, "fat": 1, "carbs": 1},
    "ديك رومي ": {"calories": 135, "protein": 29, "fat": 2, "carbs": 0},
    

    
}
def open_food_calculator(root_window):
    root_window.withdraw() 
    app = tk.Toplevel()
    app.title("حاسبة السعرات الحرارية والمغذيات")
    app.geometry("400x600")
    app.resizable(False, False)
    bg_color1 = "#4E9EA8"
    app.configure(bg=bg_color1)

    label_font_style = ("Arial", 13)

    food_label = tk.Label(app, text="اسم الطعام (بالعربية):", font=label_font_style, fg="black", bg=bg_color1)
    food_label.pack(pady=10)
    food_entry = tk.Entry(app, width=30, font=label_font_style, justify='center', bg="#707070")
    food_entry.pack(pady=10)

    quantity_label = tk.Label(app, text="الكمية (جرام):", font=label_font_style, fg="black", bg=bg_color1)
    quantity_label.pack(pady=10)
    quantity_entry = tk.Entry(app, width=30, font=label_font_style, justify='center', bg="#707070")
    quantity_entry.pack(pady=10)

    result_label = tk.Label(app, text="⬇النتائج⬇", font=("Arial", 16), justify="left", bg="#707070")
    result_label.pack(pady=10)

    def calculate_macros_food():
        food_name = food_entry.get()
        try:
            quantity = float(quantity_entry.get())
            if quantity <= 0:
                messagebox.showerror("خطأ في الإدخال", "الكمية يجب أن تكون رقمًا موجبًا.")
                return
        except ValueError:
            messagebox.showerror("خطأ في الإدخال", "الكمية يجب أن تكون رقمًا صحيحًا.")
            return

        if food_name in food:
            food_info = food[food_name]
            calories = (food_info["calories"] / 100) * quantity
            protein = (food_info["protein"] / 100) * quantity
            fat = (food_info["fat"] / 100) * quantity
            carbs = (food_info["carbs"] / 100) * quantity

            result_label.config(
                text=f"النتائج لـ {quantity} جرام من {food_name}:\n"
                     f"السعرات الحرارية: {calories:.2f} سعرة\n"
                     f"البروتين: {protein:.2f} جم\n"
                     f"الدهون: {fat:.2f} جم\n"
                     f"الكربوهيدرات: {carbs:.2f} جم"
            )
        else:
            messagebox.showwarning( "هذا الطعام غير موجود في قاعدة البيانات لدينا.")

    calculate_button = tk.Button(app, text="احسب القيم الغذائية", command=calculate_macros_food,
    font=label_font_style, bg="#707070", fg="black", relief="raised", bd=3)
    calculate_button.pack(pady=30)

    back_button = tk.Button(app, text="🔙 رجوع", command=lambda: [app.destroy(), root_window.deiconify()],
    font=label_font_style, bg="#707070", fg="black", relief="raised", bd=3)
    back_button.pack(pady=5)

    
    exit_button = tk.Button(app, text="❌ خروج", command=app.quit,
    font=label_font_style, bg="#707070", fg="black", relief="raised", bd=3)
    exit_button.pack(pady=5)


root = tk.Tk()
root.title("حسب السعرات لكمال الأجسام")
root.geometry("400x650")
root.configure(bg="#4E9EA8")

bg_color = "#4E9EA8"
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
result_font = ("Arial", 14, "bold")


weight_label = tk.Label(root, text="الوزن (كجم):", font=label_font, bg=bg_color)
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, font=entry_font, width=30, bg="gray")
weight_entry.pack(pady=5)


height_label = tk.Label(root, text="الطول (سم):", font=label_font, bg=bg_color)
height_label.pack(pady=5)
height_entry = tk.Entry(root, font=entry_font, width=30, bg="gray")
height_entry.pack(pady=5)


age_label = tk.Label(root, text="العمر (سنة):", font=label_font, bg=bg_color)
age_label.pack(pady=5)
age_entry = tk.Entry(root, font=entry_font, width=30, bg="gray")
age_entry.pack(pady=5)


gender_label = tk.Label(root, text="الجنس:", font=label_font, bg=bg_color)
gender_label.pack(pady=5)
gender_var = tk.StringVar(root)
gender_var.set("ذكر")
gender_menu = tk.OptionMenu(root, gender_var, "ذكر", "أنثى")
gender_menu.config(font=entry_font, bg="gray")
gender_menu.pack(pady=5)

bulk_label = tk.Label(root, text="هدفك", font=label_font, bg=bg_color)
bulk_label.pack(pady=5)
bulk_var = tk.StringVar(root)
bulk_var.set("التنشيف")
bulk_menu = tk.OptionMenu(root, bulk_var, "التضخيم", "التنشيف")
bulk_menu.config(font=entry_font, bg="gray")
bulk_menu.pack(pady=5)

def calculate_macros():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        bulk = bulk_var.get()
        if weight <= 0 or height <= 0 or age <= 0:
            messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال قيم موجبة.")
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

        result_label.config(text=result_text, bg="gray")
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة.")

calculate_button = tk.Button(root, text="احسب السعرات", command=calculate_macros,
                             font=button_font, bg="#707070", fg="black", bd=0, padx=10, pady=5)
calculate_button.pack(pady=20)


als = tk.Label(root, text="⬇الإحتياجات اليومي المقدرة⬇", bg="gray")
als.pack()
result_label = tk.Label(root, text="", font=result_font, bg=bg_color, justify="left")
result_label.pack(pady=10)


food_button = tk.Button(root, text="➤ ادخل لحاسبة الطعام", command=lambda: open_food_calculator(root),
                        font=button_font, bg="#707070", fg="black")
food_button.pack(pady=20)

root.mainloop()
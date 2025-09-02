import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import os


class ImageGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("معرض الصور المتقدم")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')

        # قائمة الصور ومؤشر الصورة الحالية
        self.images = []
        self.current_index = 0
        self.current_image = None
        self.original_image = None

        # إنشاء الواجهة
        self.create_widgets()

    def create_widgets(self):
        """إنشاء عناصر واجهة المستخدم"""
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat",
                        background="#3498db", 
                        font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#2980b9")])

        # إطار العنوان
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill=tk.X, pady=10)

        title_label = tk.Label(title_frame, text="معرض الصور المتقدم",
                               font=("Arial", 18, "bold"), fg="white", bg='#2c3e50')
        title_label.pack(pady=5)

        # إطار مركزي للصورة + أدوات التحرير
        center_frame = tk.Frame(self.root, bg="#2c3e50")
        center_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # إطار أدوات التحرير على اليسار
        self.tool_frame = tk.Frame(center_frame, bg='#2c3e50', width=250)
        self.tool_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # إطار الصورة الرئيسية على اليمين
        self.image_frame = tk.Frame(center_frame, bg="#34495e", relief=tk.RAISED, bd=3)
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # تسمية لعرض الصورة
        self.image_label = tk.Label(self.image_frame, bg="#34495e")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # إطار التنقل أسفل الشاشة
        nav_frame = tk.Frame(self.root, bg='#2c3e50')
        nav_frame.pack(pady=15)

        ttk.Button(nav_frame, text="⏮ السابق", command=self.prev_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="التالي ⏭", command=self.next_image).pack(side=tk.LEFT, padx=5)

        # أزرار التحميل والحفظ
        control_frame = tk.Frame(self.root, bg='#2c3e50')
        control_frame.pack(pady=10)

        ttk.Button(control_frame, text="📂 تحميل صورة", command=self.load_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="💾 حفظ التعديلات", command=self.save_image).pack(side=tk.LEFT, padx=5)

        # إعداد أدوات التحرير
        self.setup_edit_tools()

        # تحديث حالة الأزرار
        self.update_buttons_state()

    def setup_edit_tools(self):
        """إعداد أدوات تحرير الصورة"""
        self.edit_tools_frame = tk.Frame(self.tool_frame, bg='#2c3e50')
        self.edit_tools_frame.pack(fill=tk.Y, pady=5)

        # السطوع
        tk.Label(self.edit_tools_frame, text="السطوع:", font=("Arial", 10),
                 fg="white", bg='#2c3e50').pack(anchor="w", padx=5, pady=2)
        self.brightness_var = tk.DoubleVar(value=1.0)
        brightness_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=1.5,
                                    resolution=0.1, orient=tk.HORIZONTAL,
                                    variable=self.brightness_var,
                                    command=self.adjust_brightness,
                                    length=150, bg='#2c3e50', fg='white',
                                    troughcolor='#34495e',
                                    highlightbackground='#2c3e50')
        brightness_scale.pack(anchor="w", padx=5, pady=2)

        # التباين
        tk.Label(self.edit_tools_frame, text="التباين:", font=("Arial", 10),
                 fg="white", bg='#2c3e50').pack(anchor="w", padx=5, pady=2)
        self.contrast_var = tk.DoubleVar(value=1.0)
        contrast_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=1.5,
                                  resolution=0.1, orient=tk.HORIZONTAL,
                                  variable=self.contrast_var,
                                  command=self.adjust_contrast,
                                  length=150, bg='#2c3e50', fg='white',
                                  troughcolor='#34495e',
                                  highlightbackground='#2c3e50')
        contrast_scale.pack(anchor="w", padx=5, pady=2)

        # الحدة
        tk.Label(self.edit_tools_frame, text="الحدة:", font=("Arial", 10),
                 fg="white", bg='#2c3e50').pack(anchor="w", padx=5, pady=2)
        self.sharpness_var = tk.DoubleVar(value=1.0)
        sharpness_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=2.0,
                                   resolution=0.1, orient=tk.HORIZONTAL,
                                   variable=self.sharpness_var,
                                   command=self.adjust_sharpness,
                                   length=150, bg='#2c3e50', fg='white',
                                   troughcolor='#34495e',
                                   highlightbackground='#2c3e50')
        sharpness_scale.pack(anchor="w", padx=5, pady=2)

        # زر تحويل للصورة أبيض وأسود
        ttk.Button(self.edit_tools_frame, text="⚫ أبيض وأسود",
                   command=self.apply_grayscale).pack(pady=5)

        # أزرار الدوران
        rotate_frame = tk.Frame(self.edit_tools_frame, bg='#2c3e50')
        rotate_frame.pack(pady=5)
        ttk.Button(rotate_frame, text="↺ تدوير يسار",
                   command=lambda: self.rotate_image(-90)).pack(side=tk.LEFT, padx=2)
        ttk.Button(rotate_frame, text="↻ تدوير يمين",
                   command=lambda: self.rotate_image(90)).pack(side=tk.LEFT, padx=2)

        # تغيير الحجم
        tk.Label(self.edit_tools_frame, text="تغيير الحجم:", font=("Arial", 10),
                 fg="white", bg='#2c3e50').pack(anchor="w", padx=5, pady=2)
        resize_frame = tk.Frame(self.edit_tools_frame, bg='#2c3e50')
        resize_frame.pack(pady=5)

        tk.Label(resize_frame, text="العرض:", fg="white", bg='#2c3e50').pack(side=tk.LEFT)
        self.width_entry = tk.Entry(resize_frame, width=5)
        self.width_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(resize_frame, text="الارتفاع:", fg="white", bg='#2c3e50').pack(side=tk.LEFT)
        self.height_entry = tk.Entry(resize_frame, width=5)
        self.height_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(self.edit_tools_frame, text="📏 تطبيق الحجم",
                   command=self.resize_image).pack(pady=5)

    # تحميل الصور
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("ملفات الصور", ".png;.jpg;.jpeg;.bmp;*.gif")])
        if file_path:
            self.images.append(file_path)
            self.current_index = len(self.images) - 1
            self.show_image()

    # عرض الصورة
    def show_image(self):
        if not self.images:
            return

        file_path = self.images[self.current_index]
        self.original_image = Image.open(file_path)
        self.current_image = self.original_image.copy()
        self.display_image(self.current_image)

    # تحديث عرض الصورة
    def display_image(self, img):
        if img is None:
            return
        img.thumbnail((800, 600))
        self.tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_image)

    # تعديل السطوع
    def adjust_brightness(self, val):
        if self.original_image:
            enhancer = ImageEnhance.Brightness(self.original_image)
            self.current_image = enhancer.enhance(float(val))
            self.display_image(self.current_image)

    # تعديل التباين
    def adjust_contrast(self, val):
        if self.original_image:
            enhancer = ImageEnhance.Contrast(self.original_image)
            self.current_image = enhancer.enhance(float(val))
            self.display_image(self.current_image)

    # تعديل الحدة
    def adjust_sharpness(self, val):
        if self.original_image:
            enhancer = ImageEnhance.Sharpness(self.original_image)
            self.current_image = enhancer.enhance(float(val))
            self.display_image(self.current_image)

    # أبيض وأسود
    def apply_grayscale(self):
        if self.original_image:
            self.current_image = ImageOps.grayscale(self.original_image)
            self.display_image(self.current_image)

    # تدوير
    def rotate_image(self, angle):
        if self.original_image:
            self.current_image = self.original_image.rotate(angle, expand=True)
            self.display_image(self.current_image)

    # تغيير الحجم
    def resize_image(self):
        if self.original_image:
            try:
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                self.current_image = self.original_image.resize((width, height))
                self.display_image(self.current_image)
            except ValueError:
                messagebox.showerror("خطأ", "الرجاء إدخال قيم صحيحة للأبعاد.")

    # حفظ التعديلات
    def save_image(self):
        if self.current_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg"),
                                                                ("All files", ".")])
            if file_path:
                self.current_image.save(file_path)
                messagebox.showinfo("نجاح", "تم حفظ الصورة بنجاح!")

    # الصورة التالية
    def next_image(self):
        if self.images and self.current_index < len(self.images) - 1:
            self.current_index += 1
            self.show_image()

    # الصورة السابقة
    def prev_image(self):
        if self.images and self.current_index > 0:
            self.current_index -= 1
            self.show_image()

    def update_buttons_state(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
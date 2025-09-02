import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps
import os
import shutil
from datetime import datetime

class ImageGalleryApp:
    def __init__(self, root):
        # تهيئة النافذة الرئيسية
        self.root = root
        self.root.title("معرض الصور المتقدم")
        self.root.state('zoomed')  # جعل النافذة تظهر بملء الشاشة عند التشغيل
        self.root.configure(bg='#2c3e50')
        
        # قائمة للصور
        self.images = []
        self.current_image_index = 0
        self.original_image = None
        self.edited_image = None
        self.zoom_level = 1.0
        
        # إنشاء مجلد للصور إذا لم يكن موجوداً
        self.image_folder = "gallery_images"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        
        # تحميل أي صور موجودة مسبقاً في المجلد
        self.load_existing_images()
        
        # إنشاء واجهة المستخدم
        self.create_widgets()
        
        # عرض الصورة الأولى إذا كانت هناك صور
        if self.images:
            self.show_image(0)
    
    def load_existing_images(self):
        """تحميل الصور الموجودة في مجلد المعرض"""
        for file in os.listdir(self.image_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(os.path.join(self.image_folder, file))
    
    def create_widgets(self):
        """إنشاء عناصر واجهة المستخدم"""
        # إنشاء أنماط مختلفة للأزرار بألوان متنوعة
        style = ttk.Style()
        
        style.configure('Blue.TButton', 
                        font=('Arial', 10), 
                        background='#3498db', 
                        borderwidth=1,
                        focusthickness=3,
                        focuscolor='#3498db')
        style.map('Blue.TButton', 
                  background=[('active', '#2980b9')])
        
        style.configure('Green.TButton', 
                        font=('Arial', 9), 
                        padding=(5, 2),
                        background='#27ae60')
        style.map('Green.TButton', 
                  background=[('active', '#219653')])
        
        style.configure('Purple.TButton', 
                        font=('Arial', 10),
                        background='#9b59b6')
        style.map('Purple.TButton', 
                  background=[('active', '#8e44ad')])
        
        style.configure('Orange.TButton', 
                        font=('Arial', 9),
                        background='#e67e22')
        style.map('Orange.TButton', 
                  background=[('active', '#d35400')])
        
        style.configure('Red.TButton', 
                        font=('Arial', 9),
                        background='#e74c3c')
        style.map('Red.TButton', 
                  background=[('active', '#c0392b')])
        
        # إطار العنوان
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill=tk.X, pady=10)
        
        title_label = tk.Label(title_frame, text="معرض الصور المتقدم", 
                              font=("Arial", 18, "bold"), fg="white", bg='#2c3e50')
        title_label.pack(pady=5)
        
        # إطار الصورة الرئيسية
        self.image_frame = tk.Frame(self.root, bg="#34495e", relief=tk.RAISED, bd=3)
        self.image_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # تسمية لعرض الصورة
        self.image_label = tk.Label(self.image_frame, bg="#34495e")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # إطار التحكم بالأعلى (التنقل والأدوات الأساسية)
        top_control_frame = tk.Frame(self.root, bg='#2c3e50')
        top_control_frame.pack(pady=5, fill=tk.X)
        
        # أزرار التنقل
        nav_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        nav_frame.pack(side=tk.LEFT, padx=10)
        
        self.prev_btn = ttk.Button(nav_frame, text="◀ السابق", command=self.prev_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(nav_frame, text="التالي ▶", command=self.next_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # أزرار الأدوات
        tool_btn_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        tool_btn_frame.pack(side=tk.RIGHT, padx=10)
        
        self.load_btn = ttk.Button(tool_btn_frame, text="📁 تحميل صورة", command=self.load_image, style='Green.TButton')
        self.load_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = ttk.Button(tool_btn_frame, text="🗑️ حذف", command=self.delete_image, 
                                    state=tk.DISABLED, style='Red.TButton')
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        self.fullscreen_btn = ttk.Button(tool_btn_frame, text="🔍 عرض كامل", command=self.view_fullscreen, 
                                        state=tk.DISABLED, style='Blue.TButton')
        self.fullscreen_btn.pack(side=tk.LEFT, padx=5)
        
        self.edit_btn = ttk.Button(tool_btn_frame, text="✏️ تحرير", command=self.toggle_edit_tools, 
                                  state=tk.DISABLED, style='Orange.TButton')
        self.edit_btn.pack(side=tk.LEFT, padx=5)
        
        # إطار معلومات الصورة
        info_frame = tk.Frame(self.root, bg="#34495e")
        info_frame.pack(pady=5, fill=tk.X)
        
        self.image_name_label = tk.Label(info_frame, text="لا توجد صور", font=("Arial", 12), 
                                        fg="white", bg="#34495e")
        self.image_name_label.pack(side=tk.LEFT, padx=10)
        
        self.image_count_label = tk.Label(info_frame, text="0 / 0", font=("Arial", 10), 
                                         fg="white", bg="#34495e")
        self.image_count_label.pack(side=tk.RIGHT, padx=10)
        
        # تحديث حالة الأزرار
        self.update_buttons_state()
    
    def setup_edit_tools(self):
        """إعداد أدوات تحرير الصورة في نافذة منفصلة"""
        self.edit_window = None  # سيتم إنشاء النافذة عند الحاجة
        
    def create_edit_window(self):
        """إنشاء نافذة تحرير الصورة"""
        if self.edit_window is not None and self.edit_window.winfo_exists():
            self.edit_window.lift()
            return
        
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("أدوات تحرير الصورة")
        self.edit_window.geometry('400x500')
        self.edit_window.configure(bg='#2c3e50')
        self.edit_window.transient(self.root)
        self.edit_window.grab_set()
        
        # إطار أدوات التحرير
        edit_tools_frame = tk.Frame(self.edit_window, bg='#2c3e50')
        edit_tools_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # شريط التمرير لتعديل السطوع
        tk.Label(edit_tools_frame, text="السطوع:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(anchor='w', padx=5, pady=2)
        self.brightness_var = tk.DoubleVar(value=1.0)
        brightness_scale = tk.Scale(edit_tools_frame, from_=0.5, to=1.5, 
                                   resolution=0.1, orient=tk.HORIZONTAL,
                                   variable=self.brightness_var, 
                                   command=self.adjust_brightness,
                                   length=300, bg='#2c3e50', fg='white',
                                   troughcolor='#34495e', highlightbackground='#2c3e50')
        brightness_scale.pack(anchor='w', padx=5, pady=2)
        
        # شريط التمرير لتعديل التباين
        tk.Label(edit_tools_frame, text="التباين:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(anchor='w', padx=5, pady=2)
        self.contrast_var = tk.DoubleVar(value=1.0)
        contrast_scale = tk.Scale(edit_tools_frame, from_=0.5, to=1.5, 
                                 resolution=0.1, orient=tk.HORIZONTAL,
                                 variable=self.contrast_var, 
                                 command=self.adjust_contrast,
                                 length=300, bg='#2c3e50', fg='white',
                                 troughcolor='#34495e', highlightbackground='#2c3e50')
        contrast_scale.pack(anchor='w', padx=5, pady=2)
        
        # شريط التمرير لتعديل الحدة
        tk.Label(edit_tools_frame, text="الحدة:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(anchor='w', padx=5, pady=2)
        self.sharpness_var = tk.DoubleVar(value=1.0)
        sharpness_scale = tk.Scale(edit_tools_frame, from_=0.5, to=2.0, 
                                  resolution=0.1, orient=tk.HORIZONTAL,
                                  variable=self.sharpness_var, 
                                  command=self.adjust_sharpness,
                                  length=300, bg='#2c3e50', fg='white',
                                  troughcolor='#34495e', highlightbackground='#2c3e50')
        sharpness_scale.pack(anchor='w', padx=5, pady=2)
        
        # إضافة أدوات لتغيير حجم الصورة
        resize_frame = tk.Frame(edit_tools_frame, bg='#2c3e50')
        resize_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(resize_frame, text="العرض الجديد:", font=("Arial", 10), fg="white", bg='#2c3e50').pack(side=tk.LEFT, padx=5)
        self.new_width_entry = tk.Entry(resize_frame, width=10)
        self.new_width_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(resize_frame, text="الطول الجديد:", font=("Arial", 10), fg="white", bg='#2c3e50').pack(side=tk.LEFT, padx=5)
        self.new_height_entry = tk.Entry(resize_frame, width=10)
        self.new_height_entry.pack(side=tk.LEFT, padx=5)
        
        self.keep_aspect_var = tk.BooleanVar(value=True)
        tk.Checkbutton(resize_frame, text="الحفاظ على النسبة", variable=self.keep_aspect_var, 
                      fg="white", bg='#2c3e50', selectcolor='#34495e').pack(side=tk.LEFT, padx=5)
        
        ttk.Button(resize_frame, text="تطبيق الحجم", command=self.apply_resize, style='Green.TButton').pack(side=tk.LEFT, padx=5)
        
        # أزرار تأثيرات خاصة
        effects_frame = tk.Frame(edit_tools_frame, bg='#2c3e50')
        effects_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(effects_frame, text="تأثير أبيض وأسود", 
                  command=self.apply_grayscale, style='Green.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="تدوير 90°", 
                  command=self.rotate_image, style='Blue.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="عكس الصورة", 
                  command=self.flip_image, style='Purple.TButton').pack(side=tk.LEFT, padx=5)
        
        # أزرار التحكم
        control_frame = tk.Frame(edit_tools_frame, bg='#2c3e50')
        control_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(control_frame, text="استعادة الأصل", 
                  command=self.reset_edits, style='Orange.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="حفظ التعديلات", 
                  command=self.save_edits, style='Red.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="إغلاق", 
                  command=self.close_edit_window, style='Blue.TButton').pack(side=tk.LEFT, padx=5)
    
    def close_edit_window(self):
        """إغلاق نافذة التحرير"""
        if self.edit_window and self.edit_window.winfo_exists():
            self.edit_window.destroy()
            self.edit_window = None
            self.edit_btn.config(text="✏️ تحرير")
    
    def toggle_edit_tools(self):
        """تبديل إظهار/إخفاء نافذة أدوات التحرير"""
        if self.edit_window and self.edit_window.winfo_exists():
            self.close_edit_window()
        else:
            self.create_edit_window()
            self.edit_btn.config(text="إخفاء الأدوات")
    
    def load_image(self):
        """تحميل صورة جديدة من خلال نافذة اختيار الملف"""
        file_path = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=[("ملفات الصور", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        
        if file_path:
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_extension = os.path.splitext(file_path)[1]
                new_filename = f"image_{timestamp}{file_extension}"
                new_filepath = os.path.join(self.image_folder, new_filename)
                
                shutil.copy2(file_path, new_filepath)
                
                self.images.append(new_filepath)
                self.current_image_index = len(self.images) - 1
                
                self.show_image(self.current_image_index)
                self.update_buttons_state()
                
                messagebox.showinfo("تم", "تم تحميل الصورة بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن تحميل الصورة: {str(e)}")
    
    def show_image(self, index):
        """عرض الصورة في الواجهة"""
        if 0 <= index < len(self.images):
            try:
                self.original_image = Image.open(self.images[index])
                self.edited_image = self.original_image.copy()
                
                self.brightness_var.set(1.0)
                self.contrast_var.set(1.0)
                self.sharpness_var.set(1.0)
                self.zoom_level = 1.0
                
                self.display_image()
                
                image_name = os.path.basename(self.images[index])
                self.image_name_label.config(text=image_name)
                self.image_count_label.config(text=f"{index + 1} / {len(self.images)}")
                
                self.current_image_index = index
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن عرض الصورة: {str(e)}")
    
    def display_image(self):
        """عرض الصورة الحالية مع التعديلات والتكبير/التصغير مع تحديد الحجم الأقصى"""
        if self.edited_image:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            max_width = int(screen_width * 0.75)
            max_height = int(screen_height * 0.75)
            
            width, height = self.edited_image.size
            ratio = min(max_width / width, max_height / height, 1.0)
            
            adjusted_width = int(width * ratio * self.zoom_level)
            adjusted_height = int(height * ratio * self.zoom_level)
            
            if adjusted_width > max_width or adjusted_height > max_height:
                zoom_ratio = min(max_width / adjusted_width, max_height / adjusted_height)
                adjusted_width = int(adjusted_width * zoom_ratio)
                adjusted_height = int(adjusted_height * zoom_ratio)
            
            display_image = self.edited_image.resize((adjusted_width, adjusted_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(display_image)
            
            self.image_label.configure(image=photo)
            self.image_label.image = photo
    
    def next_image(self):
        """الانتقال إلى الصورة التالية"""
        if self.current_image_index < len(self.images) - 1:
            self.show_image(self.current_image_index + 1)
            self.update_buttons_state()
    
    def prev_image(self):
        """الانتقال إلى الصورة السابقة"""
        if self.current_image_index > 0:
            self.show_image(self.current_image_index - 1)
            self.update_buttons_state()
    
    def delete_image(self):
        """حذف الصورة الحالية"""
        if not self.images:
            return
        
        result = messagebox.askyesno("تأكيد الحذف", "هل أنت متأكد من أنك تريد حذف هذه الصورة؟")
        if not result:
            return
        
        try:
            os.remove(self.images[self.current_image_index])
            self.images.pop(self.current_image_index)
            
            if len(self.images) == 0:
                self.current_image_index = 0
                self.original_image = None
                self.edited_image = None
                self.image_label.configure(image='')
                self.image_name_label.config(text="لا توجد صور")
                self.image_count_label.config(text="0 / 0")
            elif self.current_image_index >= len(self.images):
                self.current_image_index = len(self.images) - 1
                self.show_image(self.current_image_index)
            else:
                self.show_image(self.current_image_index)
            
            self.update_buttons_state()
            messagebox.showinfo("تم", "تم حذف الصورة بنجاح")
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن حذف الصورة: {str(e)}")
    
    def view_fullscreen(self):
        """عرض الصورة في نافذة منفصلة بحجم كامل"""
        if not self.images:
            return
        
        fullscreen_window = tk.Toplevel(self.root)
        fullscreen_window.title("عرض الصورة بكامل الحجم")
        fullscreen_window.attributes('-fullscreen', True)
        fullscreen_window.configure(bg='#2c3e50')
        
        fullscreen_window.transient(self.root)
        fullscreen_window.grab_set()
        
        screen_width = fullscreen_window.winfo_screenwidth()
        screen_height = fullscreen_window.winfo_screenheight()
        
        image = Image.open(self.images[self.current_image_index])
        width, height = image.size
        
        max_width = int(screen_width * 0.75)
        max_height = int(screen_height * 0.75)
        ratio = min(max_width / width, max_height / height, 1.0)
        new_size = (int(width * ratio), int(height * ratio))
        display_image = image.resize(new_size, Image.LANCZOS)
        
        photo = ImageTk.PhotoImage(display_image)
        image_label = tk.Label(fullscreen_window, image=photo, bg='#2c3e50')
        image_label.image = photo
        image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        button_frame = tk.Frame(fullscreen_window, bg='#2c3e50')
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="إغلاق", 
                  command=fullscreen_window.destroy, style='Blue.TButton').pack()
    
    def adjust_brightness(self, value):
        """تعديل سطوع الصورة"""
        if self.edited_image:
            enhancer = ImageEnhance.Brightness(self.original_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()
    
    def adjust_contrast(self, value):
        """تعديل تباين الصورة"""
        if self.edited_image:
            enhancer = ImageEnhance.Contrast(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()
    
    def adjust_sharpness(self, value):
        """تعديل حدة الصورة"""
        if self.edited_image:
            enhancer = ImageEnhance.Sharpness(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()
    
    def apply_grayscale(self):
        """تطبيق تأثير الأبيض والأسود على الصورة"""
        if self.ed_image:
            self.edited_image = ImageOps.grayscale(self.edited_image)
            self.display_image()
    
    def rotate_image(self):
        """تدوير الصورة 90 درجة"""
        if self.edited_image:
            self.edited_image = self.edited_image.rotate(90, expand=True)
            self.display_image()
    
    def flip_image(self):
        """عكس الصورة أفقياً"""
        if self.edited_image:
            self.edited_image = ImageOps.mirror(self.edited_image)
            self.display_image()
    
    def apply_resize(self):
        """تطبيق تغيير حجم الصورة بناءً على الإدخالات"""
        if not self.edited_image:
            return
        
        try:
            new_width = int(self.new_width_entry.get())
            new_height = int(self.new_height_entry.get())
            
            if new_width <= 0 or new_height <= 0:
                raise ValueError("يجب أن تكون الأبعاد إيجابية")
            
            if self.keep_aspect_var.get():
                orig_width, orig_height = self.edited_image.size
                ratio = min(new_width / orig_width, new_height / orig_height)
                new_width = int(orig_width * ratio)
                new_height = int(orig_height * ratio)
            
            self.edited_image = self.edited_image.resize((new_width, new_height), Image.LANCZOS)
            self.display_image()
            
            self.new_width_entry.delete(0, tk.END)
            self.new_height_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("خطأ", f"قيم غير صالحة: {str(e)}")
    
    def reset_edits(self):
        """استعادة الصورة إلى حالتها الأصلية"""
        if self.original_image:
            self.edited_image = self.original_image.copy()
            self.brightness_var.set(1.0)
            self.contrast_var.set(1.0)
            self.sharpness_var.set(1.0)
            self.display_image()
    
    def save_edits(self):
        """حفظ التعديلات على الصورة"""
        if self.edited_image and self.images:
            try:
                self.edited_image.save(self.images[self.current_image_index])
                self.original_image = self.edited_image.copy()
                messagebox.showinfo("تم", "تم حفظ التعديلات بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن حفظ التعديلات: {str(e)}")
    
    def update_buttons_state(self):
        """تحديث حالة أزرار التنقل"""
        if self.current_image_index <= 0:
            self.prev_btn.config(state=tk.DISABLED)
        else:
            self.prev_btn.config(state=tk.NORMAL)
        
        if self.current_image_index >= len(self.images) - 1:
            self.next_btn.config(state=tk.DISABLED)
        else:
            self.next_btn.config(state=tk.NORMAL)
        
        if len(self.images) == 0:
            self.prev_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.DISABLED)
            self.delete_btn.config(state=tk.DISABLED)
            self.fullscreen_btn.config(state=tk.DISABLED)
            self.edit_btn.config(state=tk.DISABLED)
            self.image_name_label.config(text="لا توجد صور")
            self.image_count_label.config(text="0 / 0")
            self.image_label.config(image='')
            if self.edit_window and self.edit_window.winfo_exists():
                self.close_edit_window()
        else:
            self.delete_btn.config(state=tk.NORMAL)
            self.fullscreen_btn.config(state=tk.NORMAL)
            self.edit_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
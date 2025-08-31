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
        self.root.geometry('1000x800')
        self.root.resizable(True, True)
        self.root.configure(bg='#2c3e50')
        
        # مركزية النافذة على الشاشة
        self.center_window()
        
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
    
    def center_window(self):
        """توسيط النافذة على الشاشة"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    def load_existing_images(self):
        """تحميل الصور الموجودة في مجلد المعرض"""
        # الحصول على قائمة بجميع الملفات في المجلد
        for file in os.listdir(self.image_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(os.path.join(self.image_folder, file))
    
    def create_widgets(self):
        """إنشاء عناصر واجهة المستخدم"""
        # إنشاء نمط للأزرار بألوان متناسقة
        style = ttk.Style()
        style.configure('TButton', 
                        font=('Arial', 10), 
                        background='#3498db', 
                        foreground='white',
                        borderwidth=1,
                        focusthickness=3,
                        focuscolor='#3498db')
        style.map('TButton', 
                  background=[('active', '#2980b9')],
                  foreground=[('active', 'white')])
        
        style.configure('Tool.TButton', 
                        font=('Arial', 9), 
                        padding=(5, 2),
                        background='#3498db',
                        foreground='white')
        style.map('Tool.TButton', 
                  background=[('active', '#2980b9')],
                  foreground=[('active', 'white')])
        
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
        
        # إطار أدوات التحرير (سيتم إظهاره عند التحرير)
        self.tool_frame = tk.Frame(self.root, bg='#2c3e50')
        
        # إطار التحكم بالأعلى (التنقل والأدوات الأساسية)
        top_control_frame = tk.Frame(self.root, bg='#2c3e50')
        top_control_frame.pack(pady=5, fill=tk.X)
        
        # أزرار التنقل
        nav_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        nav_frame.pack(side=tk.LEFT, padx=10)
        
        # استخدام رموز Unicode للأسهم
        self.prev_btn = ttk.Button(nav_frame, text="◀ السابق", command=self.prev_image, 
                                  state=tk.DISABLED, style='Tool.TButton')
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(nav_frame, text="التالي ▶", command=self.next_image, 
                                  state=tk.DISABLED, style='Tool.TButton')
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # أزرار الأدوات
        tool_btn_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        tool_btn_frame.pack(side=tk.RIGHT, padx=10)
        
        # زر تحميل صورة جديدة
        self.load_btn = ttk.Button(tool_btn_frame, text="📁 تحميل صورة", command=self.load_image, style='Tool.TButton')
        self.load_btn.pack(side=tk.LEFT, padx=5)
        
        # زر حذف الصورة الحالية
        self.delete_btn = ttk.Button(tool_btn_frame, text="🗑️ حذف", command=self.delete_image, 
                                    state=tk.DISABLED, style='Tool.TButton')
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        # زر عرض الصورة بكامل الحجم
        self.fullscreen_btn = ttk.Button(tool_btn_frame, text="🔍 عرض كامل", command=self.view_fullscreen, 
                                        state=tk.DISABLED, style='Tool.TButton')
        self.fullscreen_btn.pack(side=tk.LEFT, padx=5)
        
        # زر تحرير الصورة
        self.edit_btn = ttk.Button(tool_btn_frame, text="✏️ تحرير", command=self.toggle_edit_tools, 
                                  state=tk.DISABLED, style='Tool.TButton')
        self.edit_btn.pack(side=tk.LEFT, padx=5)
        
        # إطار معلومات الصورة
        info_frame = tk.Frame(self.root, bg="#34495e")
        info_frame.pack(pady=5, fill=tk.X)
        
        # تسمية لعرض اسم الصورة
        self.image_name_label = tk.Label(info_frame, text="لا توجد صور", font=("Arial", 12), 
                                        fg="white", bg="#34495e")
        self.image_name_label.pack(side=tk.LEFT, padx=10)
        
        # تسمية لعرض رقم الصورة
        self.image_count_label = tk.Label(info_frame, text="0 / 0", font=("Arial", 10), 
                                         fg="white", bg="#34495e")
        self.image_count_label.pack(side=tk.RIGHT, padx=10)
        
        # إعداد أدوات التحرير
        self.setup_edit_tools()
        
        # تحديث حالة الأزرار
        self.update_buttons_state()
    
    def setup_edit_tools(self):
        """إعداد أدوات تحرير الصورة"""
        # إطار أدوات التحرير
        self.edit_tools_frame = tk.Frame(self.tool_frame, bg='#2c3e50')
        self.edit_tools_frame.pack(fill=tk.X, pady=5)
        
        # شريط التمرير لتعديل السطوع
        tk.Label(self.edit_tools_frame, text="السطوع:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(side=tk.LEFT, padx=5)
        self.brightness_var = tk.DoubleVar(value=1.0)
        brightness_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=1.5, 
                                   resolution=0.1, orient=tk.HORIZONTAL,
                                   variable=self.brightness_var, 
                                   command=self.adjust_brightness,
                                   length=150, bg='#2c3e50', fg='white',
                                   troughcolor='#34495e', highlightbackground='#2c3e50')
        brightness_scale.pack(side=tk.LEFT, padx=5)
        
        # شريط التمرير لتعديل التباين
        tk.Label(self.edit_tools_frame, text="التباين:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(side=tk.LEFT, padx=5)
        self.contrast_var = tk.DoubleVar(value=1.0)
        contrast_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=1.5, 
                                 resolution=0.1, orient=tk.HORIZONTAL,
                                 variable=self.contrast_var, 
                                 command=self.adjust_contrast,
                                 length=150, bg='#2c3e50', fg='white',
                                 troughcolor='#34495e', highlightbackground='#2c3e50')
        contrast_scale.pack(side=tk.LEFT, padx=5)
        
        # شريط التمرير لتعديل الحدة
        tk.Label(self.edit_tools_frame, text="الحدة:", font=("Arial", 10), 
                fg="white", bg='#2c3e50').pack(side=tk.LEFT, padx=5)
        self.sharpness_var = tk.DoubleVar(value=1.0)
        sharpness_scale = tk.Scale(self.edit_tools_frame, from_=0.5, to=2.0, 
                                  resolution=0.1, orient=tk.HORIZONTAL,
                                  variable=self.sharpness_var, 
                                  command=self.adjust_sharpness,
                                  length=150, bg='#2c3e50', fg='white',
                                  troughcolor='#34495e', highlightbackground='#2c3e50')
        sharpness_scale.pack(side=tk.LEFT, padx=5)
        
        # أزرار تأثيرات خاصة
        effects_frame = tk.Frame(self.tool_frame, bg='#2c3e50')
        effects_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(effects_frame, text="تأثير أبيض وأسود", 
                  command=self.apply_grayscale, style='Tool.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="تدوير 90°", 
                  command=self.rotate_image, style='Tool.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="عكس الصورة", 
                  command=self.flip_image, style='Tool.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="استعادة الأصل", 
                  command=self.reset_edits, style='Tool.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(effects_frame, text="حفظ التعديلات", 
                  command=self.save_edits, style='Tool.TButton').pack(side=tk.LEFT, padx=5)
    
    def load_image(self):
        """تحميل صورة جديدة من خلال نافذة اختيار الملف"""
        file_path = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=[("ملفات الصور", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        
        if file_path:
            try:
                # إنشاء اسم فريد للصورة بناء على التاريخ والوقت
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_extension = os.path.splitext(file_path)[1]
                new_filename = f"image_{timestamp}{file_extension}"
                new_filepath = os.path.join(self.image_folder, new_filename)
                
                # نسخ الصورة إلى مجلد المعرض
                shutil.copy2(file_path, new_filepath)
                
                # إضافة الصورة إلى القائمة
                self.images.append(new_filepath)
                self.current_image_index = len(self.images) - 1
                
                # عرض الصورة الجديدة
                self.show_image(self.current_image_index)
                
                # تحديث حالة الأزرار
                self.update_buttons_state()
                
                messagebox.showinfo("تم", "تم تحميل الصورة بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن تحميل الصورة: {str(e)}")
    
    def show_image(self, index):
        """عرض الصورة في الواجهة"""
        if 0 <= index < len(self.images):
            try:
                # فتح الصورة الأصلية
                self.original_image = Image.open(self.images[index])
                self.edited_image = self.original_image.copy()
                
                # إعادة تعيين مستويات التعديل
                self.brightness_var.set(1.0)
                self.contrast_var.set(1.0)
                self.sharpness_var.set(1.0)
                self.zoom_level = 1.0
                
                # عرض الصورة
                self.display_image()
                
                # تحديث معلومات الصورة
                image_name = os.path.basename(self.images[index])
                self.image_name_label.config(text=image_name)
                self.image_count_label.config(text=f"{index + 1} / {len(self.images)}")
                
                self.current_image_index = index
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن عرض الصورة: {str(e)}")
    
    def display_image(self):
        """عرض الصورة الحالية مع التعديلات والتكبير/التصغير"""
        if self.edited_image:
            # تطبيق مستوى التكبير/التصغير
            width, height = self.edited_image.size
            new_size = (int(width * self.zoom_level), int(height * self.zoom_level))
            
            if new_size != self.edited_image.size:
                display_image = self.edited_image.resize(new_size, Image.LANCZOS)
            else:
                display_image = self.edited_image
            
            # تحويل الصورة إلى تنسيق متوافق مع Tkinter
            photo = ImageTk.PhotoImage(display_image)
            
            # تحديث التسمية بالصورة الجديدة
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # حفظ المرجع لمنع جمع القمامة
    
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
        
        # تأكيد الحذف
        result = messagebox.askyesno("تأكيد الحذف", "هل أنت متأكد من أنك تريد حذف هذه الصورة؟")
        if not result:
            return
        
        try:
            # حذف الملف من النظام
            os.remove(self.images[self.current_image_index])
            
            # إزالة الصورة من القائمة
            self.images.pop(self.current_image_index)
            
            # تحديد الصورة التي سيتم عرضها بعد الحذف
            if len(self.images) == 0:
                # لا توجد صور متبقية
                self.current_image_index = 0
                self.original_image = None
                self.edited_image = None
                self.image_label.configure(image='')
                self.image_name_label.config(text="لا توجد صور")
                self.image_count_label.config(text="0 / 0")
            elif self.current_image_index >= len(self.images):
                # إذا كنا في نهاية القائمة، انتقل إلى الصورة السابقة
                self.current_image_index = len(self.images) - 1
                self.show_image(self.current_image_index)
            else:
                # عرض الصورة الحالية (تم تحديث الفهرس تلقائياً)
                self.show_image(self.current_image_index)
            
            # تحديث حالة الأزرار
            self.update_buttons_state()
            
            messagebox.showinfo("تم", "تم حذف الصورة بنجاح")
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن حذف الصورة: {str(e)}")
    
    def view_fullscreen(self):
        """عرض الصورة في نافذة منفصلة بحجم كامل"""
        if not self.images:
            return
        
        # إنشاء نافذة جديدة
        fullscreen_window = tk.Toplevel(self.root)
        fullscreen_window.title("عرض الصورة بكامل الحجم")
        fullscreen_window.geometry('800x600')
        fullscreen_window.configure(bg='#2c3e50')
        
        # جعل النافذة تظهر في المقدمة
        fullscreen_window.transient(self.root)
        fullscreen_window.grab_set()
        
        # الحصول على حجم الشاشة
        screen_width = fullscreen_window.winfo_screenwidth()
        screen_height = fullscreen_window.winfo_screenheight()
        
        # عرض الصورة بحجم كامل مع الحفاظ على النسبة
        image = Image.open(self.images[self.current_image_index])
        width, height = image.size
        
        # حساب الحجم المناسب للعرض
        ratio = min(screen_width/width, screen_height/height) * 0.8
        new_size = (int(width * ratio), int(height * ratio))
        display_image = image.resize(new_size, Image.LANCZOS)
        
        # تحويل الصورة لعرضها
        photo = ImageTk.PhotoImage(display_image)
        
        # إنشاء تسمية لعرض الصورة
        image_label = tk.Label(fullscreen_window, image=photo, bg='#2c3e50')
        image_label.image = photo  # حفظ المرجع
        image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # إضافة أزرار للتحكم
        button_frame = tk.Frame(fullscreen_window, bg='#2c3e50')
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="إغلاق", 
                  command=fullscreen_window.destroy, style='Tool.TButton').pack()
    
    def toggle_edit_tools(self):
        """تبديل إظهار/إخفاء أدوات التحرير"""
        if self.tool_frame.winfo_ismapped():
            self.tool_frame.pack_forget()
            self.edit_btn.config(text="✏️ تحرير")
        else:
            self.tool_frame.pack(fill=tk.X, pady=5)
            self.edit_btn.config(text="إخفاء الأدوات")
    
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
        if self.edited_image:
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
                # حفظ الصورة المعدلة فوق الأصلية
                self.edited_image.save(self.images[self.current_image_index])
                self.original_image = self.edited_image.copy()
                messagebox.showinfo("تم", "تم حفظ التعديلات بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن حفظ التعديلات: {str(e)}")
    
    def update_buttons_state(self):
        """تحديث حالة أزرار التنقل"""
        # تعطيل زر السابق إذا كنا في الصورة الأولى
        if self.current_image_index <= 0:
            self.prev_btn.config(state=tk.DISABLED)
        else:
            self.prev_btn.config(state=tk.NORMAL)
        
        # تعطيل زر التالي إذا كنا في الصورة الأخيرة
        if self.current_image_index >= len(self.images) - 1:
            self.next_btn.config(state=tk.DISABLED)
        else:
            self.next_btn.config(state=tk.NORMAL)
        
        # تعطيل الأزرار إذا لم توجد صور
        if len(self.images) == 0:
            self.prev_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.DISABLED)
            self.delete_btn.config(state=tk.DISABLED)
            self.fullscreen_btn.config(state=tk.DISABLED)
            self.edit_btn.config(state=tk.DISABLED)
            self.image_name_label.config(text="لا توجد صور")
            self.image_count_label.config(text="0 / 0")
            self.image_label.config(image='')  # إزالة أي صورة معروضة
            # إخفاء أدوات التحرير إذا كانت ظاهرة
            if self.tool_frame.winfo_ismapped():
                self.tool_frame.pack_forget()
                self.edit_btn.config(text="✏️ تحرير")
        else:
            self.delete_btn.config(state=tk.NORMAL)
            self.fullscreen_btn.config(state=tk.NORMAL)
            self.edit_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
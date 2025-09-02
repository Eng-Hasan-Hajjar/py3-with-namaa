
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
        
        # جعل النافذة تظهر على الجانب الأيمن من الشاشة
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.8)  # 80% من عرض الشاشة
        window_height = int(screen_height * 0.9)  # 90% من ارتفاع الشاشة
        
        # تحديد موقع النافذة على الجانب الأيمن
        x_position = screen_width - window_width
        y_position = (screen_height - window_height) // 2
        
        # تعيين حجم وموقع النافذة
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.configure(bg='#2c3e50')
        
        # قائمة للصور
        self.images = []
        self.current_image_index = 0
        self.original_image = None
        self.edited_image = None
        self.zoom_level = 1.0
        
        # متغيرات التعديل
        self.brightness_var = tk.DoubleVar(value=1.0)
        self.contrast_var = tk.DoubleVar(value=1.0)
        self.sharpness_var = tk.DoubleVar(value=1.0)
        self.keep_aspect_var = tk.BooleanVar(value=True)
        
        # نافذة التحرير
        self.edit_window = None
        
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
        # الحصول على قائمة بجميع الملفات في المجلد
        for file in os.listdir(self.image_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(os.path.join(self.image_folder, file))
    
    def create_widgets(self):
        """إنشاء عناصر واجهة المستخدم"""
        # إنشاء أنماط مختلفة للأزرار بألوان متنوعة
        style = ttk.Style()
        
        # نمط للأزرار الأساسية (أزرق)
        style.configure('Blue.TButton', 
                        font=('Arial', 10), 
                        background='#3498db', 
                        borderwidth=1,
                        focusthickness=3,
                        focuscolor='#3498db')
        style.map('Blue.TButton', 
                  background=[('active', '#2980b9')])
        
        # نمط لأزرار الأدوات (أخضر)
        style.configure('Green.TButton', 
                        font=('Arial', 9), 
                        padding=(5, 2),
                        background='#27ae60')
        style.map('Green.TButton', 
                  background=[('active', '#219653')])
        
        # نمط لأزرار التنقل (أرجواني)
        style.configure('Purple.TButton', 
                        font=('Arial', 10),
                        background='#9b59b6')
        style.map('Purple.TButton', 
                  background=[('active', '#8e44ad')])
        
        # نمط لأزرار التحرير (برتقالي)
        style.configure('Orange.TButton', 
                        font=('Arial', 9),
                        background='#e67e22')
        style.map('Orange.TButton', 
                  background=[('active', '#d35400')])
        
        # نمط لأزرار التأثيرات (أحمر)
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
        
        # استخدام رموز Unicode للأسهم
        self.prev_btn = ttk.Button(nav_frame, text="◀ السابق", command=self.prev_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(nav_frame, text="التالي ▶", command=self.next_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # أزرار الأدوات
        tool_btn_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        tool_btn_frame.pack(side=tk.RIGHT, padx=10)
        
        # زر تحميل صورة جديدة
        self.load_btn = ttk.Button(tool_btn_frame, text="📁 تحميل صورة", command=self.load_image, style='Green.TButton')
        self.load_btn.pack(side=tk.LEFT, padx=5)
        
        # زر حذف الصورة الحالية
        self.delete_btn = ttk.Button(tool_btn_frame, text="🗑 حذف", command=self.delete_image, 
                                    state=tk.DISABLED, style='Red.TButton')
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        # زر عرض الصورة بكامل الحجم
        self.fullscreen_btn = ttk.Button(tool_btn_frame, text="🔍 عرض كامل", command=self.view_fullscreen, 
                                        state=tk.DISABLED, style='Blue.TButton')
        self.fullscreen_btn.pack(side=tk.LEFT, padx=5)
        
        # زر تحرير الصورة
        self.edit_btn = ttk.Button(tool_btn_frame, text="✏ فتح أدوات التحرير", command=self.open_edit_tools, 
                                  state=tk.DISABLED, style='Orange.TButton')
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
        
        # تحديث حالة الأزرار
        self.update_buttons_state()
    
    def open_edit_tools(self):
        """فتح نافذة أدوات التحرير المنبثقة"""
        if not self.images:
            return
            
        if self.edit_window and self.edit_window.winfo_exists():
            # إذا كانت نافذة التحرير مفتوحة بالفعل، اجلبها إلى المقدمة
            self.edit_window.lift()
            return
            
        # إنشاء نافذة منبثقة لأدوات التحرير
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("أدوات تحرير الصورة")
        self.edit_window.geometry("400x600")
        self.edit_window.configure(bg='#34495e')
        self.edit_window.resizable(True, True)
        
        # جعل النافذة تظهر بجوار النافذة الرئيسية
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        self.edit_window.geometry(f"+{main_x - 420}+{main_y}")
        
        # جعل النافذة تظهر في المقدمة
        self.edit_window.transient(self.root)
        self.edit_window.grab_set()
        
        # إعداد أدوات التحرير في النافذة المنبثقة
        self.setup_edit_tools(self.edit_window)
        
        # ربط حدث إغلاق النافذة
        self.edit_window.protocol("WM_DELETE_WINDOW", self.close_edit_tools)
    
    def close_edit_tools(self):
        """إغلاق نافذة أدوات التحرير"""
        if self.edit_window:
            self.edit_window.grab_release()
            self.edit_window.destroy()
            self.edit_window = None
    
    def setup_edit_tools(self, parent):
        """إعداد أدوات تحرير الصورة في النافذة المنبثقة"""
        # عنوان أدوات التحرير
        title_label = tk.Label(parent, text="أدوات تحرير الصورة", 
                              font=("Arial", 16, "bold"), fg="white", bg='#34495e')
        title_label.pack(pady=15)
        
        # إطار لأدوات التعديل الأساسية
        basic_tools_frame = tk.LabelFrame(parent, text="التعديلات الأساسية", 
                                         font=("Arial", 12), fg="white", bg='#34495e')
        basic_tools_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # شريط التمرير لتعديل السطوع
        brightness_frame = tk.Frame(basic_tools_frame, bg='#34495e')
        brightness_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(brightness_frame, text="السطوع:", font=("Arial", 10), 
                fg="white", bg='#34495e').pack(side=tk.LEFT)
        
        self.brightness_var.set(1.0)
        brightness_scale = tk.Scale(brightness_frame, from_=0.5, to=1.5, 
                                   resolution=0.1, orient=tk.HORIZONTAL,
                                   variable=self.brightness_var, 
                                   command=self.adjust_brightness,
                                   length=250, bg='#34495e', fg='white',
                                   troughcolor='#2c3e50', highlightbackground='#34495e')
        brightness_scale.pack(side=tk.RIGHT)
        
        # شريط التمرير لتعديل التباين
        contrast_frame = tk.Frame(basic_tools_frame, bg='#34495e')
        contrast_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(contrast_frame, text="التباين:", font=("Arial", 10), 
                fg="white", bg='#34495e').pack(side=tk.LEFT)
        
        self.contrast_var.set(1.0)
        contrast_scale = tk.Scale(contrast_frame, from_=0.5, to=1.5, 
                                 resolution=0.1, orient=tk.HORIZONTAL,
                                 variable=self.contrast_var, 
                                 command=self.adjust_contrast,
                                 length=250, bg='#34495e', fg='white',
                                 troughcolor='#2c3e50', highlightbackground='#34495e')
        contrast_scale.pack(side=tk.RIGHT)
        
        # شريط التمرير لتعديل الحدة
        sharpness_frame = tk.Frame(basic_tools_frame, bg='#34495e')
        sharpness_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(sharpness_frame, text="الحدة:", font=("Arial", 10), 
                fg="white", bg='#34495e').pack(side=tk.LEFT)
        
        self.sharpness_var.set(1.0)
        sharpness_scale = tk.Scale(sharpness_frame, from_=0.5, to=2.0, 
                                  resolution=0.1, orient=tk.HORIZONTAL,
                                  variable=self.sharpness_var, 
                                  command=self.adjust_sharpness,
                                  length=250, bg='#34495e', fg='white',
                                  troughcolor='#2c3e50', highlightbackground='#34495e')
        sharpness_scale.pack(side=tk.RIGHT)
        
        # إطار لتغيير حجم الصورة
        resize_frame = tk.LabelFrame(parent, text="تغيير الحجم", 
                                    font=("Arial", 12), fg="white", bg='#34495e')
        resize_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # حقول إدخال الأبعاد
        width_frame = tk.Frame(resize_frame, bg='#34495e')
        width_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(width_frame, text="العرض:", font=("Arial", 10), fg="white", bg='#34495e').pack(side=tk.LEFT)
        self.new_width_entry = tk.Entry(width_frame, width=10)
        self.new_width_entry.pack(side=tk.RIGHT)
        
        height_frame = tk.Frame(resize_frame, bg='#34495e')
        height_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(height_frame, text="الطول:", font=("Arial", 10), fg="white", bg='#34495e').pack(side=tk.LEFT)
        self.new_height_entry = tk.Entry(height_frame, width=10)
        self.new_height_entry.pack(side=tk.RIGHT)
        
        # خيار الحفاظ على النسبة
        aspect_frame = tk.Frame(resize_frame, bg='#34495e')
        aspect_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.keep_aspect_var.set(True)
        tk.Checkbutton(aspect_frame, text="الحفاظ على النسبة", variable=self.keep_aspect_var, 
                      fg="white", bg='#34495e', selectcolor='#2c3e50').pack(side=tk.LEFT)
        
        # زر تطبيق تغيير الحجم
        ttk.Button(resize_frame, text="تطبيق الحجم", command=self.apply_resize, 
                  style='Green.TButton').pack(pady=5)
        
        # إطار للتأثيرات الخاصة
        effects_frame = tk.LabelFrame(parent, text="التأثيرات", 
                                     font=("Arial", 12), fg="white", bg='#34495e')
        effects_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # أزرار التأثيرات في شبكة
        effects_grid = tk.Frame(effects_frame, bg='#34495e')
        effects_grid.pack(padx=5, pady=5)
        
        ttk.Button(effects_grid, text="أبيض وأسود", 
                  command=self.apply_grayscale, style='Green.TButton', width=15).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(effects_grid, text="تدوير 90°", 
                  command=self.rotate_image, style='Blue.TButton', width=15).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(effects_grid, text="عكس الصورة", 
                  command=self.flip_image, style='Purple.TButton', width=15).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(effects_grid, text="تأثير ضبابي", 
                  command=self.apply_blur, style='Orange.TButton', width=15).grid(row=1, column=1, padx=5, pady=5)
        
        # إطار لأزرار التحكم
        control_frame = tk.LabelFrame(parent, text="التحكم", 
                                     font=("Arial", 12), fg="white", bg='#34495e')
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        control_grid = tk.Frame(control_frame, bg='#34495e')
        control_grid.pack(padx=5, pady=5)
        
        ttk.Button(control_grid, text="استعادة الأصل", 
                  command=self.reset_edits, style='Blue.TButton', width=15).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(control_grid, text="حفظ التعديلات", 
                  command=self.save_edits, style='Green.TButton', width=15).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(control_grid, text="إغلاق الأدوات", 
                  command=self.close_edit_tools, style='Red.TButton', width=15).grid(row=1, column=0, columnspan=2, pady=10)
    
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
        """عرض الصورة الحالية مع التعديلات والتكبير/التصغير مع تحديد الحجم الأقصى"""
        if self.edited_image:
            # الحصول على حجم إطار الصورة
            frame_width = self.image_frame.winfo_width() - 20
            frame_height = self.image_frame.winfo_height() - 20
            
            # إذا لم يتم بعد تحديد حجم الإطار، استخدام قيم افتراضية
            if frame_width <= 1 or frame_height <= 1:
                frame_width = 600
                frame_height = 400
            
            # حجم الصورة الحالي
            width, height = self.edited_image.size
            
            # حساب نسبة التعديل لتناسب الإطار
            ratio = min(frame_width / width, frame_height / height, 1.0)
            
            # تطبيق مستوى التكبير/التصغير مع النسبة
            adjusted_width = int(width * ratio * self.zoom_level)
            adjusted_height = int(height * ratio * self.zoom_level)
            
            # التحقق من عدم تجاوز حجم الإطار بعد التكبير
            if adjusted_width > frame_width or adjusted_height > frame_height:
                zoom_ratio = min(frame_width / adjusted_width, frame_height / adjusted_height)
                adjusted_width = int(adjusted_width * zoom_ratio)
                adjusted_height = int(adjusted_height * zoom_ratio)
            
            display_image = self.edited_image.resize((adjusted_width, adjusted_height), Image.LANCZOS)
            
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
                # إغلاق نافذة التحرير إذا كانت مفتوحة
                if self.edit_window:
                    self.close_edit_tools()
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
        fullscreen_window.attributes('-fullscreen', True)
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
        ratio = min(screen_width / width, screen_height / height, 1.0)
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
        if self.edited_image:
            self.edited_image = ImageOps.grayscale(self.edited_image)
            self.display_image()
    
    def apply_blur(self):
        """تطبيق تأثير ضبابي على الصورة"""
        if self.edited_image:
            self.edited_image = self.edited_image.filter(ImageFilter.BLUR)
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
                # الحفاظ على النسبة
                orig_width, orig_height = self.edited_image.size
                ratio = min(new_width / orig_width, new_height / orig_height)
                new_width = int(orig_width * ratio)
                new_height = int(orig_height * ratio)
            
            self.edited_image = self.edited_image.resize((new_width, new_height), Image.LANCZOS)
            self.display_image()
            
            # تنظيف الحقول بعد التطبيق
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
        else:
            self.delete_btn.config(state=tk.NORMAL)
            self.fullscreen_btn.config(state=tk.NORMAL)
            self.edit_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
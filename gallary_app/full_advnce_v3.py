import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont
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
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.9)
        x_position = screen_width - window_width
        y_position = (screen_height - window_height) // 2
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
        
        # متغيرات النصوص والرموز التعبيرية
        self.text_content = tk.StringVar(value="")
        self.text_x = tk.IntVar(value=50)
        self.text_y = tk.IntVar(value=50)
        self.emoji_var = tk.StringVar(value="😊")
        
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
        for file in os.listdir(self.image_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(os.path.join(self.image_folder, file))
    
    def create_widgets(self):
        """إنشاء عناصر واجهة المستخدم"""
        style = ttk.Style()
        style.configure('Blue.TButton', font=('Arial', 10), background='#3498db', 
                        borderwidth=1, focusthickness=3, focuscolor='#3498db')
        style.map('Blue.TButton', background=[('active', '#2980b9')])
        style.configure('Green.TButton', font=('Arial', 9), padding=(5, 2), background='#27ae60')
        style.map('Green.TButton', background=[('active', '#219653')])
        style.configure('Purple.TButton', font=('Arial', 10), background='#9b59b6')
        style.map('Purple.TButton', background=[('active', '#8e44ad')])
        style.configure('Orange.TButton', font=('Arial', 9), background='#e67e22')
        style.map('Orange.TButton', background=[('active', '#d35400')])
        style.configure('Red.TButton', font=('Arial', 9), background='#e74c3c')
        style.map('Red.TButton', background=[('active', '#c0392b')])
        
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill=tk.X, pady=10)
        title_label = tk.Label(title_frame, text="معرض الصور المتقدم", 
                              font=("Arial", 18, "bold"), fg="white", bg='#2c3e50')
        title_label.pack(pady=5)
        
        self.image_frame = tk.Frame(self.root, bg="#34495e", relief=tk.RAISED, bd=3)
        self.image_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.image_label = tk.Label(self.image_frame, bg="#34495e")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        top_control_frame = tk.Frame(self.root, bg='#2c3e50')
        top_control_frame.pack(pady=5, fill=tk.X)
        
        nav_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        nav_frame.pack(side=tk.LEFT, padx=10)
        self.prev_btn = ttk.Button(nav_frame, text="◀ السابق", command=self.prev_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        self.next_btn = ttk.Button(nav_frame, text="التالي ▶", command=self.next_image, 
                                  state=tk.DISABLED, style='Purple.TButton')
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        tool_btn_frame = tk.Frame(top_control_frame, bg='#2c3e50')
        tool_btn_frame.pack(side=tk.RIGHT, padx=10)
        self.load_btn = ttk.Button(tool_btn_frame, text="📁 تحميل صورة", command=self.load_image, style='Green.TButton')
        self.load_btn.pack(side=tk.LEFT, padx=5)
        self.delete_btn = ttk.Button(tool_btn_frame, text="🗑 حذف", command=self.delete_image, 
                                    state=tk.DISABLED, style='Red.TButton')
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        self.fullscreen_btn = ttk.Button(tool_btn_frame, text="🔍 عرض كامل", command=self.view_fullscreen, 
                                        state=tk.DISABLED, style='Blue.TButton')
        self.fullscreen_btn.pack(side=tk.LEFT, padx=5)
        self.edit_btn = ttk.Button(tool_btn_frame, text="✏ فتح أدوات التحرير", command=self.open_edit_tools, 
                                  state=tk.DISABLED, style='Orange.TButton')
        self.edit_btn.pack(side=tk.LEFT, padx=5)
        
        info_frame = tk.Frame(self.root, bg="#34495e")
        info_frame.pack(pady=5, fill=tk.X)
        self.image_name_label = tk.Label(info_frame, text="لا توجد صور", font=("Arial", 12), 
                                        fg="white", bg="#34495e")
        self.image_name_label.pack(side=tk.LEFT, padx=10)
        self.image_count_label = tk.Label(info_frame, text="0 / 0", font=("Arial", 10), 
                                         fg="white", bg="#34495e")
        self.image_count_label.pack(side=tk.RIGHT, padx=10)
        
        self.update_buttons_state()
    
    def open_edit_tools(self):
        """فتح نافذة أدوات التحرير المنبثقة"""
        if not self.images:
            return
        if self.edit_window and self.edit_window.winfo_exists():
            self.edit_window.lift()
            return
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("أدوات تحرير الصورة")
        self.edit_window.geometry("400x700")
        self.edit_window.configure(bg='#34495e')
        self.edit_window.resizable(True, True)
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        self.edit_window.geometry(f"+{main_x - 420}+{main_y}")
        self.edit_window.transient(self.root)
        self.edit_window.grab_set()
        self.setup_edit_tools(self.edit_window)
        self.edit_window.protocol("WM_DELETE_WINDOW", self.close_edit_tools)
    
    def close_edit_tools(self):
        """إغلاق نافذة أدوات التحرير"""
        if self.edit_window:
            self.edit_window.grab_release()
            self.edit_window.destroy()
            self.edit_window = None
            self.edit_btn.config(text="✏ فتح أدوات التحرير")
    
    def setup_edit_tools(self, parent):
        """إعداد أدوات تحرير الصورة في النافذة المنبثقة"""
        title_label = tk.Label(parent, text="أدوات تحرير الصورة", 
                              font=("Arial", 16, "bold"), fg="white", bg='#34495e')
        title_label.pack(pady=15)
        
        basic_tools_frame = tk.LabelFrame(parent, text="التعديلات الأساسية", 
                                         font=("Arial", 12), fg="white", bg='#34495e')
        basic_tools_frame.pack(fill=tk.X, padx=10, pady=5)
        
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
        
        resize_frame = tk.LabelFrame(parent, text="تغيير الحجم", 
                                    font=("Arial", 12), fg="white", bg='#34495e')
        resize_frame.pack(fill=tk.X, padx=10, pady=5)
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
        aspect_frame = tk.Frame(resize_frame, bg='#34495e')
        aspect_frame.pack(fill=tk.X, padx=5, pady=5)
        self.keep_aspect_var.set(True)
        tk.Checkbutton(aspect_frame, text="الحفاظ على النسبة", variable=self.keep_aspect_var, 
                      fg="white", bg='#34495e', selectcolor='#2c3e50').pack(side=tk.LEFT)
        ttk.Button(resize_frame, text="تطبيق الحجم", command=self.apply_resize, 
                  style='Green.TButton').pack(pady=5)
        
        # إطار النصوص
        text_frame = tk.LabelFrame(parent, text="إضافة نص", 
                                  font=("Arial", 12), fg="white", bg='#34495e')
        text_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(text_frame, text="النص:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        self.text_content_entry = tk.Entry(text_frame, textvariable=self.text_content, width=30)
        self.text_content_entry.pack(anchor='w', padx=5, pady=2)
        tk.Label(text_frame, text="الموضع X:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        tk.Entry(text_frame, textvariable=self.text_x, width=10).pack(anchor='w', padx=5, pady=2)
        tk.Label(text_frame, text="الموضع Y:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        tk.Entry(text_frame, textvariable=self.text_y, width=10).pack(anchor='w', padx=5, pady=2)
        ttk.Button(text_frame, text="إضافة النص", command=self.add_text, style='Green.TButton').pack(anchor='w', padx=5, pady=5)
        
        # إطار الرموز التعبيرية
        emoji_frame = tk.LabelFrame(parent, text="إضافة رمز تعبيري", 
                                   font=("Arial", 12), fg="white", bg='#34495e')
        emoji_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(emoji_frame, text="اختر رمزًا تعبيريًا:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        emojis = ["😊", "❤️", "🌟", "🎉", "👍", "😍"]
        self.emoji_var.set(emojis[0])
        tk.OptionMenu(emoji_frame, self.emoji_var, *emojis).pack(anchor='w', padx=5, pady=2)
        tk.Label(emoji_frame, text="الموضع X:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        tk.Entry(emoji_frame, textvariable=self.text_x, width=10).pack(anchor='w', padx=5, pady=2)
        tk.Label(emoji_frame, text="الموضع Y:", font=("Arial", 10), fg="white", bg='#34495e').pack(anchor='w', padx=5)
        tk.Entry(emoji_frame, textvariable=self.text_y, width=10).pack(anchor='w', padx=5, pady=2)
        ttk.Button(emoji_frame, text="إضافة الرمز", command=self.add_emoji, style='Green.TButton').pack(anchor='w', padx=5, pady=5)
        
        effects_frame = tk.LabelFrame(parent, text="التأثيرات", 
                                     font=("Arial", 12), fg="white", bg='#34495e')
        effects_frame.pack(fill=tk.X, padx=10, pady=5)
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
    
    def add_text(self):
        """إضافة نص إلى الصورة"""
        if not self.edited_image:
            return
        try:
            text = self.text_content.get()
            x = self.text_x.get()
            y = self.text_y.get()
            if not text:
                messagebox.showwarning("تحذير", "يرجى إدخال نص")
                return
            draw = ImageDraw.Draw(self.edited_image)
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            draw.text((x, y), text, fill="white", font=font, stroke_width=2, stroke_fill="black")
            self.display_image()
            self.text_content_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("خطأ", f"قيم غير صالحة للموضع: {str(e)}")
    
    def add_emoji(self):
        """إضافة رمز تعبيري إلى الصورة"""
        if not self.edited_image:
            return
        try:
            emoji = self.emoji_var.get()
            x = self.text_x.get()
            y = self.text_y.get()
            draw = ImageDraw.Draw(self.edited_image)
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            draw.text((x, y), emoji, fill="white", font=font, stroke_width=2, stroke_fill="black")
            self.display_image()
        except ValueError as e:
            messagebox.showerror("خطأ", f"قيم غير صالحة للموضع: {str(e)}")
    
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
                self.original_image = Image.open(self.images[index]).convert("RGBA")
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
            frame_width = self.image_frame.winfo_width() - 20
            frame_height = self.image_frame.winfo_height() - 20
            if frame_width <= 1 or frame_height <= 1:
                frame_width = 600
                frame_height = 400
            width, height = self.edited_image.size
            ratio = min(frame_width / width, frame_height / height, 1.0)
            adjusted_width = int(width * ratio * self.zoom_level)
            adjusted_height = int(height * ratio * self.zoom_level)
            if adjusted_width > frame_width or adjusted_height > frame_height:
                zoom_ratio = min(frame_width / adjusted_width, frame_height / adjusted_height)
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
                if self.edit_window:
                    self.close_edit_tools()
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
        ratio = min(screen_width / width, screen_height / height, 1.0)
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
        if self.edited_image:
            self.edited_image = ImageOps.grayscale(self.edited_image).convert("RGBA")
            self.display_image()
    
    def apply_blur(self):
        """تطبيق تأثير ضبابي على الصورة"""
        if self.edited_image:
            self.edited_image = self.edited_image.filter(ImageFilter.BLUR).convert("RGBA")
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
            self.text_content.set("")
            self.text_x.set(50)
            self.text_y.set(50)
            self.emoji_var.set("😊")
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
            if self.edit_window:
                self.close_edit_tools()
        else:
            self.delete_btn.config(state=tk.NORMAL)
            self.fullscreen_btn.config(state=tk.NORMAL)
            self.edit_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
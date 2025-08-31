import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil
from datetime import datetime

class ImageGalleryApp:
    def __init__(self, root):
        # تهيئة النافذة الرئيسية
        self.root = root
        self.root.title("معرض الصور")
        self.root.geometry('800x700')
        self.root.resizable(False, False)
        
        # قائمة للصور
        self.images = []
        self.current_image_index = 0
        
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
        # إطار الصورة الرئيسية
        self.image_frame = tk.Frame(self.root, bg="white", relief=tk.SUNKEN, bd=2)
        self.image_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # تسمية لعرض الصورة
        self.image_label = tk.Label(self.image_frame, bg="white")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # إطار لأزرار التحكم
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # زر الصورة السابقة
        self.prev_btn = tk.Button(control_frame, text="السابق", command=self.prev_image, 
                                 state=tk.DISABLED, width=10)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        # زر تحميل صورة جديدة
        self.load_btn = tk.Button(control_frame, text="تحميل صورة", command=self.load_image, width=10)
        self.load_btn.pack(side=tk.LEFT, padx=5)
        
        # زر الصورة التالية
        self.next_btn = tk.Button(control_frame, text="التالي", command=self.next_image, 
                                 state=tk.DISABLED, width=10)
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # إطار معلومات الصورة
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)
        
        # تسمية لعرض اسم الصورة
        self.image_name_label = tk.Label(info_frame, text="لا توجد صور", font=("Arial", 12))
        self.image_name_label.pack()
        
        # تسمية لعرض رقم الصورة
        self.image_count_label = tk.Label(info_frame, text="0 / 0", font=("Arial", 10))
        self.image_count_label.pack()
        
        # تحديث حالة الأزرار
        self.update_buttons_state()
    
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
                # فتح الصورة وتعديل حجمها لتناسب الواجهة
                image = Image.open(self.images[index])
                # الحفاظ على نسبة العرض إلى الارتفاع
                width, height = image.size
                max_size = (600, 500)
                
                if width > max_size[0] or height > max_size[1]:
                    ratio = min(max_size[0]/width, max_size[1]/height)
                    new_size = (int(width * ratio), int(height * ratio))
                    image = image.resize(new_size, Image.LANCZOS)
                
                # تحويل الصورة إلى تنسيق متوافق مع Tkinter
                photo = ImageTk.PhotoImage(image)
                
                # تحديث التسمية بالصورة الجديدة
                self.image_label.configure(image=photo)
                self.image_label.image = photo  # حفظ المرجع لمنع جمع القمامة
                
                # تحديث معلومات الصورة
                image_name = os.path.basename(self.images[index])
                self.image_name_label.config(text=image_name)
                self.image_count_label.config(text=f"{index + 1} / {len(self.images)}")
                
                self.current_image_index = index
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن عرض الصورة: {str(e)}")
    
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
        
        # تعطيل كلا الزرين إذا لم توجد صور
        if len(self.images) == 0:
            self.prev_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.DISABLED)
            self.image_name_label.config(text="لا توجد صور")
            self.image_count_label.config(text="0 / 0")
            self.image_label.config(image='')  # إزالة أي صورة معروضة

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
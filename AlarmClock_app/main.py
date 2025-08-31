import tkinter as tk  # استيراد مكتبة tkinter لإنشاء واجهة المستخدم الرسومية
from tkinter import ttk, filedialog, messagebox  # استيراد أدوات إضافية من tkinter
from PIL import Image, ImageTk  # استيراد مكتبة معالجة الصور
import pygame  # استيراد مكتبة pygame لتشغيل الأصوات
import time  # استيراد مكتبة الوقت للوظائف الزمنية
import threading  # استيراد مكتبة threading للتشغيل المتزامن
import os  # استيراد مكتبة os للتعامل مع نظام الملفات
from datetime import datetime  # استيراد datetime للتعامل مع التاريخ والوقت

class AlarmClock:
    def __init__(self, root):
        # تهيئة النافذة الرئيسية للتطبيق
        self.root = root
        self.root.title("منبه متقدم")  # تحديد عنوان النافذة
        self.root.geometry("600x700")  # تحديد حجم النافذة
        self.root.resizable(False, False)  # منع تغيير حجم النافذة
        
        # تهيئة وحدة الصوت في مكتبة pygame
        pygame.mixer.init()
        
        # قائمة لتخزين المنبهات
        self.alarms = []
        # متغير لحفظ مسار الصوت الحالي
        self.current_sound = None
        
        # استدعاء دالة إنشاء واجهة المستخدم
        self.create_widgets()
        
        # بدء تحديث الوقت الحالي
        self.update_time()
        
    def create_widgets(self):
        # إنشاء إطار لعرض الصورة
        image_frame = ttk.Frame(self.root)
        image_frame.pack(pady=10)  # وضع الإطار مع تباعد 10 بكسل
        
        # محاولة تحميل صورة الساعة الافتراضية
        try:
            # فتح صورة الساعة الافتراضية
            self.clock_image = Image.open("clock.png")
            # تغيير حجم الصورة إلى 300x300 بكسل
            self.clock_image = self.clock_image.resize((300, 300), Image.LANCZOS)
            # تحويل الصورة إلى صيغة متوافقة مع tkinter
            self.clock_photo = ImageTk.PhotoImage(self.clock_image)
            # إنشاء تسمية لعرض الصورة
            self.image_label = ttk.Label(image_frame, image=self.clock_photo)
            self.image_label.pack()  # وضع التسمية في الإطار
        except:
            # في حال فشل تحميل الصورة، عرض نص بديل
            self.image_label = ttk.Label(image_frame, text="صورة الساعة", font=("Arial", 16))
            self.image_label.pack()
        
        # زر لتحميل صورة مخصصة
        self.load_image_btn = ttk.Button(image_frame, text="تحميل صورة", command=self.load_image)
        self.load_image_btn.pack(pady=5)  # وضع الزر مع تباعد 5 بكسل
        
        # إنشاء إطار لعرض الوقت والتاريخ الحالي
        time_frame = ttk.Frame(self.root)
        time_frame.pack(pady=10)
        
        # تسمية لعرض الوقت الحالي
        self.time_label = ttk.Label(time_frame, text="", font=("Arial", 24))
        self.time_label.pack()
        
        # تسمية لعرض التاريخ الحالي
        self.date_label = ttk.Label(time_frame, text="", font=("Arial", 16))
        self.date_label.pack()
        
        # إنشاء إطار لإضافة منبه جديد
        alarm_frame = ttk.LabelFrame(self.root, text="إضافة منبه جديد")
        alarm_frame.pack(pady=10, padx=20, fill="x")  # وضع الإطار مع تعبئة المحور الأفقي
        
        # إضافة تسمية و قائمة منسدلة لاختيار الساعة
        ttk.Label(alarm_frame, text="الساعة:").grid(row=0, column=0, padx=5, pady=5)
        self.hour_var = tk.StringVar()  # متغير نصي لحفظ قيمة الساعة
        # إنشاء قائمة منسدلة للاختيار من 0 إلى 23
        self.hour_combo = ttk.Combobox(alarm_frame, textvariable=self.hour_var, 
                                      values=[f"{i:02d}" for i in range(0, 24)], width=5)
        self.hour_combo.grid(row=0, column=1, padx=5, pady=5)
        self.hour_combo.current(0)  # تعيين القيمة الافتراضية الأولى في القائمة
        
        # إضافة تسمية و قائمة منسدلة لاختيار الدقيقة
        ttk.Label(alarm_frame, text="الدقيقة:").grid(row=0, column=2, padx=5, pady=5)
        self.minute_var = tk.StringVar()  # متغير نصي لحفظ قيمة الدقيقة
        # إنشاء قائمة منسدلة للاختيار من 0 إلى 59
        self.minute_combo = ttk.Combobox(alarm_frame, textvariable=self.minute_var, 
                                        values=[f"{i:02d}" for i in range(0, 60)], width=5)
        self.minute_combo.grid(row=0, column=3, padx=5, pady=5)
        self.minute_combo.current(0)  # تعيين القيمة الافتراضية الأولى في القائمة
        
        # إضافة تسمية و قائمة منسدلة لاختيار نمط التكرار
        ttk.Label(alarm_frame, text="التكرار:").grid(row=1, column=0, padx=5, pady=5)
        self.repeat_var = tk.StringVar()  # متغير نصي لحفظ نمط التكرار
        # إنشاء قائمة منسدلة بخيارات التكرار
        self.repeat_combo = ttk.Combobox(alarm_frame, textvariable=self.repeat_var, 
                                        values=["مرة واحدة", "يومي", "أسبوعي"], width=10)
        self.repeat_combo.grid(row=1, column=1, padx=5, pady=5)
        self.repeat_combo.current(0)  # تعيين القيمة الافتراضية الأولى في القائمة
        
        # إضافة تسمية و زر لتحميل الصوت
        ttk.Label(alarm_frame, text="الصوت:").grid(row=1, column=2, padx=5, pady=5)
        self.sound_btn = ttk.Button(alarm_frame, text="تحميل صوت", command=self.load_sound)
        self.sound_btn.grid(row=1, column=3, padx=5, pady=5)
        
        # زر لإضافة المنبه الجديد
        self.add_btn = ttk.Button(alarm_frame, text="إضافة المنبه", command=self.add_alarm)
        self.add_btn.grid(row=2, column=0, columnspan=4, pady=10)  # وضع الزر عبر 4 أعمدة
        
        # إنشاء إطار لعرض قائمة المنبهات المضافة
        list_frame = ttk.LabelFrame(self.root, text="المنبهات المضافة")
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)  # وضع الإطار مع تعبئة المساحة المتاحة
        
        # إنشاء جدول لعرض المنبهات
        columns = ("الوقت", "التكرار", "الحالة", "الصوت")  # أسماء الأعمدة
        self.alarm_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
        
        # تهيئة أعمدة الجدول
        for col in columns:
            self.alarm_tree.heading(col, text=col)  # تعيين عناوين الأعمدة
            self.alarm_tree.column(col, width=100, anchor="center")  # تعيين خصائص الأعمدة
        
        self.alarm_tree.pack(fill="both", expand=True, padx=5, pady=5)  # وضع الجدول في الإطار
        
        # إنشاء إطار لأزرار التحكم
        control_frame = ttk.Frame(list_frame)
        control_frame.pack(pady=5)
        
        # زر لإزالة المنبه المحدد
        self.remove_btn = ttk.Button(control_frame, text="إزالة المنبه المحدد", command=self.remove_alarm)
        self.remove_btn.pack(side="left", padx=5)
        
        # زر لتفعيل أو إلغاء تفعيل المنبه المحدد
        self.toggle_btn = ttk.Button(control_frame, text="تفعيل/إلغاء المنبه", command=self.toggle_alarm)
        self.toggle_btn.pack(side="left", padx=5)
        
        # بدء عملية التحقق من المنبهات في الخلفية
        self.check_alarms()
    
    def load_image(self):
        # فتح نافذة لاختيار ملف صورة
        file_path = filedialog.askopenfilename(
            title="اختر صورة الساعة",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]  # تحديد أنواع الملفات المقبولة
        )
        
        if file_path:
            try:
                # تحميل الصورة المختارة
                self.clock_image = Image.open(file_path)
                # تغيير حجم الصورة
                self.clock_image = self.clock_image.resize((300, 300), Image.LANCZOS)
                # تحويل الصورة إلى صيغة متوافقة مع tkinter
                self.clock_photo = ImageTk.PhotoImage(self.clock_image)
                # تحديث التسمية لعرض الصورة الجديدة
                self.image_label.configure(image=self.clock_photo)
            except Exception as e:
                # عرض رسالة خطأ في حال فشل التحميل
                messagebox.showerror("خطأ", f"لا يمكن تحميل الصورة: {str(e)}")
    
    def load_sound(self):
        # فتح نافذة لاختيار ملف صوت
        file_path = filedialog.askopenfilename(
            title="اختر صوت المنبه",
            filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")]  # تحديد أنواع الملفات المقبولة
        )
        
        if file_path:
            # حفظ مسار الصوت المختار
            self.current_sound = file_path
            # عرض رسالة تأكيد بنجاح التحميل
            messagebox.showinfo("تم", f"تم تحميل الصوت: {os.path.basename(file_path)}")
    
    def add_alarm(self):
        # الحصول على القيم المحددة من واجهة المستخدم
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        repeat = self.repeat_var.get()
        
        # التحقق من صحة القيم المدخلة
        if not hour or not minute:
            messagebox.showerror("خطأ", "يرجى تحديد الوقت بشكل صحيح")
            return
        
        # التحقق من وجود صوت مرفق
        if not self.current_sound:
            messagebox.showerror("خطأ", "يرجى تحميل صوت للمنبه")
            return
        
        # إنشاء وقت المنبه بصيغة نصية
        alarm_time = f"{hour}:{minute}"
        # إنشاء معرف فريد للمنبه
        alarm_id = len(self.alarms) + 1
        
        # إنشاء كائن المنبه
        alarm = {
            "id": alarm_id,
            "time": alarm_time,
            "repeat": repeat,
            "sound": self.current_sound,
            "active": True  # حالة تفعيل المنبه
        }
        
        # إضافة المنبه إلى القائمة
        self.alarms.append(alarm)
        # تحديث قائمة المنبهات المعروضة
        self.update_alarm_list()
        
        # عرض رسالة تأكيد بإضافة المنبه
        messagebox.showinfo("تم", f"تم إضافة المنبه للساعة {alarm_time}")
    
    def update_alarm_list(self):
        # مسح جميع العناصر الحالية في الجدول
        for item in self.alarm_tree.get_children():
            self.alarm_tree.delete(item)
        
        # إضافة المنبهات من القائمة إلى الجدول
        for alarm in self.alarms:
            # تحديد حالة المنبه (مفعل أو غير مفعل)
            status = "مفعل" if alarm["active"] else "غير مفعل"
            # إضافة عنصر جديد إلى الجدول
            self.alarm_tree.insert("", "end", values=(
                alarm["time"], alarm["repeat"], status, os.path.basename(alarm["sound"])
            ))
    
    def remove_alarm(self):
        # الحصول على العنصر المحدد في الجدول
        selected = self.alarm_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "يرجى تحديد منبه لإزالته")
            return
        
        # الحصول على فهرس العنصر المحدد
        index = self.alarm_tree.index(selected[0])
        
        # التحقق من صحة الفهرس ثم إزالة المنبه
        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)
            # تحديث قائمة المنبهات المعروضة
            self.update_alarm_list()
    
    def toggle_alarm(self):
        # الحصول على العنصر المحدد في الجدول
        selected = self.alarm_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "يرجى تحديد منبه لتعديل حالته")
            return
        
        # الحصول على فهرس العنصر المحدد
        index = self.alarm_tree.index(selected[0])
        
        # التحقق من صحة الفهرس ثم عكس حالة التفعيل
        if 0 <= index < len(self.alarms):
            self.alarms[index]["active"] = not self.alarms[index]["active"]
            # تحديث قائمة المنبهات المعروضة
            self.update_alarm_list()
    
    def update_time(self):
        # الحصول على الوقت والتاريخ الحالي
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")  # تنسيق الوقت
        current_date = now.strftime("%Y-%m-%d")  # تنسيق التاريخ
        
        # تحديث نص التسميات بالوقت والتاريخ الحالي
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        # جدولة تحديث الوقت كل ثانية (1000 مللي ثانية)
        self.root.after(1000, self.update_time)
    
    def check_alarms(self):
        # الحصول على الوقت الحالي (بدون ثواني)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        # المرور على جميع المنبهات للتحقق من موعدها
        for alarm in self.alarms:
            # التحقق إذا كان المنبه مفعل ووصل وقته
            if alarm["active"] and alarm["time"] == current_time:
                # تشغيل صوت المنبه
                self.play_alarm(alarm["sound"])
                
                # إذا كان المنبه لمرة واحدة، إلغاء تفعيله بعد التشغيل
                if alarm["repeat"] == "مرة واحدة":
                    alarm["active"] = False
                    # تحديث قائمة المنبهات المعروضة
                    self.update_alarm_list()
        
        # حساب الوقت المتبقي حتى الدقيقة القادمة
        next_check = 60 - now.second
        # جدولة التحقق مرة أخرى بعد الوقت المتبقي
        threading.Timer(next_check, self.check_alarms).start()
    
    def play_alarm(self, sound_file):
        try:
            # تحميل ملف الصوت
            pygame.mixer.music.load(sound_file)
            # تشغيل الصوت
            pygame.mixer.music.play()
            
            # عرض نافذة التنبيه
            self.show_alarm_alert(sound_file)
        except Exception as e:
            # عرض رسالة خطأ في حال فشل تشغيل الصوت
            messagebox.showerror("خطأ", f"لا يمكن تشغيل الصوت: {str(e)}")
    
    def show_alarm_alert(self, sound_file):
        # إنشاء نافذة تنبيه جديدة
        alert_window = tk.Toplevel(self.root)
        alert_window.title("تنبيه المنبه")  # عنوان النافذة
        alert_window.geometry("300x200")  # حجم النافذة
        alert_window.resizable(False, False)  # منع تغيير حجم النافذة
        
        # جعل نافذة التنبيه تظهر فوق جميع النوافذ
        alert_window.attributes('-topmost', True)
        
        # إضافة تسمية لعرض رسالة التنبيه
        ttk.Label(alert_window, text="حان وقت المنبه!", font=("Arial", 16)).pack(pady=20)
        # إضافة تسمية لعرض اسم الصوت المستخدم
        ttk.Label(alert_window, text=f"الصوت: {os.path.basename(sound_file)}").pack(pady=10)
        
        # دالة داخلية لإيقاف الصوت وإغلاق النافذة
        def stop_alarm():
            pygame.mixer.music.stop()  # إيقاف الصوت
            alert_window.destroy()  # إغلاق نافذة التنبيه
        
        # زر لإيقاف المنبه
        ttk.Button(alert_window, text="إيقاف المنبه", command=stop_alarm).pack(pady=20)

if __name__ == "__main__":
    # إنشاء النافذة الرئيسية للتطبيق
    root = tk.Tk()
    # إنشاء كائن المنبه
    app = AlarmClock(root)
    # بدء تشغيل الواجهة الرسومية
    root.mainloop()
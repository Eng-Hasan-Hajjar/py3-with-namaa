import tkinter as tk  # استيراد مكتبة tkinter لإنشاء واجهة المستخدم الرسومية
from tkinter import ttk, filedialog, messagebox  # استيراد أدوات إضافية من tkinter
from PIL import Image, ImageTk  # استيراد مكتبة معالجة الصور
import pygame  # استيراد مكتبة pygame لتشغيل الأصوات
import time  # استيراد مكتبة الوقت للوظائف الزمنية
import threading  # استيراد مكتبة threading للتشغيل المتزامن
import os  # استيراد مكتبة os للتعامل مع نظام الملفات
from datetime import datetime  # استيراد datetime للتعامل مع التاريخ والوقت
import json  # استيراد مكتبة json لحفظ الإعدادات

class AlarmClock:
    def __init__(self, root):
        # تهيئة النافذة الرئيسية للتطبيق
        self.root = root
        self.root.title("منبه متقدم")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # تهيئة وحدة الصوت في مكتبة pygame
        pygame.mixer.init()
        
        # قائمة لتخزين المنبهات
        self.alarms = []
        # متغير لحفظ مسار الصوت الحالي
        self.current_sound = None
        # متغير لحفظ مسار الصورة الحالي
        self.clock_image_path = "clock.png"
        
        # متغير لحفظ مسار ملف الإعدادات
        self.settings_file = "app_settings.json"
        
        # استدعاء دالة لتحميل الإعدادات المحفوظة
        self.load_settings()
        
        # استدعاء دالة إنشاء واجهة المستخدم
        self.create_widgets()
        
        # بدء تحديث الوقت الحالي
        self.update_time()
        
    def create_widgets(self):
        # إنشاء إطار لعرض الصورة
        image_frame = ttk.Frame(self.root)
        image_frame.pack(pady=10)
        
        # محاولة تحميل صورة الساعة
        self.image_label = ttk.Label(image_frame)
        self.image_label.pack()
        self.load_image(self.clock_image_path, from_startup=True)
        
        # زر لتحميل صورة مخصصة
        self.load_image_btn = ttk.Button(image_frame, text="تحميل صورة", command=self.load_image)
        self.load_image_btn.pack(pady=5)
        
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
        alarm_frame.pack(pady=10, padx=20, fill="x")
        
        # إضافة تسمية و قائمة منسدلة لاختيار الساعة
        ttk.Label(alarm_frame, text="الساعة:").grid(row=0, column=0, padx=5, pady=5)
        self.hour_var = tk.StringVar()
        self.hour_combo = ttk.Combobox(alarm_frame, textvariable=self.hour_var, 
                                      values=[f"{i:02d}" for i in range(0, 24)], width=5)
        self.hour_combo.grid(row=0, column=1, padx=5, pady=5)
        self.hour_combo.current(0)
        
        # إضافة تسمية و قائمة منسدلة لاختيار الدقيقة
        ttk.Label(alarm_frame, text="الدقيقة:").grid(row=0, column=2, padx=5, pady=5)
        self.minute_var = tk.StringVar()
        self.minute_combo = ttk.Combobox(alarm_frame, textvariable=self.minute_var, 
                                        values=[f"{i:02d}" for i in range(0, 60)], width=5)
        self.minute_combo.grid(row=0, column=3, padx=5, pady=5)
        self.minute_combo.current(0)
        
        # إضافة تسمية و قائمة منسدلة لاختيار نمط التكرار
        ttk.Label(alarm_frame, text="التكرار:").grid(row=1, column=0, padx=5, pady=5)
        self.repeat_var = tk.StringVar()
        self.repeat_combo = ttk.Combobox(alarm_frame, textvariable=self.repeat_var, 
                                        values=["مرة واحدة", "يومي", "أسبوعي"], width=10)
        self.repeat_combo.grid(row=1, column=1, padx=5, pady=5)
        self.repeat_combo.current(0)
        
        # إضافة تسمية و زر لتحميل الصوت
        ttk.Label(alarm_frame, text="الصوت:").grid(row=1, column=2, padx=5, pady=5)
        self.sound_btn = ttk.Button(alarm_frame, text="تحميل صوت", command=self.load_sound)
        self.sound_btn.grid(row=1, column=3, padx=5, pady=5)
        
        # زر لإضافة المنبه الجديد
        self.add_btn = ttk.Button(alarm_frame, text="إضافة المنبه", command=self.add_alarm)
        self.add_btn.grid(row=2, column=0, columnspan=4, pady=10)
        
        # إنشاء إطار لعرض قائمة المنبهات المضافة
        list_frame = ttk.LabelFrame(self.root, text="المنبهات المضافة")
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # إنشاء جدول لعرض المنبهات
        columns = ("الوقت", "التكرار", "الحالة", "الصوت")
        self.alarm_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
        
        # تهيئة أعمدة الجدول
        for col in columns:
            self.alarm_tree.heading(col, text=col)
            self.alarm_tree.column(col, width=100, anchor="center")
        
        self.alarm_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
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
    
    def load_settings(self):
        # تحميل الإعدادات من ملف json
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                try:
                    settings = json.load(f)
                    if "image_path" in settings and os.path.exists(settings["image_path"]):
                        self.clock_image_path = settings["image_path"]
                    if "sound_path" in settings and os.path.exists(settings["sound_path"]):
                        self.current_sound = settings["sound_path"]
                    if "alarms" in settings:
                        self.alarms = settings["alarms"]
                        self.update_alarm_list()
                except (json.JSONDecodeError, KeyError):
                    pass
    
    def save_settings(self):
        # حفظ الإعدادات في ملف json
        settings = {
            "image_path": self.clock_image_path,
            "sound_path": self.current_sound,
            "alarms": self.alarms
        }
        with open(self.settings_file, "w") as f:
            json.dump(settings, f, indent=4)
            
    def load_image(self, file_path=None, from_startup=False):
        if not file_path:
            file_path = filedialog.askopenfilename(
                title="اختر صورة الساعة",
                filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif;*.bmp")]
            )
        
        if file_path:
            try:
                self.clock_image = Image.open(file_path)
                self.clock_image = self.clock_image.resize((300, 300), Image.LANCZOS)
                self.clock_photo = ImageTk.PhotoImage(self.clock_image)
                self.image_label.configure(image=self.clock_photo)
                
                self.clock_image_path = file_path
                self.save_settings()
                
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن تحميل الصورة: {str(e)}")
        elif not from_startup:
            self.clock_image_path = "clock.png"
            self.save_settings()
            self.image_label.configure(image='') # مسح الصورة الحالية إذا لم يتم اختيار واحدة
            
    def load_sound(self):
        file_path = filedialog.askopenfilename(
            title="اختر صوت المنبه",
            filetypes=[("Audio Files", ".mp3;.wav;*.ogg")]
        )
        
        if file_path:
            self.current_sound = file_path
            self.save_settings()
            messagebox.showinfo("تم", f"تم تحميل الصوت: {os.path.basename(file_path)}")
    
    def add_alarm(self):
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        repeat = self.repeat_var.get()
        
        if not hour or not minute:
            messagebox.showerror("خطأ", "يرجى تحديد الوقت بشكل صحيح")
            return
        
        if not self.current_sound:
            messagebox.showerror("خطأ", "يرجى تحميل صوت للمنبه")
            return
        
        alarm_time = f"{hour}:{minute}"
        alarm_id = len(self.alarms) + 1
        
        alarm = {
            "id": alarm_id,
            "time": alarm_time,
            "repeat": repeat,
            "sound": self.current_sound,
            "active": True
        }
        
        self.alarms.append(alarm)
        self.save_settings()
        self.update_alarm_list()
        
        messagebox.showinfo("تم", f"تم إضافة المنبه للساعة {alarm_time}")
    
    def update_alarm_list(self):
        for item in self.alarm_tree.get_children():
            self.alarm_tree.delete(item)
        
        for alarm in self.alarms:
            status = "مفعل" if alarm["active"] else "غير مفعل"
            self.alarm_tree.insert("", "end", values=(
                alarm["time"], alarm["repeat"], status, os.path.basename(alarm["sound"])
            ))
    
    def remove_alarm(self):
        selected = self.alarm_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "يرجى تحديد منبه لإزالته")
            return
        
        index = self.alarm_tree.index(selected[0])
        
        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)
            self.save_settings()
            self.update_alarm_list()
    
    def toggle_alarm(self):
        selected = self.alarm_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "يرجى تحديد منبه لتعديل حالته")
            return
        
        index = self.alarm_tree.index(selected[0])
        
        if 0 <= index < len(self.alarms):
            self.alarms[index]["active"] = not self.alarms[index]["active"]
            self.save_settings()
            self.update_alarm_list()
    
    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        self.root.after(1000, self.update_time)
    
    def check_alarms(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        for alarm in self.alarms:
            if alarm["active"] and alarm["time"] == current_time:
                self.play_alarm(alarm["sound"])
                
                if alarm["repeat"] == "مرة واحدة":
                    alarm["active"] = False
                    self.save_settings()
                    self.update_alarm_list()
        
        next_check = 60 - now.second
        threading.Timer(next_check, self.check_alarms).start()
    
    def play_alarm(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            self.show_alarm_alert(sound_file)
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن تشغيل الصوت: {str(e)}")
    
    def show_alarm_alert(self, sound_file):
        alert_window = tk.Toplevel(self.root)
        alert_window.title("تنبيه المنبه")
        alert_window.geometry("300x200")
        alert_window.resizable(False, False)
        
        alert_window.attributes('-topmost', True)
        
        ttk.Label(alert_window, text="حان وقت المنبه!", font=("Arial", 16)).pack(pady=20)
        ttk.Label(alert_window, text=f"الصوت: {os.path.basename(sound_file)}").pack(pady=10)
        
        def stop_alarm():
            pygame.mixer.music.stop()
            alert_window.destroy()
        
        ttk.Button(alert_window, text="إيقاف المنبه", command=stop_alarm).pack(pady=20)

if __name__ == "__main__":
    # إنشاء النافذة الرئيسية للتطبيق
    root = tk.Tk()
    # إنشاء كائن المنبه
    app = AlarmClock(root)
    # بدء تشغيل الواجهة الرسومية
    root.mainloop()
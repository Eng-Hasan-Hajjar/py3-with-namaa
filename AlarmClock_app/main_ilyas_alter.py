import tkinter as tk  # استيراد مكتبة tkinter لإنشاء واجهة المستخدم الرسومية
from tkinter import ttk, filedialog, messagebox  # استيراد أدوات إضافية من tkinter
from PIL import Image, ImageTk  # استيراد مكتبة معالجة الصور
import pygame  # استيراد مكتبة pygame لتشغيل الأصوات
import threading  # استيراد مكتبة threading للتشغيل المتزامن
import os  # استيراد مكتبة os للتعامل مع نظام الملفات
from datetime import datetime  # استيراد datetime للتعامل مع التاريخ والوقت
import json  # لتخزين الإعدادات

class AlarmClock:
    def __init__(self,root):
        self.root = root
        self.root.title("منبه متقدم")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        pygame.mixer.init()
        
        self.alarms = []
        self.current_sound = None

        # ملف الإعدادات لتخزين مسار الصورة
        self.config_file = "config.json"

        # تحميل مسار الصورة إذا كان محفوظ سابقاً
        self.saved_image_path = self.load_saved_image_path()

        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        image_frame = ttk.Frame(self.root)
        image_frame.pack(pady=10)

        # إذا عندي صورة محفوظة أستخدمها
        if self.saved_image_path and os.path.exists(self.saved_image_path):
            try:
                self.clock_image = Image.open(self.saved_image_path)
                self.clock_image = self.clock_image.resize((300, 300), Image.LANCZOS)
                self.clock_photo = ImageTk.PhotoImage(self.clock_image)
                self.image_label = ttk.Label(image_frame, image=self.clock_photo)
                self.image_label.pack()
            except:
                self.image_label = ttk.Label(image_frame, text="صورة الساعة", font=("Arial", 16))
                self.image_label.pack()
        else:
            # صورة افتراضية (clock.png) إذا ما في مسار محفوظ
            try:
                self.clock_image = Image.open("clock.png")
                self.clock_image = self.clock_image.resize((300, 300), Image.LANCZOS)
                self.clock_photo = ImageTk.PhotoImage(self.clock_image)
                self.image_label = ttk.Label(image_frame, image=self.clock_photo)
                self.image_label.pack()
            except:
                self.image_label = ttk.Label(image_frame, text="صورة الساعة", font=("Arial", 16))
                self.image_label.pack()

        self.load_image_btn = ttk.Button(image_frame, text="تحميل صورة", command=self.load_image)
        self.load_image_btn.pack(pady=5)

        # إنشاء إطار لعرض الوقت والتاريخ الحالي
        time_frame = ttk.Frame(self.root)
        time_frame.pack(pady=10)

        self.time_label = ttk.Label(time_frame, text="", font=("Arial", 24))
        self.time_label.pack()

        self.date_label = ttk.Label(time_frame, text="", font=("Arial", 16))
        self.date_label.pack()

        # إنشاء إطار لإضافة منبه جديد
        alarm_frame = ttk.LabelFrame(self.root, text="إضافة منبه جديد")
        alarm_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(alarm_frame, text="الساعة:").grid(row=0, column=0, padx=5, pady=5)
        self.hour_var = tk.StringVar()
        self.hour_combo = ttk.Combobox(alarm_frame, textvariable=self.hour_var, 
                                      values=[f"{i:02d}" for i in range(0, 24)], width=5)
        self.hour_combo.grid(row=0, column=1, padx=5, pady=5)
        self.hour_combo.current(0)

        ttk.Label(alarm_frame, text="الدقيقة:").grid(row=0, column=2, padx=5, pady=5)
        self.minute_var = tk.StringVar()
        self.minute_combo = ttk.Combobox(alarm_frame, textvariable=self.minute_var, 
                                        values=[f"{i:02d}" for i in range(0, 60)], width=5)
        self.minute_combo.grid(row=0, column=3, padx=5, pady=5)
        self.minute_combo.current(0)

        ttk.Label(alarm_frame, text="التكرار:").grid(row=1, column=0, padx=5, pady=5)
        self.repeat_var = tk.StringVar()
        self.repeat_combo = ttk.Combobox(alarm_frame, textvariable=self.repeat_var, 
                                        values=["مرة واحدة", "يومي", "أسبوعي"], width=10)
        self.repeat_combo.grid(row=1, column=1, padx=5, pady=5)
        self.repeat_combo.current(0)

        ttk.Label(alarm_frame, text="الصوت:").grid(row=1, column=2, padx=5, pady=5)
        self.sound_btn = ttk.Button(alarm_frame, text="تحميل صوت", command=self.load_sound)
        self.sound_btn.grid(row=1, column=3, padx=5, pady=5)

        self.add_btn = ttk.Button(alarm_frame, text="إضافة المنبه", command=self.add_alarm)
        self.add_btn.grid(row=2, column=0, columnspan=4, pady=10)

        list_frame = ttk.LabelFrame(self.root, text="المنبهات المضافة")
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        columns = ("الوقت", "التكرار", "الحالة", "الصوت")
        self.alarm_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)

        for col in columns:
            self.alarm_tree.heading(col, text=col)
            self.alarm_tree.column(col, width=100, anchor="center")

        self.alarm_tree.pack(fill="both", expand=True, padx=5, pady=5)

        control_frame = ttk.Frame(list_frame)
        control_frame.pack(pady=5)

        self.remove_btn = ttk.Button(control_frame, text="إزالة المنبه المحدد", command=self.remove_alarm)
        self.remove_btn.pack(side="left", padx=5)

        self.toggle_btn = ttk.Button(control_frame, text="تفعيل/إلغاء المنبه", command=self.toggle_alarm)
        self.toggle_btn.pack(side="left", padx=5)

        self.check_alarms()

    def load_image(self):
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

                # حفظ المسار الجديد بالملف
                self.save_image_path(file_path)

            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن تحميل الصورة: {str(e)}")

    def save_image_path(self, path):
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump({"image_path": path}, f)
        except Exception as e:
            print("خطأ في حفظ المسار:", e)

    def load_saved_image_path(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("image_path", None)
            except:
                return None
        return None

    def load_sound(self):
        file_path = filedialog.askopenfilename(
            title="اختر صوت المنبه",
            filetypes=[("Audio Files", ".mp3;.wav;*.ogg")]
        )
        
        if file_path:
            self.current_sound = file_path
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
            self.update_alarm_list()
    
    def toggle_alarm(self):
        selected = self.alarm_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "يرجى تحديد منبه لتعديل حالته")
            return
        
        index = self.alarm_tree.index(selected[0])
        if 0 <= index < len(self.alarms):
            self.alarms[index]["active"] = not self.alarms[index]["active"]
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
# -- coding: utf-8 --
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont
import os
import shutil
from datetime import datetime


class ImageGalleryApp:
    def __init__(self, root):
        # النافذة الرئيسية
        self.root = root
        self.root.title("معرض الصور المتقدم")
        self.root.configure(bg="#2c3e50")
        # حجم وموقع مناسب
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        win_w, win_h = int(screen_w * 0.85), int(screen_h * 0.9)
        x = (screen_w - win_w) // 2
        y = (screen_h - win_h) // 2
        self.root.geometry(f"{win_w}x{win_h}+{x}+{y}")

        # بيانات الصور والتحرير
        self.images = []                  # قائمة المسارات
        self.current_image_index = 0
        self.original_image = None        # PIL.Image (نسخة الأصل)
        self.edited_image = None          # الصورة تحت التحرير
        self.photo = None                 # ImageTk لعرض الصورة
        self.zoom_level = 1.0

        # عوامل التعديل السريعة
        self.brightness_var = tk.DoubleVar(value=1.0)
        self.contrast_var   = tk.DoubleVar(value=1.0)
        self.sharpness_var  = tk.DoubleVar(value=1.0)
        self.keep_aspect_var = tk.BooleanVar(value=True)

        # بيانات النصوص القابلة للسحب
        # كل عنصر: {text, x, y, size, fill, canvas_id}
        # (x, y) بإحداثيات الصورة (وليس الكانفس)
        self.text_overlays = []
        self.selected_text_idx = None
        self.drag_dx = 0
        self.drag_dy = 0

        # نافذة التحرير الجانبية
        self.edit_window = None

        # مجلد تخزين الصور
        self.image_folder = "gallery_images"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        self.load_existing_images()

        # واجهة المستخدم
        self.create_widgets()

        # أعِد الرسم عند تغيير حجم الـ Canvas
        self.canvas.bind("<Configure>", lambda e: self.redraw_canvas())

        # ربط أحداث السحب للنصوص
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        if self.images:
            self.show_image(0)

    # ============== بناء الواجهة ==============

    def create_widgets(self):
        # عنوان
        title_frame = tk.Frame(self.root, bg="#2c3e50")
        title_frame.pack(fill=tk.X, pady=6)
        tk.Label(
            title_frame, text="معرض الصور المتقدم",
            font=("Arial", 18, "bold"), fg="white", bg="#2c3e50"
        ).pack()

        # إطار الصورة (Canvas فقط للعرض والرسم فوقه)
        self.canvas_frame = tk.Frame(self.root, bg="#34495e", relief=tk.RAISED, bd=2)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
        self.canvas = tk.Canvas(self.canvas_frame, bg="#34495e", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # شريط معلومات تحت الصورة
        info_frame = tk.Frame(self.root, bg="#34495e")
        info_frame.pack(fill=tk.X, padx=10, pady=6)
        self.image_name_label = tk.Label(info_frame, text="لا توجد صور", fg="white", bg="#34495e", font=("Arial", 11))
        self.image_name_label.pack(side=tk.LEFT, padx=10)
        self.image_count_label = tk.Label(info_frame, text="0 / 0", fg="white", bg="#34495e", font=("Arial", 11))
        self.image_count_label.pack(side=tk.RIGHT, padx=10)

        # أزرار التحكم السفلية (دائمًا ثابتة)
        controls = tk.Frame(self.root, bg="#2c3e50")
        controls.pack(fill=tk.X, pady=8, padx=10)

        btn_style = dict(font=("Arial", 11, "bold"), fg="white", padx=10, pady=6, bd=0, relief=tk.FLAT)

        self.prev_btn = tk.Button(controls, text="◀ السابق", bg="#3498db", command=self.prev_image, **btn_style)
        self.prev_btn.pack(side=tk.LEFT, padx=4)

        self.next_btn = tk.Button(controls, text="التالي ▶", bg="#3498db", command=self.next_image, **btn_style)
        self.next_btn.pack(side=tk.LEFT, padx=4)

        self.load_btn = tk.Button(controls, text="📁 تحميل صورة", bg="#27ae60", command=self.load_image, **btn_style)
        self.load_btn.pack(side=tk.LEFT, padx=4)

        self.delete_btn = tk.Button(controls, text="🗑 حذف", bg="#e74c3c", command=self.delete_image, **btn_style)
        self.delete_btn.pack(side=tk.LEFT, padx=4)

        self.fullscreen_btn = tk.Button(controls, text="⛶ عرض كامل", bg="#9b59b6", command=self.view_fullscreen, **btn_style)
        self.fullscreen_btn.pack(side=tk.RIGHT, padx=4)

        self.edit_btn = tk.Button(controls, text="✏ أدوات التحرير", bg="#e67e22", command=self.open_edit_tools, **btn_style)
        self.edit_btn.pack(side=tk.RIGHT, padx=4)

        self.update_buttons_state()

    # ============== تحميل/حفظ/تنقّل ==============

    def load_existing_images(self):
        for f in os.listdir(self.image_folder):
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                self.images.append(os.path.join(self.image_folder, f))

    def load_image(self):
        path = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=[("ملفات الصور", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if not path:
            return
        try:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            ext = os.path.splitext(path)[1]
            new_name = f"image_{ts}{ext}"
            dst = os.path.join(self.image_folder, new_name)
            shutil.copy2(path, dst)
            self.images.append(dst)
            self.show_image(len(self.images) - 1)
            self.update_buttons_state()
            messagebox.showinfo("تم", "تم تحميل الصورة بنجاح")
        except Exception as e:
            messagebox.showerror("خطأ", f"تعذر تحميل الصورة:\n{e}")

    def show_image(self, index):
        if not (0 <= index < len(self.images)):
            return
        try:
            self.original_image = Image.open(self.images[index]).convert("RGBA")
            self.edited_image = self.original_image.copy()
            self.current_image_index = index
            self.brightness_var.set(1.0)
            self.contrast_var.set(1.0)
            self.sharpness_var.set(1.0)
            self.text_overlays.clear()      # نبدأ بنصوص فارغة للصورة الجديدة
            self.redraw_canvas()
            name = os.path.basename(self.images[index])
            self.image_name_label.config(text=name)
            self.image_count_label.config(text=f"{index+1} / {len(self.images)}")
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن عرض الصورة:\n{e}")

    def delete_image(self):
        if not self.images:
            return
        if not messagebox.askyesno("تأكيد الحذف", "هل تريد حذف هذه الصورة؟"):
            return
        try:
            os.remove(self.images[self.current_image_index])
        except Exception:
            # إن فشل الحذف من القرص، نحذفها من القائمة فقط
            pass
        del self.images[self.current_image_index]
        if not self.images:
            self.current_image_index = 0
            self.original_image = None
            self.edited_image = None
            self.canvas.delete("all")
            self.image_name_label.config(text="لا توجد صور")
            self.image_count_label.config(text="0 / 0")
            if self.edit_window:
                self.close_edit_tools()
        else:
            if self.current_image_index >= len(self.images):
                self.current_image_index = len(self.images) - 1
            self.show_image(self.current_image_index)
        self.update_buttons_state()

    def prev_image(self):
        if not self.images:
            return
        self.show_image(max(0, self.current_image_index - 1))
        self.update_buttons_state()

    def next_image(self):
        if not self.images:
            return
        self.show_image(min(len(self.images) - 1, self.current_image_index + 1))
        self.update_buttons_state()

    def update_buttons_state(self):
        state = tk.NORMAL if self.images else tk.DISABLED
        self.prev_btn.config(state=state)
        self.next_btn.config(state=state)
        self.delete_btn.config(state=state)
        self.fullscreen_btn.config(state=state)
        self.edit_btn.config(state=state)

    # ============== عرض الصورة + النصوص ==============

    def compute_fit(self):
        """حساب حجم الصورة على الكانفس وإزاحتها (للمركز) ونسبة المقياس."""
        if not self.edited_image:
            return 1.0, 0, 0, 1, 1
        cw = max(1, self.canvas.winfo_width())
        ch = max(1, self.canvas.winfo_height())
        iw, ih = self.edited_image.size
        scale = min(cw / iw, ch / ih)
        disp_w, disp_h = int(iw * scale), int(ih * scale)
        off_x = (cw - disp_w) // 2
        off_y = (ch - disp_h) // 2
        return scale, off_x, off_y, disp_w, disp_h

    def image_to_canvas(self, x, y):
        """تحويل إحداثيات من الصورة إلى الكانفس."""
        scale, off_x, off_y, _, _ = self.compute_fit()
        return off_x + x * scale, off_y + y * scale

    def canvas_to_image(self, cx, cy):
        """تحويل إحداثيات من الكانفس إلى الصورة (يقيد داخل الصورة)."""
        scale, off_x, off_y, disp_w, disp_h = self.compute_fit()
        if scale == 0:
            return 0, 0
        x = (cx - off_x) / scale
        y = (cy - off_y) / scale
        # تقييد داخل الصورة
        iw, ih = self.edited_image.size
        x = max(0, min(iw, x))
        y = max(0, min(ih, y))
        return x, y

    def redraw_canvas(self):
        """إعادة رسم الصورة والنصوص على الكانفس."""
        self.canvas.delete("all")
        if not self.edited_image:
            return
        scale, off_x, off_y, disp_w, disp_h = self.compute_fit()
        # عرض الصورة
        disp_img = self.edited_image.resize((max(1, disp_w), max(1, disp_h)), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(disp_img)
        self.canvas.create_image(off_x, off_y, image=self.photo, anchor="nw", tags=("image",))

        # عرض كل النصوص (overlay)
        for i, item in enumerate(self.text_overlays):
            cx, cy = self.image_to_canvas(item["x"], item["y"])
            # نص الكانفس (لا يدعم stroke، معاينة فقط)
            cid = self.canvas.create_text(
                cx, cy, text=item["text"], anchor="nw",
                font=("Arial", item["size"], "bold"),
                fill=item["fill"], tags=("textOverlay", f"text_{i}")
            )
            item["canvas_id"] = cid

    # ============== التفاعل مع النصوص (سحب/إفلات) ==============

    def on_canvas_click(self, event):
        """تحديد النص القريب للنقرة والتهيئة للسحب."""
        self.selected_text_idx = None
        # البحث عن عنصر نصي تحت المؤشر
        ids = self.canvas.find_overlapping(event.x-2, event.y-2, event.x+2, event.y+2)
        for cid in ids:
            tags = self.canvas.gettags(cid)
            if "textOverlay" in tags:
                # tags مثل ('textOverlay', 'text_3')
                for t in tags:
                    if t.startswith("text_"):
                        idx = int(t.split("_")[1])
                        self.selected_text_idx = idx
                        # احسب فرق السحب
                        tx, ty = self.canvas.coords(cid)
                        self.drag_dx = event.x - tx
                        self.drag_dy = event.y - ty
                        return

    def on_canvas_drag(self, event):
        """سحب النص المحدد وتحديث مكانه (إحداثيات صورة)."""
        if self.selected_text_idx :
            return
        item = self.text_overlays[self.selected_text_idx]
        cid = item.get("canvas_id")
        if not cid:
            return
        new_cx = event.x - self.drag_dx
        new_cy = event.y - self.drag_dy
        self.canvas.coords(cid, new_cx, new_cy)
        # حدّث إحداثيات الصورة
        ix, iy = self.canvas_to_image(new_cx, new_cy)
        item["x"], item["y"] = ix, iy

    def on_canvas_release(self,_event):
        """إنهاء السحب."""
        pass

    # ============== نافذة أدوات التحرير ==============

    def open_edit_tools(self):
        if not self.edited_image:
            return
        if self.edit_window and self.edit_window.winfo_exists():
            self.edit_window.lift()
            return

        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("أدوات تحرير الصورة")
        self.edit_window.configure(bg="#34495e")
        self.edit_window.geometry("420x760")
        self.edit_window.resizable(True, True)
        self.edit_window.transient(self.root)
        self.edit_window.grab_set()
        self.edit_window.protocol("WM_DELETE_WINDOW", self.close_edit_tools)

        # ===== أقسام =====
        def section(label):
            frm = tk.LabelFrame(self.edit_window, text=label, font=("Arial", 12, "bold"),
                                fg="white", bg="#34495e")
            frm.pack(fill=tk.X, padx=10, pady=8)
            return frm

        # التعديلات الأساسية
        basic = section("التعديلات الأساسية")
        self._make_scale(basic, "السطوع", 0.5, 1.5, 0.1, self.brightness_var, self.apply_basic_adjust)
        self._make_scale(basic, "التباين", 0.5, 1.5, 0.1, self.contrast_var, self.apply_basic_adjust)
        self._make_scale(basic, "الحدة",   0.5, 2.0, 0.1, self.sharpness_var, self.apply_basic_adjust)

        # التأثيرات
        effects = section("التأثيرات")
        self._make_btn(effects, "أبيض وأسود", self.apply_grayscale)
        self._make_btn(effects, "تأثير ضبابي", self.apply_blur)
        self._make_btn(effects, "تدوير 90°", self.rotate_image)
        self._make_btn(effects, "عكس أفقي", self.flip_image)

        # تغيير الحجم
        resize = section("تغيير الحجم")
        row1 = tk.Frame(resize, bg="#34495e"); row1.pack(fill=tk.X, padx=6, pady=4)
        tk.Label(row1, text="العرض:", fg="white", bg="#34495e").pack(side=tk.LEFT)
        self.new_width_entry = tk.Entry(row1, width=8); self.new_width_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(row1, text="الطول:", fg="white", bg="#34495e").pack(side=tk.LEFT, padx=(10,0))
        self.new_height_entry = tk.Entry(row1, width=8); self.new_height_entry.pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(resize, text="الحفاظ على النسبة", variable=self.keep_aspect_var,
                       fg="white", bg="#34495e", selectcolor="#2c3e50").pack(anchor="w", padx=6, pady=4)
        self._make_btn(resize, "تطبيق الحجم", self.apply_resize)

        # النصوص
        textsec = section("النصوص (أضف ثم اسحب على الصورة)")
        rowt1 = tk.Frame(textsec, bg="#34495e"); rowt1.pack(fill=tk.X, padx=6, pady=4)
        tk.Label(rowt1, text="النص:", fg="white", bg="#34495e").pack(side=tk.LEFT)
        self.text_content_entry = tk.Entry(rowt1, width=22); self.text_content_entry.pack(side=tk.LEFT, padx=6)

        rowt2 = tk.Frame(textsec, bg="#34495e"); rowt2.pack(fill=tk.X, padx=6, pady=4)
        tk.Label(rowt2, text="الحجم:", fg="white", bg="#34495e").pack(side=tk.LEFT)
        self.text_size_var = tk.IntVar(value=40)
        tk.Spinbox(rowt2, from_=10, to=150, textvariable=self.text_size_var, width=6).pack(side=tk.LEFT, padx=6)

        tk.Label(rowt2, text="اللون:", fg="white", bg="#34495e").pack(side=tk.LEFT)
        self.text_color_var = tk.StringVar(value="white")
        color_menu = ttk.Combobox(rowt2, width=8, state="readonly",
                                  values=["white", "black", "red", "green", "blue", "yellow", "cyan", "magenta"])
        color_menu.set(self.text_color_var.get())
        color_menu.bind("<<ComboboxSelected>>", lambda e: self.text_color_var.set(color_menu.get()))
        color_menu.pack(side=tk.LEFT, padx=6)

        rowt3 = tk.Frame(textsec, bg="#34495e"); rowt3.pack(fill=tk.X, padx=6, pady=6)
        self._make_btn(rowt3, "➕ إضافة النص", self.add_text_overlay, side=tk.LEFT)
        self._make_btn(rowt3, "🧹 حذف النص المحدد", self.delete_selected_text, side=tk.LEFT)
        self._make_btn(rowt3, "📌 تثبيت النصوص على الصورة", self.bake_texts_into_image, side=tk.LEFT)

        # التحكم العام
        ctrl = section("التحكم")
        self._make_btn(ctrl, "استعادة الأصل", self.reset_edits)
        self._make_btn(ctrl, "💾 حفظ التعديلات", self.save_edits)
        self._make_btn(ctrl, "إغلاق الأدوات", self.close_edit_tools)

    def _make_scale(self, parent, label, frm, to, step, var, cmd):
        row = tk.Frame(parent, bg="#34495e"); row.pack(fill=tk.X, padx=6, pady=4)
        tk.Label(row, text=f"{label}:", fg="white", bg="#34495e").pack(side=tk.LEFT)
        sc = tk.Scale(row, from_=frm, to=to, orient=tk.HORIZONTAL, resolution=step,
                      variable=var, command=lambda _=None: cmd(), length=250,
                      bg="#34495e", fg="white", highlightbackground="#34495e", troughcolor="#2c3e50")
        sc.pack(side=tk.RIGHT)

    def _make_btn(self, parent, text, cmd, side=tk.LEFT):
        tk.Button(parent, text=text, command=cmd, bg="#27ae60", fg="white",
                  font=("Arial", 10, "bold"), padx=8, pady=4, bd=0).pack(side=side, padx=5, pady=4)

    def close_edit_tools(self):
        if self.edit_window:
            try:
                self.edit_window.grab_release()
            except Exception:
                pass
            self.edit_window.destroy()
            self.edit_window = None

    # ============== عمليات التحرير ==============

    def apply_basic_adjust(self):
        """تطبيق سطوع/تباين/حدة على الصورة الحالية (تراكميًا)."""
        if not self.original_image:
            return
        # نبدأ من الأصل ثم نراكم التعديلات
        img = self.original_image.copy()
        img = ImageEnhance.Brightness(img).enhance(self.brightness_var.get())
        img = ImageEnhance.Contrast(img).enhance(self.contrast_var.get())
        img = ImageEnhance.Sharpness(img).enhance(self.sharpness_var.get())
        self.edited_image = img
        self.redraw_canvas()

    def apply_grayscale(self):
        if self.edited_image:
            self.edited_image = ImageOps.grayscale(self.edited_image).convert("RGBA")
            self.redraw_canvas()

    def apply_blur(self):
        if self.edited_image:
            self.edited_image = self.edited_image.filter(ImageFilter.BLUR).convert("RGBA")
            self.redraw_canvas()

    def rotate_image(self):
        """تدوير 90° مع تدوير مواقع النصوص."""
        if self.edited_image:
            w, h = self.edited_image.size
            self.edited_image = self.edited_image.rotate(-90, expand=True)  # مع عقارب الساعة
            # تدوير إحداثيات النصوص: (x, y) -> (h - y, x)
            for item in self.text_overlays:
                x, y = item["x"], item["y"]
                item["x"], item["y"] = (h - y), x
            self.redraw_canvas()

    def flip_image(self):
        """عكس أفقي مع تعديل مواقع النصوص."""
        if self.edited_image:
            w, h = self.edited_image.size
            self.edited_image = ImageOps.mirror(self.edited_image)
            for item in self.text_overlays:
                item["x"] = w - item["x"]
            self.redraw_canvas()

    def apply_resize(self):
        if not self.edited_image:
            return
        try:
            new_w = int(self.new_width_entry.get())
            new_h = int(self.new_height_entry.get())
            if new_w <= 0 or new_h <= 0:
                raise ValueError
            ow, oh = self.edited_image.size
            if self.keep_aspect_var.get():
                ratio = min(new_w / ow, new_h / oh)
                new_w = max(1, int(ow * ratio))
                new_h = max(1, int(oh * ratio))
            # تحويل مواقع النصوص مع القياس
            sx = new_w / ow
            sy = new_h / oh
            for item in self.text_overlays:
                item["x"] *= sx
                item["y"] *= sy
            self.edited_image = self.edited_image.resize((new_w, new_h), Image.LANCZOS)
            self.redraw_canvas()
            self.new_width_entry.delete(0, tk.END)
            self.new_height_entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("خطأ", "يرجى إدخال أبعاد صحيحة (أعداد صحيحة موجبة).")

    def reset_edits(self):
        if self.original_image:
            self.edited_image = self.original_image.copy()
            self.brightness_var.set(1.0)
            self.contrast_var.set(1.0)
            self.sharpness_var.set(1.0)
            self.text_overlays.clear()
            self.redraw_canvas()

    def save_edits(self):
        if self.edited_image and self.images:
            try:
                # ثبّت أي نصوص قبل الحفظ
                if self.text_overlays:
                    self.bake_texts_into_image()
                self.edited_image.save(self.images[self.current_image_index])
                self.original_image = self.edited_image.copy()
                messagebox.showinfo("تم", "تم حفظ التعديلات بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"تعذر الحفظ:\n{e}")

    # ============== النصوص (إضافة/حذف/تثبيت) ==============

    def add_text_overlay(self):
        if not self.edited_image:
            return
        txt = self.text_content_entry.get()
        if not txt.strip():
            messagebox.showwarning("تنبيه", "أدخل نصًا أولًا.")
            return
        # أضف النص في أعلى-يسار الصورة بشكل ابتدائي
        item = {
            "text": txt,
            "x": 20.0,
            "y": 20.0,
            "size": int(self.text_size_var.get()),
            "fill": self.text_color_var.get(),
            "canvas_id": None
        }
        self.text_overlays.append(item)
        self.redraw_canvas()
        messagebox.showinfo("معلومة", "تمت إضافة النص. اسحبه بالفأرة لتغيير مكانه.")

    def delete_selected_text(self):
        if self.selected_text_idx is None:
            # إن لم يُحدد عنصر، نحاول آخر عنصر
            if not self.text_overlays:
                return
            self.text_overlays.pop()
        else:
            if 0 <= self.selected_text_idx < len(self.text_overlays):
                self.text_overlays.pop(self.selected_text_idx)
            self.selected_text_idx = None
        self.redraw_canvas()

    def bake_texts_into_image(self):
        """تثبيت النصوص الحالية على الصورة (PIL) ثم مسح الـ overlays."""
        if not self.text_overlays or not self.edited_image:
            return
        draw = ImageDraw.Draw(self.edited_image)
        for item in self.text_overlays:
            try:
                # نحاول خط TrueType، وإلا نستخدم الافتراضي
                font = None
                try:
                    font = ImageFont.truetype("arial.ttf", item["size"])
                except Exception:
                    font = ImageFont.load_default()
                # رسم بحد أسود بسيط (stroke)
                draw.text((item["x"], item["y"]), item["text"],
                          fill=item["fill"], font=font, stroke_width=2, stroke_fill="black")
            except Exception:
                pass
        self.text_overlays.clear()
        self.redraw_canvas()
        messagebox.showinfo("تم", "تم تثبيت النصوص على الصورة.")

    # ============== عرض كامل للشاشة ==============

    def view_fullscreen(self):
        if not self.edited_image:
            return
        fs = tk.Toplevel(self.root)
        fs.title("عرض بكامل الشاشة")
        fs.attributes("-fullscreen", True)
        fs.configure(bg="#2c3e50")
        fs.transient(self.root)
        fs.grab_set()

        canvas = tk.Canvas(fs, bg="#2c3e50", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        def draw_fullscreen(_=None):
            canvas.delete("all")
            sw, sh = canvas.winfo_width(), canvas.winfo_height()
            iw, ih = self.edited_image.size
            scale = min(sw / iw, sh / ih)
            dw, dh = int(iw * scale), int(ih * scale)
            ox, oy = (sw - dw)//2, (sh - dh)//2
            disp = self.edited_image.resize((max(1, dw), max(1, dh)), Image.LANCZOS)
            photo = ImageTk.PhotoImage(disp)
            canvas.create_image(ox, oy, image=photo, anchor="nw")
            canvas.image = photo  # مرجع

        canvas.bind("<Configure>", draw_fullscreen)

        btn = tk.Button(fs, text="إغلاق", command=fs.destroy, bg="#3498db",
                        fg="white", font=("Arial", 12, "bold"), padx=12, pady=6, bd=0)
        btn.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
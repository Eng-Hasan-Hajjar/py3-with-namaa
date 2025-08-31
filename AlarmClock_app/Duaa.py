import tkinter as tk
from tkinter import *

class duaaApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x800')
        self.root.resizable(False, False) 
        
        # إضافة صورة إلى النافذة
        try:
            self.photo = PhotoImage(file="C:/Users/engya/Downloads/2.PNG")
            self.res = self.photo.subsample(1, 1)
            self.img = Label(self.root, image=self.res)
            self.img.pack()
        except:
            # في حالة وجود خطأ في تحميل الصورة
            error_label = Label(self.root, text="تعذر تحميل الصورة", font=("Arial", 16))
            error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = duaaApp(root)
    root.mainloop()
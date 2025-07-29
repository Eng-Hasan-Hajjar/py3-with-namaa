import cv2
import numpy as np
import tkinter as tk
from playsound import playsound
import threading

# تابع تشغيل صوت الإنذار (بخيط منفصل)
def play_alarm():
    playsound("alarm.mp3")  # تأكد أن ملف الإنذار بنفس المجلد

# إنشاء واجهة tkinter
root = tk.Tk()
root.title("مراقبة الحريق 🔥")
root.geometry("400x200")
label = tk.Label(root, text="لا يوجد نار حالياً", font=("Arial", 18), fg="green")
label.pack(pady=40)

# فتح الكاميرا
cap = cv2.VideoCapture(0)

def detect_fire():
    fire_detected = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # تحويل للإطار اللوني HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # نطاق لون النار (أحمر - برتقالي - أصفر)
        lower_fire = np.array([0, 50, 50])
        upper_fire = np.array([35, 255, 255])
        mask = cv2.inRange(hsv, lower_fire, upper_fire)

        # حساب عدد البكسلات النارية
        fire_pixels = cv2.countNonZero(mask)

        if fire_pixels > 5000:  # عدد بكسلات كبير = نار
            if not fire_detected:
                fire_detected = True
                label.config(text="🚨 تم اكتشاف نار!", fg="red")
                threading.Thread(target=play_alarm, daemon=True).start()
        else:
            if fire_detected:
                fire_detected = False
                label.config(text="لا يوجد نار حالياً", fg="green")

        cv2.imshow("كاميرا", frame)
        if cv2.waitKey(1) == 27:  # اضغط Esc للخروج
            break

    cap.release()
    cv2.destroyAllWindows()
    root.quit()

# تشغيل اكتشاف الحريق بخيط منفصل
threading.Thread(target=detect_fire, daemon=True).start()

# تشغيل الواجهة الرسومية
root.mainloop()
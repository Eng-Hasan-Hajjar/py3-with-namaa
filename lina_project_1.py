import tkinter as tk
from tkinter import messagebox
import random

# قائمة كلمات
words = ["school", "python", "apple", "hello", "mouse"]
word = random.choice(words)
guessed_word = ["_" for _ in word]
attempts_left = 6
guessed_letters = []

# عند التخمين
def guess_letter():
    global attempts_left
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("خطأ", "أدخل حرفًا واحدًا فقط!")
        return

    if letter in guessed_letters:
        messagebox.showinfo("مكرر", "أدخلت هذا الحرف من قبل!")
        return

    guessed_letters.append(letter)

    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                guessed_word[i] = letter
        word_label.config(text=" ".join(guessed_word))
        if "_" not in guessed_word:
            messagebox.showinfo("تهانينا", f"ربحت! الكلمة كانت: {word}")
            reset_game()
    else:
        attempts_left -= 1
        attempts_label.config(text=f"محاولات متبقية: {attempts_left}")
        if attempts_left == 0:
            messagebox.showinfo("انتهت اللعبة", f"خسرت! الكلمة كانت: {word}")
            reset_game()

# إعادة اللعبة
def reset_game():
    global word, guessed_word, attempts_left, guessed_letters
    word = random.choice(words)
    guessed_word = ["_" for _ in word]
    attempts_left = 6
    guessed_letters = []
    word_label.config(text=" ".join(guessed_word))
    attempts_label.config(text=f"محاولات متبقية: {attempts_left}")

# واجهة
window = tk.Tk()
window.title("لعبة تخمين الكلمة")
window.geometry("400x250")

word_label = tk.Label(window, text=" ".join(guessed_word), font=("Arial", 24))
word_label.pack(pady=20)

entry = tk.Entry(window)
entry.pack()

guess_btn = tk.Button(window, text="تحقق من الحرف", command=guess_letter)
guess_btn.pack(pady=10)

attempts_label = tk.Label(window, text=f"محاولات متبقية: {attempts_left}")
attempts_label.pack()

reset_btn = tk.Button(window, text="إعادة اللعبة", command=reset_game)
reset_btn.pack(pady=10)

window.mainloop()
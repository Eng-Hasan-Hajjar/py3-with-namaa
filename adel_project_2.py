import tkinter as tk
from tkinter import messagebox
import pyperclip

def paste_text():
    clipboard_text = pyperclip.paste()
    entry_text.delete(0, tk.END)
    entry_text.insert(0, clipboard_text)

def update_text():
    text = entry_text.get()
    search = entry_search.get()
    replace = entry_replace.get()

    count = text.count(search)
    
    if count == 0:
        messagebox.showinfo("Not Found", f"❌ '{search}' not found in your text.")
        result_label.config(text=f"Original Text: {text}")
    else:
        new_text = text.replace(search, replace).strip()
        messagebox.showinfo("Success", f"✅ Replaced {count} occurrence(s).")
        result_label.config(text=f"Updated Text: {new_text}")
        result_label.updated_text = new_text

def delete_text():
    text = entry_text.get()
    search = entry_search.get()

    if search in text:
        new_text = text.replace(search, "").strip()
        messagebox.showinfo("Deleted", f"🗑️ Removed all instances of '{search}'")
        result_label.config(text=f"Updated Text: {new_text}")
        result_label.updated_text = new_text
    else:
        messagebox.showinfo("Not Found", f"❌ '{search}' not found in your text.")
        result_label.config(text=f"Original Text: {text}")

def copy_result():
    copied = getattr(result_label, 'updated_text', None)
    if copied:
        pyperclip.copy(copied)
        messagebox.showinfo("Copied", "📋 Text copied to clipboard!")
    else:
        messagebox.showinfo("Empty", "⚠️ No text to copy yet.")

# GUI setup

root = tk.Tk()
root.title("🔤 Text Search, Replace & Delete")
root.geometry("750x400")
root.configure(bg="#f8f8f8")

tk.Label(root, text="Your Text:", bg="#f8f8f8").pack()
entry_text = tk.Entry(root, width=70)
entry_text.pack()

# Paste button
tk.Button(root, text="📥 Paste from Clipboard", command=paste_text, bg="#FFC107", fg="black").pack(pady=5)

tk.Label(root, text="Search For:", bg="#f8f8f8").pack()
entry_search = tk.Entry(root, width=30)
entry_search.pack()

tk.Label(root, text="Replace With:", bg="#f8f8f8").pack()
entry_replace = tk.Entry(root, width=30)
entry_replace.pack()

# Buttons
btn_frame = tk.Frame(root, bg="#f8f8f8")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🔁 Replace", command=update_text, bg="#4CAF50", fg="white", width=13).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="🗑️ Delete", command=delete_text, bg="#f44336", fg="white", width=13).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="📋 Copy Result", command=copy_result, bg="#2196F3", fg="white", width=13).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", bg="#f8f8f8", wraplength=440, justify="left", font=("Arial", 10, "bold"))
result_label.pack(pady=10)

root.mainloop()

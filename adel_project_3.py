import tkinter as tk
from tkinter import ttk, messagebox

class StudentInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anadolu University Student Information System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f2f5")

        # Data
        self.anadolu_university = {
            "Name": "Anadolu University",
            "Founded in": 1958,
            "Languages of Instruction": "Turkish, English",
            "Number of Professors": 2581,
            "Number of Students": "23,000",
            "Membership": "European University Association",
            "Website": "www.anadolu.edu.tr"
        }

        self.student_data = {
            "Ahmed": {
                "student_id": "1110",
                "full_name": "Ahmed Al-Sayed",
                "department": "Computer Engineering",
                "year": "3rd Year",
                "GPA": "3.4",
                "courses": ["Algorithms", "Databases", "Operating Systems"],
                "advisor": "Dr. Khalid",
                "email": "ahmed.sayed@anadolu.edu.tr",
                "phone": "+90 555 123 4567",
                "enrollment_date": "2022-09-01",
                "status": "Active"
            },
            "Adel": {
                "student_id": "1111",
                "full_name": "Adel Nrakken",
                "department": "Software Engineering",
                "year": "2nd Year",
                "GPA": "3.7",
                "courses": ["Web Development", "Data Structures", "UI/UX Design"],
                "advisor": "Dr. Aylin",
                "email": "adel.nrakken@anadolu.edu.tr",
                "phone": "+90 555 987 6543",
                "enrollment_date": "2023-02-15",
                "status": "Active"
            },
            "Ilyas": {
                "student_id": "1112",
                "full_name": "Ilyas Ben Youssef",
                "department": "Artificial Intelligence",
                "year": "1st Year",
                "GPA": "3.9",
                "courses": ["Python Programming", "Machine Learning", "Ethics in AI"],
                "advisor": "Dr. Cem",
                "email": "ilyas.youssef@anadolu.edu.tr",
                "phone": "+90 555 321 7890",
                "enrollment_date": "2024-01-10",
                "status": "Active"
            }
        }

        # Create main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  # Fixed typo: selfBike -> self

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12), background="#f0f2f5")
        self.style.configure("TButton", font=("Helvetica", 11, "bold"), padding=10)
        self.style.configure("TCombobox", font=("Helvetica", 11))

        # Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="Anadolu University Student Information System",
            font=("Helvetica", 16, "bold"),
            foreground="#1a73e8",
            background="#f0f2f5"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Student selection
        self.select_frame = ttk.Frame(self.main_frame)
        self.select_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Label(self.select_frame, text="Select Student:").grid(row=0, column=0, padx=(0, 10))
        self.student_var = tk.StringVar()
        self.student_combo = ttk.Combobox(
            self.select_frame,
            textvariable=self.student_var,
            values=list(self.student_data.keys()),
            state="readonly",
            width=30
        )
        self.student_combo.grid(row=0, column=1)
        self.student_combo.bind("<<ComboboxSelected>>", self.display_info)

        # University Info Frame
        self.uni_frame = ttk.LabelFrame(self.main_frame, text="University Information", padding=10)
        self.uni_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

        # Student Info Frame
        self.student_frame = ttk.LabelFrame(self.main_frame, text="Student Information", padding=10)
        self.student_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

        # Initialize university info
        self.display_university_info()

    def display_university_info(self):
        for i, (key, value) in enumerate(self.anadolu_university.items()):
            ttk.Label(self.uni_frame, text=f"{key}:", font=("Helvetica", 11, "bold")).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            ttk.Label(self.uni_frame, text=str(value), wraplength=700).grid(row=i, column=1, sticky="w", padx=5, pady=2)

    def display_info(self, event=None):
        # Clear previous student info
        for widget in self.student_frame.winfo_children():
            widget.destroy()

        selected_student = self.student_var.get()
        if selected_student:
            student_info = self.student_data.get(selected_student)
            if student_info:
                for i, (key, value) in enumerate(student_info.items()):
                    ttk.Label(self.student_frame, text=f"{key.replace('_', ' ').title()}:", font=("Helvetica", 11, "bold")).grid(row=i, column=0, sticky="w", padx=5, pady=2)
                    if key == "courses":
                        value = ", ".join(value)
                    ttk.Label(self.student_frame, text=str(value), wraplength=700).grid(row=i, column=1, sticky="w", padx=5, pady=2)
            else:
                messagebox.showerror("Error", "Student not found!")
        else:
            messagebox.showwarning("Warning", "Please select a student!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentInfoApp(root)
    root.mainloop()
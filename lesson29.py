##lesson29

import sqlite3

# ============================================================
# إنشاء أو الاتصال بقاعدة البيانات SQLite
# إذا لم تكن قاعدة البيانات موجودة فسيتم إنشاؤها تلقائياً
# ============================================================
conn = sqlite3.connect("school_management.db")
cursor = conn.cursor()

# ============================================================
# إنشاء الجداول الخاصة بالمشروع (مشروع إدارة مدرسة)
# ============================================================

# جدول الطلاب
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- مفتاح أساسي
    name TEXT NOT NULL,                             -- اسم الطالب
    age INTEGER,                                    -- عمر الطالب
    grade TEXT                                      -- الصف الدراسي
)
""")

# جدول المعلمين
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- مفتاح أساسي
    name TEXT NOT NULL,                             -- اسم المعلم
    subject TEXT                                    -- المادة التي يدرسها
)
""")

# جدول المواد الدراسية
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- مفتاح أساسي
    name TEXT NOT NULL,                             -- اسم المادة
    teacher_id INTEGER,                             -- معرف المعلم
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
)
""")

# جدول الدرجات
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- مفتاح أساسي
    student_id INTEGER,                             -- معرف الطالب
    subject_id INTEGER,                             -- معرف المادة
    score REAL,                                     -- العلامة
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
)
""")

# ============================================================
# دوال التعامل مع قاعدة البيانات (CRUD)
# ============================================================

# ------------------------------------------------------------
# دالة إضافة طالب جديد
# ------------------------------------------------------------
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()

# ------------------------------------------------------------
# دالة عرض جميع الطلاب
# ------------------------------------------------------------
def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# ------------------------------------------------------------
# دالة تحديث بيانات طالب
# ------------------------------------------------------------
def update_student(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE student_id=?", (name, age, grade, student_id))
    conn.commit()

# ------------------------------------------------------------
# دالة حذف طالب
# ------------------------------------------------------------
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()

# ------------------------------------------------------------
# دالة إضافة معلم جديد
# ------------------------------------------------------------
def add_teacher(name, subject):
    cursor.execute("INSERT INTO teachers (name, subject) VALUES (?, ?)", (name, subject))
    conn.commit()

# ------------------------------------------------------------
# دالة إضافة مادة جديدة وربطها بالمعلم
# ------------------------------------------------------------
def add_subject(name, teacher_id):
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (name, teacher_id))
    conn.commit()

# ------------------------------------------------------------
# دالة إضافة درجة جديدة للطالب
# ------------------------------------------------------------
def add_grade(student_id, subject_id, score):
    cursor.execute("INSERT INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)", (student_id, subject_id, score))
    conn.commit()

# ------------------------------------------------------------
# دالة عرض جميع درجات طالب معين
# ------------------------------------------------------------
def get_student_grades(student_id):
    cursor.execute("""
        SELECT subjects.name, grades.score
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.subject_id
        WHERE grades.student_id=?
    """, (student_id,))
    return cursor.fetchall()

# ------------------------------------------------------------
# دالة البحث عن طالب بواسطة الاسم
# ------------------------------------------------------------
def search_student_by_name(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()

# ------------------------------------------------------------
# دالة عرض الطلاب مع درجاتهم بشكل شامل
# ------------------------------------------------------------
def get_students_with_grades():
    cursor.execute("""
        SELECT students.name, subjects.name, grades.score
        FROM grades
        JOIN students ON grades.student_id = students.student_id
        JOIN subjects ON grades.subject_id = subjects.subject_id
    """)
    return cursor.fetchall()

# ============================================================
# اختبارات عملية على الدوال (للتوضيح)
# ============================================================

# إضافة بيانات مبدئية
add_student("أحمد علي", 16, "العاشر")
add_student("سارة محمد", 15, "التاسع")
add_teacher("خالد يوسف", "الرياضيات")
add_teacher("منى حسن", "العلوم")
add_subject("الرياضيات", 1)
add_subject("العلوم", 2)
add_grade(1, 1, 89.5)
add_grade(1, 2, 95.0)
add_grade(2, 1, 75.0)
add_grade(2, 2, 80.0)

# طباعة جميع الطلاب
print("=== جميع الطلاب ===")
for student in get_all_students():
    print(student)

# طباعة درجات طالب معين
print("\n=== درجات الطالب أحمد ===")
for grade in get_student_grades(1):
    print(grade)

# البحث عن طالب بالاسم
print("\n=== البحث عن طالب اسمه سارة ===")
print(search_student_by_name("سارة"))

# عرض الطلاب مع درجاتهم
print("\n=== جميع الطلاب مع درجاتهم ===")
for row in get_students_with_grades():
    print(row)

# ============================================================
# إغلاق الاتصال بقاعدة البيانات
# ============================================================
conn.close()

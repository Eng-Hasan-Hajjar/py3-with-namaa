import arabic_reshaper
from bidi.algorithm import get_display

def ar(text):
    return get_display(arabic_reshaper.reshape(text))

print(ar("المشروبات المتوفرة:"))

coffees = {
    "coffee": 3.0,
    "milk": 3.0,
    "water": 1.0,
    "cola": 3.5,
    "latte": 4.0
}

for item in coffees:
    print(f"---> {item} ({coffees[item]}$) <---")

# طلب أسماء المشروبات
order_input = input(ar("أدخل المشروبات التي تريد شراءها: ")).casefold()
order_list = [item.strip() for item in order_input.split(",")]

# جمع الأسعار
total_price = 0
not_found = []
for item in order_list:
    if item in coffees:
        total_price += coffees[item]
    else:
        not_found.append(item)

# عرض النتائج
print(f"\n{ar(' المبلغ المطلوب دفعه')}: {total_price}$")

if not_found:
    print(ar("!المشروبات التالية غير موجودة:") + " " + ", ".join(not_found))

# طلب المبلغ المدفوع
payment_input = input(ar("أدخل المبلغ المدفوع: ")).replace("$", "")
try:
    payment = float(payment_input)
    if payment >= total_price:
        change = round(payment - total_price, 2)
        print(ar(" تم شراء الطلب بنجاح!"))
        if change > 0:
            print(f"{ar(' الباقي')}: {change}$")
    else:
        print(ar(" المبلغ غير كافٍ!"))
except:
    print(ar(" الرجاء إدخال مبلغ صحيح (رقم)"))
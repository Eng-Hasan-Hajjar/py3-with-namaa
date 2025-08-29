## lesson26

print("Nasir")


file=open("new_file.txt")

file=open("new_file.txt","rt")


"""
"r" - القراءة - القيمة الافتراضية. يفتح ملفا للقراءة، خطأ إذا كان الملف غير موجود.
"a" - إلحاق - يفتح ملفًا للإلحاق، وينشئ الملف إذا لم يكن موجودًا.
"w" - كتابة - يفتح ملفًا للكتابة، وينشئ الملف إذا لم يكن موجودًا.
"x" - إنشاء - إنشاء الملف المحدد، وإرجاع خطأ في حالة وجود الملف.


"""
file=open("new_file.txt","rt")
print(file.read())
file=open("C:\\Users\engya\Desktop\Duaa.txt","r")
print(file.read())

file=open("new_file.txt","rt")
print(file.read(20))

file=open("new_file.txt","rt")
print(file.readline())
print(file.readline())


file=open("new_file.txt","rt")
for line in file:
    print(line.strip())

file.close()    



import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except Exception as e:
    print(f"faild {e}")



file=open("new_file.txt","at")
file.write("this new txt")
file=open("new_file.txt","rt")
print(file.read())
file.close()   

print("\n")
file=open("new_file.txt","wt")
file.write("this new txt")
file=open("new_file.txt","rt")
print(file.read())
file.close()   


print("ex 7\n")

file=open("new_file2.txt","rt")
print(file.read())
file.close()   






print("ex 8\n")

import os
if os.path.exists("new_file13.txt"):
    x1="new_file13.txt"
    x2="new_file3.txt"

    os.rename(x1,x2)
if os.path.exists("new_file13.txt"): 
    os.remove("new_file3.txt")
if os.path.exists("jamal"): 
    os.rmdir("jamal")    



##json  ==== javaScript Object Notation

import json
x='{"name":"Lama","age":30,"city":"sedny"}'   
print(type(x)) 
u=json.loads(x)

print(type(u)) 
print(u["age"])



x={
    "name":"Lama",
   "age":30,
   "city":"sedny"
   }
u=json.dumps(x)
print(type(u))

newlist=[12,45,"fdfd"]
u=json.dumps(newlist)
print(type(u),u)







import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x,indent=4,sort_keys=True))

##lesson27
# تحويل أنواع البيانات إلى JSON في بايثون
import json
# كتابة أنواع البيانات في بايثون
data1 = {"name": "Ali", "age": 20}   # Dictionary #object
data2 = [1, 2, 3, 4]                # List #array
data3 = ("apple", "banana")         # Tuple #array

# تحويل للـ JSON
print("data1 كـ JSON:",(type( json.dumps(data1)))) #object
print("data2 كـ JSON:", (type(json.dumps(data2))))# array
print("data3 كـ JSON:", (type(json.dumps(data3))))# array
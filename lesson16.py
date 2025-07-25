##lesson16
## set 


##ex1
Watheq_set={"اللغة العربية","الانكليزية","الرياضيات"}
print(Watheq_set)

##ex2
this_set=set(("php","c#","Jvascipt","Matlap","php"))
print(this_set)
print(type(this_set))

##ex3
this_set=set(("php","c#","Jvascipt","Matlap","php",True,1,2,33,False,0,10))
print(this_set)
print(type(this_set))


##ex4
this_set=set(("php","c#","Jvascipt","Matlap","php",True,1,2,33,False,0,10))

print(len(this_set))
print(this_set)
print(len(this_set))
print(type(this_set))
##ex5
set1={1,88,77,90}
set2={True,False}
set3={"H","F"}

print(set1)
print(set2)
print(set3)


"""

مجموعات بايثون (المصفوفات)(تذكرة):
 هناك أربعة أنواع من بيانات المجموعة في لغة برمجة بايثون:
 	القائمة عبارة عن مجموعة مرتبة وقابلة للتغيير. يسمح بأعضاء مكررة.
 	Tuple عبارة عن مجموعة مرتبة وغير قابلة للتغيير. يسمح بأعضاء مكررة.
 	المجموعة عبارة عن مجموعة غير مرتبة وغير قابلة للتغيير* وغير مفهرسة. لا يوجد أعضاء مكررة.
 	القاموس عبارة عن مجموعة مرتبة وقابلة للتغيير. لا يوجد أعضاء مكررة.
*عناصر المجموعة غير قابلة للتغيير، ولكن يمكنك إزالة العناصر وإضافة عناصر جديدة.


"""
##ex6
this_set=set(("php","c#","Jvascipt","Matlap"))
for x in this_set:
    print(x)


print(this_set)
print(type(this_set))



##ex7
this_set=set(("php","c#","Jvascipt","Matlap"))
print("php" in this_set)
for x in this_set:
    if("php" == x):
        print("php exist")
    print(x)


print(this_set)
print(type(this_set))



##ex8
this_set=set(("php","c#","Jvascipt","Matlap"))

if("php" in this_set):
    print("php exist")



##ex9
this_set=set(("php","c#","Jvascipt","Matlap"))


this_set.add("C++")
print(this_set)

##ex10
this_set=set(("php","c#","Jvascipt","Matlap"))
this_set2={"python","Dart","Css","html","react"}

this_set.update(this_set2)
print(this_set)


##ex11
this_set=set(("php","c#","Jvascipt","Matlap"))
this_list=["python","Dart","Css","html","react"]

this_set.update(this_list)
print(this_set)

##ex12
this_set=set(("php","c#","Jvascipt","Matlap"))


this_set.remove("c#")

if "F#" in this_set:
    this_set.remove("F#")

print(this_set)



##ex13
this_set=set(("php","c#","Jvascipt","Matlap"))


this_set.discard("c#")


this_set.discard("F#")

print(this_set)



##ex14
this_set=set(("php","c#","Jvascipt","Matlap"))
this_set.discard("c#")
this_set.discard("F#")
print(this_set)


##ex15
this_set=set(("php","c#","Jvascipt","Matlap"))
this_set.pop()

print(this_set)



##ex16
this_set=set(("php","c#","Jvascipt","Matlap"))
uu=this_set.pop()
print(uu)
print(this_set)

##ex17
this_set=set(("php","c#","Jvascipt","Matlap"))
##del this_set
print(this_set)

##ex18
this_set=set(("php","c#","Jvascipt","Matlap"))
this_set.clear()
print(this_set)

##ex19\
this_set=set(("php","c#","Jvascipt","Matlap"))
for x in this_set:
    pass
print(this_set)


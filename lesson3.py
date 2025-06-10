#lesson3


#فك المجموعة 
#ex1
laptops_list=["Asus","HP","lenevo"]
laptop1,laptop2,laptop3=laptops_list
print(laptop1)
print(laptop2)
print(laptop3)


#ex2
laptops_list=["Asus","HP","lenevo"]
#laptops_list=["Asus","HP","lenevo","del"]
laptop1,laptop2,laptop3=laptops_list
print(laptop1)
print(laptop2)
print(laptop3)


#ex3
print(laptops_list)
print(type(laptops_list))
print(laptop1,laptop2,laptop3)

#ex4

print(laptop1+laptop2+laptop3)

print(laptop1  +" " + laptop2  +" " + laptop3)


##ex5
num1=10
num2=20
print(num1+num2)


#ex6


num1=str(10)
num2=int(20)

#error
#print(num1+num2)

print(num1,num2)

##المتغيرات العامة 
#ex7
name="Adel"
name2="Amir"
def get_name():
    print("the name is :", name)
    print("the name2 is :", name2)


get_name()

##ex8

name="ilyas"
name2="Shereen"
def get_name():
    name="nasir"
    print("the name is :", name)
    print("the name2 is :", name2)


get_name()


##ex9

name="ilyas"
name2="Shereen"
def get_name():
    name="nasir"
    print("the name is :", name)
    print("the name2 is :", name2)


get_name()
print("the name is :", name)

##ex10

name="ilyas"
name2="Shereen"
def get_name():
    name="nasir"
    print("the name is :", name)
    print("the name2 is :", name2)


print("the name is :", name)
get_name()




##ex11

name="ilyas"
name2="Shereen"
def get_name():
    global name
    name="nasir"
    print("the name is :", name)
    print("the name2 is :", name2)



get_name()
print("the name is :", name)



##ex12

name="ilyas"
name2="Shereen"
def get_name():
    global name
    name="nasir"
    print("the name is :", name)
    print("the name2 is :", name2)


print("the name is :", name)
get_name()
print("the name is :", name)


##أنواع البيانات
# str-int-float-complex-list-tuple-range-dict-set-bool------NonType
#ex13
price=20.3
print(price,type(price))

#ex14
#complex
## الأعداد العقدية
x=5+3j
print(x,type(x))
x2=5+0j
x4=5

x3=2j

#ex15
#list
x=[5,50,81]
print(x,type(x))


#ex16
#tuple
x=(5,50,81)
print(x,type(x))

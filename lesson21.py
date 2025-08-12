##lesson21
##ex1
##for
exam_list=["shereen","ilyas","Adel","asmaa","Duaa","Hamza","Lina"]
for c in exam_list:
    print(c)

##for

for c in "EXAM":
    print(c)




##ex2
##break
exam_list=["shereen","ilyas","Adel","asmaa","Duaa","Hamza","Hamza_shami","Lina"]
for c in exam_list:
    if c == "Hamza_shami":
        break
    print(c)



##ex3
##conti
exam_list=["shereen","ilyas","Adel","asmaa","Duaa","Hamza","Hamza_shami","Lina"]
for c in exam_list:
    if c == "Hamza_shami":
        continue
    print(c)



##ex4
##range
for c in range(9):
    print(c)
    

##ex5
##range
for c in range(2,9):
    print(c)
    



##ex6
##range
for c in range(1,9,2):
    print(c)

##ex7
for c in range(1,9,2):
    print(c)   
else:
    print("finally loop for")    

for c in range(1,9):
    if c == 5:
        break
    else:
        pass
    print(c)   
else:
    print("finally loop for")    



for c in range(1,9):
    if c == 5:
        continue
    print(c)   
else:
    print("Exx finally loop for")    

##ex8
list1=[1,3,5]
list2=[2,4,6]
for x in list1:
    for y in list2:
        print(x,y)

for x in list1:
    for y in list2:
        pass



list1=set(("1","3","5"))
list2=set(("2","4","6"))
for x in list1:
    for y in list2:
        print(x,y)



##ex9
##functions
def questions():
    print("6. What is lambda in Python? Why is it used?")
    print("5. What is lambda in Python? Why is it used?")

questions()


def questions_1(num):
    print(num)
    print("6. What is lambda in Python? Why is it used?")
    print("5. What is lambda in Python? Why is it used?")

questions_1(5)
questions_1(4)

def identity(fname,lname,age):
    print(fname + " "+ lname + " " + age)


identity("Lina","Ramadan","23")


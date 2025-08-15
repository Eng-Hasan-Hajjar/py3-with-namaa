#lesson22
##ex1
def fun_student(*kids):
    print("this second student:" + kids[1])


fun_student("Ahmad","Hyma","Mousa")    



##ex2
def fun_student(kid1,kid2,kid3):
    print("this second student:" + kid3)


fun_student("Ahmad","Hyma","Mousa")  


##ex3
def fun_student(kid1,kid2,kid3):
    print("this second student:" + kid3)


fun_student(kid2="Ahmad",kid1="Hyma",kid3="Mousa") 



##ex4
def fun_student(**kids):
    print("this second student:" + kids["kid1"])


fun_student(kid2="Ahmad",kid1="Hyma",kid3="Mousa") 



##ex5
def fun_nationality(country="Syria"):
    print("this second student:" + country)


fun_nationality("Turky") 
fun_nationality("Germany") 
fun_nationality() 

##ex6
def fun_nationality(country):
    for x in country:
        print(x)


fun_nationality(["Turky","Germany","USA","Egypt"]) 
 

##ex7
def fun_nationality(country):
    return country + "  nice country"


dddd=fun_nationality("Turky") 
 
print(dddd)

##ex8
def fun_nationality(v):
    return 5*v


dddd=fun_nationality(2) 
 
print(dddd)

dddd=fun_nationality(3) 
 
print(dddd)


dddd=fun_nationality(4) 
 
print(dddd)



##ex9
def fun_nationality(v):
    pass


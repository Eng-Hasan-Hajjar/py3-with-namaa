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



##ex10
def fun_1(v,/):
    print(v)
   
fun_1(6)
#fun_1(v=7)

def fun_1(v):
    print(v)
   
fun_1(6)
fun_1(v=7)
##ex11
def fun_1(*,v):
    print(v)
#fun_1(6)
fun_1(v=7)
##ex12
def fun_1(name,laname,/,*,family,age):
    print(name+laname+family+age)
fun_1("Salwa","Jamal",family="555",age="33")   
###ex13
##n!=n * n-1  * n-2 * .....  * 3 *2 *1
### 0!=1                       1!=1             2!= 2 * 1          3!=3 * 2 *1 =6       4!=4*3*2*1=24 
## 9! = 9*8*7*6*5*4*3*2*1
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
##ex14
#lambda function
## lambda arguments:expression
## أضف 16 الى الوسيط جي وقم بارجاع النتيجة في المتغير واي
y=lambda g:g+16
print(y(2))
##ex15
#lambda function
## lambda arguments:expression
mul=lambda g,k:g * k
print(mul(2,3))
sum=lambda g,k:g + k
print(sum(2,3))
sub=lambda g,k,l:g - k - l
print(sub(2,3,1))

##ex16
def fun_2(n):
    return lambda x:x*n

y=fun_2(3)
print(y(4))

##arrays
##numpy

#lesson 10

##ex1
#partition()
text="I love Python"
j=text.partition("love")
print(j)

##ex2
#partition()
text="I drink coffee every morning"
j=text.partition("love")
print(j)

##ex3
#partition()
text="I drink coffee every morning"
j=text.partition("coffee")
print(j)


## rpartition()

##ex4
##splitlines()
text="I am stunding a computer engineering in university, I will finish school next year"
h=text.splitlines()
print(text)
print(h)


##ex5
##splitlines()
text="I am stunding a computer engineering in university,\n I will finish school next year"
h=text.splitlines()
print(text)
print(h)

##ex6
##splitlines()
text="I am stunding \n a computer engineering in university,\n I will finish school next year"
h=text.splitlines()
print(text)
print(h)

##Boolean
##ex7
print(5>20)
print(55==66)
print(8>3)

##ex8
price1=200
price2=350
if price1 > price2:
    print("go to mall 2")
else:
    print("go to mall 1")

##ex9
x="hamza, tbab"
if x=="tbab":
    print("true")
else:
    print("false")


##ex10
x="hamza, tbab"
if "tbab" in x :
    print("true")
else:
    print("false")


##ex11
var="I am a good python programmer"
var2="Python is the easy language to learn"
text=var.partition("python")
text1=var2.rpartition("language")
text2=var.partition(" ")
text3=var2.rpartition(" ")
text4=var.partition("Python")
text44=var.rpartition("Python")
print(text)
print(text1)
print(text2)
print(text3)
print(text4)
print(text44)


##ex12
print(bool("developer python"))
print(bool(" "))
print(bool(""))
print(bool(55))
print(bool(0))
print(bool(22.5))
print(bool(0.0))
gh="casting to boolean"
mark=99
print(bool(gh))
print(bool(mark))


subjects=["math","programming","physics"]

print(bool(subjects))

subjects=[]

print(bool(subjects))

##ex13
def hamzaFunc():
    return True


result=hamzaFunc()
print(result)

##ex14
def hamzaFunc2():
    x="hamza, tbab"
    if "tbab" in x :
        print(" 2222 true")
    else:
        print(" 2222 false")

hamzaFunc2()



##ex15
#operators
print(5+41)
print(5-41)
print(5*41)
print(5/41)
print(5%41)
print(5**2)
print(5//41)
print(5/6)



x=6
x+=3   ## x=x+3
print(x)

x=6
x-=3   ## x=x-3
print(x)


x=6
x*=3   ## x=x*3
print(x)




x=6
x/=3   ## x=x/3
print(x)


x=6
x%=3   ## x=x%3
print(x)



x=6
x%=4   ## x=x%4
print(x)



#lesson25
##scope


def myfunc():
    x=300
    print(x)

myfunc()    





def myfunc():
    x=300
    def inner_func():
        print(x)

    inner_func()

  

myfunc()   



x=300
def myfunc():
   
    print(x)

myfunc()   
print(x)




x=300
def myfunc():
    x=200
    print(x)

myfunc()   
print(x)




x=300
def myfunc():
    global x
    x=200
    print(x)

myfunc()   
print(x)





def myfunc():
    x="Ahmad"
    def inner_func():
        nonlocal x
        x="salwa"

    inner_func()

    return x
  
print(myfunc())
   



###modules

import module1
module1.get_marks(" Hazem")

hadi=module1.subjects["label"]
print(hadi)





import module1 as mo
mo.get_marks(" Hazem")

hadi=mo.subjects["label"]
print(hadi)



import platform
x=platform.system()
print(x)

z=platform.python_version()
print(z)
y=dir(platform)
print(y)
y=dir(module1)
print(y)


from module1 import subjects
print(subjects["label"])






############
n=max(4,9,24)
print(n)


n=max(44,9,24)
print(n)



n=min(44,9,24)
print(n)


h=abs(-2.5)
print(h)

k=pow(2,3)
print(k)

import math
j=math.sqrt(64)
print(j)
l=dir(math)
print(l)

kk=math.floor(1.4)
print(kk)


kk=math.ceil(1.4)
print(kk)

kk=math.pi
print(kk)
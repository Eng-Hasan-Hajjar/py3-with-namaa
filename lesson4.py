#lesson4

#ex1
#list
x=list([5,50,81])
print(x,type(x))


#ex2
#tuple
x=tuple((5,50,81))
print(x,type(x))


#ex3
#range
x=range(6)
print(x,type(x))



#ex4
#range
x=range(10)
print(x,type(x))


#ex5
#dict
x=dict(name="nasir",age=25)   
print(x,type(x))



#ex6
#set
x=set((1,5,8,3))   
print(x,type(x))

#ex7
#set
y={"1", "2", "6"}
print(y,type(y))


#ex8
#set
y={1,5,8,3}
print(y,type(y))


#ex9
##int
x=23
x2=23565454211
x3=-23354
print(x,x2,x3,type(x),type(x2),type(x3))


#ex10
##float
x=23.23
x2=23565454211.23
x3=-23354.56
print(x,x2,x3,type(x),type(x2),type(x3))
x4=66e3
print(x4,type(x4))

x5=-99.5e5
print(x5,type(x5))

x6=-99.57e5
print(x6,type(x6))

x7=-99.57364e5
print(x7,type(x7))

x8=-99.573646e5
print(x8,type(x8))


#ex11
##casting
x=1
y=6.4
z=10j
t=float(x)
h=int(y)
k=complex(x)

print(t,h,k)

#ex12
#hamza diri
x=1
y=6.9
z=20j
t=float(x)
h=int(y)
k=complex(x)
print(t,h,k)
print(type(t),type(h),type(k))

##ex13
#random
import random
print(random.randrange(1,10))

##ex14
g=int(2)
l=int(3.6)
j=int("9")
#r=int("9.6")
print(g,l,j)


g=float(2)
l=float(3.6)
j=float("9")
r=float("9.6")
print(g,l,j,r)

g=str(2)
l=str(3.6)
j=str("9")
r=str("9.6")
print(type(g),g,l,j,r)
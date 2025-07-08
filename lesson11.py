##lesson
##ex1
x=6
x**=2   ## x=x**2
print(x)


x=6
y=2

x**=y   ## x=x**y
print(x)

x=6
y=2
z=0

z=x**y
print(z)




##ex2
x=2
## 0010
## tkinter  -- pygame
y=3
## 0011
z=4
## 0100
x&=1  ## x=x&1
print(x)
y|=1
print(y)

## xor
z^=3
print(z)


##not 
##~     ~


##معاملات المقارنة
## ==
## != 
## >
## <
## >=
## <=

## معاملات منطقية
## شرط and شرط
##  شرط or شرط
## not( شرط and شرط)




a = 5
b = 3

print("a == b:", a == b, "| a != b:",
       a != b, "| a > b:", a > b,
         "| a < b:", a < b, "| a >= b:",
           a >= b, "| a <= b:", a <= b)


x=2
y= "Hello"
c=2
g=5
print(x==c)
print(x==y) 
print(x!=y)
print(g>x)
print(c<g)


x=10
y=20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)




#exm1
x = 10
y = 10
print(x == y) # Output: True

a = "hello"
b = "world"
print(a == b) # Output: False

#exm2
x = 10
y = 5
print(x != y) # Output: True

a = "apple"
b = "apple"
print(a != b) # Output: False
#exm3

x = 20
y = 15
print(x > y) # الناتج: True (صحيح)

a = 5
b = 10
print(a > b) # الناتج: False (خطأ)
#exm4

x = 7
y = 12
print(x < y) # Output: True

a = 15
b = 10
print(a < b) # Output: False
#exm5
x = 10
y = 10
print(x >= y) # Output: True

a = 25
b = 20
print(a >= b) # Output: True

c = 5
d = 8
print(c >= d) # Output: False
#exm6
x = 5
y = 5
print(x <= y) # الناتج: True (صحيح)

a = 10
b = 15
print(a <= b) # الناتج: True (صحيح)

c = 20
d = 18
print(c <= d) # الناتج: False (خطأ)



student_score = 75
passing_score = 60

if student_score >= passing_score:
    print("The student passed the exam.")
else:
    print("The student failed the exam.")



x=5
if x>=7:
    print(True)
else:
    print(False)  


age=int(input( " what s your age ? \n"))
if age>=15:
    print("GOOD: you can use the app ")
else:
    print("sorry : you can't use it !") 



age=int(input( " what s your age ? \n"))
if age>=15 and age<=60:
    print("GOOD: you can use the app ")
else:
    print("sorry : you can't use it !") 

a="b"
x="g"

print(a==x)

x=5
print(x > 2 & x < 10)   ###true
print(x > 2 & x > 10)   ###false


"""



from colorama import init, Fore
x = input("write your title : ")
print("coloring title to blue tab 1")
Choose = input("Choose an option from above : ")

if Choose == "1":
    print(f"{Fore.BLUE} {x.upper()}")
else:
    print("invalid")
input("to exit press enter")

"""
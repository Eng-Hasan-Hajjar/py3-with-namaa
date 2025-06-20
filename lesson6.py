##lesson6
##Lina homework

print("lina")
num_int=125
num_flo=1.26
num_new= num_int + num_flo 
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("value of num_new",num_new)
print("datatype of num_new",type(num_new))
# Orijinal Text
text = """Hello, my name is Lina and I am currently studying Computer Engineering. 
Over time, I have developed a growing interest in artificial intelligence and data science. T
his curiosity led me to start learning the Python programming language, which is widely used in both fields. 
My goal is to improve my skills in AI and data analysis by building a strong foundation in Python. 
I believe that with continuous learning and practice, I will be able to contribute to innovative projects in the future. 
I'm excited about the journey ahead and passionate about exploring the endless possibilities in technology.
."""

original_text = text

upper_text = text.upper()
print("Uppercase:", upper_text)
lower_text = text.lower()
print("Lowercase:", lower_text)
print("Original:", original_text)

a = 125
b = "lina"
c = 1.25

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>


##Sheeren homework
num1= 55
num2="66"
num3="87.5"
num4= 44.4
num5= 587e4
num6= 4
num7= num1+num6
var = "Shereen"
print(float(num2))
print(int(num4))
print(complex(num6))
print(str(num1))
print(float(num7))
#converting string into list
print(list(var))
#converting string inti tuple
print(tuple(var))
#print(int(var)) #there is no converting from string text into integer 
#repr() function is used to convert an object into a string
employee = {"name": "Alice", "age": 25, "job":"programmer"}
##employee_1=repr(employee)
##print(employee_1)



string = "Python is a high language"
uppercase_string = string.upper()
print(uppercase_string) 

string1 = "Python is easy to learn"
lowercase_string = string1.lower()
print(lowercase_string) 

string2="python is open source"
capitalize_string=string2.capitalize()
print(capitalize_string)

string3="The syntax is known for its simplicity and readability"
title_string=string3.title()
print(title_string)

string4="Easy element access using indexing"
swapcase_string=string4.swapcase()
print(swapcase_string)






##Ilays homework
x=238642
print(float(x))

c=238642.0
print(int(c))


name=("hy me name ilyas")

z=name.upper()
print(z)

name1=("hy me name ilyas")

m=name1.lower()
print(m)

name2=("hy me name ilyas")

n=name2.isupper()
print(n)

name3=("hy me name ilyas")

l=name3.islower()
print(l)


names="""muhammed
cnsnmdc
dfjhlkfj
fdlkjvd;kljd
dkjv;lkjdcv
d;ofj;dlkf
dlkjf;lkd
dljflod
dkjfdlkjd
dkjhflkjd
dkjfclkjd
dkkcojdf
hclkjldk"""

print(names)


##duaa

c="Students Names, Degrees ,Classes"
c_2=c.upper()
print(c_2)
c="Students Names, Degrees ,Classes"
c_2=c.upper()
print(c_2[2:4])
## STUDENTS NAMES, DEGREES ,CLASSES



## nasir
num94="stGdenTs,naMes,degRRees,claSses"
print(num94.upper()[12:25])
print(num94.lower()[-29:-7])
num95="hi My nAme is ahMet"
print(num95.upper()[15:19])
print(num95.lower()[-19:-15])


###adil

my_jop = "im work in wholsales company"

upper_case = my_jop.upper() ##بيحول الجملة إلى أحرف كبيرة
lower_case = my_jop.lower() ##بيحول الجملة إلى أحرف صغيرة
title_case = my_jop.title() ##بيحول الجملة إلى أحرف كبيرة في بداية كل كلمة
print(f"Upper Case: {upper_case [0:2]}" )
print(f"Lower Case: {lower_case [0:7]}")
print(f"Title Case: {title_case [0:19]}")
 ## عنوان الجمل وشو معانيها 
def count_words(text):  
    words = text.split() 
    return len(words)

## hamza iysaw
name="hamza alabdullah aljfil"
x=name.replace("hamza","HAMZA")
print(x,type(x))

##hamza 

x = "hamza, tbab"
print(x.split(',')[0].strip().lower() + ", " + x.split(',')[1].strip().upper())



#حمزة العيساوي
name=("my name is hamza")
name1=name.upper()[2:7]
print("my "+name1+" is hamza")

name=("my NAME is hamza")
name1=name.lower()[2:7]
print("my "+name1+" is hamza")




##شرين
string5="Python is a popular programming language"
print(string5.upper()[8:20] + str(string5))
print(string5.lower()[5:11] + str(string5))
n=4
string5=string5.replace(string5[n],string5[n].upper())
print("The string after uppercasing character : " + str(string5))

##محمد عبد الرحمن
a = 9.8
b = int(a)
print(b)

age = 18
text = "my age is" + str(age)
print(text)

print(bool(0))
print(bool(1))
print(bool("hello"))

text = "HeLLo WoRLd"
print(text.lower()) 

text = "HelLo World"
print(text.upper())

text = "Hello WORLD"
print(text.swapcase())

text = "hello WoRld"
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("o", "5"))
print(text[3:7])

##
zeno=("hi mi NAME ilyas")

print(zeno.upper()[:5],zeno.lower()[6:])

##ex1
# Define a string variable containing a sentence
sentence = "I love programming in Python"

# Split the sentence into words
words = sentence.split()
print(words)
# Convert the second word to uppercase (index 1)
words[1] = words[1].upper()

# Join the words back into a sentence
new_sentence = " * ".join(words)

# Print the result
print(new_sentence)


##ex2
text = "hello world"
print(text.replace("w","W"))

##ex3
print(text.split())
##ex4
text = "hello* wo*rld"
print(text.split("*"))

##ex5
d="has"
c="played"
print(d+c)
##ex6
d="has "
c="played"
print(d+c)

##ex7
d="has"
c="played"
print(d+" "+c)

##ex8
price=30
product="this product cost : "
print(str(price)+" " +product)

##ex9
price=30
price=price+20
product="this product cost : {} "
print(product.format(price))

##ex10
price=30
price=price+20
product="this product cost :  "
print(product.format(price))

##ex11

quantity=5
item_number=1024
item_name="sugar"
pice=2.5
my_order="you take :quantity {} of  item_name {} that have the number {} and total price {} "
print(my_order.format(quantity,item_name,item_number,pice))




##ex12

quantity=5
item_number=1024
item_name="sugar"
pice=2.5
my_order="you take :quantity {2} of  item_name {3} that have the number {0} and total price {1} "
print(my_order.format(item_number,pice,quantity,item_name))

##ex13
txt="we are one team \"py3\""
print(txt)


###lesson5
###stings
## السلاسل
## ex1
print("strings")

print('strings')

name="mohammad"
print(name)


##ex2
students_names="Adel2 "\
"shereen2 "\
"Asmaa2 "
"Duaa2 "
"Hamza2"
"Ilyas2"
"lina2"
"maram2"
"mohammad2"
"hamza isay2" 
print(students_names)


##ex3
students_names="""Adel 
shereen 
Asmaa 
Duaa 
Hamza
Ilyas
lina
maram 
mohammad 
hamza isay """
print(students_names)


#ex4
shereen="I want to be one day a pro developer"
print(shereen[0])
print(shereen[1])
print(shereen[2])
print(shereen[3])

#ex5
for x in shereen:
    print(x)


##ex6
print(len(shereen))



##ex7
ilys="هاد هو المتغير"
print(len(ilys))

##ex8
## in
subject="elect 2 ,math"
print("math" in subject)
print("nasir" in subject)

#ex9
## not in 

subject="elect 2 ,math"
print("math" not in subject)
print("nasir" not in subject)


#ex10
## for + not in

shereen="I want to be one day a pro developer"
x="program"
if x not in shereen:
    print("yes 'program' is true")


##ex11
## اطبع الاحرف من الموضع الثاني الى الموضع الخامس 
shereen="I want to be one day a pro developer"
print(shereen[2:5])

##ex12
shereen="I want to be one day a pro developer"
print(shereen[0:5])
print(shereen[:5])
print(shereen[2:])
##ex13
print(shereen[-2:-1])
print(shereen[-6:-1])
print(shereen[-6:])


##ex14
##upper()
records="students names, degrees, classes"
records_UpperCase= records.upper()
print(records)
print(records_UpperCase)

##ex15
records="Students Names, Degrees, Classes"
records_UpperCase= records.upper()
print(records)
print(records_UpperCase)


##ex16
records="Students Names, Degrees, Classes"
records_UpperCase= records.lower()
print(records)
print(records_UpperCase)

##ex17
records="     3232Students Names, Degrees, Classes    "
records.strip()
print(records.strip())


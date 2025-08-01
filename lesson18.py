##lesson18
import arabic_reshaper
from bidi.algorithm import get_display

##ex1
iden={
    "name":"adel",
    "age":"22",
    "natialati":"Syria"
}
print(iden)


##ex2
university={
    "name":"Gazi entab",
    "rank":"6",
    "first_year":1988,
    "number_faculty":20
}
print(university)
print(university["name"])

###ex3
university={
    "name":"Gazi entab",
    "rank":"6",
    "first_year":1988,
    "number_faculty":20,
     "number_faculty":30
}
print(university)

###ex4
university={
    "name":"Gazi entab",
    "rank":"6",
    "first_year":1988,
    "number_faculty":20,
     "number_faculty":30
}
##polymorohism
##تعدد الأشكال
print(len(university))

###ex5
university={
    "name":"Gazi entab",
    "rank":"6",
    "first_year":1988,
    "number_faculty":20,
   "الأقسام":["كلية التربية" ,"كلية الرياضة" ,"كلية العلوم الاسلامية"]
}
reshaped_text = arabic_reshaper.reshape(university["الأقسام"][0])
reshaped_text2 = arabic_reshaper.reshape(university["الأقسام"][1])
print(get_display(reshaped_text))
print(get_display(reshaped_text2))
##ex6
university={
    "name":"Gazi entab",
    "rank":"6",
    "first_year":1988,
    "number_faculty":20
}
print(type(university))

##ex7
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)

print(university)
print(type(university))

##ex8
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)
x=university.keys()
print(x)
print(university)
print(type(university))


##ex9
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)
x=university.keys()
print(x)
university["gloabal_rank"]=2100
print(x)


##ex10
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)
x=university.values()
print(x)
university["gloabal_rank"]=2100
print(x)



##ex11
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)
x=university.items()
print(x)
university["gloabal_rank"]=2100
print(x)


##ex12
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)

if "global_rank" in university:
    print("yes ")

if "rank" in university:
    print("yes ")    

university["rank"]=7
print(university)

university.update({"rank":8})
print(university)

university.pop("rank")
print(university)

university.popitem()
print(university)


del university["name"]
print(university)

##del university
university.clear()
print(university)




##ex13
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20)


for y in university:
    print(y)

for y in university:
    print(university[y]) 


for y in university.values():
    print(y) 



for y in university.keys():
    print(y)          

for y in university.items():
    print(y)


university2=university.copy()
print(university2)


university2=dict(university)
print(university2)


university["shahadah_thana"]=True
print(university)



##ex14
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20,
    faculty1={
         "name":"math",
          "first_year":1990,
    },
    faculty2={
         "name":"phsics",
          "first_year":1990,
    },
    faculty3={
         "name":"Dentetals",
          "first_year":1990,
    }
    
    )

print(university)



##ex15
faculty1={
         "name":"math",
          "first_year":1990,
    }
faculty2={
         "name":"phsics",
          "first_year":1990,
    }
faculty3={
         "name":"Dentetals",
          "first_year":1990,
    }
university=dict( 
    name="Gazi entab",
    rank="6",
    first_year=1988,
    number_faculty=20,
    faculty11=faculty1,
    faculty12=faculty2,
    faculty13=faculty3
    
    )

print(university)



##ex16
print(university["faculty11"])
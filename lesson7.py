#lesson 7
##ex1
##capitalize
x="mohammad ilyas"
print(x.capitalize())

#ex2
x="mohammad ilyas STUDENT"
b=x.capitalize()
print(b)


#ex3
##casefold()
adel="trade With shop BABE"
string_adel=adel.casefold()
print(string_adel)


#ex4
##center
# 
text="apple"
g_center=text.center(20)
print(g_center)


#ex5
##center
# 
text="apple orange"
g_center=text.center(20)
print(g_center)


#ex6
##center
# 
text="apple orange"
g_center=text.center(10)
print(g_center)


#ex7
##center
# 
text="apple orange"
g_center=text.center(20,"*")
print(g_center)




#ex8
##center
# 
text="apple orange"
g_center=text.center(40,"*")
print(g_center)




#ex9
##count
# 
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_count=text.count("apple")
print(g_count)



#ex10
##count 
# 
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_count=text.count("apple",1,25)
print(g_count)

#ex11
##count 
# 
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_count=text.count("fruits")
print(g_count)

#ex12
##count 
# 
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_count=text.count("ap ple")
print(g_count)


##ex13
x="ILYAS"
print(x.lower())


c="ÇIÇEK"
print(c.casefold())




text = "Straße,  groß"

print(text.casefold())
print(text.lower())


text = "نتعلم لغة بايثون"
print(text)
print(text.casefold())
print(text.lower())


##ex14
##endwith()
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange."
g_endwith=text.endswith(".")
print(g_endwith)

##ex15
##endwith()
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_endwith=text.endswith(" ")
print(g_endwith)

##ex16
##endwith()
text="1 apple orange 2 apple orange 3 apple orange 4 apple orange "
g_endwith=text.endswith(".",1,25)
print(text[25],g_endwith)



##ex17
##find()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_find=text.find(".")
print(text[25],g_find)


##ex18
##find()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_find=text.find("apple")
print(text[25],g_find)



##ex19
##find()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_find=text.find("fruit")
print(text[25],g_find)


##ex20
##find()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_find=text.find("apple",22,44)
print(text[22],text[44],g_find)


##ex21
##index()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_index=text.index("apple")
print(text[22],text[44],g_index)


##ex22
##index()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
g_index=text.index("apple",22,44)
print(text[22],text[44],g_index)


##ex23
##index()
text="1 apple orange 2 apple. orange 3 apple orange 4 apple orange "
#g_index=text.index("fruit")
#print(text[22],text[44],g_index)


##ex24
##isdigit()
text="123456789"
g=text.isdigit()
print("is",g)
text="123456gfdg789"
g=text.isdigit()
print("is",g)

##ex25
##isalpha()
text="123456789"
g=text.isalpha()
print("is",g)


text="123gfjghg456789"
g=text.isalpha()
print("is",g)

text="hasad"
g=text.isalpha()
print("is",g)

##ex26
##isalnum()
text="12345gfdgfdyhh6789"
g=text.isalnum()
print("is",g)


text="132456"
g=text.isalnum()
print("is",g)

text="**"
g=text.isalnum()
print("is",g)

print("muhamme\"d")



print("muhammed\t atrash")


print("ilyas\natrash")


suad="muhammed \
muhammed"

print(suad)

name5="muhammed \\ muhammed"

print(name5)



name6="muhammed \r muhammed ilyas"

print(name6)



name7="muhammed\b muhammed ilyas"

print(name7)


name8="muhammed \a muhammed ilyas"

print(name8)


name9="muhammed \f muhammed ilyas"

print(name9)


name10="muhammed \v muhammed ilyas"

print(name10)


name11="muhammed \000 muhammed ilyas"

print(name11)

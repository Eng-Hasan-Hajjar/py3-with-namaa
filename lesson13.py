##lesson13
##ex1
list_laptops=["Hp","Asus","Dell"]

for elem in list_laptops:
    print(elem)

print(list_laptops)


##ex2
list_laptops=["Hp","Asus","Dell"]

for i in range(len(list_laptops)):
    print(list_laptops[i])

print(list_laptops)




##ex3
list_laptops=["Hp","Asus","Dell"]
i=0
while(i<len(list_laptops)):
    print(list_laptops[i])
    i+=1

print(list_laptops)


##ex4
list_laptops=["Hp","Asus","Dell"]
[print(elem) for elem in list_laptops]
print(list_laptops)

##ex5
list_laptops=["Hp","Asus","Dell"]
new_list=[]
for elem in list_laptops:
    if "l" in elem:
        new_list.append(elem)

print(new_list)
print(list_laptops)




##ex6
list_laptops=["Hp","Asus","Dell","MAc"]
new_list=[]
for elem in list_laptops:
    if "A" in elem:
        new_list.append(elem)

print(new_list)
print(list_laptops)

##ex7

##short hand
## newlist = [expression for item in iterable if condition == True]


list_laptops=["Hp","Asus","Dell","MAc"]
new_list=[elem for elem in list_laptops if "A" in elem]

print(new_list)
print(list_laptops)



##ex8
list_laptops=["Hp","Asus","Dell","MAc"]
[new_list.append(elem) for elem in list_laptops if "A" in elem]

print(new_list)
print(list_laptops)


##ex9

##short hand
## newlist = [expression for item in iterable if condition != True]


list_laptops=["Hp","Asus","Dell","MAc"]
new_list=[elem for elem in list_laptops if "MA" not in elem]

print(new_list)
print(list_laptops)


##ex10
new_list=[h for h in range(10)]
print(new_list)

##ex11
new_list=[h for h in range(10) if h < 5]
print(new_list)


##ex12
microsoft_office=["Excel","Word","Powerpoint","Access"]
new_list=[h.upper() for h in microsoft_office ]
print(new_list)


##ex13
microsoft_office=["Excel","Word","Powerpoint","Access"]
new_list=["Shereen Watheq Amir Nasir" for h in microsoft_office ]
print(new_list)



##ex14
microsoft_office=["Excel","Word","Powerpoint","Access"]
new_list=[h if h!="Excel" else "Access" for h in microsoft_office ]
print(new_list)
##ex15
microsoft_office=["Excel","Word","Powerpoint","Access"]
microsoft_office.sort()
print(microsoft_office)



##ex16
microsoft_office=[2,5,6,99,55,33]
microsoft_office.sort()
print(microsoft_office)


##ex17
microsoft_office=["Excel","Word","Powerpoint","Access"]
microsoft_office.sort(reverse=True)
print(microsoft_office)


##ex18
def my_func(n):
    return abs(n-50)
   

microsoft_office=[2,5,6,99,55,33]
microsoft_office.sort(key=my_func)
print(microsoft_office)




##ex19
microsoft_office=["excel","word","Powerpoint","Access"]
microsoft_office.sort()
print(microsoft_office)


##ex20
microsoft_office=["excel","word","Powerpoint","Access"]
microsoft_office.sort(key=str.lower)
print(microsoft_office)

##ex21
microsoft_office=["excel","word","Powerpoint","Access"]
microsoft_office.reverse()
print(microsoft_office)

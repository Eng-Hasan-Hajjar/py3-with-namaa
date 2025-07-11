## lesson12

##list
##tuple
##set
##dictionary
## list
#ex1
list_laptops=["Hp","Asus","Dell"]
print(list_laptops)


##ex2
list_laptops=list(("Hp","Asus","Dell"))
print(list_laptops)

##ex3
list_laptops=list(("Hp","Asus","Dell"))
print(type(list_laptops))


#ex4
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
print(list_laptops)

#ex5
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
print(len(list_laptops))

#ex6
list_laptops1=["Hp","Asus","Dell"]
list_laptops2=[2018,2016,2020]
list_laptops3=[True,False,True]
print(list_laptops1)
print(list_laptops2)
print(list_laptops3)

##ex7
list_laptops=[2018,"Asus",False]
print(list_laptops)

##ex8

list_laptops=[2018,"Asus",False]


print(type(list_laptops[0]))
print(type(list_laptops[1]))
print(type(list_laptops[2]))
print(list_laptops)

##ex9
list_laptops=[2018,"Asus",False]


print(list_laptops[0])
print(list_laptops[1])
print(list_laptops[2])
print(list_laptops)


##ex10
list_laptops=[2018,"Asus",False]


print(list_laptops[-1])
print(list_laptops[-2])
print(list_laptops[-3])
print(list_laptops)

##ex11
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
print(list_laptops[3:])

##ex12
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
print(list_laptops[:3])

##ex13
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
if "MSI" in list_laptops:
    print("yes MSI laptops exist in this list")
else:
    print("no MSI laptop is not found")

##ex14
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops[3]="MSI"
print(list_laptops)



##ex15
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops[1:3]=["MSI","Mac"]
print(list_laptops)



##ex16
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops[1:3]=["Mac"]
print(list_laptops)




##ex17
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops[4]=["MSI","Mac"]
print(list_laptops)

##ex18
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops[4]="MSI","Mac"
print(list_laptops)

##ex19
##insert
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops.insert(3,"MAC")

print(list_laptops)

##ex20
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops.append("MSI")
print(list_laptops)

##ex21
list_laptops=["Hp","Asus","Dell"]
list_laptops2=["MSI","MAC","Lenevo"]
list_laptops.extend(list_laptops2)
print(list_laptops)
print(list_laptops2)



##ex22
list_laptops=["Hp","Asus","Dell"]
tuple_laptops2=("MSI","MAC","Lenevo")
list_laptops.extend(tuple_laptops2)
print(list_laptops)
print(tuple_laptops2)



##ex23
list_laptops=["Hp","Asus","Dell"]

list_laptops.remove("Hp")
print(list_laptops)

##ex24
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops.remove("Asus")
print(list_laptops)


##ex25
list_laptops=["Hp","Asus","Dell","Asus","Dell"]
list_laptops.remove("Asus")
list_laptops.remove("Asus")
print(list_laptops)


##ex26
list_laptops=["Hp","Asus","Dell","Asus","Dell"]

list_laptops.remove("Asus")
list_laptops.remove("Asus")

print(list_laptops)


##ex27
list_laptops=["Hp","Asus","Dell","Asus","Dell"]

list_laptops.pop(3)

print(list_laptops)



##ex28
list_laptops=[1,2,3,5,10,2]

list_laptops.remove(10)


print(list_laptops)



##ex29
list_laptops=[1,2,"2025",5,10,2]

list_laptops.remove(10)


print(list_laptops)

##ex30
list_laptops=[1,2,5,10,2]

list_laptops.pop()


print(list_laptops)

##ex31
list_laptops=[1,2,5,10,2]

del list_laptops[0]


print(list_laptops)


##ex32
list_laptops=[1,2,5,10,2]

del list_laptops


### print(list_laptops)  ## error

##ex33
list_laptops=[1,2,5,10,2]
list_laptops.clear()
print(list_laptops)



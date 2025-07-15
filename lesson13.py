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
list_laptops=["Hp","Asus","Dell","MAc"]
new_list=[elem for elem in list_laptops if "A" in elem]

print(new_list)
print(list_laptops)



##ex8
list_laptops=["Hp","Asus","Dell","MAc"]
[new_list.append(elem) for elem in list_laptops if "A" in elem]

print(new_list)
print(list_laptops)
##lesson17
##ex1
products={"dress","bag","cap","hat","shose","cap"}
for x in products:
    print(x)
print(len(products))
##ex2
products={"dress","bag","cap","hat","shose","cap"}
prices={1,2,3,4,5}
result=products.union(prices)
print(result)
##ex3
products={"dress","bag","cap","hat","shose","cap"}
prices={1,2,3,4,5}
result=products|prices
print(result)
##ex4
products={"dress","bag","cap","hat","shose","cap"}
prices={1,2,3,4,5}
phones={"samsung","iphone","nokia","inifinicx  x g pro30"}
result=products|prices|phones
print(result)
##ex5
products={"dress","bag","cap","hat","shose","cap"}
prices={1,2,3,4,5}
phones={"samsung","iphone","nokia","inifinicx  x g pro30"}
result=products.union(prices,phones)
print(result)

##ex6
products={"dress","bag","cap","hat","shose","cap"}
new_products=set(("T-shirt","sunglasses"))
products.update(new_products)
print(products)
##ex7
products={"dress","bag","cap","hat","shose","cap"}
new_products=set(("T-shirt","sunglasses","shose"))
products.update(new_products)
print(products)
##ex8
products={"dress","bag","cap","hat","shose","cap"}
new_products=set(("T-shirt","sunglasses","shose"))
new_set=products.intersection(new_products)
print(new_set)
##ex9
products={"dress","bag","cap","hat","shose","cap"}
new_products=set(("T-shirt","sunglasses","shose"))
products.intersection_update(new_products)
print(products)
##ex10
products={"dress",1,"cap","hat","shose",0}
new_products=set(("T-shirt",True,"shose"))
new_set=products.intersection(new_products)
print(new_set)
##ex11
products={"dress",1,"cap","hat","shose",0}
new_products=set(("T-shirt",True,"shose"))
new_set=products & new_products
print(new_set)

##ex12
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","tie","shose"))
new_set=products.difference(new_products) 
print(new_set)
##ex13
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","tie","shose"))
new_set=new_products.difference(products) 
print(new_set)

##ex14
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","tie","shose"))
new_set=products - new_products 
print(new_set)
##ex15
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","tie","shose"))
products.difference_update(new_products) 
print(products)

##ex16
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","shose"))
products.symmetric_difference_update(new_products) 
print(products)
##ex17
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","shose"))
set3=products.symmetric_difference(new_products) 
print(set3)
##ex18
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","shose"))
set3=new_products.symmetric_difference(products) 
print(set3)
##ex19
products={"dress","tie","cap","hat","shose"}
new_products=set(("dress","tie","cap","hat","shose"))
set3=new_products.symmetric_difference(products) 
print(set3)
##ex20
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","shose"))
set3=new_products ^ products
print(set3)
##ex21
##isdisjoint
products={"dress","tie","cap","hat","shose"}
new_products=set(("T-shirt","shose"))
set3=products.isdisjoint(new_products)
print(set3)


##ex22
##issubset
products={"dress","tie","cap","hat","shose"}
new_products=set(("cap","hat","shose"))
set3=products.issubset(new_products)
print(set3)


##ex23
##issubset
products={"dress","tie","cap","hat","shose"}
new_products=set(("cap","hat","shose"))
set3=new_products.issubset(products)
print(set3)

##ex24
##issubset
products={"dress","tie","cap","hat","shose"}
new_products=set(("cap","hat","shose"))
set3=new_products <= products
print(set3)

##ex25
##issuperset
products={"dress","tie","cap","hat","shose"}
new_products=set(("cap","hat","shose"))
set3=new_products.issuperset(products)
print(set3)

##ex26
##issuperset
products={"dress","tie","cap","hat","shose"}
new_products=set(("cap","hat","shose"))
set3=new_products >= products
print(set3)
##lesson23
##class 
##ex1
class Student:
    name="Asmaa"
    age=22
    father="Ahmad"
    mather="Hayma"
    id=123456

##object
s1=Student()
print("name",s1.name,"age",s1.age)
##ex2
class Person:
    name="Adel"
    age=22
    father="Samer"
    mather="Tayma"
    id=123235456

p1=Person()
p2=Person()
print("name",p1.name,"age",p1.age)
print("name",p2.name,"age",p2.age)



##ex3
class Person:
    def __init__(self,name,age,father,mother,id):
            self.name=name
            self.age=age
            self.father=father
            self.mother=mother
            self.id=id
  

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p2=Person("Jamal",60,"watheq","Salwa",12568987)
print("name",p1.name,"age",p1.age)
print("name",p2.name,"age",p2.age)

##ex4
class Person:
    def __init__(self,name,age,father,mother,id):
            self.name=name
            self.age=age
            self.father=father
            self.mother=mother
            self.id=id
  

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p2=Person("Jamal",60,"watheq","Salwa",12568987)
print("name",p1.name,"age",p1.age)
print("name",p2.name,"age",p2.age)
print(p1)
print(p2)





##ex5
class Person:
    def __init__(self,name,age,father,mother,id):
            self.name=name
            self.age=age
            self.father=father
            self.mother=mother
            self.id=id
    def __str__(self):
          return self.father +" "+ self.name

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p2=Person("Jamal",60,"watheq","Salwa",12568987)
print("name",p1.name,"age",p1.age)
print("name",p2.name,"age",p2.age)
print(p1)
print(p2)


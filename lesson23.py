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

##ex6
class Person:
    def __init__(self,name,age,father,mother,id):
        self.name=name
        self.age=age
        self.father=father
        self.mother=mother
        self.id=id
    def __str__(self):
        return self.father +" "+ self.name
    
    def info(self):
        print("my name is :"+ self.name)

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p1.info()


##ex7
class Person:
    def __init__(self,name,age,father,mother,id):
        self.name=name
        self.age=age
        self.father=father
        self.mother=mother
        self.id=id
    def __str__(self):
        return self.father +" "+ self.name
    
    def info(ggg):
        print("my name is :"+ ggg.name)

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p1.info()



##ex8
class Person:
    def __init__(self,name,age,father,mother,id):
        self.name=name
        self.age=age
        self.father=father
        self.mother=mother
        self.id=id
    def __str__(self):
        return self.father +" "+ self.name
    
    def info(ggg):
        print("my name is :"+ ggg.name)


    def get_age(ggg):
        print("my age is :"+ str(ggg.age))

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p1.age=22
print(p1)
p1.get_age()


##ex9
class Person:
    def __init__(self,name,age,father,mother,id):
        self.name=name
        self.age=age
        self.father=father
        self.mother=mother
        self.id=id
    def __str__(self):
        return self.father +" "+ self.name
    
    def info(ggg):
        print("my name is :"+ ggg.name)


    def get_age(ggg):
        print("my age is :"+ str(ggg.age))

p1=Person("Ilyas",60,"Hamed","Hamida",13245698)
p1.age=22
print(p1)
p1.get_age()
del p1.age
#p1.get_age()
del p1

##ex10
class Car:
     pass



##ex11
class Player:
    def __init__(self,name,health=100):
          self.name=name
          self.health=health
          self.inventory=[]
          self.position=(0,0)
    def move(self,xx,yy):
        self.position=(xx,yy)
        print(f"{self.name} moved to : {self.position}")

    def take_damage(self,damage):
         self.health-=damage
         if self.health <= 0:
              print(f"{self.name} has been eliminated!")
         else:
              print(f"{self.name} took {damage} ,{self.health} health remaining")   
    def pick_up_weapon(self,weapon):
         self.inventory.append(weapon)
         print(f"{self.name} picked up {weapon}")


player1=Player("Asmaa")  
player2=Player("Watheq")       

player1.move(10,12)
player2.move(55,300)


player1.pick_up_weapon("AKM")
player2.pick_up_weapon("M4")


player2.take_damage(20)
player2.take_damage(30)
player1.take_damage(220)
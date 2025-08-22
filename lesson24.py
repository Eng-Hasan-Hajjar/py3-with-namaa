##lesson24
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printfullname(self):
        print(self.firstname , self.lastname)    

v=Person("Duaa","Naeem") 
v.printfullname()


v23=Person("Duaa23","Naeem23") 
v23.printfullname()


class Student(Person):
    def __init__(self,id_parameter,fname,lname):
        Person.__init__(self,fname,lname)
        self.id=id_parameter

s=Student(132456,"Jamal","Hamed")
print(s.id)
s.printfullname()



class Employee(Person):
    def __init__(self,id_parameter,fname,lname,id_salary):
        super().__init__(fname,lname)
        self.id=id_parameter
        self.salary=id_salary

e=Employee(132456,"Jamal","Hamed",5000)
print(e.id)
print(e.salary)
e.printfullname()


class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclass must implement adbstract method")    
    def move(self):
        print(f"{self.name} is moving")

class Dog(Animal):
    def __init__(self, name ,color):
        super().__init__(name)
        self.color=color
    def speak(self):
        print(f"{self.name} is speaking nnnnnnn")
    
    def fetch(self):
        print(f"{self.name} is fetching ball")


my_dog=Dog("ddd","red")

my_dog.speak()

my_dog.fetch()
my_dog.move()


# Father class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "When the animal makes a sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor using super()
        super().__init__(name)
        self.breed = breed
     

    def speak(self):
        return f"{self.name} says Woof!"
        

# Another child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

# Using the classes
dog1 = Dog("Buddy", "Golden")
cat1 = Cat("Whiskers", "White")

print(dog1.speak())   # Buddy says Woof!
print(cat1.speak())   # Whiskers says Meow!





##
name="kamel"
print(len(name))


name=[1,2,3,6,7,456,456,4654,77]
print(len(name))


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("fly!")

car1=Car("bmw","2010")
boat1=Boat("boatggg","2020")
plane1=Plane("pool","2030")


for x in (car1,boat1,plane1):
    x.move()








class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail!")

class Plane(Vehicle):
    def move(self):
        print("fly!")

car1=Car("bmw","2010")
boat1=Boat("boatggg","2020")
plane1=Plane("pool","2030")


for x in (car1,boat1,plane1):
    print(x.model)
    print(x.brand)
    x.move()















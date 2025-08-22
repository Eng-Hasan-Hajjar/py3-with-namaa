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
    def _init_(self, name):
        self.name = name
    def speak(self):
        return "When the animal makes a sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def _init_(self, name, breed):
        # Call parent constructor using super()
        super()._init_(name)
        self.breed = breed
     

    def speak(self):
        return f"{self.name} says Woof!"
        

# Another child class
class Cat(Animal):
    def _init_(self, name, color):
        super()._init_(name)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

# Using the classes
dog1 = Dog("Buddy", "Golden")
cat1 = Cat("Whiskers", "White")

print(dog1.speak())   # Buddy says Woof!
print(cat1.speak())   # Whiskers says Meow!






























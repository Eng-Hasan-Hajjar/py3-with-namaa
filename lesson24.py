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







































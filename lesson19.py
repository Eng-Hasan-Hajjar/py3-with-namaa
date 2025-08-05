##lesson19

##ex1
"""
b==a
b!=a
b>c
c<g
g<=h
j>=d

"""

tt=99
oo=55
if tt> oo:
    print("true for if statements")



if (tt > oo):
    print("true 2 for if statements")
    print("true 3  for if statements")

print("true out of if  for if statements")    



##ex2
##elif
name_student="Ilyass"
if name_student == "Hamza":
    print("he lives in Istanbul") 
elif name_student=="Shereen":
    print("he lives in Syria")
else:
    print("Eygpt")


##ex3
if len(name_student) > 5: print("str greater than 5") 

##ex4
print("str greater than 5") if len(name_student)-3 > 5 else print("str not greater than 5")     
##ex5
name_student="Ilyas"
print("str greater than 5") if len(name_student) > 5 else print("str smaller than 5") if len(name_student)< 5 else print("==")   
##ex6
students_list=["Adel","Ilyas","Hamza","Lina"]
if "Duaa" in students_list and "Lina" in students_list and "Asmaa" in students_list:
    print("proffessional project")

##ex7
students_list=["Adel","Ilyas","Hamza","Lina"]
if "Duaa" in students_list or "Lina" in students_list or "Asmaa" in students_list:
    print("proffessional project")



##ex8
students_list=["Adel","Ilyas","Hamza","Lina"]
if not "Duaa" in students_list: 
    print("proffessional project 222222222222222")


##ex9
students_list=["Adel","Ilyas","Hamza","Lina"]
if not "Duaa" in students_list: 
   pass

##ex10
ss=3
dd=5 
ff=7
if ss < dd :
    if ff > ss:
        print("true")
    else:
        print("false")
else : 
    print("false")





name = "Adel"
mark = 60
if mark <70 :
    print(f"{name} has crossed the mark. : {mark}")
elif mark >55 :
    print(f"{name} did not exceed the mark {mark}")

    

has_access_card = True
knows_password = True
treasure_available = True
no_traps = False
if has_access_card:  # Step 1: Access card
    print("✔ Access card confirmed. Proceeding to password check...")
    if knows_password:  # Step 2: Password
        print("✔ Password accepted. Proceeding to treasure check...")
        if treasure_available:  # Step 3: Treasure availability
            print("✔ Treasure is still here. Checking for traps...")
            if no_traps:  # Step 4: Trap check
                print("🔥 You safely take the treasure! You're rich!")
            else:
                print("💀 Oh no! The treasure is trapped. You can't take it.")
        else:
            print("❌ The treasure has already been taken by someone else.")
    else:
        print("❌ Wrong password. Access denied.")
else:
    print("❌ No access card. You can't even enter the vault.")  


toplam_tutar = float(input("Alışveriş toplamını giriniz (TL): "))

if toplam_tutar >= 100:
    print("Tebrikler! İndirime hak kazandınız.")
else:
    print("Üzgünüz, indirim için en az 100 TL harcamanız gerekiyor.")    


username = "Shereen"
password = "secure123"
access_level = "superuser"

# First check: correct username
if username == "Shereen":
    print("Username accepted.")
    # Second check: correct password
    if password == "secure123":
        print("Password correct.")
        # Third check: check access level
        if access_level == "superuser":
            print("Full access granted.")
        elif access_level == "user":
            print("Limited access granted.")
        else:
            print("Unknown access level.")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")    



##ex11
i=0
while i<9:
    print(i)
    i+=1

##ex12
i=0
while i<4:
    print(i)
    if i==2:
        break
    i+=1

##ex13
i=0
while i<4:
    print(i)
    i+=1

    break
    
print(i)

##ex14
print("ex14")
i=0
while i<3:
    i+=1
    if i==1:
        continue
    print(i)

##ex15
print("ex15")
i=0
while i<3:
    print(i)
    i+=1
else:
    print("out of while condition")

    
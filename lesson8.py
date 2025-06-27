##lesson8
#ilyas
print("muhamme\"d")
print("muhammed\tatrash")
print("ilyas\natrash")
suad="muhammed \
muhammed"
print(suad)
name5="muhammed \\ muhammed"
print(name5)
name6="muhammed \r 23muhammed ilyas"
print(name6)
name7="muhammed\b muhammed ilyas"
print(name7)
name8="muhammed \a muhammed ilyas"
print(name8)
name9="muhammed \f muhammed ilyas"
print(name9)
name10="muhammed \v muhammed ilyas"
print(name10)
name11="muhammed \000 muhammed ilyas"
print(name11)


##nasir
#مثال1 : سطر جديد (\n)
print("first line. \n second line.")
#مثال2 : مجموعة أسطر (\t)
print("name:\tnasir\nage:\t17\ncity:\tTurkey")
#مثال3 : طبع شرطة مائلة (\\)
print("am 17 yours old\\")
#مثال4 : حذف ما قبل شرطة مائلة(\b)
print("hi\b my\b name\b nasir\b ")
#exm 1مثال5 : علامة  الاقتباس المفردة(\') 
print('a was born in\'2008\'')
#exm 2مثال5 : علامة  الاقتباس المفردة(\')
print('a was born in"2008"')
#exm 1مثال6 : علامة الاقتباس المزدوجة(\")
print("a was born in\"1999\"")
#exm 2مثال6 : علامة الاقتباس المزدوجة(\")
print("a was born in '1999'")
#hex value:\xhh (IBM)

##shereen
print("Shereen\nMohammad") #normal
print(r"Shereen\nMohammad") #raw  
#when there is r or R before quotation the enterpreter don't execute the escape characters
print("Shereen Mohammad\n") #normal
print(r"Shereen Mohammad\n") #raw
print(r"Shereen\Mohammad\Programmer")
print("Shereen\rMohammad\rprogrammer") #Carriage Return
print("Python is \reasy to learn") #Carriage Return
var='Python is \
easy to learn'
print(var) #ignore
print("Python \\ is easy to learn") #return one slash
print('Python is  \'easy\' to learn')
print("Python is \"easy\" to learn")
print("Pyt\bhon is easy to learn") #to remove a letter
print("Python is \teasy to learn") #to make a tab
print("Shereen \fMohammad") #to add symbol
##hamaz
print('hamza \balabdulah')
print("hamza\talabdullah")
print("hello  "\
"word")
print("hamza \\")
print("Hamza Alabdullah \'Aljafil\'")
print("Türkiye'ye Hoş \nGeldiniz")
print("0000000 büyük bir ülke\rTürkiye")
print("\x48\x41\x4d\x5a\x41")

#adil
from colorama import Fore, Style, init
init()
#///////////////////////////////////////////طباعة التفاصيل الشخصية مع تنسيق ///////////////////////////////////////////////#------------------------\
My_name = "Adil"                                             #/////////الاسم                                                  #/     A    D    I    L   \
My_age = 20                                                  #///////////////العمر                                           #/                         \
My_height = 1.78                                             #/////////////////////الطول                                     #/                          \
My_country = "Syria"                                         #/////////////////////////////البلد                             #/                           \
phone_model = "Samsung Galaxy S21"                           #///////////////////////////////////موديل الهاتف                #/                            \
ip_address = "example.194.111.1.1"                           #////////////////////////////////////////////عنوان الاي بي       #/                             \
user_detail = "\nName: {} \nAge: {} \nCountry: {} \nPhone Model: {} \nIp Address {} \nHeight: {} m"                           #/                              \
print(user_detail.format(My_name, My_age, My_country, phone_model ,ip_address ,My_height ))                                   #/         وظيفة رقم 2          \
#OR THIS                                                                                                                      #/                                \
## طباعة التفاصيل الشخصية مع ارقام المتغيرات                                                                               #/         ESCAPE OF ""            \
user_detail = "\nName: {1} \nAge: {0} \nCountry: {3} \nPhone Model: {2} \nIp Address {5} \nHeight: {4} m"                     #/                                  \
print(user_detail. format( My_age, My_name, phone_model ,My_country,My_height,ip_address ))                                    #/                                   \
###############################################################################################################################/                                    \
##/////////////////////////// طباعة التفاصيل الشخصية مع تنسيق واسرع +مع الهروب من الكوتيشن //////////////////////////////#/                                     \
print(f"My Name: {My_name:!^34} \nMy Age: {My_age}  \nMy Country: {My_country} \nMy Phone Model: {phone_model} \nMy Ip Address: {ip_address} \nMy Height: {My_height} m") 
#########################################################################################################################################################################
#///////////////////////////////////////////////////////////////  طباعة التفاصيل الشخصية مع امر اي/لا /////////////////////////////////////////////////////////////////#
user_detail ="no"                                                                                              #

#user_detail = input( "Do you want to see your details? (yes/no): ")                                                                                              #
if user_detail == "yes":                                                                                                                                                 #
   ##
   #  print(f"\n{banner}")                                                                                                                                                 #
    print(f"My Name: {My_name} \nMy Age: {My_age}  \nMy Country: {My_country} \nMy Phone Model: {phone_model} \nMy Ip Address: {ip_address} \nMy Height: {My_height} m") # 
###########################################################################################################################################################################
print(f"\n{Fore.YELLOW}{Style.BRIGHT}Thank you for using the program {My_name}! ")      
#
input("\nPress Enter to exit...")                                                                                                                                          #
#////////////////////////////////////////////////////////////////////////////THE END 🌟////////////////////////////////////////////////////////////////////////////////////#

X1="DUAA"
print("duaa\d" ) 

##ex1
##isalpha()
text="123456789"
result=text.isalpha()
print("is",result)


##ex2
##isalpha()
text="123456789"
result=text.isalpha()
if result:
    print("the text is alpha")
print("is",result)

##ex3
##isascii()
text="123456789"
result=text.isascii()
if result:
    print("the text is isascii")
print("is",result)


##ex4
##isascii()
text="😍"
result=text.isascii()
if result:
    print("the text is isascii")
print("is",result)


##ex5
##isspace()
text="       "
result=text.isspace()
if result:
    print("the text is isspace")
print("is",result)


##ex6
##istitle()
text="For example: escape fo python"
result=text.istitle()
if result:
    print("the text is istitle")
print("is",result)


##ex7
##istitle()
text="For Example: Escape For Python"
result=text.istitle()
if result:
    print("the text is istitle")
print("is",result)

##ex8
##join()
mytuple=("shereen","hamza","ilays")
related="&".join(mytuple)
print(related)


##ex9
##join()
mylist=list(("wathq","lina","nasir"))
mylist=["wathq","lina","nasir"]
related="&".join(mylist)
print(related)


##ex10
##join()

mylist=["duaa","maram","asmaa"]
seperator=" and "
related=seperator.join(mylist)
print(related)

##ex11
##strip()

txt="    banana    "
print(txt.strip())



##ex12
##lstrip()

txt="     banana    "
txt2=txt.lstrip()
print("person eat ",txt2,"end ex" )

##ex13
##lstrip()

txt="bnbnc....banana    "
txt2=txt.lstrip("bnbnc")
print("person eat ",txt2,"end ex" )



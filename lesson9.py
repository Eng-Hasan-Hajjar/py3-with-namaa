#lesson9


##ilyas
import string
##استخراج السلسلة بلستخدام التقطيع  1

s = "Programming"
print(s[3:7])

#$#استخراج الحرف الاخير باستخدام الفهرس السالب
print(s[-1])

#$#طباعة احرف من مكان الى مكان معين
print(s[3:8])

""" 2 التعديل على السلاسل
 ازالة السبيس من على الاطراف
تحويل النص لاحرف صغيرة 
تبديل كلمة بكلمة بمساعدة ريبلس"""
text="  Hello, World!  "

nan1=text.strip()
nan2=nan1.lower()
nan3=nan2.replace("world","py")

print(nan3)

# 3 التحقق من محتوى النص
txt = "Python is fun"

print("fun" in txt,\
      "Py" in txt,\
        "!" in txt)


# 4 تقسيم السلاسل ودمج

fruits="apple,banana,cherry"

print(fruits.replace(",","-"))


# 5 العمل باستخدام فورمت
name="ilyas"
age=25
score=100
information="my name {}  my age {}  my score {} %".format(name,age,score)
print(information)


#ex6
num = 1234567.89

#  تنسيق الرقم مع فواصل آلاف وعشريتين
formatted_with_commas = "{:,.2f}".format(num)
print(formatted_with_commas)  # النتيجة: 1,234,567.89

# تنسيق الرقم بدون فواصل آلاف وأربع خانات عشرية
formatted_without_commas = "{:.4f}".format(num)
print(formatted_without_commas)  # النتيجة: 1234567.8900


#ex7
s = "Hello, Python!"

#  احسب طول السلسلة
length = len(s)
print("طول السلسلة:", length)

#  عدد مرات ظهور الحرف 'o'
count_o = s.count("o")
print("عدد مرات ظهور الحرف 'o':", count_o)

#  عدد المسافات
count_spaces = s.count(" ")
print("عدد المسافات:", count_spaces)


#ex8import string

clean_text = "Hello! 123 World,?"
new_text = "".join([i for i in clean_text if not i.isdigit() and i not in string.punctuation])
print(new_text)


#ex9#توليد سلسلة مخصصة

ahmed1="""Name: Ahmed
Age: 25
Country: Egypt"""

ahmed2="Name: Ahmed\nAge: 25\nCountry: Egypt"

print(ahmed2,ahmed1)




import arabic_reshaper
from bidi.algorithm import get_display

text = " مرحبا بكم في عالم البرمجة"
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)
bidi2_text = get_display(text)
print(reshaped_text)
print(bidi_text)
print(bidi2_text)


print(dir(arabic_reshaper))




##shereen
#Slicing (1)
s="Programming"
print(s[3:7]) #Extract the "gram" series by slicing
print(s[-1]) #Extract the last letter by negative number
print(s[3:7]) #print the letter from 3 to 7

#Modificatin (2)
text= " Hello, World! "
print(text.strip()) #This method removes any whitespace from both sides of the text
print(text.lower()) #return into small letters
print(text.replace("World","Python"))

#Content verification
text1= "Python is fun"
print(text1.find("fun"))
print(len(text1))
var = "fun"
if var in text1:
    print(True)
else:
    print(False)
print("fun" in text1) #Another way
print(text1.startswith("Py")) #to verify if the string starts with "py"
print(text1.endswith("!"))    #to verify if the string ends with "!"

#Slicing strings and merging them
fruits="apple, banana, cherry"
fruits1="apple-banana-cherry"

print(fruits.split(","))
print(fruits1.split())
print(fruits1.split("-",1))
print(fruits1.split("-"))

#Coordination with format
name="Ahmed"
age=25
score= "95.5%"
result= f"Ahmed is {age} years old and his score is {score}"
print(result)

#f-string
num= 1234567.89
num2=123456789
text2=","
text2=f"Comma as thousand separators: {num:,}"
text3=f"The number is sheren {num:.20f}"
text4=f"The number here is {num2:.2f}"
print(text2)
print(text3)
print(text4)

#Count the lang of the string
s="Hello, Python"
print(len(s)) #Count the lang of the string
s1=s.count("o") #Count the numbers of "O" letterts
print(s1)
print(s.count(" ")) #Count the numbers of spaces

#Rmove the numbers and characters from the string
clean_text="Hello! . $123 World"
new_text="".join([i for i in clean_text if not i.isdigit()]).replace("!","")
print(new_text)

#Generating an associative sring
name22="Ahmed"
age22=25
country="Egypt"
student_a22= f"{name22} {age22} {country}"
print(f"{name22} his age is {age22} and he is from {country}" )
print(name22 + " " + country + " " + str(age22))
print(f"{name22} \nhis age is {age22} and \nhe is from {country}" )
print("""Ahmed
his age is 25
and he is from Egypt
      
      """)

##Hamaza Isaye
# ex1
s="Programming"
print(s[3:7])
print(s[-1])
print(s[3:7])

# ex2
text=" Hello, World! "
text_strip=text.strip()
print(text_strip)

text_lower=text.lower()
print(text_lower)

text_replace=text.replace("World!","Python")
print(text_replace)                                                                                             

# ex3
txt="Python is fun"
i="fun"
if i in txt:
   print("True")
else:
   print("False")


txt_startswith=txt.startswith("Py")
print(txt_startswith)

txt_endswith=txt.endswith("!")
print(txt_endswith)

# ex4
fruits=("appel","banana","cherry")
for i in fruits:
    print(i)


fruits_join="-".join(fruits)
print(fruits_join)

# ex5
name="Ahmed"
age=25
score="95.5%"
information="Your name :{} Your age :{} And your scores :{}"
print(information.format(name,age,score))


name="Ahmed"
age=25
score="95.5%"
information="Your name :{1} Your age :{2} And your scores :{0}"
print(information.format(score,name,age))


# ex6

num= 1234567.89
text2=","
text2=f"Comma as thousand separators: {num:,}"
text3=f"The number is {num:.2f} $"
text4=f"The number here is {num:.4f} $"
print(text3)
print(text2)
print(text4)


# ex7
s="Hello, Python!"
s_len=len(s)
print(s_len)

s_count=s.count("o")
print(s_count)

s_count=s.count(" ")
print(s_count)


# ex8
import string
clean_text = "Hello! 123 World,?"
new_text = "".join([hamza for hamza in clean_text if not hamza.isdigit() and hamza not in string.punctuation])
print(new_text) 



# ex9
x="\"Name:Ahmed\" \"Age:25\" \"Country:Egypt\""
print(x)

x="Name:Ahmed \bAge:25 \bCountry:Egypt"
print(x)

x="Name :Ahmed \nAge :25 \nCountry :Egypt"
print(x)


##lina

#1.
s = "Programming"
# Extract the substring "gram" using slicing
substring = s[3:7]
print("Slicing from 3 to 7:", substring)
# Extract the last character using a negative index
last_char = s[-1]
print("Last character:", last_char)
# Print the characters from position 3 to 7 (inclusive)
print("Characters from position 3 to 7:", s[3:8])

#2.
text = " Hello, World! "
# 1. Remove spaces from the beginning and end (trim spaces)
trimmed_text =text.strip()
print("After trimming spaces:", '"' + trimmed_text + '"')
# 2. Convert the entire text to lowercase
lower_text = trimmed_text.lower()
print("Lowercase text:", lower_text)
# 3. Replace the word "World" with "Python"
replaced_text = trimmed_text.replace("World", "Python")
print("After replacing 'World' with 'Python':", replaced_text)

#3. 
txt = "Python is fun"
# Check if "fun" is in the string
contains_fun = "fun" in txt
print(type(contains_fun))
print("Contains 'fun':", contains_fun)
# Check if the string starts with "Py"
starts_with_py = txt.startswith("Py")
print("Starts with 'Py':", starts_with_py)

#4.
fruits = "apple-banana-cherry"
# Split the string into a list using the '-' delimiter
fruits_list = fruits.split("-")
print("List of fruits:", fruits_list)  # Output: ['apple', 'banana', 'cherry']
# Join the list elements into a string using the '-' delimiter
fruits_str = "-".join(fruits_list)
print(fruits_str)  # Output: apple-banana-cherry


#5
name = "Ahmed"
age = 25
score = 95.5
sentence = "{} is {} years old and scored {}".format(name, age, score)
print(sentence)

#6 
num = 1234567.89
# Currency format with commas and dollar sign at the end
formatted_currency = f"{num:,.2f}$"
print(formatted_currency)
# Number with 4 decimal places
formatted_decimal = f"{num:.4f}"
print(formatted_decimal)


#7 
s = "Hello, Python!"
# 2. Count the occurrences of the letter "o"
count_o = s.count("o")
print("Number of 'o':", count_o)
# 3. Length of the string
length_s = len(s)
print("Length of the string:", length_s)
# 4. Count the number of spaces
count_spaces = s.count(" ")
print("Number of spaces:", count_spaces)


#8 
def clean_text(txt):
    # List of punctuation marks we want to remove
    punctuation = [',', '.', '?', '!', ':'] 
    # Remove all digits from the text
    no_digits = ''.join(char for char in txt if not char.isdigit())  
    # Remove all punctuation marks
    cleaned = ''.join(char for char in no_digits if char not in punctuation)   
    # Remove leading and trailing spaces
    return cleaned.strip()
text = ":Hello! 123 World."
result = clean_text(text)
print(result)


#9 
# 1. Using triple quotes
text1 = """Name: Ahmed
Age: 25
Country: Egypt"""

# 2. Using escape characters (\n)
text2 = "Name: Ahmed\nAge: 25\nCountry: Egypt"

# 3. Using format method to generate the string
text3 = "Name: {}\nAge: {}\nCountry: {}".format("Ahmed", 25, "Egypt")

# Print the results
print("Using triple quotes:")
print(text1)
print("\nUsing escape characters:")
print(text2)
print("\nUsing format method:")
print(text3)


## sheren complete
original_string = "Hello, 123 World!"
filtered_chars = filter(str.isalpha, original_string)
modified_string = ' '.join(filtered_chars)
print(original_string) # Output: Hello, 123 World! 
print(modified_string) # Output: HelloWorld



##عادل
#################################المكتبات#############################################
from colorama import Fore, Style
import re
#######################################################################################
color_banner = Fore.RED
color_Explain = Fore.LIGHTBLUE_EX
Explain = f"""{color_Explain}"""
banner = F"""{color_banner}
oooooooooo ooooo  oooo ooooooo  
 888    888  888  88 o88    888o
 888oooo88     888       88888o 
 888           888   88o    o888
o888o         o888o    88ooo88
""" 
print(banner)
##########################################################################################################################
                          #1 Request                                              
######################################طباعة مع تقطع الكلمة ##############################################################
#start
print(f"{color_Explain}" + "-"*5)
skill = "Programming"
print(f"{Fore.YELLOW}{Style.RESET_ALL}{skill [0:3].upper()}")
print(f"{Fore.YELLOW}{Style.RESET_ALL}{skill [3:7].upper() }")
print(f"{color_Explain}" + "-"*5)
#end
#########################################################################################################################
                          #2 Request                                                
####################طباعة المتغير مع تصغير الاحرف واستبدال الكلمة######################################################
#start
print(f"{color_Explain}" + "-"*17)
color_spaces = Fore.YELLOW                                                             
spaces = "    Hello World    "                                                       
print(f"{color_spaces}{spaces.strip().replace('World', 'Python').lower()}{Style.RESET_ALL}")##ازالة المسافات من الطرفين#
print(f"{color_spaces}{spaces.rstrip().replace('World', 'Python').lower()}{Style.RESET_ALL}")##ازالة المسافات من اليمين#
print(f"{color_spaces}{spaces.lstrip().replace('World', 'Python').lower()}{Style.RESET_ALL}")##ازالة المسافات من اليسار#
print(f"{color_Explain}" + "-"*17)
#end
###########################################################################################################################
                          #3 Request
###############################فحص المحتوى من الكلمات الموجودة والغبر موجودة############################################
#start
print(f"{color_Explain}" + "-"*35+ Style.RESET_ALL)
py = "pytohn is fun"#ممنوع يكون في مسافة في اول السترنج وفي نهايته ! 
control = "perfict" in py
start_with = py.startswith("py")
end_with = py.endswith("fun")
color_control = Fore.RED                                                    # A D I L
color_start = Fore.GREEN
color_end = Fore.GREEN
print(f"start with py:{color_start} {start_with}{Style.RESET_ALL}")
print(f"end with fun:{color_end} {end_with}{Style.RESET_ALL}")
print(f"the variable have perfict ?:{color_control}{Style.BRIGHT} {control}{Style.RESET_ALL}") 
                   # او مع شرط يطبعلك انو غير موجودة هذه الكلمة #
if "perfect" in py:
    print("Found perfect")
else:
    print("not find perfect")
    print(f"{color_Explain}" + "-"*35)
#end
###########################################################################################################################
                          #4 Request
################################################تقسيم السالسل والدمج######################################################
#start
print(f"{color_Explain}" + "-"*20)
color_apple = Fore.GREEN
color_banana = Fore.YELLOW
color_cherry = Fore.RED
fruits = f"{color_apple}apple,{color_banana}banana,{color_cherry}cherry"
fruits = fruits.replace(",", "-")
print(fruits)
print(f"{color_Explain}" + "-"*20)
#end
#############################################################################################################################
                          #5 Request
###############################################التنسيق باستخدام()format#####################################################
print(f"{color_Explain}" + "-"*45)
name = "Adil"
age = 20
score = 91.25
color_vbls = Fore.LIGHTBLACK_EX
the_vbls = (f"{color_vbls}{name} is {age} years old and his score is: {score}%".format(name, age, score,{Style.RESET_ALL}))
print(the_vbls)
print(f"{color_Explain}" + "-"*45)
###############################################################################################################################
                          #6 Request
############################################تحويل الرقم العددي الى عملة######################################################
print(f"{color_Explain}" + "-"*12+ Style.RESET_ALL)
number = 10545.45
monney = f"{number:,.2f}{Fore.GREEN}$"
print(monney)
print(f"{color_Explain}" + "-"*12+Style.RESET_ALL)
###############################################################################################################################
                          #7 Request
################################################ حساب الطول والعد #############%%%%%%#########################################
s = "Hello im Adil developing Py3"
char_to_count = "i"
total_length = len(s)
space_count = s.count(" ")
char_count = s.count(char_to_count)
print(color_Explain + "-" * 35 + Style.RESET_ALL)
print(f"{s}")
print(Fore.GREEN + f"Total Length:{Fore.WHITE}{total_length}")
print(Fore.GREEN + f"Spaces:       {Fore.WHITE}{space_count}")
print(Fore.GREEN + f"'{char_to_count}' Count:    {Fore.WHITE}{char_count}")
print(color_Explain + "-" * 35 + Style.RESET_ALL)
###############################################################################################################################
                          #8 Request
######################################## إزالة الرموز واألرقام###############################################################
print(color_Explain + "-" * 35 + Style.RESET_ALL)
def text_clean(txt, to_upper=True):
    txt = re.sub(r'\d+', '', txt)
    txt = re.sub(r'[^\w\s]', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    if to_upper:
        txt = txt.title()
    return txt
dirty_text:str = "Hey!! Im Adil, welcome to Py3 💻 #Coding 101?"
cleaned = text_clean(dirty_text)
print(cleaned)
print(color_Explain + "-" * 35 + Style.RESET_ALL)
###############################################################################################################################
                          #9 Request
#############################################توليد سلسلة مخصصة################################################################
print(color_Explain + "-" * 15 + Style.RESET_ALL)
name="adil"
age="20"
country="syria"
print(f"Name: {name}\nAge: {age}\nCountry: {country}")
print(color_Explain + "-" * 15 + Style.RESET_ALL)
################################################## THE END 🌟###################################################################



##دعاء


##1-- التعامل مع الفهارس والتقطيع
s="Programming"
##ستخرج السلسلة "gram "باستخدام التقطيع
print(s[3:7])
## استخرج الحرف األخير باستخدام فهرس سالب
print(s[-1:])
## اطبع األحرف من الموضع 3 إلى 7
print(s[3:7])


##2--التعديل الأساسي للسلاسل

text = "  Hello, World! "
## أزل المسافات البيضاء من الطرفين 
print(text.strip())
##حّول األحرف إلى صغيرة
print(text.lower())
## استبدل كلمة "World "بـ"Python"
x=text.replace("World!","python")
print(x)


##3== التحقق من المحتوى 
text=" Python is fun "
x1="fun" in text 
## إذا كانت تبدأ بـ"Py"
x2=text.find("py")
## إذا كانت تنتهي بـ "!" )اطبع النتائج( 
x3=text.endswith("!")
print(x1,x2,x3)




##4 تقسيم السلاسل والدمج
fruits = "apple,banana,cherry"
#ق ّسمها إلى قائمة باستخدام الفاصلة 
list_fruits=["apple","banana","cherry"] 
x1,x2,x3=list_fruits
print(x1,x2, x3)
# ادمج العناصر باستخدام الشرطة )-( لتصبح"cherry-banana-apple"
fruits = ("apple","banana","cherry")
duaa="-".join(fruits)
print(duaa)





##%5 التنسيق باستخدام()format
name= "Ahmed"
age= 25
score= 95.5
ahmed=": {}  is : {}  years old ,  and his score is:  {}  %" 
print(ahmed.format(name ,age ,score))



##6" 1,234,567.89$"
##x1=int(" 1,234,567.89$")
##print(x1)






##7 حساب الطول والعد
s="Hello, Python!"
## احسب طول السلسلة
print(len(s))
##عد عدد مرات ظهور حرف"o"
print(s.count("o"))
##عد عدد المسافات
print(s.count(" "))

##8 إزالة الرموز واألرقام

## إزالة جميع األرقام
x1= "Hello! 123 World."
x2=x1.replace("123"," ")
print(x2)

##ازالة الرموز

x1= "Hello! 123 World."
def clean_text():
    s1=x1.translate(x1)
    print(s1)


clean_text()

##9 توليد سلسلة مخصصة
x=dict(Name=" Ahmed" ,Age= 25, Country=" is Egypt")
print(x)



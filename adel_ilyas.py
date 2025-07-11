from colorama import Fore, Style, init
init(autoreset=True)

yes_green = Fore.GREEN
no_red = Fore.RED
made_blue = Fore.BLUE
score = 14

banner = """
 _ _    __ __ _ ___ 
|_ / _ \  |   | _/ _|   _|
 | | () |   | | | |\ \ | |  
|\\\   || ||/ ||           
"""
print(f"{Fore.LIGHTBLUE_EX} {banner}")
print(f"{made_blue}This program was made by Elias and Adil. 💻")
print(f"{Fore.BLACK}-"*40)
################# السؤال الأول 1 ##################
def user_test1():
    global score
    # هل الدالة strip() تزيل الفراغات من بداية ونهاية النص؟
    user_test1 = "Does the 'strip' function remove spaces?"
    print(user_test1)
    answer = input(f"{yes_green}Yes {made_blue}or {no_red}No : {Style.RESET_ALL}").casefold().strip()

    if answer == 'yes':
        print(f"{yes_green}True, it removes spaces.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False, the 'strip' function removes spaces from the start and end only.{Style.RESET_ALL}")

user_test1()
print(f"{Fore.BLACK}-"*40)

################# السؤال الثاني 2 ##################
def user_test2():
    global score
    # هل الدالة lower() تكبر النص؟
    user_test2 = "Does the function 'lower()' enlarge the text?"
    print(user_test2)
    answer = input(f"{yes_green}Yes {made_blue}or {no_red}No : {Style.RESET_ALL}").casefold().strip()

    if answer == 'no':
        print(f"{yes_green}True, it actually converts text to lowercase.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False, 'lower()' makes the text lowercase.{Style.RESET_ALL}")

user_test2()
print(f"{Fore.BLACK}-"*40)

################# السؤال الثالث 3 ##################
def user_test3():
    global score
    # إذا كان عندك نص يحتوي على JavaScript وتريد استبداله بكلمة Python، أي دالة تستخدم؟
    user_test3 = "If you have text containing JavaScript and want to replace it with Python, which function do you use?"
    print(user_test3)
    answer = input("'replace' OR 'pyplace' OR 'join' : ").casefold().strip()

    if answer == 'replace':
        print(f"{yes_green}True, 'replace' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'replace' is the right choice.{Style.RESET_ALL}")

user_test3()
print(f"{Fore.BLACK}-"*40)
################# السؤال الرابع 4 ##################
def user_test4():
    global score
    # إذا كان لديك جملة من كلمتين وتريد أن تجعل أول حرف في كل كلمة كبيرًا، أي دالة تستخدم؟
    user_test4 = "If you have a string with two words and want to capitalize the first letter of each word, which function do you use?"
    print(user_test4)
    answer = input("'capitalize' OR 'title' OR 'upper' : ").casefold().strip()

    if answer == 'title':
        print(f"{yes_green}True, 'title' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'title' is the right choice.{Style.RESET_ALL}")

user_test4()
print(f"{Fore.BLACK}-"*40)
################# السؤال الخامس 5 ##################
def user_test5():
    global score
    # إذا كان لديك نص يحتوي على أحرف كبيرة بالألمانية وتريد تحويلها إلى صغيرة مع تجاهل الفروقات الخاصة، أي دالة تستخدم؟
    user_test5 = "If you have uppercase German text and want to convert it to lowercase ignoring special character differences, which function do you use?"
    print(user_test5)
    answer = input("'lower' OR 'casefold' OR 'format' : ").casefold().strip()

    if answer == 'casefold':
        print(f"{yes_green}True, 'casefold' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'casefold' is the right choice.{Style.RESET_ALL}")

user_test5()
print(f"{Fore.BLACK}-"*40)
################# السؤال السادس 6 ##################
def user_test6():
    global score
    # ما الدالة التي تستخدم لتقسيم النص إلى قائمة كلمات بناءً على فاصل مثل الفراغ أو الفاصلة؟
    user_test6 = "What function splits a string into a list of elements based on a separator like space or comma?"
    print(user_test6)
    answer = input("'slice' OR 'score' OR 'split' : ").casefold().strip()

    if answer == 'split':
        print(f"{yes_green}True, 'split' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'split' is the right choice.{Style.RESET_ALL}")

user_test6()
print(f"{Fore.BLACK}-"*40)
################# السؤال السابع 7 ##################
def user_test7():
    global score
    # كيف تجد موقع أول ظهور لكلمة أو حرف معين داخل نص؟
    user_test7 = "How do you find the position of the first occurrence of a specific word or letter in a text?"
    print(user_test7)
    answer = input("'index' OR 'invex' OR 'len' : ").casefold().strip()

    if answer == 'index':
        print(f"{yes_green}True, 'index' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'index' is the right choice.{Style.RESET_ALL}")

user_test7()
print(f"{Fore.BLACK}-"*40)
################# السؤال الثامن 8 ##################
def user_test8():
    global score
    # كيف تقسم جملة إلى ثلاثة أجزاء: قبل أول رمز معين (نقطة أو فاصلة)، الرمز نفسه، وبعده؟
    user_test8 = "If you want to split a sentence into three parts: before the first specific character (like dot or comma), the character itself, and after it, how do you do that?"
    print(user_test8)
    answer = input("'rsplit' OR 'partition' OR 'bool' : ").casefold().strip()

    if answer == 'partition':
        print(f"{yes_green}True, 'partition' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'partition' is the right choice.{Style.RESET_ALL}")

user_test8()
print(f"{Fore.BLACK}-"*40)
################# السؤال التاسع 9 ##################
def user_test9():
    global score
    # كيف تحول نص يحتوي عدة أسطر إلى قائمة عناصر كل عنصر يمثل سطر؟
    user_test9 = "If you have multi-line text, how do you split each line into a separate list item?"
    print(user_test9)
    answer = input("'split' OR 'splitlines' OR 'count' : ").casefold().strip()

    if answer == 'splitlines':
        print(f"{yes_green}True, 'splitlines' is correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}'splitlines' is the right choice.{Style.RESET_ALL}")

user_test9()
print(f"{Fore.BLACK}-"*40)
################# السؤال العاشر 10 ##################
def user_test10():
    global score
    # إذا كان x=5، هل العبارة x > 3 صحيحة أم خاطئة؟
    user_test10 = """
x = 5
if x > 3:
  print("true")
else:
  print("false")
"""
    print(user_test10)
    answer = input(F"{no_red}TRUE {made_blue}OR {yes_green}FALSE : {Style.RESET_ALL}").casefold().strip()

    if answer == 'true':
        print(f"{yes_green}True, correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False.{Style.RESET_ALL}")

user_test10()
print(f"{Fore.BLACK}-"*40)
################# السؤال الحادي عشر 11 ##################
def user_test11():
    global score
    # في التعبير a ^ b حيث a=True و b=False، هل الناتج True أم False؟ (XOR)
    user_test11 = """
a = True
b = False
print(a ^ b)
"""
    print(user_test11)
    answer = input(F"{yes_green}TRUE {made_blue}OR {no_red}FALSE : {Style.RESET_ALL}").casefold().strip()

    if answer == 'true':
        print(f"{yes_green}True, correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False.{Style.RESET_ALL}")

user_test11()
print(f"{Fore.BLACK}-"*40)
################# السؤال الثاني عشر 12 ##################
def user_test12():
    global score
    # هل نتيجة x > 5 and y < 15 صحيحة إذا كانت x=10 و y=20؟
    user_test12 = """
x = 10
y = 20
print(x > 5 and y < 15)
"""
    print(user_test12)
    answer = input(F"{yes_green}TRUE {made_blue}OR {no_red}FALSE : {Style.RESET_ALL}").casefold().strip()

    if answer == 'false':
        print(f"{yes_green}True, correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False.{Style.RESET_ALL}")

user_test12()
print(f"{Fore.BLACK}-"*40)
################# السؤال الثالث عشر 13 ##################
def user_test13():
    global score
    # ما نتيجة not False؟
    user_test13 = """
flag = False
print(not flag)
"""
    print(user_test13)
    answer = input(F"{yes_green}TRUE {made_blue}OR {no_red}FALSE : {Style.RESET_ALL}").casefold().strip()

    if answer == 'true':
        print(f"{yes_green}True, correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False.{Style.RESET_ALL}")

user_test13()
print(f"{Fore.BLACK}-"*40)
################# السؤال الرابع عشر 14 ##################
def user_test14():
    global score
    # هل نتيجة a > 5 or b > 5 صحيحة إذا a=3 و b=7؟
    user_test14 = """
a = 3
b = 7
print(a > 5 or b > 5)
"""
    print(user_test14)
    answer = input(F"{yes_green}TRUE {made_blue}OR {no_red}FALSE : {Style.RESET_ALL}").casefold().strip()

    if answer == 'true':
        print(f"{yes_green}True, correct.{Style.RESET_ALL}")
        score -= 1
    else:
        print(f"{no_red}False.{Style.RESET_ALL}")

user_test14()
print(f"{Fore.BLACK}-"*40)

################# عرض النتيجة ##################
if score == 0:
    print("Congratulations, you answered all questions correctly!")
else:
    print("Your final score:", 14 - score)
    last = """
                You are a genius, you made it
___  _    _   __   __   _    _   _    _   __   _    _ 
  | |   | |  | | | |  | | | |  \ \ | |  / /   \ \  | | / |  | \ | |  | |
  | |   | |--| | | || | | |  | | | |-< <     \\| | | |  | | | |  | |
  ||   ||  || ||  || ||  || ||  \\    __|| \||/ \|||
"""
    print(f"{Fore.LIGHTBLUE_EX} {last}")
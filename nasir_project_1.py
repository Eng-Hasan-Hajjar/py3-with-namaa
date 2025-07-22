from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Listbox
root = Tk ()
root.title("looking for experienced")
root.geometry("500x300")

def thanks ():
    messagebox.showinfo(title="thanks",message="thenks"+Button1.get())

def myfunction():
    exit()




title =ttk.Label(root, text="We are looking for experienced programmers.",font="calibre 20 bold")
title.grid(row=0,column=0, columnspan=4)

name_label=ttk.Label(root, text="frist name")
name_label.grid(row=1,column=0)

name_entry=ttk.Entry(root, width=20)
name_entry.grid(row=1,column=1)



lname_label=ttk.Label(root, text="last name")
lname_label.grid(row=1,column=2)

lname_entry=ttk.Entry(root, width=20)
lname_entry.grid(row=1,column=3)



gender_label=ttk.Label(root, text="gender")
gender_label.grid(row=3,column=0)


gender = StringVar()

male =ttk.Radiobutton(root, text="male",variable=gender, value="male")
male.grid(row=3,column=1)

female =ttk.Radiobutton(root, text="female",variable=gender,value="female")
female.grid(row=3,column=2)




age_label=ttk.Label(root, text="age")
age_label.place(x=45, y=80)

age_label=ttk.Entry(root, width=20)
age_label.place(x=147, y=80)

myoptins =Listbox(root)
myoptins.place(x=15,y=130)



title2 =ttk.Label(root, text="How much of yourself do you give\n in percentage, in Python?",font="calibre 9 bold")
title2.place(x=150,y=110 )
mygroup = IntVar()
myoptins1=Radiobutton(root, text =25,variable=mygroup,value="25").place(x=150,y=150)
myoptins2=Radiobutton(root, text =50,variable=mygroup,value="50").place(x=150,y=180)
myoptins3=Radiobutton(root, text =75,variable=mygroup,value="75").place(x=150,y=210)
myoptins4=Radiobutton(root, text =100,variable=mygroup,value="100").place(x=150,y=240)


title2 =ttk.Label(root, text="How much of yourself do you give\n in percentage, in 2. JavaScript?",font="calibre 9 bold")
title2.place(x=380,y=110 )
mygroup = IntVar()
myoptins1=Radiobutton(root, text =25,variable=mygroup,value="25").place(x=380,y=150)
myoptins2=Radiobutton(root, text =50,variable=mygroup,value="50").place(x=380,y=180)
myoptins3=Radiobutton(root, text =75,variable=mygroup,value="75").place(x=380,y=210)
myoptins4=Radiobutton(root, text =100,variable=mygroup,value="100").place(x=380,y=240)


title2 =ttk.Label(root, text="How much of yourself do you give\n in percentage, in 3. Java?",font="calibre 9 bold")
title2.place(x=610,y=110 )
mygroup = IntVar()
myoptins1=Radiobutton(root, text =25,variable=mygroup,value="25").place(x=610,y=150)
myoptins2=Radiobutton(root, text =50,variable=mygroup,value="50").place(x=610,y=180)
myoptins3=Radiobutton(root, text =75,variable=mygroup,value="75").place(x=610,y=210)
myoptins4=Radiobutton(root, text =100,variable=mygroup,value="100").place(x=610,y=240)



title2 =ttk.Label(root, text="How much of yourself do you give\n in percentage, in 4. html?",font="calibre 9 bold")
title2.place(x=840,y=110 )
mygroup = IntVar()
myoptins1=Radiobutton(root, text =25,variable=mygroup,value="25").place(x=840,y=150)
myoptins2=Radiobutton(root, text =50,variable=mygroup,value="50").place(x=840,y=180)
myoptins3=Radiobutton(root, text =75,variable=mygroup,value="75").place(x=840,y=210)
myoptins4=Radiobutton(root, text =100,variable=mygroup,value="100").place(x=840,y=240)



title2 =ttk.Label(root, text="How much of yourself do you give\n in percentage, in 5. css?",font="calibre 9 bold")
title2.place(x=1070,y=110 )
mygroup = IntVar()
myoptins1=Radiobutton(root, text =25,variable=mygroup,value="25").place(x=1070,y=150)
myoptins2=Radiobutton(root, text =50,variable=mygroup,value="50").place(x=1070,y=180)
myoptins3=Radiobutton(root, text =75,variable=mygroup,value="75").place(x=1070,y=210)
myoptins4=Radiobutton(root, text =100,variable=mygroup,value="100").place(x=1070,y=240)



title1 =ttk.Label(root, text="Where are you from?",font="calibre 9 bold")
title1.place(x=15,y=110 )

myoptins.insert(1," Syria")
myoptins.insert(1,"Turkey")
myoptins.insert(1,"Iraq")
myoptins.insert(1,"Egypt")
myoptins.insert(1,"Germany")

Button1= Button(root,text="Send",fg="red",bg="black",font="calibre 25 bold",command=myfunction)
Button1.place(x=1000,y=500,)






root.mainloop()
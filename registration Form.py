from tkinter import *
from mysql import connector
from tkinter import messagebox


root = Tk()
root.title("LOGIN FORM")
def database():
    conn=connector.connect(
        user="root",
        password="simar2844",
        host="localhost",
        port="3306",
        database="registrationForm")
    mycursor=conn.cursor()
    mycursor.execute("insert into Form(%s,%d,%,s,%d,%s)",entry1.get(),entry2.get(),entry3.get(),var.get,c.get)

b1=Button(root,text='Login',fg='black',command="database")
b1.place(x=80,y=250)
label1 =Label(root,text="S_NO.", fg='Black')
label1.place(x=15,y=20)
entry1=Entry(root)
entry1.place(x=70,y=22)
label2 =Label(root,text="NAME", fg='Black')
label2.place(x=15,y=60)
entry2=Entry(root)
entry2.place(x=70,y=60)
label3 =Label(root,text="ROLL_NO", fg='Black')
label3.place(x=15,y=100)
entry3=Entry(root)
entry3.place(x=70,y=100)
label4 =Label(root,text="GENDER", fg='Black')
label4.place(x=15,y=140)
var=StringVar()
r1=Radiobutton(root,text="Male",value=1,variable=var).place(x=70,y=138)
r2=Radiobutton(root,text="Female",value=2,variable=var).place(x=130,y=138)
#Radiobutton(root,a,)
var.set("choose gender")
label5 =Label(root,text="BRANCH", fg='Black')
label5.place(x=15,y=180)
list_of_Branches=[ 'CSE' ,'ELECTRICAL' , 'CIVIL' ,'MECHANICAL' ,'AUTO MOBILE']
c=StringVar()
droplist=OptionMenu(root,c, *list_of_Branches)
droplist.config(width=15)
c.set('Select your Branch')
droplist.place(x=70,y=175)
#label6 =Label(root,text)
root.mainloop()

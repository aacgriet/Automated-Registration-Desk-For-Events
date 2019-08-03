# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:25:59 2019

@author: K V S Achari
"""

from tkinter import *
import sqlite3
import os
global h
h=0
root=Tk()
root.geometry("3000x3000")
root.title("registration form")


def clo():
     tp.destroy()
     test ="Registration done successfully"
     os.system('espeak "{}"'.format(test,500))
 
          
'''def scs():
    global tp
    if check==1:
        bt.config(state='disabled')
        tp=Toplevel(root)
        tp.geometry("300x300")
        tp.title("terms and conditions")
        label=Label(tp,text="Done sucessfully!",font=("bold",20))
        label.grid(row=0,column=1)
        butn=Button(tp,text="OK",command=clo)
        butn.grid(row=1,column=1)'''
dataVar1 = IntVar()
chkBoxVar = dataVar1.get()   

        
    
        
     
def greyBtnOut():
    

        if chkBoxVar == 1:
            testBtn.config(state='disabled')
                 

        else :
            testBtn.config(state='normal')


def doSomething():
      
        greyBtnOut()

def testBtn():
       
        doSomething()
        resetTestBtn()
        global tp
        global h
        tp=Toplevel(root)
        tp.geometry("1000x1000")
        tp.title("terms and conditions")
        
        label=Label(tp,text="Done sucessfully!",font=("bold",20))
        label.grid(row=0,column=1)
        label=Label(tp,text=" Note registration number",font=("bold",20))
        label.grid(row=1,column=0)
       
        
       
        butn=Button(tp,text="OK",command=clo)
        butn.grid(row=2,column=1)
        fname1=name1.get()
        fname=var1.get()
        fname2=name2.get()
        fname14=var.get()
        fname15=var2.get()
        fname3=name3.get()
        fname4=name4.get()
        fname5=name5.get()
        fname6=name6.get()
        fname7=name7.get()
        fname8=name8.get()
        fname9=name9.get()
        fname10=name10.get()
        fname11=name11.get()
        fname12=name12.get()
        fname13=name13.get()
        conn=sqlite3.connect("student.db")
        with conn:
            cursor=conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Student (name1 TEXT,var1 TEXT,name2 TEXT,var TEXT,var2 TEXT,name3 TEXT,name4 TEXT,name5 TEXT,name6 TEXT,name7 TEXT,name8 TEXT,name9 TEXT,name10 TEXT,name11 TEXT,name12 TEXT,name13 TEXT)")
            cursor.execute("INSERT INTO Student (name1,var1,name2,var,var2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(fname1,fname,fname2,fname14,fname15,fname3,fname4,fname5,fname6,fname7,fname8,fname9,fname10,fname11,fname12,fname13))
            conn.commit()
        entry1.delete(0,END)
        entry4.delete(0,END)
        entry7.delete(0,END)
        entry8.delete(0,END)
        entry9.delete(0,END)
        entry10.delete(0,END)
        entry11.delete(0,END)
        entry12.delete(0,END)
        entry13.delete(0,END)
        entry15.delete(0,END)
        entry16.delete(0,END)
        entry17.delete(0,END)
        entry18.delete(0,END)
        var.set(OPTIONS[0])
        var2.set(OPTIONS[0])
        chkBox.deselect()
        test ="please note the registration number"
        os.system('espeak "{}"'.format(test,500))
        test1 ="insert money"
        os.system('espeak "{}"'.format(test1,1000))
        h=h+1
        variable="GRAAC19"+str(h)
        labei=Label(tp,text=variable,font=(50))
        labei.grid(row=1,column=1)
        
        
def resetTestBtn():
       
        

        if chkBoxVar == 0:
            testBtn.config(state='disabled')
        else:
            doSomething()
        
   
    
    
    
def term():
    global top
    top=Toplevel(root)
    top.geometry("500x500")
    top.title("terms and conditions")
    label=Label(top,text="TERMS AND CONDITIONS:",font=("bold",20))
    label.grid(row=0,column=0)
    label=Label(top,text="1.The amount once paid will not be refunded")
    label.grid(row=1)
    label=Label(top,text="2.Payment doesn't guarantee your selection")
    label.grid(row=2,)
    label=Label(top,text="3.AAC will fund your projects once you are selected")
    label.grid(row=3)
    label=Label(top,text="4.For workshops,AAC will charge you bare minimum")
    label.grid(row=4)
    label=Label(top,text="5.No Re-examination or Re-interview will be conducted")
    label.grid(row=5)
    label=Label(top,text="6.Recommendations will not be entertained")
    label.grid(row=6)
    label=Label(top,text="7.Registering into AAC implies you have agreed to work for")
    label.grid(row=7)
    label=Label(top,text="extra hours than the regular college timings")
    label.grid(row=8)
    but=Button(top,text="OK",command=clos)
    but.grid(row=10)
while True:
    test ="Welcome AAC Registration"
    os.system('espeak "{}"'.format(test,500))
    label1=Label(root,text="Registration Form",fg="black",font=("calibri",20))
    label1.grid(row=0,column=3)
    
    label2=Label(root,text="NAME",font=("arial",10))
    label2.grid(row=1,column=0,padx=10)
    name1=StringVar()
    entry1=Entry(root,textvariable=name1,width=25)
    entry1.grid(row=1,column=1)
    Lb1=Label(text="")
    Lb1.grid(row=2)

    label3=Label(root,text="GENDER",font=("arial",10))
    label3.grid(row=3,column=0)
    var1=IntVar()
    rad1=Radiobutton(root,variable=var1,text="Female",value=1)
    rad1.grid(row=3,column=1)
    rad2=Radiobutton(root,text="Male",variable=var1,value=2)
    rad2.grid(row=3,column=2)
    Lb2=Label(text="")
    Lb2.grid(row=4)

    label4=Label(root,text="ROLLNO",font=("arial",10))
    label4.grid(row=5,column=0,padx=10)
    name2=StringVar()
    entry4=Entry(root,textvariable=name2,width=25)
    entry4.grid(row=5,column=1)
    Lb3=Label(text="")
    Lb3.grid(row=6)


    label5=Label(root,text="BRANCH",font=("arial",10))
    label5.grid(row=7,column=0,padx=10)
    OPTIONS=["   ",
             "CSE",
             "ECE",
             "EEE",
             "IT",
             "ME",
             "NONE",
            ]
    var=StringVar()
    var.set(OPTIONS[0])
    drop=OptionMenu(root,var,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6])
    drop.config(width=10,bg="white")
    drop.grid(row=7,column=1)
    Lb4=Label(text="")
    Lb4.grid(row=8)

    label6=Label(root,text="SECTION",font=("arial",10))
    label6.grid(row=9,column=0,padx=10)
    OPTIONS=["   ",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
       ]
    var2=StringVar()
    var2.set(OPTIONS[0])
    drop=OptionMenu(root,var2,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6])
    drop.config(width=10,bg="white")
    drop.grid(row=9,column=1)
    Lb5=Label(text="")
    Lb5.grid(row=10)

    label7=Label(root,text="PHONE NO",font=("arial",10))
    label7.grid(row=11,column=0,padx=10)
    name3=StringVar()
    entry7=Entry(root,textvariable=name3,width=25)
    entry7.grid(row=11,column=1)
    Lb6=Label(text="")
    Lb6.grid(row=12)

    label8=Label(root,text="PARENTS PHONE NO",font=("arial",10))
    label8.grid(row=13,column=0,padx=10)
    name4=StringVar()
    entry8=Entry(root,textvariable=name4,width=25)
    entry8.grid(row=13,column=1)
    Lb7=Label(text="")
    Lb7.grid(row=14)

    label9=Label(root,text="EMAIL-ID",font=("arial",10))
    label9.grid(row=15,column=0,padx=10)
    name5=StringVar()
    entry9=Entry(root,textvariable=name5,width=25)
    entry9.grid(row=15,column=1)
    Lb8=Label(text="")
    Lb8.grid(row=16)

    label10=Label(root,text="INTER MARKS",font=("arial",10))
    label10.grid(row=17,column=0,padx=10)
    name6=StringVar()
    entry10=Entry(root,textvariable=name6,width=25)
    entry10.grid(row=17,column=1)
    Lb9=Label(text="")
    Lb9.grid(row=18)

    label11=Label(root,text="10th GPA",font=("arial",10))
    label11.grid(row=17,column=2,padx=10)
    name7=StringVar()
    entry11=Entry(root,textvariable=name7,width=25)
    entry11.grid(row=17,column=3)
    Lb9=Label(text="")
    Lb9.grid(row=18)

    label12=Label(root,text="EAMCET RANK",font=("arial",10))
    label12.grid(row=17,column=4,padx=10)
    name8=StringVar()
    entry12=Entry(root,textvariable=name8,width=25)
    entry12.grid(row=17,column=5)
    Lb9=Label(text="")
    Lb9.grid(row=18)

    label13=Label(root,text="JEE-MAINS RANK",font=("arial",10))
    label13.grid(row=19,column=0,padx=10)
    name9=StringVar()
    entry13=Entry(root,textvariable=name9,width=25)
    entry13.grid(row=19,column=1)
    Lb10=Label(text="")
    Lb10.grid(row=20)


    label15=Label(root,text="INTERMEDIATE COLLEGE",font=("arial",10))
    label15.grid(row=19,column=2,padx=10)
    name10=StringVar()
    entry15=Entry(root,textvariable=name10,width=25)
    entry15.grid(row=19,column=3)
    Lb12=Label(text="")
    Lb12.grid(row=20)



    label16=Label(root,text="PERMANENT ADDRESS",font=("arial",10))
    label16.grid(row=19,column=4,padx=10)
    name11=StringVar()
    entry16=Entry(root,textvariable=name11,width=25)
    entry16.grid(row=19,column=5)
    Lb13=Label(text="")
    Lb13.grid(row=20,padx=10)

    label17=Label(root,text="DATE OF FORM",font=("arial",10))
    label17.grid(row=21,column=0,padx=10)
    label18=Label(root,text=" FILLING (DD/MM/YYYY)",font=("arial",10))
    label18.grid(row=22,column=0,padx=10)
    name12=StringVar()
    entry17=Entry(root,textvariable=name12,width=12)
    entry17.grid(row=21,column=1)


    label18=Label(root,text="TIME(HRS:MINS)",font=("arial",10))
    label18.grid(row=21,column=2,padx=10)
    name13=StringVar()
    entry18=Entry(root,textvariable=name13,width=12)
    entry18.grid(row=21,column=3)


    but=Button(root,text="terms & conditions",command=term,relief=RIDGE)
    but.grid(row=23,column=0) 

    


    chkBox = Checkbutton(root, variable=dataVar1, text="terms and conditions", command=doSomething)  
    chkBox.grid(column=1, row=23, padx=10, pady=10)

    testBtn = Button(root, text="Register", bg=('sky blue'),state='disabled',  font=('Calibri Bold', 12), command=testBtn)
    testBtn.grid(column=3, row=24, padx=75, pady=10)   
     
    test ="Welcome AAC Registration"
    os.system('espeak "{}"'.format(test,500))


    root.mainloop()
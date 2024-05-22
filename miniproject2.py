from tkinter import *
from tkinter import ttk
import pymysql
class myclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x800')
        title1=Label(self.root,text='Welcome to NTH Students Information',bd=10,
                    relief='raised' ,font=('copper black ',40),bg='green',fg='white')
        title1.pack(fill='x')
        # creating Variables
        self.rollVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.cnameVar=StringVar()
        self.mobileVar=StringVar()
        self.emailVar=StringVar()
        self.feeVar=StringVar()
        self.qualificationVar=StringVar()

        # creating formlabel
        formframe=Frame(self.root,bg='purple')
        formframe.place(x=10,y=100,width=500,height=700)

        #creating display frame
        displayframe=Frame(self.root,bg='gold')
        displayframe.place(x=520,y=102,width=970,height=700)

        #working on formframe
        title2=Label(formframe,text='Data Entry Here!!!',font=('book antiqua',12),bg='red',fg='white',bd=3,relief='raised')
        title2.grid(row=0,columnspan=2,padx=140,pady=10)

        #roll no
        rollLbl=Label(formframe,text='Enter Roll No: ',font=('book antiqua',12),bg='black',fg='white')
        rollLbl.grid(row=1,column=0,sticky='W')

        rollEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.rollVar)
        rollEntry.grid(row=1,column=1,sticky='W',pady=10)
        # first name
        fnameLb1=Label(formframe,text='Enter First Name: ',font=('book antiqua',12),bg='black',fg='white')
        fnameLb1.grid(row=2,column=0,sticky='W')

        fnameEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.fnameVar)
        fnameEntry.grid(row=2,column=1,sticky='W',pady=10)
        # last name
        lnameLb1=Label(formframe,text='Enter Last Name: ',font=('book antiqua',12),bg='black',fg='white')
        lnameLb1.grid(row=3,column=0,sticky='W')

        lnameEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.lnameVar)
        lnameEntry.grid(row=3,column=1,sticky='W',pady=10)

        #Course
        cnameLb1=Label(formframe,text='Enter Course Name: ',font=('book antiqua',12),bg='black',fg='white')
        cnameLb1.grid(row=4,column=0,sticky='W')

        cnameEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.cnameVar)
        cnameEntry.grid(row=4,column=1,sticky='W',pady=10)

        # mobile number
        mobileLb1=Label(formframe,text='Enter Mobile Number: ',font=('book antiqua',12),bg='black' ,fg='white')
        mobileLb1.grid(row=5,column=0,sticky='W')

        mobileEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.mobileVar)
        mobileEntry.grid(row=5,column=1,sticky='W',pady=10)

        # email id
        emailLb1=Label(formframe,text='Enter Email Id: ',font=('book antiqua',12),bg='black',fg='white')
        emailLb1.grid(row=6,column=0,sticky='W')

        emailEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.emailVar)
        emailEntry.grid(row=6,column=1,sticky='W',pady=10)


        # fee
        feeLb1=Label(formframe,text=' Enter Fee: ',font=('book antiqua',12),bg='black',fg='white')
        feeLb1.grid(row=7,column=0,sticky='W')

        feeEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.feeVar)
        feeEntry.grid(row=7,column=1,sticky='W',pady=10)

        # qualification
        
        quaLb1=Label(formframe,text='Enter  qualification:',font=('book antiqua',12),bg='black',fg='white')
        quaLb1.grid(row=8,column=0,sticky='W')

        quaEntry=Entry(formframe,font=('book antiqua',12),textvariable=self.qualificationVar)
        quaEntry.grid(row=8,column=1,sticky='W',pady=10)


        #button

        buttonframe=Frame(formframe,bg='green')
        buttonframe.place(x=20,y=500,width=460,height=100)

        #add button
        addbtn=Button(buttonframe,text='Add',font=('book antiqua',12),bg='pink',fg='black',command=self.addingdata)
        addbtn.grid(row=0,column=1,padx=20,pady=30)

        # update button
        updbtn=Button(buttonframe,text='Update',font=('book antiqua',12),bg='orange',fg='black',command=self.updatedata)
        updbtn.grid(row=0,column=2,padx=20,pady=30)

        # delete button
        delbtn=Button(buttonframe,text='Delete',font=('book antiqua',12),bg='yellow',fg='black',command=self.deletedata)
        delbtn.grid(row=0,column=3,padx=20,pady=30)

        # clear
        clearbtn=Button(buttonframe,text='Clear',font=('book antiqua',12),bg='red',fg='black',command=self.cleardata)
        clearbtn.grid(row=0,column=4,padx=20,pady=30)

        # working Display frame
        title3=Label(displayframe,text='Data Display Here',font=('book antiqua',12),bg='red',fg='black',relief='raised',bd=3)
        title3.place(x=380,y=10)

        tableFrame=Frame(displayframe,bg='white',bd=3,relief='raised')
        tableFrame.place(x=20,y=45,width=930,height=250)

        self.studentsinfo=ttk.Treeview(tableFrame,columns=('roll','fname','lname','cname','mobile','email','fee','qualification'))

        self.studentsinfo.heading('roll',text='rollNo')
        self.studentsinfo.heading('fname',text='first name')
        self.studentsinfo.heading('lname',text='last name')
        self.studentsinfo.heading('cname',text='course')
        self.studentsinfo.heading('mobile',text='contact')
        self.studentsinfo.heading('email',text='email id')
        self.studentsinfo.heading('fee',text='fee')
        self.studentsinfo.heading('qualification',text='qualification')


        self.studentsinfo.column('roll',width=110,anchor='center')
        self.studentsinfo.column('fname',width=120,anchor='center')
        self.studentsinfo.column('lname',width=150,anchor='center')
        self.studentsinfo.column('cname',width=100,anchor='center')
        self.studentsinfo.column('mobile',width=120,anchor='center')
        self.studentsinfo.column('email',width=120,anchor='center')
        self.studentsinfo.column('fee',width=100,anchor='center')
        self.studentsinfo.column('qualification',width=100,anchor='center')



        self.studentsinfo['show']='headings'

        self.fetchingData()

        self.studentsinfo.pack()
        self.studentsinfo.bind('<ButtonRelease-1>',self.cursorRow)
        

    def addingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db="guidb",charset='utf8')
        c=connection.cursor()
        c.execute('insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s,%s)',
        (
            self.rollVar.get(),
            self.fnameVar.get(),
            self.lnameVar.get(),
            self.cnameVar.get(),
            self.mobileVar.get(),
            self.emailVar.get(),
            self.feeVar.get(),
            self.qualificationVar.get()
            )
                  )
        connection.commit()
        self.fetchingData()
        self.cleardata()
        connection.close()
        
    def cleardata(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db="guidb",charset='utf8')
        c=connection.cursor()
        c.execute('insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s,%s)',
        (
            self.rollVar.set(''),
            self.fnameVar.set(''),
            self.lnameVar.set(''),
            self.cnameVar.set(''),
            self.mobileVar.set(''),
            self.emailVar.set(''),
            self.feeVar.set(''),
            self.qualificationVar.set('')
            )
                  )
    def cursorRow(self,x):
        cursor_row=self.studentsinfo.focus()
        content=self.studentsinfo.item(cursor_row)
        row=content['values']
        self.rollVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.cnameVar.set(row[3])
        self.mobileVar.set(row[4])
        self.emailVar.set(row[5])
        self.feeVar.set(row[6])
        self.qualificationVar.set(row[7])
        
    def updatedata(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db="guidb",charset='utf8')
        c=connection.cursor()
        c.execute('update studentsdata set fname=%s,lname=%s,cname=%s,mobile=%s,email=%s,fee=%s,qualification=%s where rollNo=%s',
             (
              self.fnameVar.get(),
              self.lnameVar.get(),
              self.cnameVar.get(),
              self.mobileVar.get(),
              self.emailVar.get(),
              self.feeVar.get(),
              self.qualificationVar.get(),
              self.rollVar.get()
              )
                  )
        connection.commit()
        self.fetchingData()
        self.cleardata()
        connection.close()

       
        
    def fetchingData(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db="guidb",charset='utf8')
        c=connection.cursor()
        c.execute('select * from studentsdata')
        data=c.fetchall()
        self.studentsinfo.delete(*self.studentsinfo.get_children())
        for i in data:
            self.studentsinfo.insert('',END,value=i)
        connection.commit()
        connection.close()
        
    
    def deletedata(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db="guidb",charset='utf8')
        c=connection.cursor()
        c.execute('delete from studentsdata where rollNo=%s',self.rollVar.get())
        connection.commit()
        self.fetchingData()
        self.cleardata()
        connection.close()
        
        
        
        
        
        
        
        
                        

        










obj=Tk()
x=myclass(obj)

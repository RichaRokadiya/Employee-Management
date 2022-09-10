from sqlite3 import connect
from tkinter import*
from tkinter import ttk
from tokenize import Name, String
from turtle import update
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import re

class Employee: 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        # Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM', font=('arial', 37, 'bold'),fg='darkblue', bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        # logo
        img_logo=Image.open('images/emplogo.jpg')
        img_logo=img_logo.resize((50,50), Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root, image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st img
        img_1=Image.open('images/img1.png')
        img_1=img_1.resize((540,160), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img_1)
        
        self.img_1=Label(img_frame, image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        # 2nd img
        img_2=Image.open('images/img2.jpg')
        img_2=img_2.resize((540,160), Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)
        
        self.img_2=Label(img_frame, image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        # 3rd img
        img_3=Image.open('images/img3.jpg')
        img_3=img_3.resize((540,160), Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)
        
        self.img_3=Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        # Upper Frame..in label frame u can give text, not in just frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information', font=('arial', 11, 'bold'),fg='red', bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department', font=('arial', 11, 'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep, font=('arial', 12, 'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(upper_frame,text='Name:', font=('arial', 12, 'bold'),bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        validate_name = self.root.register(self.checkname)
        txt_name.config(validate='key', validatecommand=(validate_name,'%P'))

        # lbl_Designation
        lbl_Designation=Label(upper_frame,text='Designation:', font=('arial', 12, 'bold'),bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable = self.var_designation, width=22, font=('arial', 11, 'bold'))
        txt_Designation.grid(row=1,column=1,padx=2,pady=7)

        validate_Designation = self.root.register(self.checkdesignation)
        txt_Designation.config(validate='key', validatecommand=(validate_Designation, '%P'))

        # Email
        lbl_email=Label(upper_frame,text='Email:', font=('arial', 12, 'bold'),bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=('arial', 11, 'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)        

        validate_email = self.root.register(self.checkemail)
        txt_email.config(validate='key', validatecommand=(validate_email,'%P'))

        # Address
        lbl_address=Label(upper_frame,text='Address:', font=('arial', 12, 'bold'),bg='white')
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,text='Relationship Status:', font=('arial', 12, 'bold'),bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        com_txt_married=ttk.Combobox(upper_frame, textvariable=self.var_married, state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_married['value']=('Select Marital Status', 'Married', 'Single', 'Divorced')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)
        
        # Dob
        lbl_dob=Label(upper_frame,text='DOB: (dd/mm/yyyy)', font=('arial', 12, 'bold'),bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=('arial', 11, 'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # Doj
        lbl_doj=Label(upper_frame,text='DOJ: (dd/mm/yyyy)', font=('arial', 12, 'bold'),bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=('arial', 11, 'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        # Id Proof
        com_txt_proof=ttk.Combobox(upper_frame,state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_proof['value']=('Select ID Proof','PAN CARD','AADHAR CARD','DRIVING LICENSE')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof=ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame, text='Gender:', font=('arial', 12, 'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame, textvariable=self.var_gender, state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_gender['value']=('Select Gender', 'Female','Male','Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # Phone
        lbl_phone=Label(upper_frame,text='Phone No:', font=('arial', 12, 'bold'),bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=('arial', 11, 'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        validate_phone = self.root.register(self.checkphone)
        txt_phone.config(validate='key', validatecommand=(validate_phone,'%P'))

        # Country
        lbl_ctc=Label(upper_frame, text='Country:', font=('arial', 12, 'bold'),bg='white')
        lbl_ctc.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame, textvariable=self.var_country, width=22, font=('arial', 11, 'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        validate_country = self.root.register(self.checkcountry)
        txt_country.config(validate='key', validatecommand=(validate_country,'%P'))

        # CTC
        lbl_ctc=Label(upper_frame, text='Salary(CTC):', font=('arial', 12, 'bold'),bg='white')
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=('arial', 11, 'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        validate_salary = self.root.register(self.checksalary)
        txt_ctc.config(validate='key', validatecommand=(validate_salary,'%P'))

        # mask image
        img_mask=Image.open('images/emplogo.jpg')
        img_mask=img_mask.resize((220,220), Image.ANTIALIAS)
        self.photomask=ImageTk.PhotoImage(img_mask)
        
        self.img_mask=Label(upper_frame, image=self.photomask)
        self.img_mask.place(x=1000,y=0,width=220,height=220)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(button_frame,text='Save',command=(self.add_data, self.validation), font=('arial',15,'bold'),width=13,fg='white',bg='blue')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='Update',command = self.update_data, font=('arial',15,'bold'),width=13,fg='white',bg='blue')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text='Delete',command = self.delete_data, font=('arial',15,'bold'),width=13,fg='white',bg='blue')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text='Clear',command = self.reset_data, font=('arial',15,'bold'),width=13,fg='white',bg='blue')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        # Down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information Table', font=('arial', 11, 'bold'),fg='red', bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)

        # Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Employee Information', font=('arial', 11, 'bold'),fg='red', bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)        
        
        search_by=Label(search_frame,font=('arial',11,'bold'),width=18,text='Search By:', fg='white',bg='red')
        search_by.grid(row=0,column=0,padx=5)

        # Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame, textvariable=self.var_com_search, state='readonly',font=('arial',12,'bold'),width=18)
        com_txt_search['value']=('Select Option', 'Phone', 'id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=2)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search, width=22, font=('arial', 11, 'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text='Search',command = self.search_data, font=('arial',11,'bold'),width=14,fg='white',bg='blue')
        btn_search.grid(row=0,column=3,padx=5, sticky = W)
        
        btn_ShowAll=Button(search_frame,text='Show All',command = self.fetch_data, font=('arial',11,'bold'),width=14,fg='white',bg='blue')
        btn_ShowAll.grid(row=0,column=4,padx=5, sticky = W)

        stayhome=Label(search_frame,text='Wear a Mask',font=('arial',30,'bold'),width=18,fg='red', bg='white')
        stayhome.place(x=700,y=0,width=600,height=30)
        '''
        img_logo_mask=Image.open(r'images\emplogo.jpg')
        img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        self.photoimg_logo_mask=Image.Tk.PhotoImage(img_logo_mask)

        self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=30)
        '''
        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
    # Call back function check name
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid', 'Not Allowed'+name[-1])
            return False

    # Check Designation
    def checkdesignation(self,designation):
        if designation.isalnum():
            return True
        if designation=='':
            return True
        else:
            messagebox.showerror('Invalid', 'Not Allowed'+designation[-1])
            return False
    
    # Check Email
    def checkemail(self, email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@(a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
                return True
            else:
                messagebox.showwarning('Alert', 'Invalid email, enter valid user email (example: abcdefgh@gmail.com')
                return False
        else:
            messagebox.showinfo('Invalid', 'Email length is too small')

    # Check DOB
    # def checkdob(self, dob):
    #     if   

    # Check Phone
    def checkphone(self, phone):
        if phone.isdigit():
            return True
        if len(str(phone))==0:
            return True
        else:
            messagebox.showerror('Invalid', 'Invalid Entry')
            return False

    # Check Country
    def checkcountry(self,country):
        if country.isalnum():
            return True
        if country=='':
            return True
        else:
            messagebox.showerror('Invalid', 'Not Allowed'+country[-1])
            return False

    # Check Salary
    def checksalary(self, salary):
        if salary.isdigit():
            return True
        if len(str(salary))==0:
            return True
        else:
            messagebox.showerror('Invalid', 'Invalid Entry')
            return False


    # VALIDATION
    def validation(self):
        if self.var_dep.get()=='' or self.var_dep.get()=='Select Department':
            messagebox.showerror('Error', 'Please select your department', parent=self.root)

        elif self.var_name.get()=='':
            messagebox.showerror('Error', 'Please enter your name', parent=self.root)

        elif self.var_designation.get()=='':
            messagebox.showerror('Error', 'Please enter your designation', parent=self.root)

        # elif self.var_email.get()=='':
        #     messagebox.showerror('Error', 'Please enter your email id', parent=self.root)

        elif self.var_address.get()=='':
            messagebox.showerror('Error', 'Please enter your address', parent=self.root)

        elif self.var_married.get()=='' or self.var_married.get()=='Select Marital Status':
            messagebox.showerror('Error', 'Please select your marital status', parent=self.root)

        elif self.var_dob.get()=='':
            messagebox.showerror('Error', 'Please enter your dob', parent=self.root)

        elif self.var_doj.get()=='':
            messagebox.showerror('Error', 'Please enter your doj', parent=self.root)

        elif self.var_idproofcomb.get()=='' or self.var_idproofcomb.get()=='Select ID Proof':
            messagebox.showerror('Error', 'Please select your id proof', parent=self.root)

        elif self.var_idproof.get()=='':
            messagebox.showerror('Error', 'Please enter your id proof', parent=self.root)

        elif self.var_gender.get()=='' or self.var_gender.get()=='Select Gender':
            messagebox.showerror('Error', 'Please select your gender', parent=self.root)

        elif self.var_phone.get()=='' or len(self.var_phone.get())!=10:
            messagebox.showerror('Error', 'Please enter your valid phone no', parent=self.root)

        elif self.var_country.get()=='':
            messagebox.showerror('Error', 'Please enter your country', parent=self.root)

        elif self.var_salary.get()=='':
            messagebox.showerror('Error', 'Please enter your salary', parent=self.root)        

        elif self.var_email.get()!=None:
            x = self.checkemail(self.var_email.get())
    
        # ================= Employee table =================
        # Table Frame
        # table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        # table_frame.place(x=0,y=60,width=1470,height=170)

        # scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # scroll_x.pack(side=BOTTOM,fill=X)
        # scroll_y.pack(side=RIGHT,fill=Y)

        # scroll_x.config(command=self.employee_table.xview)
        # scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'

        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind('<ButtonRelease>', self.get_cursor)

        self.fetch_data()

    # ===================FUnction Declaratn==============

    # Add data
    def add_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='Richa Rokadiya MySQL', password='Bharat#1947', database='employee')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!',parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)                                                                          

    # Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='Richa Rokadiya MySQL', password='Bharat#1947', database='employee')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert('',END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=''):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    # Update data
    def update_data(self):
        if self.var_dep.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update', 'Are you sure you want to update this employee data?')
                if update>0:
                    conn=mysql.connector.connect(host='localhost', username='Richa Rokadiya MySQL', password='Bharat#1947', database='employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s, Name=%s, Designation=%s, Email=%s, Address=%s, Rel_Status=%s, DOB=%s, DOJ=%s, ID_Proof_Type=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s where ID_Proof=%s', (
                        self.var_dep.get(),
                        self.var_name.get(),
                        self.var_designation.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_married.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_idproofcomb.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_country.get(),
                        self.var_salary.get(),
                        self.var_idproof.get(),

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Employee successfully updated', parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    # Delete data
    def delete_data(self):
        if self.var_idproof.get()=='':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete', 'Are you sure you want to delete this employee data?', parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost', username='Richa Rokadiya MySQL', password='Bharat#1947', database='employee')
                    my_cursor = conn.cursor()
                    sql='delete from employee1 where ID_Proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee successfully deleted', parent=self.root)
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    # Reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # Search data
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error', 'Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='Richa Rokadiya MySQL', password='Bharat#1947', database='employee')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
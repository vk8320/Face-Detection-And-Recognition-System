

import string
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Face recognition System")
        self.root.geometry("1530x790+0+0")
        
        ##########vairables
        self.var_dep=StringVar()
        self.var_c=StringVar()
        self.var_y=StringVar()
        self.var_s=StringVar()
        self.var_studentid=StringVar()
        self.var_studentiname=StringVar()
        self.var_class_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_Email=StringVar()
        self.var_phone_number=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       
     
        #first
        img=Image.open("photo/b.jfif") 
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #second  
        img1=Image.open("photo/c.jpg") 
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#third       
        img2=Image.open("photo/b.jfif") 
        img2=img2.resize((555,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=555,height=130)
#forth
        img3=Image.open("photo/a.jfif") 
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1538,height=710)
        
        title_lbl=Label(bg_img,text="STUDENTS DETAILS",font=("times new roman",35,"bold"),bg="orange",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="blue",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open("photo/a.jfif") 
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="blue",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=200)
        #############################
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="blue")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #course
        
      
        
        c_label=Label(current_course_frame,text="course",font=("times new roman",12,"bold"),bg="blue")
        c_label.grid(row=0,column=2,padx=10,sticky=W)
        
        c_combo=ttk.Combobox(current_course_frame,textvariable=self.var_c,font=("times new roman",12,"bold"),state="readonly",width=20)
        c_combo["values"]=("Select course","computer","FE","SE","TE","BE")
        c_combo.current(0)
        c_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #year
        
        
        y_label=Label(current_course_frame,text="year",font=("times new roman",12,"bold"),bg="blue")
        y_label.grid(row=1,column=0,padx=10,sticky=W)
        
        y_combo=ttk.Combobox(current_course_frame,textvariable=self.var_y,font=("times new roman",12,"bold"),state="readonly",)
        y_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semister
        s_label=Label(current_course_frame,text="semister",font=("times new roman",12,"bold"),bg="blue")
        s_label.grid(row=1,column=2,padx=10,sticky=W)
        
        s_combo=ttk.Combobox(current_course_frame,textvariable=self.var_s,font=("times new roman",12,"bold"),state="readonly")
        s_combo["values"]=("Select Semester","semister-1","semister-2")
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #####################
        
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="blue",relief=RIDGE,text="class_student_information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)
        
        studentid_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="blue")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentid,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)
        ##########################
        
      #  studentname_label=Label(class_student_frame,text="studentname:",font=("times new roman",12,"bold"),bg="blue")
       # studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        #studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentid,width=20,font=("times new roman",13,"bold"))
        #studentid_entry.grid(row=0,column=3,padx=10,sticky=W)
        ##########
        
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="blue")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentiname_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentiname,width=20,font=("times new roman",13,"bold"))
        studentiname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        ###########################
        
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="blue")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_class_div,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #################################################
        
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="blue")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #################################################################################3
       
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="blue")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        ##########################
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="blue")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #########
        
        Email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="blue")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #################################
        
        phone_number_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="blue")
        phone_number_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone_number,width=20,font=("times new roman",13,"bold"))
        phone_number_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #####################################################################
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="blue")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        ############################################################################################################################
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="blue")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #####################################
        self.var_radiobtn1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)  
     
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="No1 Photo Sample",value="No")
        radiobtn1.grid(row=6,column=1)   
             
        #####################################################################################################################
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="blue")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.genetrate_datase,text="Take Photo Sample",width=70,font=("times new roman",13,"bold"),bg="red",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
       
        ###################################
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="red",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)
        
        
        img_right=Image.open("photo/a.jfif") 
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
       ################################################# 
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="blue",relief=RIDGE,font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(Search_frame,text="Fetching Data From Database",font=("times new roman",15,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
       
        
        ###############################################################################
        table_frame=Frame(Right_frame,bd=2,bg="orange",relief=RIDGE)
        table_frame.place(x=5,y=210,width=690,height=250)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","c","y","s","studentid","studentiname","class_div","roll_no","gender","dob","Email","phone_number","address","teacher","photo_sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("c",text="Course")
        self.student_table.heading("y",text="Year") 
        self.student_table.heading("s",text="Semister")
        self.student_table.heading("studentid",text="studentID")
        self.student_table.heading("studentiname",text="Student Name")
        self.student_table.heading("class_div",text="Division")
        self.student_table.heading("roll_no",text="Roll No")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="DOB") 
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("phone_number",text="phone number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo_sample",text="Photo Sample Status")
       
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("c",width=100)
        self.student_table.column("y",width=100) 
        self.student_table.column("s",width=100)
        self.student_table.column("studentid",width=100)
        self.student_table.column("studentiname",width=100)
        self.student_table.column("class_div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100) 
        self.student_table.column("Email",width=100)
        self.student_table.column("phone_number",width=100) 
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo_sample",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        ####################################################
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentiname.get()=="" or self.var_studentid.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
         try:
           conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
           my_cursor=conn.cursor()
           my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.var_dep.get(),
                                                                  self.var_c.get(),
                                                                  self.var_y.get(),
                                                                  self.var_s.get(),
                                                                  self.var_studentid.get(),
                                                                  self.var_studentiname.get(),
                                                                  self.var_class_div.get(),
                                                                  self.var_roll_no.get(),
                                                                  self.var_gender.get(),
                                                                  self.var_dob.get(),
                                                                  self.var_Email.get(),
                                                                  self.var_phone_number.get(),
                                                                  self.var_address.get(),
                                                                  self.var_teacher.get(),
                                                                  self.var_radiobtn1.get()
                                                                  
                                                                ))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("success","student details has been added successfully",parent=self.root)
         except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
  #######################################################

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
           
        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                      self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()           
 #####################################################################################
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus) 
      data=content["values"]
      
      self.var_dep.set(data[0]) 
      self.var_c.set(data[1])
      self.var_y.set(data[2]) 
      self.var_s.set(data[3])  
      self.var_studentid.set(data[4])
      self.var_studentiname.set(data[5]) 
      self.var_class_div.set(data[6]) 
      self.var_roll_no.set(data[7])
      self.var_gender.set(data[8]) 
      self.var_dob.set(data[9])
      self.var_Email.set(data[10])
      self.var_phone_number.set(data[11])
      
      self.var_address.set(data[12]) 
      self.var_teacher.set(data[13])  
      self.var_radiobtn1.set(data[14])
      
       
                    
           
 #################################################################################################3
      #update function
    def update_data(self):      
        if self.var_dep.get()=="Select Department" or self.var_studentiname.get()=="" or self.var_studentid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)   
        else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)  
                    if Update>0 :   
                        conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
                        my_cursor=conn.cursor()   
                        my_cursor.execute("update  student set dep=%s,c=%s,y=%s,s=%s,studentiname=%s,class_div=%s,roll_no=%s,gender=%s,dob=%s,Email=%s,phone_number=%s,address=%s,teacher=%s, photo_sample=%s where studentid=%s",(
                                                                  
                                                                  
                                                                  self.var_dep.get(),
                                                                  self.var_c.get(),
                                                                  self.var_y.get(),
                                                                  self.var_s.get(),
                                                                  self.var_studentiname.get(),
                                                                  self.var_class_div.get(),
                                                                  self.var_roll_no.get(),
                                                                  self.var_gender.get(),
                                                                  self.var_dob.get(),
                                                                  self.var_Email.get(),
                                                                  self.var_phone_number.get(),
                                                                  self.var_address.get(),
                                                                  self.var_teacher.get(),
                                                                  self.var_radiobtn1.get(),   
                                                                  self.var_studentid.get()
                                                                       
                                                                ))          
                    else:
                        if not Update:
                         return
                    messagebox.showinfo("success","Student details successfully update comleted",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                   messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
##########################################################################################################################################################3
    def delete_data(self):
         if self.var_studentid.get()=="":
                 messagebox.showerror("Error","student id must be required",parent=self.root)
         else:
                 try:
                         delete=messagebox.askyesno("student Delete page","do you want to delete this student",parent=self.root)
                         if delete>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
                                my_cursor=conn.cursor()
                                sql="delete from student where studentid=%s"
                                val=(self.var_studentid.get(),)
                                my_cursor.execute(sql,val)
                         else: 
                                 if not delete:
                                         return
                         conn.commit()
                         self.fetch_data()    
                         conn.close()                             
                         messagebox.showinfo("delete","successfully student deleated",parent=self.root)
                 except Exception as es:
                       messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
          ############################################################################################################
    def reset_data(self):
          
           self.var_dep.set("Select Department")
           self.var_c.set("Select Course")   
           self.var_y.set("Select Year")
           self.var_s.set("Select Semester")
           self.var_studentid.set("")
           self.var_studentiname.set("")
           self.var_class_div.set("")
           self.var_roll_no.set("")
           self.var_gender.set("")
           self.var_dob.set("")
           self.var_Email.set("")
           self.var_phone_number.set("")
           self.var_address.set("")
           self.var_teacher.set("")
           self.var_radiobtn1.set("")                                                        
                                                                    
          ##############################################################################################
    def genetrate_datase(self):
            if self.var_dep.get()=="Select Department" or self.var_studentiname.get()=="" or self.var_studentid.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)   
            else:
                try:
                   conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("select *from student")
                   myresult=my_cursor.fetchall()
                   id=0
                   for x in myresult:
                           id+=1
                   my_cursor.execute("update  student set dep=%s,c=%s,y=%s,s=%s,studentiname=%s,class_div=%s,roll_no=%s,gender=%s,dob=%s,Email=%s,phone_number=%s,address=%s,teacher=%s, photo_sample=%s where studentid=%s",(
                                                                  
                                                                  
                                                                  self.var_dep.get(),
                                                                  self.var_c.get(),
                                                                  self.var_y.get(),
                                                                  self.var_s.get(),
                                                                  self.var_studentiname.get(),
                                                                  self.var_class_div.get(),
                                                                  self.var_roll_no.get(),
                                                                  self.var_gender.get(),
                                                                  self.var_dob.get(),
                                                                  self.var_Email.get(),
                                                                  self.var_phone_number.get(),
                                                                  self.var_address.get(),
                                                                  self.var_teacher.get(),
                                                                  self.var_radiobtn1.get(),   
                                                                  self.var_studentid.get()==id+1
                                                                       
                                                                ))          
       
                   conn.commit()
                   self.fetch_data()
                   self.reset_data()
                   conn.close()
                        
          ######################################################################3
                            
                   face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                   def face_cropped(img):
                                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                                   #####################
                                   ################
                                   for(x,y,w,h) in faces:
                                           face_cropped=img[y:y+h,x:x+w]
                                           return face_cropped 
                                   
                   cap=cv2.VideoCapture(0)
                   img_id=0
                   while True:
                                   ret,my_frame=cap.read()
                                   if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face=cv2.resize(face_cropped(my_frame),(450,450))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)      
                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("Cropped Face",face)
                                   
                                   if cv2.waitKey(1)==13 or int(img_id)==100:
                                      break
                   cap.release()
                   cv2.destroyAllWindows()
                   messagebox.showinfo("Result","Generating data sets complited!!!!",parent=self.root)                    
                except Exception as es:
                       messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)           
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
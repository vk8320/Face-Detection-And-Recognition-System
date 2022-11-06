

import string
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

from mysqlx import Column

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Face recognition System")
        self.root.geometry("1530x790+0+0")
        
        
        self.var_id=StringVar()
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()
        self.var_name=StringVar()
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
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="blue",relief=RIDGE,text="Student Attendance System",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open("photo/a.jfif") 
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
       
        #####################
        
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="blue",relief=RIDGE,text="Students Attendance Details",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=135,width=750,height=420)
        
        studentid_label=Label(class_student_frame,text="Attendanceid:",font=("times new roman",12,"bold"),bg="blue")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)
        ##########################
        
     
        
        studentname_label=Label(class_student_frame,text="Roll:",font=("times new roman",12,"bold"),bg="blue")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentiname_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",13,"bold"))
        studentiname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        ###########################
        dep_label=Label(class_student_frame,text="Name",font=("times new roman",12,"bold"),bg="blue")
       
        dep_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        dep_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))  
       
        dep_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        ################################################################
        dep_label=Label(class_student_frame,text="Department:",font=("times new roman",12,"bold"),bg="blue")
        dep_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dep_entry=ttk.Entry(class_student_frame,textvariable=self.var_dep,width=20,font=("times new roman",13,"bold"))  
        dep_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        ##########################################################################
        
        
        class_div_label=Label(class_student_frame,text="Time:",font=("times new roman",12,"bold"),bg="blue")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_time,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #################################################
        
        roll_no_label=Label(class_student_frame,text="Date:",font=("times new roman",12,"bold"),bg="blue")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_date,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #################################################################################3
       
        gender_label=Label(class_student_frame,text="Attendance status:",font=("times new roman",12,"bold"),bg="blue")
        gender_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_attendance,width=20,font=("times new roman",13,"bold"))
      
        gender_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#####################################################################3
       




        ##########################
        save_btn=Button(class_student_frame,text="Import",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=4,column=0)
        
        update_btn=Button(class_student_frame,text="Export",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=6,column=0)
        
       
        reset_btn=Button(class_student_frame,command=self.reset_data,text="Reset",width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=10,column=0)
        
        #####################################################################################################################
       
        Right_frame=LabelFrame(main_frame,bd=2,bg="red",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)
        
        
        img_right=Image.open("photo/a.jfif") 
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
       ################################################# 
        
        
     
        
        ###############################################################################
        table_frame=Frame(Right_frame,bd=2,bg="orange",relief=RIDGE)
        table_frame.place(x=5,y=135,width=710,height=330)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AR_table=ttk.Treeview(table_frame,column=("id","roll_no","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AR_table.xview)
        scroll_y.config(command=self.AR_table.yview)
        
        self.AR_table.heading("id",text="Attendanceid")
        self.AR_table.heading("roll_no",text="Roll")
        self.AR_table.heading("name",text="Name")
        self.AR_table.heading("dep",text="Department") 
        self.AR_table.heading("time",text="Time")
        self.AR_table.heading("date",text="Date")
        self.AR_table.heading("attendance",text="Attendance Status")
        self.AR_table.heading("name",text="Name")
       
        self.AR_table["show"]="headings"
        
        self.AR_table.column("id",width=100)
        self.AR_table.column("roll_no",width=100)
        self.AR_table.column("name",width=100)
        self.AR_table.column("dep",width=100) 
        self.AR_table.column("time",width=100)
        self.AR_table.column("date",width=100)
        self.AR_table.column("attendance",width=100)
    
        
        self.AR_table.pack(fill=BOTH,expand=1)
        self.AR_table.bind("<ButtonRelease>",self.get_cursor)
        
       
       ######################3
    def fetch_data(self,rows):
      
                self.AR_table.delete(*self.AR_table.get_children())
                for i in rows:
                      self.AR_table.insert("",END,values=i)
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                   csvread=csv.reader(myfile,delimiter=",")
                   for i in csvread:
                           mydata.append(i)
                   self.fetch_data(mydata)
       ###############################################################################
    #export cSV

    def exportCsv(self):
         try:

           if len(mydata)<1:
  
              messagebox.showerror("No Data", "No Data found to export",parent=self.root)
              return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
           with open(fln,mode="w", newline="") as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
               exp_write.writerow(i)
             messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")
         except Exception as es:
                   messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   
    #######################################
    def get_cursor(self,event=""):
      cursor_row=self.AR_table.focus()
      content=self.AR_table.item(cursor_row) 
      rows=content["values"]
      
      self.var_id.set(rows[0]) 
      self.var_roll_no.set(rows[1])
      self.var_name.set(rows[2]) 
      self.var_dep.set(rows[3]) 
      self.var_time.set(rows[4])  
      self.var_date.set(rows[5])
      self.var_attendance.set(rows[6]) 
    
      
    def reset_data(self):
          
      self.var_id.set("")
      self.var_roll_no.set("") 
      self.var_name.set("")     
      self.var_dep.set("")
      self.var_time.set("")
      self.var_date.set("")
      self.var_attendance.set("")   
      
       
      
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        
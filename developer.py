from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Developer:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")
    
        
        title_lbl=Label(self.root,text="Developer Information",font=("times new roman",35,"bold"),bg="WHITE",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open("photo/b.jfif") 
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)  
      #################################################################3
        main_frame=Frame( f_lbl,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=500,y=0,width=500,height=800)
      
       
        dev_label=Label(main_frame,text='''Education Qualifications
Graduation: -
Bachelor of Science in Computer Science (BSC.CS)
New Arts, Commerce and Science College, Parner
Pune University
Year of completion: 2022
First Year CGPA:8.3/10
Second Year CGPA:8.2/10
Third year appearing
Senior Secondary (XII), Science: -
(HSC board)
Kissan International School and Jr College of Science College, Parner
Maharashtra State Board
Year of completion: 2019
Percentage: 64.92%
Secondary (X): -
(SSC board)
Shri Shivaji Vidyalaya, Ranjangaon Mashid
Maharashtra State Board
Year of completion: 2017
Percentage: 83.20%


''',font=("times new roman",12,"bold"))
        dev_label.place(x=13,y=13)
        
        
       ##################################################################################################################
         #################################################################3
        main_frame1=Frame( f_lbl,bd=2,relief=RIDGE,bg="orange")
        main_frame1.place(x=0,y=0,width=500,height=800)
      
       
        dev_label=Label(main_frame1,text='''Kale Vaibhav
      E-mail: vkale2262@gmail.com
      Mobile No:  +91 7666836077
      Ahmednagar

Personal Details
Name: Kale Vaibhav Manik
Father Name: Manik
Date of Birth: 30, March 2001
Hobbies: I like travelling, playing Cricket also reading Books
Strengths: Ability to work in a team, honesty, Initiative
Weaknesses: Soft Skills (such as public speaking)
Address: At Post Ranjangaon Mashid, Taluka Parner,
District Ahmednagar - 413703

''',font=("times new roman",12,"bold"))
        dev_label.place(x=30,y=30)
        
        
       ##################################################################################################################
        
        
        
        
        
        main_frame2=Frame( f_lbl,bd=2,relief=RIDGE,bg="green")
        main_frame2.place(x=1000,y=0,width=525,height=800)
      
        dev_label=Label(main_frame2,text='''Skills
                Languages   
                     English (Pre-Intermediate), Hindi (Professional),                
                     Marathi (Proficient)
                Beginner                                               Intermediate
                     Python                                                     C Language
                Beginner                                               Intermediate
                     Java Programming                                 HTML 
                Beginner                                               Intermediate
                     PHP                                                            CSS
Thank you ...''',font=("times new roman",12,"bold"))
        dev_label.place(x=25,y=25)
       
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        
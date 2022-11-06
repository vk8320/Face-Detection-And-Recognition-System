from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from matplotlib.pyplot import title
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import face_Recognition
from  developer import Developer
from help import Help
from chatbot import ChatBot
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Face recognition System")
        self.root.geometry("1530x790+0+0")
        
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
        
        title_lbl=Label(bg_img,text="FACE DETECTION",font=("times new roman",35,"bold"),bg="orange",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        ######################################################
        def time():
                string=strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)
        lbl=Label ( title_lbl, font = ('times new roman',14,'bold'),background='orange',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        ###################################
        
        
        
        
        
#button student        
        img4=Image.open("photo/1.jpg") 
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)      
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 
        
        
        #button detect face       
        img5=Image.open("photo/2.jpeg") 
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)      
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="face detecter",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40) 
        
        
         #button Attentance     
        img6=Image.open("photo/a.jfif") 
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)      
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40) 
        
         
        
        
        
        #button train       
        img8=Image.open("photo/vv.jpg") 
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)      
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="train details",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40) 
        
        
        #button photo face      
        img9=Image.open("photo/10.jfif") 
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)      
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="photo face",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40) 
        
        
         #button  developer   
        img10=Image.open("photo/5.jfif") 
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)      
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40) 
        
         #button exit
        img11=Image.open("photo/4.jfif") 
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)      
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40) 
        
       #button help
        #img7=Image.open(r"C:\Users\vkale\Desktop\project\9.jfif") 
        #img7=img7.resize((220,220),Image.ANTIALIAS)
        #self.photoimg7=ImageTk.PhotoImage(img7)      
        
       # b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        #b1.place(x=1100,y=100,width=220,height=220) 
        
        #b1_1=Button(bg_img,text="help",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=300,width=220,height=40) 
    #################################################################
    #chatbot
        img_chat=Image.open("photo/9.jfif") 
        img_chat=img_chat.resize((220,220),Image.ANTIALIAS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)      
        
        b1=Button(bg_img,image=self.photoimg_chat,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="help",command=self.chatbot,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40) 
        #b1_1=Button(bg_img,text="ChatBot",command=self.chatbot,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=300,width=220,height=40) 
            
    
    
    ##########################################
    
    def open_img(self):
            os.startfile("data")
    ##################################################################
    def iExit(self):
            self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
            if self.iExit >0:
                    self.root.destroy()
            else:
                    return        
    
    
    
    
    
    
    
    ######################################################################################    
    def student_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Student(self.new_window)        
        #############################################################################################################
    def train_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Train(self.new_window)       
        
        
        
   #####################################################################################################################################     
        
    def face_data(self):
          self.new_window=Toplevel(self.root)
          self.app=face_Recognition(self.new_window)       
     ############################################################################################################
    def developer_data(self):
              self.new_window=Toplevel(self.root)
              self.app=Developer(self.new_window)       
           ###################################################################################
    def help_data(self):
                  self.new_window=Toplevel(self.root)
                  self.app=Help(self.new_window)  
      #####################################################3  
    def chatbot(self):
            self.new_window=Toplevel(self.root)
            self.app=ChatBot(self.new_window)   
   #########################################################################
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)        
        ################################################
        
if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()
            
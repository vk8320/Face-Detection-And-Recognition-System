from tkinter import *
from tkinter import ttk
from tokenize import Name
from unicodedata import name
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class face_Recognition:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="WHITE",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open("photo/a.jfif") 
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        #############################################
        #######################################
        img_bottom=Image.open("photo/a.jfif") 
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40) 
        ######################################################
        
    def mark_attendance(self,s,i,n,d):
            with open("attendance_report/vaibhav.csv","r+",newline="\n")as f:
              myDataList=f.readlines()
              name_list=[] 
              for line in myDataList:
                   entry=line.split((",")) 
                   name_list.append(entry[0])
              if((s not in name_list) and (i not in name_list) and (n not in name_list) and(d not in name_list)):
                  now=datetime.now()
                  d1=now.strftime("%d/%m/%Y")
                  dtString=now.strftime("%H:%M:%S")
                  f.writelines(f"\n{s},{i},{n},{d},{dtString},{d1},Present")
        #####################################################################
        
    def face_recog(self):  
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for(x,y,w,h) in features:
             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
             id,predict=clf.predict(gray_image[y:y+h,x:x+w])
             confidence=int((100*(1-predict/300)))
             conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="face_recognizer")
             my_cursor=conn.cursor()
             
             my_cursor.execute("select studentid from  student where studentid="+str(id))
             s=my_cursor.fetchone()
             s="+".join(s)
             my_cursor.execute("select roll_no from  student where studentid="+str(id))
             i=my_cursor.fetchone()
             i="+".join(i)
             my_cursor.execute("select studentiname from  student where studentid="+str(id))
             n=my_cursor.fetchone()
             n="+".join(n)
             my_cursor.execute("select dep from  student where studentid="+str(id))
             d=my_cursor.fetchone()
             d="+".join(d)
             if confidence>77:   
                 cv2.putText(img,f":(S_ID:{s})",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f":(Roll_NO:{i})",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f":(Name:{n})",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f":(Department:{d})",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 
                 self.mark_attendance(s,i,n,d)
             else:
                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                 cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)   
                   
                   
                   
                   
                   
                   
                        
             coord=[x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,250),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
    
        while True:
          ret,img=video_cap.read() 
          img=recognize(img,clf,faceCascade)
          cv2.imshow("Welcome To Recognition",img)
        
          if cv2.waitKey(1)==13:
            break
        video_cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    root=Tk()
    obj=face_Recognition(root)
    root.mainloop()                
        
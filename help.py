from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")
          
          
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="WHITE",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open("photo/10.jfif") 
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)  
      
        dev_label=Label(f_lbl,text="E-mail:vkale2262@gmail.com ",font=("times new roman",12,"bold"),fg="blue",bg="white")
        dev_label.place(x=650,y=360)
      
      
      
      
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()        
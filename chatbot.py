from cProfile import label
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class ChatBot:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("730x620+0+0")
       
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)
        
        
        
        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()
        
        
        
        img_chat=Image.open('photo/c.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)               
      
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type something",font=('arial',14,'bold'),fg='green',bg='white')        
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="send>>",command=self.send,font=('arial',14,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',14,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')        
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
        
        
        
   
    ###################################################################################3
   
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
       
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
   
   
   
   
   
   
   
   
    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)    
        self.text.yview(END)
        
        
        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')
          
        if(self.entry.get()=="hello"):
            self.text.insert(END,"\n\n"+"Bot:Hi")
            
        
        elif (self.entry.get()=="how are you"):
            self.text.insert(END,"\n\n"+"Bot:fine and you")
            
        elif (self.entry.get()=="Fantastic"):
                self.text.insert(END,"\n\n"+"Bot:Nice to Hear")
                
        elif (self.entry.get()=="who created you?"):
                self.text.insert(END,"\n\n"+"Bot:mr.vaibhav")
                
        elif (self.entry.get()=="what is your name"):
                self.text.insert(END,"\n\n"+"Bot:my name is mr.vaibhav")
                    
        elif (self.entry.get()=="can you speak marathi"):
                self.text.insert(END,"\n\n"+"Bot:I'm still learning it....")
                
        elif (self.entry.get()=="what is machine learning"):
                self.text.insert(END,"\n\n"+"Bot:I'm still learning it....")
        else:
            self.text.insert(END,"\n\n"+"Bot:sorry I dindn't get it...............")
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()        
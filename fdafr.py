from re import I
from tkinter import*
from tkinter import ttk
from winreg import QueryInfoKey
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from matplotlib.pyplot import get
from soupsieve import select
from main import Face_Recognition_System
def main():
        win=Tk()
        app=Login_window(win)
        win.mainloop()

  
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
       

        self.bg=ImageTk.PhotoImage(file="photo/vvv.jpg") 
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open("photo/kkk (1).webp")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
     
     ######################################################3
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="blue",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"),)
        self.txtuser.place(x=40,y=180,width=270)
  ###############################################################################
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="blue",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

###############################################3
        img2=Image.open("photo/kkk (1).webp")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open("photo/kkk (1).webp")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=394,width=25,height=25)


################
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="blue",activeforeground="black",activebackground="yellow")
        loginbtn.place(x=110,y=300,width=120,height=35)
############################################################################
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="orange",bg="white",activeforeground="white",activebackground="blue")
        registerbtn.place(x=12,y=350,width=160)

#############################################
        loginbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="green",bg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=12,y=370,width=160)
        
    def rigister_window(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)
                
        
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
         messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Kale" and self.txtpass.get()=="123":
         messagebox.showinfo("Success","Wlecome")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="mydata")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                          self.txtuser.get(),
                                                                                          self.txtpass.get()
                                                                        
                                                                                         
                                                                                ))                          
             row=my_cursor.fetchone()
             if row==None:
                     messagebox.showerror("Error","Invalid Username and password")
             else:
                     open_main=messagebox.askyesno("YesNo","Access only admin")
                     if open_main>0:
                             self.new_window=Toplevel(self.root)
                             self.app=Face_Recognition_System(self.new_window)
                     else:
                             if not open_main:
                                     return
             conn.commit()
             conn.close() 
            ###############################################################
    def reset_pass(self):
            if self.combo_security_Q.get()=="Select":
                    messagebox.showerror("Error","Select The Security question",parent=self.root2)
            elif self.txt_security.get()=="":
                    messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
            elif self.txt_newpass.get()=="":
                    messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
            else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="mydata")
                    my_cursor=conn.cursor()
                    query=("select * from register where email=%s and securityQ=%s and securityA=%s") 
                    value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    if row==None:
                            messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
                    else:
                            query=("update register set password=%s where email=%s")
                            value=(self.txt_newpass.get(),self.txtuser.get())
                            my_cursor.execute(query,value)
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Success","Your Password Has Been Reset,Please Login New password",parent=self.root2)                                    
                            self.root2.destroy()
             
             
             
             
              
             ##############################################################
    def forgot_password_window(self):
            if self.txtuser.get()=="":
                    messagebox.showerror("Error","Please Enter the  address to reset password")
            else:        
               conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="mydata")
               my_cursor=conn.cursor()
               query=("select * from register where email=%s")
               value=(self.txtuser.get(),)
               my_cursor.execute(query,value)
               row=my_cursor.fetchone()
               #print(row)
               if row==None:
                       messagebox.showerror("My Error","Please enter The valid Username")
               else:
                       conn.close()
                       self.root2=Toplevel()
                       self.root2.title("Forgot Password")
                       self.root2.geometry("340x450+610+170")
                        
                       lbl=Label(self.root2,text="Forgot Password",font=("times new roman",25,"bold"),fg="red",bg="white")
                       lbl.place(x=0,y=10,relwidth=1)
                       security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                       security_Q.place(x=50,y=80)
       
                       self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                       self.combo_security_Q["values"]=("Select","your Birth Place","your mother name","your pet name")
                       self.combo_security_Q.place(x=50,y=110,width=250)
                       self.combo_security_Q.current(0)
       
       
        #############################################################################
                       security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                       security_A.place(x=50,y=150)
        
                       self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                       self.txt_security.place(x=50,y=180,width=250) 
                       #############################                      
                       new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                       new_password.place(x=50,y=220)
        
                       self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                       self.txt_newpass.place(x=50,y=250,width=250)
             
             
             
             
                       btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                       btn.place(x=100,y=290)          
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                          
#######################################################################################################
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("16000x900+0+0")
        ################################################################################
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
                
        
        
        
        
        
        
        
       ############################################################### 
        self.bg=ImageTk.PhotoImage(file="photo/8788.png") 
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
      ####################################################  
        self.bg1=ImageTk.PhotoImage(file="photo/nnn.jpg") 
        lbl_left=Label(self.root,image=self.bg1)
        lbl_left.place(x=50,y=100,width=470,height=650)
        
       ########################################################################### 
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=650)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)
        ############################################################
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        ############################################
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        ##############################################################3
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        ######################################################
        email=Label(frame,text="E-mail",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        ###############################################
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
       
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","your Birth Place","your mother name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
       
       
        #############################################################################
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        ###################################################################################
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        ##############################################################################################################
        confirm_pswd=Label(frame,text="Conform Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        ################################################################################################################################
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agree The Trems & Conditions",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
    ######################################################################
        img=Image.open("photo/8788.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)        
        rn=Label(frame,text="Register Now",font=("times new roman",15,"bold"),bg="white")
        rn.place(x=0,y=480,width=250)
      ################################################
        img1=Image.open("photo/8788.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)   
        ln=Label(frame,text="Login Now",font=("times new roman",15,"bold"),bg="white")
        ln.place(x=320,y=480,width=250)

        ####################################################
    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","password & confirm password must be same")   
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms & condition")
            else:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Vaibhavk@123",database="mydata")
                 my_cursor=conn.cursor()
                 query=("select * from register where email=%s")
                 value=(self.var_email.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()
                 if row!=None:
                     messagebox.showerror("Error","User already exist,please try another email")
                 else:
                     my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_fname.get(),
                                                                                             self.var_lname.get(),
                                                                                             self.var_contact.get(),
                                                                                             self.var_email.get(),
                                                                                             self.var_securityQ.get(),
                                                                                             self.var_securityA.get(),
                                                                                             self.var_pass.get(),
                                                                                                                                                                             
                         
                                                                                         ))    
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
            self.root.destroy()











if __name__ == "__main__":
   main()
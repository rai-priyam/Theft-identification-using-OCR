#from _typeshed import Self
from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #==Bg Image==
        self.bg=ImageTk.PhotoImage(file="images/b5.png")
        # self.bg=ImageTk.PhotoImage(file="C:/Users/HP/ProjectFinal/images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #==Left Image==
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=50,width=400,height=720)

        #==Register Frame==
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=50,width=1000, height=720)

        title=Label(frame1, text = "REGISTER HERE", font=("orbitron",20,"bold"),bg="white", fg = "green").place(x=50,y=30)

        #-------------------------Row 1
        
        f_name=Label(frame1, text = "First Name", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_fname.place(x=50,y=130,width=200)

        l_name=Label(frame1, text = "Last Name", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=100)
        self.txt_lname=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_lname.place(x=350,y=130,width=200)

        contact=Label(frame1, text = "Phone", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=650,y=100)
        self.txt_contact=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_contact.place(x=650,y=130,width=200)

        #------------------------Row 2
        
        email=Label(frame1, text = "Email", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=170)
        self.txt_email=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_email.place(x=50,y=200,width=200)

        password=Label(frame1, text = "Password", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=170)
        self.txt_password=Entry(frame1,show='*',font=("Segeo UI",13),bg="white")
        self.txt_password.place(x=350,y=200,width=200)

        cpassword=Label(frame1, text = "Confirm Password", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=650,y=170)
        self.txt_cpassword=Entry(frame1,show='*',font=("Segeo UI",13),bg="white")
        self.txt_cpassword.place(x=650,y=200,width=200)

        #------------------------Row 3

        question=Label(frame1, text = "Security Question", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("Segeo UI",11),state='readonly',justify=LEFT)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name","Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=200)
        self.cmb_quest.current(0)

        answer=Label(frame1, text = "Answer", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=240)
        self.txt_answer=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_answer.place(x=350,y=270,width=200)

        #------------------------Row 4

        line=Label(frame1, text = "VEHICLE INFORMATION HERE", font=("orbitron",16,"bold"),bg="white", fg = "blue").place(x=50,y=330)

        #------------------------Row 5

        v_no=Label(frame1, text = "Vehicle Number", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=390)
        self.txt_vno=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_vno.place(x=50,y=420,width=200)

        v_type=Label(frame1, text = "Vehicle Type", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=390)
        self.txt_vtype=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_vtype.place(x=350,y=420,width=200)

        brand=Label(frame1, text = "Vehicle Brand", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=650,y=390)
        self.txt_brand=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_brand.place(x=650,y=420,width=200)

        #------------------------Row 6

        vcol=Label(frame1, text = "Vehicle Color", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=450)
        self.txt_vcol=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_vcol.place(x=50,y=480,width=200)

        regd=Label(frame1, text = "Registration Date", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=450)
        self.txt_regd=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_regd.place(x=350,y=480,width=200)

        vald=Label(frame1, text = "Validity Date", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=650,y=450)
        self.txt_vald=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_vald.place(x=650,y=480,width=200)

        #------------------------Row 7

        eno=Label(frame1, text = "Engine Number", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=50,y=510)
        self.txt_eno=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_eno.place(x=50,y=540,width=200)

        cno=Label(frame1, text = "Chassis Number", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=350,y=510)
        self.txt_cno=Entry(frame1,font=("Segeo UI",13),bg="white")
        self.txt_cno.place(x=350,y=540,width=200)

        stat=Label(frame1, text = "Theft Status", font=("orbitron",13,"bold"),bg="white", fg = "grey").place(x=650,y=510)
        self.cmb_stat=ttk.Combobox(frame1,font=("Segeo UI",11),state='readonly',justify=LEFT)
        self.cmb_stat['values'] = ("Select", "Stolen","Not Stolen")
        self.cmb_stat.place(x=650,y=540,width=200)
        self.cmb_stat.current(0)

        #==========Terms=============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I have read and agree to the Terms and Conditions",variable=self.var_chk,onvalue=1, offvalue=0,bg="white", font = ("calibri", 12)).place(x=50,y=590)
        
        self.btn=Button(frame1, text="Register Now", padx= 50, font = ("orbitron", 15 , "bold"),bg="blue", fg="white", cursor="hand2",command=self.register_data).place(x=50,y=630)

        btn_login=Button(self.root, text="Sign In",command=self.login_window, padx= 80, font = ("orbitron", 15 , "bold"),bg="white", fg="grey", cursor="hand2").place(x=160,y=680)
    
    def login_window(self):
        self.root.destroy()
        import login
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_vno.delete(0,END)
        self.txt_vtype.delete(0,END)
        self.txt_brand.delete(0,END)
        self.txt_vcol.delete(0,END)
        self.txt_regd.delete(0,END)
        self.txt_vald.delete(0,END)
        self.txt_eno.delete(0,END)
        self.txt_cno.delete(0,END)
        self.cmb_quest.current(0)
        self.cmb_stat.current(0)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_vno.get()=="" or self.txt_vtype.get()=="" or self.txt_brand.get()=="" or self.txt_vcol.get()=="" or self.txt_regd.get()=="" or self.txt_vald.get()=="" or self.txt_eno.get()=="" or self.txt_cno.get()=="" or self.cmb_stat.get()=="Select":
            messagebox.showerror("Error","All fields are Required.",parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same.",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree to our Terms & Conditions.",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s", self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exist. Try with another Email.",parent=self.root)

                else:    
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password,vno,vtype,brand,vcol,regd,vald,eno,cno,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get(),
                                    self.txt_vno.get(),
                                    self.txt_vtype.get(),
                                    self.txt_brand.get(),
                                    self.txt_vcol.get(),
                                    self.txt_regd.get(),
                                    self.txt_vald.get(),
                                    self.txt_eno.get(),
                                    self.txt_cno.get(),
                                    self.cmb_stat.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registeration Successful",parent=self.root)
                    self.clear()                 

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()
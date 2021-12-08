from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #==Bg Image==
        self.bg=ImageTk.PhotoImage(file="images/b6.jpg")
        # self.bg=ImageTk.PhotoImage(file="C:/Users/HP/ProjectFinal/images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #==Left Image==
        self.left=ImageTk.PhotoImage(file="images/side2.jpg")
        left=Label(self.root,image=self.left).place(x=180,y=100,width=400,height=620)

        #==Register Frame==
        frame1=Frame(self.root,bg="black")
        frame1.place(x=580,y=100,width=800, height=620)

        title=Label(frame1, text = "SIGN IN", font=("orbitron",30,"bold"),bg="black", fg = "yellow").place(x=60,y=60)

        email=Label(frame1, text = "Email Address", font=("orbitron",20,"bold"),bg="black", fg = "lightblue").place(x=60,y=150)
        self.txt_email=Entry(frame1, font=("Segeo UI",15),bg="black", fg = "white")
        self.txt_email.place(x=60,y=200,width=400,height=30)

        pass_=Label(frame1, text = "Password", font=("orbitron",20,"bold"),bg="black", fg = "lightblue").place(x=60,y=250)
        self.txt_pass_=Entry(frame1, show='*',font=("Segeo UI",15),bg="black", fg = "white")
        self.txt_pass_.place(x=60,y=300,width=400,height=30)

        btn_reg=Button(frame1,text="Sign Up",command=self.register_window,padx=25,font=("orbitron",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=270, y=380)

        btn_login=Button(frame1,text="Login",command=self.login,padx=25,font=("orbitron",20,"bold"),bg="blue",fg="white",cursor="hand2").place(x=60, y=380)

        

    def register_window(self):
        self.root.destroy()
        import register

    # def login_window(self):
    #     self.root.destroy()
    #     import display
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required", parent = self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="", database="employee2")
                cur=con.cursor()
                eid = self.txt_email.get()
                #print(eid)
                cur.execute("select * from employee where email=%s and password=%s",(eid, self.txt_pass_.get()))
                row=cur.fetchone()
                # fetch_query = "select * from employee where email='{}'".format(eid)
                # print(cur.execute(fetch_query))
                print(cur.execute("select * from employee where email='{}'".format(self.txt_email.get())))
                row=cur.fetchone()
                self.root.destroy()
                import guifinal



                if row == None:
                    messagebox.showerror("Error","Invalid Username or Password.", parent = self.root)
                    
                else:
                    command=self.display
                    
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent = self.root)    
    




root=Tk()
obj=Login_window(root)
root.mainloop()
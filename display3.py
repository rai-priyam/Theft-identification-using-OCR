from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Theft Identification Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")

        title = Label(self.root,text="Theft Identification System",font=("orbitron",40,"bold"),bg="black",fg="white")
        title.pack(side=TOP)

        #============All Variables===============
        self.vno_var=StringVar()
        self.name_var=StringVar()
        self.contact_var=StringVar()
        self.brand_var=StringVar()
        self.vcol_var=StringVar()
        self.vtype_var=StringVar()
        self.eno_var=StringVar()
        self.cno_var=StringVar()
        self.vstat_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()




        #=========Manage Frame=============================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_Frame.place(x=20,y=100,width=450,height=650)

        m_title = Label(Manage_Frame,text="Manage Victims", font=("orbitron",20,"bold"),fg="black")
        m_title.grid(row=0,columnspan=2,padx=90,pady=20)

        v_no=Label(Manage_Frame,text="Vehicle Number", font=("orbitron",12,"bold"),fg="black")
        v_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_vno=Label(Manage_Frame,textvariable=self.vno_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_vno.grid(row=1,column=1,pady=10,padx=20,sticky="w")  

        name=Label(Manage_Frame,text="Owner's Name", font=("orbitron",12,"bold"),fg="black")
        name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Label(Manage_Frame,textvariable=self.name_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        contact=Label(Manage_Frame,text="Contact", font=("orbitron",12,"bold"),fg="black")
        contact.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Label(Manage_Frame,textvariable=self.contact_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_contact.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        brand=Label(Manage_Frame,text="Brand", font=("orbitron",12,"bold"),fg="black")
        brand.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_brand=Label(Manage_Frame ,textvariable=self.brand_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_brand.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        vcol=Label(Manage_Frame,text="Color", font=("orbitron",12,"bold"),fg="black")
        vcol.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_vcol=Label(Manage_Frame,textvariable=self.vcol_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_vcol.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        vtype=Label(Manage_Frame,text="Vehicle Type", font=("orbitron",12,"bold"),fg="black")
        vtype.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_vtype=Label(Manage_Frame,textvariable=self.vtype_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_vtype.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        eno=Label(Manage_Frame,text="Engine Number", font=("orbitron",12,"bold"),fg="black")
        eno.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_eno=Label(Manage_Frame,textvariable=self.eno_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_eno.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        cno=Label(Manage_Frame,text="Chassis Number", font=("orbitron",12,"bold"),fg="black")
        cno.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        txt_cno=Label(Manage_Frame,textvariable=self.cno_var, font=("Segeo UI",12,"bold"),fg="black")
        txt_cno.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
        # combo_vtype=ttk.Combobox(Manage_Frame,textvariable=self.vtype_var,font=("Segeo UI",12,"bold"),state='readonly')
        # combo_vtype['values']=("2 Wheeler","4 Wheeler")
        # combo_vtype.grid(row=6,column=1,pady=10,padx=20)

        vstat=Label(Manage_Frame,text="Vehicle Status", font=("orbitron",12,"bold"),fg="black")
        vstat.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        combo_vstat=ttk.Combobox(Manage_Frame,textvariable=self.vstat_var,font=("Segeo UI",12,"bold"),state='readonly')
        combo_vstat['values']=("Stolen","Recovered")
        combo_vstat.grid(row=9,column=1,pady=10,padx=20)

        #=================Button Frame=====================
        btn_Frame=Frame(Manage_Frame)
        btn_Frame.place(x=20,y=500,width=400)

        #Addbtn=Button(btn_Frame,text="Add",width=7,command=self.add_users,font=("orbitron",10,"bold")).grid(row=0,column=0,padx=10, pady=10)
        Updtbtn=Button(btn_Frame,text="Update Status",width=12,command=self.update_data,font=("orbitron",10,"bold")).grid(row=0,column=1,padx=10, pady=10)
        Delbtn=Button(btn_Frame,text="Delete Data",width=10,command=self.delete_data,font=("orbitron",10,"bold")).grid(row=0,column=2,padx=10, pady=10)
        Clebtn=Button(btn_Frame,text="Clear ",width=10,command=self.clear,font=("orbitron",10,"bold")).grid(row=0,column=3,padx=10, pady=10)


        #=========Detail Frame=============================    
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Detail_Frame.place(x=500,y=100,width=1000,height=650)

        lbl_search=Label(Detail_Frame,text="Search By", font=("orbitron",12,"bold"),fg="black")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("Segeo UI",12,"bold"),state='readonly')
        combo_search['values']=("vno","f_name","contact","status")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("orbitron",12,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=10,pady=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data,font=("orbitron",10,"bold")).grid(row=0,column=3,padx=10, pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data,font=("orbitron",10,"bold")).grid(row=0,column=4,padx=10, pady=10)

        #===============Table Frame===========================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=70,width=970,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.User_table=ttk.Treeview(Table_Frame,columns=("vno","name","contact","brand","vcol","vtype","eno","cno","vstat","time","date","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.User_table.xview)
        scroll_y.config(command=self.User_table.yview)
        self.User_table.heading("vno",text="Vehicle Number")
        self.User_table.heading("name",text="Owner's Name")
        self.User_table.heading("contact",text="Contact")
        self.User_table.heading("brand",text="Brand")
        self.User_table.heading("vcol",text="Color")
        self.User_table.heading("vtype",text="Vehicle Type")
        self.User_table.heading("eno",text="Engine Number")
        self.User_table.heading("cno",text="Chassis Number")
        self.User_table.heading("vstat",text="Vehicle Status")
        self.User_table.heading("time",text="Time of Theft")
        self.User_table.heading("date",text="Date of Theft")
        self.User_table.heading("address",text="Area of Theft")
        self.User_table['show']='headings'
        self.User_table.column("vno",width=150)
        self.User_table.column("name",width=100)
        self.User_table.column("contact",width=150)
        self.User_table.column("brand",width=100)
        self.User_table.column("vcol",width=100)
        self.User_table.column("vtype",width=100)
        self.User_table.column("eno",width=100)
        self.User_table.column("cno",width=100)
        self.User_table.column("vstat",width=100)
        self.User_table.column("time",width=100)
        self.User_table.column("date",width=100)
        self.User_table.column("address",width=150)
        self.User_table.pack(fill=BOTH,expand=1)
        self.User_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #===========Add Data============================
    # def add_users(self):
    #     con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
    #     cur=con.cursor()
    #     cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)"(
    #         self.vno_var.get(),
    #         self.name_var.get(),
    #         self.contact_var.get(),
    #         self.brand_var.get(),
    #         self.vcol_var.get(),
    #         self.vtype_var.get(),
    #         self.vstat_var.get()))

    #     con.commit()
    #     self.fetch_data()
    #     self.clear()
    #     con.close()

    #===========Fetch Data============================
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
        cur=con.cursor()
        cur.execute("select vno,f_name,contact,brand,vcol,vtype,eno,cno,status,time,date,address from employee")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.User_table.delete(*self.User_table.get_children())
            for row in rows:
                self.User_table.insert('',END,values=row)
            con.commit()
        con.close()

    #===========Clear Data============================
    def clear(self):
        self.vno_var.set("")
        self.name_var.set("")
        self.contact_var.set("")
        self.brand_var.set("")
        self.vcol_var.set("")
        self.vtype_var.set("")
        self.eno_var.set("")
        self.cno_var.set("")
        self.vstat_var.set("") 

    #===========Fetch Data inManage Victim Frame============================
    def get_cursor(self,ev):
        cursor_row=self.User_table.focus()
        contents=self.User_table.item(cursor_row)
        row=contents['values']
        self.vno_var.set(row[0])
        self.name_var.set(row[1])
        self.contact_var.set(row[2])
        self.brand_var.set(row[3])
        self.vcol_var.set(row[4])
        self.vtype_var.set(row[5])
        self.eno_var.set(row[6])
        self.cno_var.set(row[7])
        self.vstat_var.set(row[8]) 
      
    #===========Update Data============================
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
        cur=con.cursor()
        cur.execute("update employee set status=%s where vno=%s",(
            self.vstat_var.get(),
            self.vno_var.get()))
        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    #===========Delete Data============================
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
        cur=con.cursor()
        cur.execute("delete from employee where vno=%s",self.vno_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
        cur=con.cursor()

        cur.execute("select vno,f_name,contact,brand,vcol,vtype,eno,cno,status,time,date,address from employee where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.User_table.delete(*self.User_table.get_children())
            for row in rows:
                self.User_table.insert('',END,values=row)
            con.commit()
        con.close()    

root=Tk()
ob=Student(root)
root.mainloop()

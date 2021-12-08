import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
import numpy as np
import cv2
import pytesseract
import imutils
import pymysql

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
res_text=[]
top=tk.Tk()
top.geometry('1920x1080')
top.title('Number Plate Recognition')
bg = PhotoImage(file="images/b5.png")
canvas1 = Canvas(top, width=1920, height=1080)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")
label=Label(top,background='#CDCDCD', font=('arial',35,'bold'))
sign_image = Label(top)
plate_image=Label(top)

def classify(file_path):
    img = cv2.imread(file_path)
    img = cv2.resize(img, (400, 200))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 13, 15, 15)

    edged = cv2.Canny(gray, 30, 200)

    contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None

    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

        if screenCnt is None:
            detected = 0
            print("No contour detected")
        else:
            detected = 1

        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
    text = pytesseract.image_to_string(Cropped, config='--psm 11')

    print("Detected license plate Number is:", text)
    
    T = Text(top, height = 1, width = 30,font=("arial", 16, "bold"),pady=10)
    cls = Label(top, text="Detected license plate Number is:", font=("arial", 13, "bold"))
    cls.place(x=800,y=300)

    T.pack()
    T.place(x=800,y=350)
    T.insert(tk.END, text)
    def check():
        plate_no = T.get(1.0,"end-3c")
        #print(plate_no)
        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
        cur=con.cursor()
        cur.execute("select status from employee where vno LIKE '%{}%'".format(plate_no))
        for veh in cur.fetchone():
            listoutput = veh
        check_print = Label(top, text="Vehicle is ",font=('arial',15,'bold'))
        check_print.place(x=800,y=400)
        check_ans = Label(top, text=listoutput,font=('arial',15,'bold'))
        check_ans.place(x=900,y=400)
        con.commit()
        con.close()
            
        def report_stolen():
            tim=Label(top, text ="Time of Theft",font=('arial',15,'bold'))
            tim.place(x=800,y=500)
            thef=Entry(top,font=('arial',15,'bold'))
            thef.place(x=950,y=500,width=200)
            
            dat=Label(top, text = "Date of Theft",font=('arial',15,'bold')) 
            dat.place(x=800,y=550)
            da=Entry(top,font=('arial',15,'bold'))
            da.place(x=950,y=550,width=200)
            
            addr=Label(top, text = "Area of Theft",font=('arial',15,'bold'))
            addr.place(x=800,y=600)
            add=Entry(top,font=('arial',15,'bold'))
            add.place(x=950,y=600,width=200)

            def add_details():
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("update employee set time='{}', date='{}' ,address='{}' where vno LIKE '%{}%'".format(thef.get(),da.get(),add.get(),plate_no))
                con.commit()
                con.close()
            submit=Button(top,text="Submit",command=add_details,padx=10,pady=5)
            submit.configure(background='#364156', foreground='white',font=('arial',15,'bold'))
            submit.pack()
            submit.place(x=900,y=650)


        report = Button(top,text="Report stolen",command=report_stolen,padx=23,pady=5)
        report.configure(background='#364156', foreground='white',font=('arial',15,'bold'))
        report.place(x=100,y=700)


    search = Button(top,text="Check Status",command =check, padx=17,pady=5)
    search.configure(background='#364156', foreground='white',font=('arial',15,'bold'))
    search.place(x=350,y=700)


        




    

    # uploaded=Image.open("result.png")
    # im=ImageTk.PhotoImage(uploaded)

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',15,'bold'))
    classify_b.place(x=350,y=610)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
        img = cv2.imread(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',15,'bold'))
upload.pack()
upload.place(x=100,y=610)



sign_image.pack()
sign_image.place(x=70,y=200)

label.pack()
label.place(x=500,y=220)







top.mainloop()
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance





class Face_Recognition_System:
    def __init__(self,root):
       self.root=root 
       self.root.geometry("1590x790+0+0")
       self.root.title("face Recognition System")

       # first img
       img=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\BestFacialRecognition.jpg")
       img=img.resize((500,130),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)

       # second img
       img1=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\facialrecognition.png")
       img1=img1.resize((500,130),Image.ANTIALIAS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=450,y=0,width=500,height=130)

        # Third img
       img2=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\Images.jpg")
       img2=img2.resize((500,130),Image.ANTIALIAS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=940,y=0,width=500,height=130)

       # bg image
       img3=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\bgimg.png")
       img3=img3.resize((1530,710),Image.ANTIALIAS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0,width=1400,height=45)

        # student button
       img4=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\college_image\Stud.png")
       img4=img4.resize((180,180),Image.ANTIALIAS)
       self.photoimg4=ImageTk.PhotoImage(img4)

       b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
       b1.place(x=200,y=85,width=220,height=220)

       b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=200,y=280,width=220,height=40)

       # Detect face button
       img5=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\face_detector1.jpg")
       img5=img5.resize((200,200),Image.ANTIALIAS)
       self.photoimg5=ImageTk.PhotoImage(img5)

       b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
       b1.place(x=550,y=85,width=220,height=220)

       b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=550,y=280,width=220,height=40)

       # Attendance face button
       img6=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\college_image\Attendance face.jpg")
       img6=img6.resize((200,200),Image.ANTIALIAS)
       self.photoimg6=ImageTk.PhotoImage(img6)

       b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
       b1.place(x=900,y=85,width=220,height=220)

       b1_1=Button(bg_img,text="ATTENDANCE",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=900,y=280,width=220,height=40)

      

       # Train face button
       img8=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\college_image\train.jpg")
       img8=img8.resize((200,200),Image.ANTIALIAS)
       self.photoimg8=ImageTk.PhotoImage(img8)

       b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
       b1.place(x=200,y=350,width=220,height=220)

       b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=200,y=530,width=220,height=40)

       # Photos face button
       img9=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\college_image\photos.jpg")
       img9=img9.resize((200,200),Image.ANTIALIAS)
       self.photoimg9=ImageTk.PhotoImage(img9)

       b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
       b1.place(x=550,y=350,width=220,height=220)

       b1_1=Button(bg_img,text="DATASET",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=550,y=530,width=220,height=40)
       

       
       # Exit face button
       img11=Image.open(r"C:\Users\dell\OneDrive\Desktop\face_recognition system\img\exit.jpg")
       img11=img11.resize((200,200),Image.ANTIALIAS)
       self.photoimg11=ImageTk.PhotoImage(img11)

       b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
       b1.place(x=900,y=350,width=220,height=220)

       b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=900,y=530,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
       if self.iExit >0:
          self.root.destroy()
       else:
          return

   

# =================Functions buttons=================

    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)

    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)

    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)

   
      






       



       
     


       


if __name__ == "__main__":
   root=Tk()
   obj=Face_Recognition_System(root)
   root.mainloop()
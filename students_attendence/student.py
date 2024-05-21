from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Students Details")

        img = Image.open(r"C:\Users\gagan\Desktop\FaceRecognition\images\face.jpg")
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1920, relheight=1)

        title_lbl = Label(bg_img, text="STUDENTS MANAGEMENT SYSTEM", font=("Helvetica", 20, "bold"), fg="white",
                          bg="#1b1b33", pady=10)
        title_lbl.place(x=273, y=100, anchor="w")

        main_frame=Frame(bg_img,bd=2,bg="#21618e")
        main_frame.place(x=20,y=150,width=1210,height=500)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="#04385f",relief=RAISED,text="Students Details",font=("Helvetica",12,"bold"),fg="white")
        Left_frame.place(x=10,y=10,width=660,height=470)

        # current course
        current_course=LabelFrame(Left_frame, bd=2, bg="#04385f", relief=RAISED, text="Current course information",
                                font=("Helvetica", 12, "bold"), fg="white")
        current_course.place(x=10, y=10, width=635, height=200)

        # department
        dep_label=Label(current_course,text="Department",font=("Helvetica",12,"bold"),fg="white",bg="#36607f")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,font=("Helvetica",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","Data Science","AI/ML","IOT","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course


        # right label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="#04385f", relief=RAISED, text="Students Details",
                                font=("Helvetica", 12, "bold"), fg="white")
        Left_frame.place(x=675, y=10, width=520, height=470)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

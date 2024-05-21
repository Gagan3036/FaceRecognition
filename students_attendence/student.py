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
        main_frame.place(x=20,y=150,width=1215,height=500)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="#04385f",relief=RAISED,text="Students Details",font=("Helvetica",12,"bold"),fg="white")
        Left_frame.place(x=10,y=10,width=665,height=470)

        # current course information
        current_course=LabelFrame(Left_frame, bd=2, bg="#04385f", relief=RAISED, text="Current course information",
                                font=("Helvetica", 12, "bold"), fg="white")
        current_course.place(x=10, y=10, width=645, height=125)

        # department
        dep_label=Label(current_course,text="Department",font=("Helvetica",12,"bold"),fg="white",bg="#36607f")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,font=("Helvetica",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","Data Science","AI/ML","IOT","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label = Label(current_course, text="Course", font=("Helvetica", 12, "bold"), fg="white", bg="#36607f")
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_label = ttk.Combobox(current_course, font=("Helvetica", 12, "bold"), width=17, state="readonly")
        course_label["values"] = (
        "Select Course", "FE","SE","TE","BE")
        course_label.current(0)
        course_label.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course, text="Year", font=("Helvetica", 12, "bold"), fg="white", bg="#36607f")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course, font=("Helvetica", 12, "bold"), width=17, state="read only")
        year_combo["values"] = (
        "Select Year", "2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester

        semester_label = Label(current_course, text="Semester", font=("Helvetica", 12, "bold"), fg="white", bg="#36607f")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course, font=("Helvetica", 12, "bold"), width=17, state="read only")
        semester_combo["values"] = (
        "Select Semester", "Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="#04385f", relief=RAISED, text="Class Students Information",
                                    font=("Helvetica", 12, "bold"), fg="white")
        class_student_frame.place(x=10, y=135, width=645, height=300)

        # student id
        studentId_label = Label(class_student_frame, text="StudentID", font=("Helvetica", 12, "bold"), fg="white",
                                bg="#36607f")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,width=20,font=("Helvetica", 12, "bold"))
        studentID_entry.grid(row=0,column=1, padx=10, sticky=W)

        # student name
        studentName_label = Label(class_student_frame, text="Student Name", font=("Helvetica", 12, "bold"), fg="white",
                                bg="#36607f")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, width=20, font=("Helvetica", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)


        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="#04385f", relief=RAISED, text="Students Details",
                                font=("Helvetica", 12, "bold"), fg="white")
        right_frame.place(x=680, y=10, width=520, height=470)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

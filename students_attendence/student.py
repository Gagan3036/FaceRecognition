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

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=50,y=150,width=950,height=500)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

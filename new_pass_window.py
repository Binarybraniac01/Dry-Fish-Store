from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import subprocess
import mysql.connector


class New_Pass_Page(Tk):
    def __init__(self):
        super().__init__()

        self.title("Change Password")

        self.width = 925
        self.height = 500

        self.resizable(FALSE, FALSE)

        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        self.set_geometry()
        # self.image_frame()
        self.details_frame()
        self.establish_connection()

    def set_geometry(self):
        self.geometry(f"{self.width}x{self.height}+{300}+{150}")

    def on_user_enter(self, event):
        self.user.delete(0, 'end')

    def on_user_leave(self, event):
        self.name = self.user.get()

        if self.name == '':
            self.user.insert(0, 'Username')

    # ----------------------------------------------------
    def on_psw_enter(self, event):
        self.pasw.delete(0, 'end')

    def on_psw_leave(self, event):
        self.name = self.pasw.get()

        if self.name == '':
            self.pasw.insert(0, 'Password')


    # ----------------------------------------------------
    def on_new_psw_enter(self, event):
        self.new_pasw.delete(0, 'end')

    def on_new_psw_leave(self, event):
        self.new_name = self.new_pasw.get()

        if self.new_name == '':
            self.new_pasw.insert(0, 'New Password')




    def details_frame(self):
        self.info_frame = Frame(self, width=925, height=500, bg="#D9C9B2")
        self.info_frame.place(x=-2, y=0)

        self.img = Image.open('All_images/login2.jpg')
        self.img = self.img.resize((925, 500))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label1 = Label(self.info_frame, image=self.photo)
        self.label1.pack(side="left")

        self.label2 = Label(self.info_frame, text="Welcome!!!", bg="#B3BDC7", fg="black",
                            font=('Eras Bold ITC', 23, 'bold'), borderwidth=0)
        self.label2.place(x=130, y=70)

        # --------------------------------------
        self.user = Entry(self.info_frame, width=31, fg='black', borderwidth=0, bg="#B3BDC7",
                          font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.user.place(x=70, y=150)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_user_enter)
        self.user.bind('<FocusOut>', self.on_user_leave)

        self.line_frame1 = Frame(self.info_frame, width=295, height=2, bg='black')
        self.line_frame1.place(x=75, y=177)

        # --------------------------------------
        self.pasw = Entry(self.info_frame, width=31, fg='black', borderwidth=0, bg="#B3BDC7",
                          font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.pasw.place(x=70, y=220)
        self.pasw.insert(0, 'Password')
        self.pasw.bind('<FocusIn>', self.on_psw_enter)
        self.pasw.bind('<FocusOut>', self.on_psw_leave)
        # self.pasw.bind('<Return>', self.Enter_signin)

        self.line_frame2 = Frame(self.info_frame, width=295, height=2, bg='black')
        self.line_frame2.place(x=75, y=247)


        # --------------------------------------
        self.new_pasw = Entry(self.info_frame, width=31, fg='black', borderwidth=0, bg="#B3BDC7",
                          font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.new_pasw.place(x=70, y=290)
        self.new_pasw.insert(0, 'New Password')
        self.new_pasw.bind('<FocusIn>', self.on_new_psw_enter)
        self.new_pasw.bind('<FocusOut>', self.on_new_psw_leave)
        # self.pasw.bind('<Return>', self.Enter_signin)

        self.line_frame2 = Frame(self.info_frame, width=295, height=2, bg='black')
        self.line_frame2.place(x=75, y=317)

        # --------------------------------------
        self.button1 = Button(self.info_frame, width=30, pady=7, text='Submit', bg='orange', fg='white',
                              command=self.change_pass, border=0)
        self.button1.place(x=110, y=370)

        # ----------------------------------------
        self.button2 = Button(self.info_frame, width=30, pady=7, text='Back', bg='#B3BDC7', fg='black',
                              command=self.set_back, border=0,activebackground='#B3BDC7')  # C0CAD4
        self.button2.place(x=110, y=420)



    def change_pass(self):
        self.username = self.user.get()
        self.password = self.pasw.get()
        self.new_password = self.new_pasw.get()

        if self.username == 'Username' or self.password == 'Password':
            tmsg.showwarning(title="Validation", message="Please Enter Username and Password !!")
            # pass

        else :
            self.sql_query = "select * from login_table where username = %s and password = %s"

            self.cursor.execute(self.sql_query, [self.username, self.password])
            self.results = self.cursor.fetchall()
            if self.results:
                self.update_query = ("UPDATE `login_table` SET `password` = %s WHERE `username` = %s ")
                self.vals = (self.new_password, self.username)
                self.cursor.execute(self.update_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Password Changed Successfully")

                self.destroy()
                subprocess.call(["python", "login.py"])


            else:
                tmsg.showerror(title="Error", message="Please Enter The Valid Credentials !!!")



    def set_back(self):
        self.destroy()
        subprocess.call(["python", "login.py"])

        # pass



    def establish_connection(self):
        """Function for establishing connection with MySQl Database"""
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", password="1234",
                                                      port="3306", database="FishData")
            self.cursor = self.connection.cursor()
        except Exception as server_error:
            print(f"Error: {server_error}")
            tmsg.showwarning("Server Issue", "Can't connect to MySQL server."
                                             "\nCheck connection")


if __name__ == '__main__':
    pas = New_Pass_Page()
    pas.mainloop()

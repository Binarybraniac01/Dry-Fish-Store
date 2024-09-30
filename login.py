from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import subprocess
import mysql.connector



class login_page(Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")

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


    def on_user_enter(self,event):
        self.user.delete(0, 'end')

    def on_user_leave(self,event):
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

    def details_frame(self):
        self.info_frame = Frame(self, width=925, height=500, bg="#D9C9B2")
        self.info_frame.place(x=-2, y=0)

        self.img = Image.open('All_images/login2.jpg')
        self.img = self.img.resize((925, 500))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label1 = Label(self.info_frame, image=self.photo)
        self.label1.pack(side="left")


        self.label2 = Label(self.info_frame, text="Welcome!!!",bg="#B3BDC7", fg="black", font=('Eras Bold ITC', 23, 'bold'), borderwidth=0)
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
        self.pasw = Entry(self.info_frame, show="*", width=31, fg='black', borderwidth=0, bg="#B3BDC7",
                          font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.pasw.place(x=70, y=220)
        self.pasw.insert(0, 'Password')
        self.pasw.bind('<FocusIn>', self.on_psw_enter)
        self.pasw.bind('<FocusOut>', self.on_psw_leave)
        self.pasw.bind('<Return>', self.Enter_signin)


        self.line_frame2 = Frame(self.info_frame, width=295, height=2, bg='black')
        self.line_frame2.place(x=75, y=247)

        # --------------------------------------
        self.button1 = Button(self.info_frame, width=30, pady=7, text='Log in', bg='orange', fg='white', command=self.signin, border=0)
        self.button1.place(x=110, y=300)

        #----------------------------------------
        self.button2 = Button(self.info_frame, width=30, pady=7, text='Change Password  ?', bg='#B3BDC7', fg='black',
                              command=self.change_password, border=0, activebackground='#B3BDC7') #C0CAD4
        self.button2.place(x=110, y=350)


    def signin(self):
        try:
            self.username = self.user.get()
            self.password = self.pasw.get()

            self.sql_query = "select * from login_table where username = %s and password = %s"

            self.cursor.execute(self.sql_query, [self.username, self.password])
            self.results = self.cursor.fetchall()
            if self.results:
                # print(self.results)
                tmsg.showinfo("Login Success", "You have been successfully "
                                               "login :)")
                self.destroy()
                # Dashboard_cls()
                subprocess.call(["python", "dashboard.py"])

            else:
                tmsg.showerror("Login Error", "Your Username or Password is incorrect")

        except Exception as server_error:
            print(f"Error: {server_error}")
            tmsg.showwarning("Server Issue", "Can't connect to MySQL server.\nCheck connection")






    def Enter_signin(self,ev):
        try:
            self.username = self.user.get()
            self.password = self.pasw.get()

            self.sql_query = "select * from login_table where username = %s and password = %s"

            self.cursor.execute(self.sql_query, [self.username, self.password])
            self.results = self.cursor.fetchall()
            if self.results:
                # print(self.results)
                tmsg.showinfo("Login Success", "You have been successfully "
                                               "login :)")
                self.destroy()
                # Dashboard_cls()
                subprocess.call(["python", "dashboard.py"])

            else:
                tmsg.showerror("Login Error", "Your Username or Password is incorrect")

        except Exception as server_error:
            print(f"Error: {server_error}")
            tmsg.showwarning("Server Issue", "Can't connect to MySQL server.\nCheck connection")

    def change_password(self):
        self.destroy()
        subprocess.call(["python", "new_pass_window.py"])
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
    log = login_page()
    log.mainloop()

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import datetime

class Profilecls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770

        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        
        
        # variable
        self.p_id = IntVar()
        self.profile_name = StringVar()
        self.user_name = StringVar()
        self.user_pass = StringVar()
        self.user_pass_reset = StringVar()
        self.curr_date = StringVar()


        
    
    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")



    def set_user_frames(self):
        self.ParentFrame = Frame(self, height=770, width=1450,bg="#DFD7BF")
        self.ParentFrame.place(x=0, y=146)

        self.profile_Frame = Frame(self.ParentFrame, bd=4, height=770, width=1450, bg="#DFD7BF")
        self.profile_Frame.place(x=0,y=0)
        
    
    def user_label(self):
        self.profile_name_lbl = Label(self.profile_Frame, text="User Name", font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.profile_name_lbl.place(x=50, y=100)
        self.profile_name_lbl_entry = Entry(self.profile_Frame, textvariable=self.profile_name, font=("comic", 20))
        self.profile_name_lbl_entry.place(x=300, y=100)

        self.user_name_lbl = Label(self.profile_Frame, text="User Name", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.user_name_lbl.place(x=50, y=170)
        self.user_name_entry = Entry(self.profile_Frame, textvariable=self.user_name, font=("comic", 20))
        self.user_name_entry.place(x=300, y=170)

        self.user_pass_lbl = Label(self.profile_Frame, text="User Password", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.user_pass_lbl.place(x=50,y=240)
        self.user_pass_entry = Entry(self.profile_Frame,textvariable=self.user_pass,font=("comic",20))
        self.user_pass_entry.place(x=300,y=240)

        self.user_pass_reset_lbl = Label(self.profile_Frame, text="Reset Password", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.user_pass_reset_lbl.place(x=50, y=310)
        self.user_pass_reset_lbl_entry = Entry(self.profile_Frame, textvariable=self.user_pass_reset, font=("comic", 20))
        self.user_pass_reset_lbl_entry.place(x=300, y=310)

        # self.user_stock_lbl = Label(self.profile_Frame, text="Quantity", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        # self.user_stock_lbl.place(x=50, y=310)
        # self.user_stock_entry = Entry(self.profile_Frame, textvariable=self.user_stock, font=("comic", 20),width=15)
        # self.user_stock_entry.place(x=300, y=310)


    def pro_bttons(self, btn_name, x, y):
        self.btn = Button(self.profile_Frame, text=btn_name, font=("Poor Richard",20, "bold"),bd=2, width=6, fg="white", bg="#3F2305")
        self.btn.place(x=x, y=y)
        self.btn.bind("<Button - 1>", self.check_profile_btn_event)




    def Product_table(self):

        self.P_frame = Frame(self.profile_Frame,bd=3,bg="#DFD7BF")
        self.P_frame.place(x=700,y=100,height=480,width=720)

        self.scollx = Scrollbar(self.P_frame,orient=HORIZONTAL)
        self.scolly = Scrollbar(self.P_frame, orient=VERTICAL)

        self.P_profile_table = ttk.Treeview(self.P_frame,columns=("id", "pname", "username", "password", "date"),
                                          xscrollcommand=self.scollx.set,yscrollcommand=self.scolly.set,)
        self.scollx.pack(side=BOTTOM, fill="x")
        self.scolly.pack(side=RIGHT, fill="y")

        self.scollx.config(command=self.P_profile_table.xview)
        self.scolly.config(command=self.P_profile_table.yview)


        # giving headings
        self.P_profile_table.heading("id",text="Profile Id")
        self.P_profile_table.heading("pname", text="Profile Name")
        self.P_profile_table.heading("username", text="Username")
        self.P_profile_table.heading("password", text="Password")
        self.P_profile_table.heading("date", text="Date")

        # self.P_profile_table.heading("price", text="Total Cost Price")
        # self.P_profile_table.heading("sp_price", text="Selling Price Per KG")

        self.P_profile_table["show"] = "headings"


        self.P_profile_table.column("id", width=100, minwidth=100, anchor=CENTER)
        self.P_profile_table.column("pname", width=150, minwidth=100, anchor=CENTER)
        self.P_profile_table.column("username", width=200, minwidth=100, anchor=CENTER)
        self.P_profile_table.column("password", width=150, minwidth=100, anchor=CENTER)
        self.P_profile_table.column("date", width=100, minwidth=100, anchor=CENTER)


        # self.P_profile_table.column("price",width=100,minwidth=100,anchor=CENTER)
        # self.P_profile_table.column("sp_price",width=200,minwidth=100,anchor=CENTER)


        self.P_profile_table.pack(fill=BOTH,expand=1)


        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `id`, `pname`, `username`, `password`, `date` "
                              "FROM `login_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.P_profile_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        # self.P_profile_table.bind("<<TreeviewSelect>>", self.show_prod_data)



    def add_profile_info(self):
        search_query = ("select * from `login_table` where `username` = %s ")
        vals = (self.user_name.get(),)
        self.cursor.execute(search_query, vals)
        result = self.cursor.fetchall()
        if result:
            # print(f"{self.user_name.get()} is already exist.")
            tmsg.showwarning("Warning", f"{self.user_name.get()} "
                                        f"is already available.")
        else:
            joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
            self.curr_date.set(joining_date)
            self.insert_query = (
                "INSERT INTO `login_table`( `pname`, `username`, `password`, `date`) "
                "VALUES (%s, %s, %s, %s)")
            vals = (self.profile_name.get(), self.user_name.get(), self.user_pass.get(), self.curr_date.get())
            self.cursor.execute(self.insert_query, vals)
            self.connection.commit()
            tmsg.showinfo("Success", "User Added Successfully")

            # self.profile_name = StringVar()
            # self.user_name = StringVar()
            # self.user_pass = StringVar()
            # self.user_pass_reset = StringVar()
            # self.curr_date = StringVar()

            self.profile_name.set("")
            self.user_name.set("")
            self.user_pass.set("")

            

            self.P_inven_table.delete(*self.P_inven_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `pid`, `name`, `description`, `category`, `quantity`, `price`, `sp_price` "
                                  "FROM `product_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.P_inven_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")








    def check_inventory_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_profile_info()
        elif event.widget.cget("text") == "Update":
            self.update_inventory_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_inventory_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_inventory_fields()


if __name__ == '__main__':
    pro = Profilecls()
    pro.mainloop()

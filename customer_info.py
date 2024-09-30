from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg


class Customercls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770

        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)


        # variables
        self.cust_id = IntVar()
        self.cust_name = StringVar()
        self.cust_mail = StringVar()
        self.cust_contact = StringVar()
        self.cust_address = StringVar()
        self.cust_purchase = IntVar()

        self.cust_search = StringVar()


        # calling methods
        self.setgeometry()







    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")


    def set_cust_frames(self):
        self.ParentFrame = Frame(self, height=770, width=1450,bg="#DFD7BF")
        self.ParentFrame.place(x=0, y=146)

    def sub_frame_1(self):
        self.child_1 = Frame(self.ParentFrame, height=770, width=1450, bg="#DFD7BF")
        self.child_1.place(x=1, y=2)

    # def sub_frame_2(self):
    #     self.child_2 = Frame(self.ParentFrame, bg="#DFD7BF")
    #     self.child_2.place(x=700, y=2, height=480, width=720,)


    def cust_label(self):

        self.cust_name_lbl = Label(self.child_1, text="Customer Name :", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.cust_name_lbl.place(x=50, y=120)
        self.cust_name_entry = Entry(self.child_1, textvariable=self.cust_name, font=("comic", 20))
        self.cust_name_entry.place(x=300, y=120)

        self.cust_mail_lbl = Label(self.child_1, text="Customer mail :", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.cust_mail_lbl.place(x=50,y=190)
        self.cust_mail_entry = Entry(self.child_1,textvariable=self.cust_mail,font=("comic",20))
        self.cust_mail_entry.place(x=300,y=190)

        self.cust_contact_lbl = Label(self.child_1, text="Contact :", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.cust_contact_lbl.place(x=50, y=260)
        self.cust_contact_entry = Entry(self.child_1, textvariable=self.cust_contact, font=("comic", 20))
        self.cust_contact_entry.place(x=300, y=260)

        self.cust_address_lbl = Label(self.child_1, text="Address :", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.cust_address_lbl.place(x=50, y=330)
        self.cust_address_entry = Entry(self.child_1, textvariable=self.cust_address, font=("comic", 20))
        self.cust_address_entry.place(x=300, y=330)

        # Purchase done by Customer
        self.Total_Purchase = Label(self.child_1, text=f"Total  Purchase : ",
                                        font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.Total_Purchase.place(x=50, y=400)



    def cust_bttons(self, btn_name, x, y):
        self.btn = Button(self.child_1, text=btn_name, font=("Poor Richard",20, "bold"),bd=2, width=6, fg="white", bg="#3F2305")
        self.btn.place(x=x, y=y)
        self.btn.bind("<Button - 1>", self.check_cust_btn_event)


    def search_bar(self):

        self.search_Lable = Label(self.child_1,text="Search Customer By Name :",font=("Poor Richard", 20, "bold"),borderwidth=0,bg="#DFD7BF")
        self.search_Lable.place(x=700,y=60)

        self.search_Lable_entry = Entry(self.child_1,textvariable=self.cust_search,font=("comic", 20),borderwidth=0)
        self.search_Lable_entry.place(x=1020,y=60)
        self.search_Lable_entry.bind("<Key>",self.c_search)


    def Customer_table(self):

        self.P_frame = Frame(self.child_1,bd=3,bg="#DFD7BF")
        self.P_frame.place(x=700,y=100,height=480,width=720)

        self.scollx = Scrollbar(self.P_frame,orient=HORIZONTAL)
        self.scolly = Scrollbar(self.P_frame, orient=VERTICAL)

        self.cust_table = ttk.Treeview(self.P_frame,columns=("cust_id", "cust_name", "cust_mail", "cust_contact",
                                                                "cust_address", "total_purchase"),
                                          xscrollcommand=self.scollx.set,yscrollcommand=self.scolly.set,)
        self.scollx.pack(side=BOTTOM, fill="x")
        self.scolly.pack(side=RIGHT, fill="y")

        self.scollx.config(command=self.cust_table.xview)
        self.scolly.config(command=self.cust_table.yview)


        # giving headings
        self.cust_table.heading("cust_id",text="Customer Id")
        self.cust_table.heading("cust_name", text="Customer Name")
        self.cust_table.heading("cust_mail", text="Customer mail")
        self.cust_table.heading("cust_contact", text="Customer Contact")
        self.cust_table.heading("cust_address", text="Customer address")
        self.cust_table.heading("total_purchase", text="Total Purchase")

        self.cust_table["show"] = "headings"


        self.cust_table.column("cust_id",width=100,minwidth=100,anchor=CENTER)
        self.cust_table.column("cust_name", width=150,minwidth=100,anchor=CENTER)
        self.cust_table.column("cust_mail",width=200,minwidth=100,anchor=CENTER)
        self.cust_table.column("cust_contact", width=150, minwidth=100,anchor=CENTER)
        self.cust_table.column("cust_address", width=100,minwidth=100,anchor=CENTER)
        self.cust_table.column("total_purchase",width=100,minwidth=100,anchor=CENTER)

        self.cust_table.pack(fill=BOTH,expand=1)



        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
                              "FROM `customer_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.cust_table.bind("<<TreeviewSelect>>", self.show_cust_data)

    # self.cust_mail = StringVar()
    # self.cust_contact = StringVar()
    # self.cust_address = StringVar()


    def show_cust_data(self, event):
        self.cur_position = self.cust_table.selection()
        self.cur_position = self.cust_table.item(self.cur_position)
        # print(self.cur_position["values"][0])
        self.len_cur_position = len(self.cur_position["values"])
        if self.len_cur_position == 6:
            self.cust_id.set(int(self.cur_position["values"][0]))
            self.cust_name.set(self.cur_position["values"][1])
            self.cust_mail.set(self.cur_position["values"][2])
            self.cust_contact.set(self.cur_position["values"][3])
            self.cust_address.set(self.cur_position["values"][4])
            self.cust_purchase.set(int(self.cur_position["values"][5]))
            self.Total_Purchase.config(text=f"Total  Purchase : {self.cust_purchase.get()}  Rs")







    def add_cust_data(self):
        if (self.cust_name.get() == "" or self.cust_mail.get() == "" or
                self.cust_contact.get() == "" or self.cust_address.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled")

        else:
            search_query = ("select * from `customer_table` where `cust_name` = %s AND `cust_contact`= %s ")
            vals = (self.cust_name.get(), self.cust_contact.get())
            self.cursor.execute(search_query, vals)
            result = self.cursor.fetchall()
            if result:
                tmsg.showwarning("Warning", f"{self.cust_name.get()} "
                                            f"is already available.")
            else:
                self.insert_query = (
                    "INSERT INTO `customer_table`( `cust_name`, `cust_mail`, `cust_contact`, `cust_address`) "
                    "VALUES (%s, %s, %s, %s)")
                vals = (self.cust_name.get(), self.cust_mail.get(), self.cust_contact.get(), self.cust_address.get())
                self.cursor.execute(self.insert_query, vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Customer Added Successfully")
                self.cust_name.set("")
                self.cust_mail.set("")
                self.cust_contact.set("")
                self.cust_address.set("")
                self.Total_Purchase.config(text="Total  Purchase : ")

                self.cust_table.delete(*self.cust_table.get_children())
                # Todo Complete : Added connectivity to show the data to the treeview
                try:
                    self.sql_query = (
                        "SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
                        "FROM `customer_table`")
                    self.cursor.execute(self.sql_query)
                    self.results = self.cursor.fetchall()
                    # print(self.results)
                    for self.idx, self.values in enumerate(self.results):
                        # print(self.values)
                        self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
                except Exception as server_error:
                    tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")


        # search_query = ("select * from `customer_table` where `cust_name` = %s AND `cust_contact`= %s ")
        # vals = (self.cust_name.get(), self.cust_contact.get())
        # self.cursor.execute(search_query, vals)
        # result = self.cursor.fetchall()
        # if result:
        #     tmsg.showwarning("Warning", f"{self.cust_name.get()} "
        #                                 f"is already available.")
        # else:
        #     self.insert_query = (
        #         "INSERT INTO `customer_table`( `cust_name`, `cust_mail`, `cust_contact`, `cust_address`) "
        #         "VALUES (%s, %s, %s, %s)")
        #     vals = (self.cust_name.get(), self.cust_mail.get(), self.cust_contact.get(), self.cust_address.get())
        #     self.cursor.execute(self.insert_query, vals)
        #     self.connection.commit()
        #     tmsg.showinfo("Success", "Customer Added Successfully")
        #     self.cust_name.set("")
        #     self.cust_mail.set("")
        #     self.cust_contact.set("")
        #     self.cust_address.set("")
        #     self.Total_Purchase.config(text="Total  Purchase : ")
        #
        #
        #     self.cust_table.delete(*self.cust_table.get_children())
        #     # Todo Complete : Added connectivity to show the data to the treeview
        #     try:
        #         self.sql_query = ("SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
        #                           "FROM `customer_table`")
        #         self.cursor.execute(self.sql_query)
        #         self.results = self.cursor.fetchall()
        #         # print(self.results)
        #         for self.idx, self.values in enumerate(self.results):
        #             # print(self.values)
        #             self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        #     except Exception as server_error:
        #         tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def update_cust_data(self):
        if (self.cust_name.get() == "" or self.cust_mail.get() == "" or
                self.cust_contact.get() == "" or self.cust_address.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled")

        else:
            self.update_query = ("UPDATE `customer_table` SET `cust_name` = %s, `cust_mail` = %s, `cust_contact` = %s,`cust_address` = %s "
                                 "WHERE `cust_id` = %s ")
            vals = (
            self.cust_name.get(), self.cust_mail.get(), self.cust_contact.get(), self.cust_address.get(), self.cust_id.get())
            self.cursor.execute(self.update_query, vals)
            self.connection.commit()
            tmsg.showinfo("Success", "Customer Updated Successfully")

            self.cust_name.set("")
            self.cust_mail.set("")
            self.cust_contact.set("")
            self.cust_address.set("")
            self.Total_Purchase.config(text="Total  Purchase : ")


            self.cust_table.delete(*self.cust_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
                                  "FROM `customer_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def delete_cust_data(self):
        if (self.cust_name.get() == "" or self.cust_mail.get() == "" or
                self.cust_contact.get() == "" or self.cust_address.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:
            self.del_query = ("DELETE from `customer_table` WHERE `cust_id` = %s")
            vals = (self.cust_id.get(),)
            self.cursor.execute(self.del_query, vals)
            print("deleted from database")
            self.connection.commit()
            tmsg.showinfo("Success", "Customer deleted successfully")

            self.cust_name.set("")
            self.cust_mail.set("")
            self.cust_contact.set("")
            self.cust_address.set("")
            self.Total_Purchase.config(text="Total  Purchase : ")
            self.cust_search.set("")

            self.cust_table.delete(*self.cust_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
                                  "FROM `customer_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def clear_cust_fields(self):
        self.cust_name.set("")
        self.cust_mail.set("")
        self.cust_contact.set("")
        self.cust_address.set("")
        self.Total_Purchase.config(text="Total  Purchase : ")
        self.cust_search.set("")

        self.cust_table.delete(*self.cust_table.get_children())
        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `cust_id`, `cust_name`, `cust_mail`, `cust_contact`, `cust_address`, `total_purchase` "
                              "FROM `customer_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.cust_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        # self.cust_table.bind("<<TreeviewSelect>>", self.show_cust_data)









    def check_cust_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_cust_data()
        elif event.widget.cget("text") == "Update":
            self.update_cust_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_cust_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_cust_fields()



    def c_search(self, ev):
        try:
            self.search_query = ("SELECT * FROM customer_table where cust_name LIKE '%" + self.cust_search.get() + "%'")
            self.cursor.execute(self.search_query)
            self.row = self.cursor.fetchall()
            # print(self.row)
            if len(self.row) > 0:
                self.cust_table.delete(*self.cust_table.get_children())
                for i in self.row:
                    self.cust_table.insert('', END, values=i)
            else:
                self.cust_table.delete(*self.cust_table.get_children())

        except EXCEPTION as ex:
            tmsg.showerror(title="Connection Error", message=f"Error due to {str(ex)}")







if __name__ == '__main__':
    cust = Customercls()
    cust.mainloop()
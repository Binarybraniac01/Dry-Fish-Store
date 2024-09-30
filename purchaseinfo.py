from tkinter import *
from tkinter import ttk
import subprocess
import tkinter.messagebox as tmsg


class Vendorcls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        # Frame variables
        self.Transaction_id = IntVar()
        self.vendor_name = StringVar()
        self.vendor_phone = StringVar()
        self.vendor_address = StringVar()

        self.p_name = StringVar()
        self.p_cat = StringVar()
        self.p_desc = StringVar()
        self.p_stock = DoubleVar()
        self.p_price = IntVar()
        self.p_date = StringVar()

        self.v_search = StringVar()

        self.reference_stk = IntVar()


        # Calling Methods
        self.geometry()
        self.set_main_frame()
        self.set_sub_frames()
        self.Search_bar()
        self.Purchase_details()






    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")



    def set_main_frame(self):
        self.ParentFrame = Frame(self, height=650, width=1450, bg="#DFD7BF")
        self.ParentFrame.place(x=0, y=146)


    def set_sub_frames(self):
        self.sub_frame1 = LabelFrame(self.ParentFrame,text="Vendor Details",font=("Poor Richard", 20, "bold"),
                                     height=80,width=1430,bg="#DFD7BF")
        self.sub_frame1.place(x=10,y=50)

        self.sub_frame2 = LabelFrame(self.ParentFrame, text="Product Details", font=("Poor Richard", 20, "bold"),
                                    height=180, width=1430,bg="#DFD7BF")
        self.sub_frame2.place(x=10, y=140)



        self.v_name = Label(self.sub_frame1,text="Vendor Name :",font=("Poor Richard", 15, "bold"),bg="#DFD7BF")
        self.v_name.place(x=5, y=10)
        self.v_name_entry = Entry(self.sub_frame1,textvariable=self.vendor_name,
                                  font=("Poor Richard", 15, "bold"), width=20)
        self.v_name_entry.place(x=180, y=10)

        self.v_contact = Label(self.sub_frame1, text="Contact Details :",
                               font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.v_contact.place(x=500, y=10)
        self.v_contact_entry = Entry(self.sub_frame1, textvariable=self.vendor_phone,
                                     font=("Poor Richard", 15, "bold"), width=17)
        self.v_contact_entry.place(x=650, y=10)

        self.v_address = Label(self.sub_frame1, text="Shop Address :",
                               font=("Poor Richard", 15, "bold"),bg="#DFD7BF")
        self.v_address.place(x=925, y=10)
        self.v_address_entry = Entry(self.sub_frame1, textvariable=self.vendor_address,
                                     font=("Poor Richard", 15, "bold"))
        self.v_address_entry.place(x=1100, y=10)




        # Product Details
        self.prod_name_lbl = Label(self.sub_frame2, text="Product Name :", font=("Poor Richard", 15, "bold"),
                                   bg="#DFD7BF")
        self.prod_name_lbl.place(x=5, y=10)
        self.prod_name_entry = Entry(self.sub_frame2, textvariable=self.p_name, font=("comic", 15))
        self.prod_name_entry.place(x=180, y=10)

        self.prod_category_lbl = Label(self.sub_frame2, text="Category :", font=("Poor Richard", 15, "bold"),
                                       bg="#DFD7BF")
        self.prod_category_lbl.place(x=500, y=10)
        self.prod_category_entry = Entry(self.sub_frame2, textvariable=self.p_cat, font=("comic", 15),width=20)
        self.prod_category_entry.place(x=620, y=10)

        self.prod_description_lbl = Label(self.sub_frame2, text="Description :", font=("Poor Richard", 15, "bold")
                                          , bg="#DFD7BF")
        self.prod_description_lbl.place(x=900, y=10)
        self.prod_description_entry = Entry(self.sub_frame2, textvariable=self.p_desc, font=("comic", 15),width=30)
        self.prod_description_entry.place(x=1040, y=10)

        self.prod_stock_lbl = Label(self.sub_frame2, text="Quantity :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.prod_stock_lbl.place(x=5, y=60)
        self.prod_stock_entry = Entry(self.sub_frame2, textvariable=self.p_stock, font=("comic", 15), width=15)
        self.prod_stock_entry.place(x=180, y=60)
        # For KG
        self.prod_stock_lbl_kg = Label(self.sub_frame2, text="KG", font=("Poor Richard", 12),bg="#DFD7BF")
        self.prod_stock_lbl_kg.place(x=350, y=60)

        self.prod_price_lbl = Label(self.sub_frame2, text="Price :", font=("Poor Richard", 15, "bold"),bg="#DFD7BF")
        self.prod_price_lbl.place(x=500, y=60)
        self.prod_price_entry = Entry(self.sub_frame2, textvariable=self.p_price, font=("comic", 15))
        self.prod_price_entry.place(x=600, y=60)

        self.date_lbl = Label(self.sub_frame2, text="Date :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.date_lbl.place(x=5, y=100)
        self.date_lbl_entry = Entry(self.sub_frame2, textvariable=self.p_date, font=("comic", 15), width=15)
        self.date_lbl_entry.place(x=180, y=100)
        self.date_lbl_format = Label(self.sub_frame2, text="(YYYY-MM-DD)", font=("Poor Richard", 12), bg="#DFD7BF")
        self.date_lbl_format.place(x=360, y=105)



    def Buttons(self, btn_name=None, x=None, y=None, btn_type=None):
        if btn_type == None :
            self.f_btns = Button(self.sub_frame2, text=btn_name, font=("comic", 15, "bold"), padx=15, pady=3,
                                 fg="white", bg="#3F2305")
            self.f_btns.place(x=x,y=y)
            self.f_btns.bind("<Button - 1>", self.check_vendorcls_btn_event)

        elif btn_type == "Chart":
            self.ord_btn = Button(self.ParentFrame, text=btn_name, font=("comic", 10, "bold"), padx=2, pady=10
                                  , width=20, fg="white", bg="#3F2305")
            self.ord_btn.place(x=x, y=y)
            self.ord_btn.bind("<Button - 1>", self.show_p_chart)

        else:
            self.ord_btn = Button(self.ParentFrame, text=btn_name, font=("comic", 10, "bold"), padx=2, pady=10
                                  , width=20, fg="white", bg="#3F2305")
            self.ord_btn.place(x=x, y=y)
            self.ord_btn.bind("<Button - 1>", self.check_vendorcls_cart_btn_event)





    def Search_bar(self):
        self.search_Lable = Label(self.ParentFrame, text="Search Product By Name :",
                                  font=("Poor Richard", 20, "bold"), borderwidth=0, bg="#DFD7BF")
        self.search_Lable.place(x=8, y=330)

        self.search_Lable_entry = Entry(self.ParentFrame, textvariable=self.v_search, font=("comic", 20),
                                        borderwidth=0)
        self.search_Lable_entry.place(x=310, y=330)
        self.search_Lable_entry.bind("<Key>", self.V_search)


    def Purchase_details(self):
        self.V_frame = Frame(self.ParentFrame, borderwidth=0)
        self.V_frame.place(x=8, y=385, height=230, width=1430)

        self.xscroll = Scrollbar(self.V_frame, orient=HORIZONTAL)
        self.yscroll = Scrollbar(self.V_frame, orient=VERTICAL)

        self.Details_table = ttk.Treeview(self.V_frame, columns=("Tran_id", "v_name", "v_contact", "v_address", "name",
                                                                 "category", "description", "quantity", "price", "date" ),
                                          xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)

        self.xscroll.pack(fill="x", side=BOTTOM)
        self.yscroll.pack(fill="y", side=RIGHT)

        self.xscroll.config(command=self.Details_table.xview)
        self.yscroll.config(command=self.Details_table.yview)

        # Headings
        self.Details_table.heading("Tran_id", text="Transaction ID")
        # self.Details_table.heading("vid", text="Vendor Id")
        self.Details_table.heading("v_name", text="Vendor name")
        self.Details_table.heading("v_contact", text="Contact Details")
        self.Details_table.heading("v_address", text="Address")
        # self.Details_table.heading("Transaction_id", text="Product Id")
        self.Details_table.heading("name", text="Name")
        self.Details_table.heading("category", text="Category")
        self.Details_table.heading("description", text="Description")
        self.Details_table.heading("quantity", text="Quantity")
        self.Details_table.heading("price", text="Price")
        self.Details_table.heading("date", text="Date")


        self.Details_table["show"] = "headings"

        self.Details_table.column("Tran_id", width=100, anchor=CENTER)
        # self.Details_table.column("vid", width=100, anchor=CENTER)
        self.Details_table.column("v_name", width=300, anchor=CENTER)
        self.Details_table.column("v_contact", width=200, anchor=CENTER)
        self.Details_table.column("v_address", width=500, anchor=CENTER)
        # self.Details_table.column("Transaction_id", width=100, anchor=CENTER)
        self.Details_table.column("name", width=200, anchor=CENTER)
        self.Details_table.column("category", width=200, anchor=CENTER)
        self.Details_table.column("description", width=100, anchor=CENTER)
        self.Details_table.column("quantity", width=100, anchor=CENTER)
        self.Details_table.column("price", width=100, anchor=CENTER)
        self.Details_table.column("date", width=300, anchor=CENTER)


        self.Details_table.pack(fill=BOTH, expand=1)


        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`, `name`,  `category`,"
                              " `description`, `quantity`, `price`, `date` "
                              "FROM `vendor_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)

            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.Details_table.bind("<<TreeviewSelect>>", self.show_purchase_data)


    # SHOWING DATA  OF THE TABLE ON REFRESH
    def show_purchase_data(self, event):
        # global curr_position
        self.curr_position = self.Details_table.selection()
        self.curr_position = self.Details_table.item(self.curr_position)
        # print(self.curr_position["values"][0])
        self.len_curr_position = len(self.curr_position["values"])
        if (self.len_curr_position < 10):
            pass
        else:
            self.Transaction_id.set(int(self.curr_position["values"][0]))
            self.vendor_name.set(self.curr_position["values"][1])
            self.vendor_phone.set(self.curr_position["values"][2])
            self.vendor_address.set(self.curr_position["values"][3])

            # self.p_id.set(int(self.curr_position["values"][]))
            self.p_name.set(self.curr_position["values"][4])
            self.p_cat.set(self.curr_position["values"][5])
            self.p_desc.set(self.curr_position["values"][6])
            self.p_stock.set(float(self.curr_position["values"][7]))
            self.p_price.set(int(self.curr_position["values"][8]))
            self.p_date.set(self.curr_position["values"][9])

            # for update query
            self.reference_stk = (self.curr_position["values"][7])
            # print(self.reference_stk)



    # UPDATE BUTTION QUERY
    def add_purchase_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0 or self.p_price.get() == 0
                or self.p_date.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")

        else:
            self.insert_query = (
                "INSERT INTO `vendor_table`(`v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                " `quantity`, `price`, `date`) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            vals = (self.vendor_name.get(), self.vendor_phone.get(), self.vendor_address.get(), self.p_name.get(),
                    self.p_cat.get(), self.p_desc.get(), self.p_stock.get(), self.p_price.get(), self.p_date.get())
            self.cursor.execute(self.insert_query, vals)
            self.connection.commit()


            # Todo : Add quantity and product in product table
            # self.check_n = self.p_name.get()
            self.check_query = ("select * from product_table where `name`=%s")
            vals = (self.p_name.get(),)
            self.cursor.execute(self.check_query, vals)
            self.result = self.cursor.fetchall()
            if self.result :
                # print(self.result)
                self.stk_n = self.result[0][4]
                self.check_stk = self.p_stock.get()
                self.check_n = self.p_name.get()

                self.updated_stk = self.stk_n + self.check_stk
                self.add_query = ("UPDATE `product_table` SET `quantity` = %s WHERE `name`=%s")
                self.vals = (self.updated_stk, self.check_n)
                self.cursor.execute(self.add_query, self.vals)
                tmsg.showinfo("Success", "Transaction Added Successfully")

            else:
                self.p_insert_query = (
                    "INSERT INTO `product_table`( `name`, `description`, `category`, `quantity`, `price`, `date`) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
                vals = (self.p_name.get(), self.p_desc.get(), self.p_cat.get(),
                        self.p_stock.get(),self.p_price.get(), self.p_date.get())
                self.cursor.execute(self.p_insert_query, vals)
                tmsg.showinfo("Success", "Transaction Added Successfully With New Product Data")


            # self.Transaction_id.set(0)
            self.vendor_name.set("")
            self.vendor_phone.set("")
            self.vendor_address.set("")
            self.p_name.set("")
            self.p_cat.set("")
            self.p_desc.set("")
            self.p_stock.set(0)
            self.p_price.set(0)
            self.p_date.set("")

            self.Details_table.delete(*self.Details_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = (
                    "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                    " `quantity`, `price`, `date` "
                    "FROM `vendor_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

            print(self.check_n)



    # UPDATE BUTTION QUERY
    def update_purchase_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0 or self.p_price.get() == 0
                or self.p_date.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")
        else:
            self.update_query = ("UPDATE `vendor_table` SET `v_name` = %s, `v_contact` = %s, `v_address` = %s, "
                                 "`name` = %s, `category` = %s, `description` = %s, `quantity` = %s, `price` = %s,"
                                 " `date` = %s WHERE `Tran_id` = %s")
            vals = (self.vendor_name.get(), self.vendor_phone.get(), self.vendor_address.get(), self.p_name.get(),
                         self.p_cat.get(), self.p_desc.get(), self.p_stock.get(), self.p_price.get(), self.p_date.get(),
                         self.Transaction_id.get())
            self.cursor.execute(self.update_query, vals)
            self.connection.commit()
            tmsg.showinfo("Success", "Transaction Updated Successfully")


            # Todo : Update the updated quantity
            self.pur_check_query = ("select * from product_table where `name`=%s")
            vals = (self.p_name.get(),)
            self.cursor.execute(self.pur_check_query, vals)
            self.result = self.cursor.fetchall()
            if self.result:
                # print(self.result)
                self.stk_n = self.result[0][4]
                self.check_stk = self.p_stock.get()
                self.check_n = self.p_name.get()
                self.minus_stk = self.reference_stk

                self.updated_stk = self.stk_n + self.check_stk - self.minus_stk
                self.pur_query = ("UPDATE `product_table` SET `quantity` = %s WHERE `name`=%s")
                self.vals = (self.updated_stk, self.check_n)
                self.cursor.execute(self.pur_query, self.vals)
            else:
                print("Please check again")



            # self.Transaction_id.set(0)
            self.vendor_name.set("")
            self.vendor_phone.set("")
            self.vendor_address.set("")
            self.p_name.set("")
            self.p_cat.set("")
            self.p_desc.set("")
            self.p_stock.set(0)
            self.p_price.set(0)
            self.p_date.set("")


            self.Details_table.delete(*self.Details_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`,"
                                  " `description`, `quantity`, `price`, `date` "
                                  "FROM `vendor_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")



    # DELETE BUTTON QUERY
    def delete_purchase_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0 or self.p_price.get() == 0
                or self.p_date.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")
        else:
            self.del_query = ("DELETE from `vendor_table` WHERE `Tran_id` = %s")
            vals = (self.Transaction_id.get(),)
            self.cursor.execute(self.del_query, vals)
            print("deleted from database")
            self.connection.commit()
            tmsg.showinfo("Success", "Transaction deleted successfully")
            # self.Transaction_id.set(0)
            self.vendor_name.set("")
            self.vendor_phone.set("")
            self.vendor_address.set("")
            self.p_name.set("")
            self.p_cat.set("")
            self.p_desc.set("")
            self.p_stock.set(0)
            self.p_price.set(0)
            self.p_date.set("")

            self.Details_table.delete(*self.Details_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`,"
                                  "`description`, `quantity`, `price`, `date` "
                                  "FROM `vendor_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")



    # CLEAR BUTTON QUERY
    def clear_purchase_fields(self):
        # self.Transaction_id.set(0)
        self.vendor_name.set("")
        self.vendor_phone.set("")
        self.vendor_address.set("")
        self.p_name.set("")
        self.p_cat.set("")
        self.p_desc.set("")
        self.p_stock.set(0)
        self.p_price.set(0)
        self.p_date.set("")

        self.Details_table.delete(*self.Details_table.get_children())
        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`,"
                              "`description`, `quantity`, `price`, `date` "
                              "FROM `vendor_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

        self.v_search.set("")
    




    # TO CHECK WHICH BUTTON IS PRESSED
    def check_vendorcls_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_purchase_data()
        elif event.widget.cget("text") == "Update":
            self.update_purchase_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_purchase_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_purchase_fields()




    def V_search(self,ev):
        try:
            self.search_query = ("SELECT * FROM vendor_table where name LIKE '%"+self.v_search.get()+"%'")
            self.cursor.execute(self.search_query)
            self.row = self.cursor.fetchall()
            if len(self.row) > 0:
                self.Details_table.delete(*self.Details_table.get_children())
                for self.idx, self.values in enumerate(self.row):
                    # print(self.values)
                    self.Details_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            else:
                # print("table not found")
                self.Details_table.delete(*self.Details_table.get_children())

        except Exception as ex:
            tmsg.showerror(title="Connection Error", message=f"Error due to {str(ex)}")






    # Todo :  add new window for cart is called in dashboard file
    def check_vendorcls_cart_btn_event(self, event):
        if event.widget.cget("text") == "GO TO CART":
            subprocess.call(["python", "cart_info.py"])


    def show_p_chart(self,event):
        if event.widget.cget("text") == "Purchase Chart":
            # tmsg.showinfo(title="Inform", message="Chart Developed.....")
            subprocess.call(["python", "show_purchase_chart.py"])

    # test
    # def show_p_chart(self):
    #     subprocess.call(["python", "show_purchase_chart.py"])





if __name__ == '__main__':
    v = Vendorcls()
    v.mainloop()
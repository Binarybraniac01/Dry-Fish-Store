import tkinter
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import tkinter.messagebox as tmsg
import datetime
import sys


class Cartcls(Tk):
    def __init__(self):
        super().__init__()

        # def __init__(self, master):
        #     super().__init__(master)
        #     self.master = master


        self.title("CART WINDOW")

        self.width = 1440
        self.height = 590
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
        self.p_status = StringVar()
        self.p_date = StringVar()


        self.v_search = StringVar()

        self.reference_stk = IntVar()

        self.protocol('WM_DELETE_WINDOW', self.cart_close)



        # calling  mertthod
        self.setgeometry()
        self.set_cart_frame()
        self.set_sub_frames()
        self.establish_connection()
        self.Search_bar()
        self.Order_details()



        self.set_buttons("Add", 890, 85)
        self.set_buttons("Update", 1010, 85)
        self.set_buttons("Delete", 1160, 85)
        self.set_buttons("Clear", 1300, 85)
        self.set_buttons("Back", 1330, 8, "back_btn")







    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{48}+{182}")



    def set_cart_frame(self):
        self.Go_to_cart_frame = Frame(self, height=650, width=1440, bg="#DFD7BF")
        self.Go_to_cart_frame.place(x=0, y=0)




    def set_sub_frames(self):
        self.sub_frame1 = LabelFrame(self.Go_to_cart_frame, text="Vendor Details", font=("Poor Richard", 20, "bold"),
                                     height=80, width=1425, bg="#DFD7BF")
        self.sub_frame1.place(x=10, y=50)

        self.sub_frame2 = LabelFrame(self.Go_to_cart_frame, text="Product Details", font=("Poor Richard", 20, "bold"),
                                     height=180, width=1425, bg="#DFD7BF")
        self.sub_frame2.place(x=10, y=140)

        self.v_name = Label(self.sub_frame1, text="Vendor Name :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.v_name.place(x=5, y=10)
        self.v_name_entry = Entry(self.sub_frame1, textvariable=self.vendor_name,
                                  font=("Poor Richard", 15, "bold"), width=20)
        self.v_name_entry.place(x=180, y=10)
        self.v_name_entry.bind("<Button - 3>",self.v_details_search)

        self.v_contact = Label(self.sub_frame1, text="Contact Details :",
                               font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.v_contact.place(x=500, y=10)
        self.v_contact_entry = Entry(self.sub_frame1, textvariable=self.vendor_phone,
                                     font=("Poor Richard", 15, "bold"), width=17)
        self.v_contact_entry.place(x=650, y=10)

        self.v_address = Label(self.sub_frame1, text="Shop Address :",
                               font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
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
        # self.prod_name_entry.bind("<Button - 3>",self.p_details_search)

        self.prod_category_lbl = Label(self.sub_frame2, text="Category :", font=("Poor Richard", 15, "bold"),
                                       bg="#DFD7BF")
        self.prod_category_lbl.place(x=500, y=10)
        self.prod_category_entry = Entry(self.sub_frame2, textvariable=self.p_cat, font=("comic", 15), width=20)
        self.prod_category_entry.place(x=620, y=10)
        self.prod_category_entry.bind("<Button - 3>", self.p_details_search)

        self.prod_description_lbl = Label(self.sub_frame2, text="Description :", font=("Poor Richard", 15, "bold")
                                          , bg="#DFD7BF")
        self.prod_description_lbl.place(x=900, y=10)
        self.prod_description_entry = Entry(self.sub_frame2, textvariable=self.p_desc, font=("comic", 15), width=30)
        self.prod_description_entry.place(x=1040, y=10)

        self.prod_stock_lbl = Label(self.sub_frame2, text="Quantity :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.prod_stock_lbl.place(x=5, y=60)
        self.prod_stock_entry = Entry(self.sub_frame2, textvariable=self.p_stock, font=("comic", 15), width=15)
        self.prod_stock_entry.place(x=180, y=60)
        # For KG
        self.prod_stock_lbl_kg = Label(self.sub_frame2, text="KG", font=("Poor Richard", 12), bg="#DFD7BF")
        self.prod_stock_lbl_kg.place(x=350, y=60)

        self.prod_price_lbl = Label(self.sub_frame2, text="Price :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.prod_price_lbl.place(x=500, y=60)
        self.prod_price_lbl_entry = Entry(self.sub_frame2, textvariable=self.p_price, font=("comic", 15))
        self.prod_price_lbl_entry.place(x=600, y=60)

        self.status_lbl = Label(self.sub_frame2, text="Status :", font=("Poor Richard", 15, "bold"), bg="#DFD7BF")
        self.status_lbl.place(x=5, y=100)
        self.status_lbl_entry = ttk.Combobox(self.sub_frame2, textvariable=self.p_status, width=15,
                                          values=["Place order", "Order Received"],
                                          font=("comic", 15), state="readonly")
        # self.status_lbl_entry = Entry(self.sub_frame2, textvariable=self.p_status, font=("comic", 15), width=15)
        self.status_lbl_entry.place(x=180, y=100)



    # Todo : add this to purchase window
    def set_buttons(self, btn_name=None, x=None, y=None, btn_type=None):
        if btn_type == None:
            self.q_btn = Button(self.sub_frame2, text=btn_name, font=("commic", 15, "bold"), pady=5, padx=15, fg="white",
                                  bg="#3F2305")
            self.q_btn.place(x=x, y=y)
            self.q_btn.bind("<Button - 1>", self.check_cartclass_btn_event)

        else:
            self.btn = Button(self.Go_to_cart_frame, text=btn_name, font=("commic", 15, "bold"), pady=5, padx=15, fg="white",
                                bg="#3F2305")
            self.btn.place(x=x, y=y)  # 20/20
            self.btn.bind("<Button - 1>", self.set_back)




    def Search_bar(self):
        self.search_Lable = Label(self.Go_to_cart_frame, text="Search Product By Name :",
                                  font=("Poor Richard", 20, "bold"), borderwidth=0, bg="#DFD7BF")
        self.search_Lable.place(x=8, y=330)

        self.search_Lable_entry = Entry(self.Go_to_cart_frame, textvariable=self.v_search, font=("comic", 20),
                                        borderwidth=0)
        self.search_Lable_entry.place(x=310, y=330)
        # self.search_Lable_entry.bind("<Key>", self.S_search)




    def Order_details(self):
        self.O_frame = Frame(self.Go_to_cart_frame, borderwidth=0)
        self.O_frame.place(x=8, y=375, height=210, width=1423)

        self.xscroll = Scrollbar(self.O_frame, orient=HORIZONTAL)
        self.yscroll = Scrollbar(self.O_frame, orient=VERTICAL)

        self.Order_table = ttk.Treeview(self.O_frame, columns=("Tran_id", "v_name", "v_contact", "v_address", "name",
                                                                 "category", "description", "quantity", "price","status",
                                                                 "date"),xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)

        self.xscroll.pack(fill="x", side=BOTTOM)
        self.yscroll.pack(fill="y", side=RIGHT)

        self.xscroll.config(command=self.Order_table.xview)
        self.yscroll.config(command=self.Order_table.yview)

        # Headings
        self.Order_table.heading("Tran_id", text="Transaction ID")
        self.Order_table.heading("v_name", text="Vendor name")
        self.Order_table.heading("v_contact", text="Contact Details")
        self.Order_table.heading("v_address", text="Address")
        self.Order_table.heading("name", text="Name")
        self.Order_table.heading("category", text="Category")
        self.Order_table.heading("description", text="Description")
        self.Order_table.heading("quantity", text="Quantity")
        self.Order_table.heading("price", text="Price")
        self.Order_table.heading("status", text="Status")
        self.Order_table.heading("date", text="Date")

        self.Order_table["show"] = "headings"

        self.Order_table.column("Tran_id", width=100, anchor=CENTER)
        self.Order_table.column("v_name", width=300, anchor=CENTER)
        self.Order_table.column("v_contact", width=200, anchor=CENTER)
        self.Order_table.column("v_address", width=500, anchor=CENTER)
        self.Order_table.column("name", width=200, anchor=CENTER)
        self.Order_table.column("category", width=200, anchor=CENTER)
        self.Order_table.column("description", width=100, anchor=CENTER)
        self.Order_table.column("quantity", width=100, anchor=CENTER)
        self.Order_table.column("price", width=100, anchor=CENTER)
        self.Order_table.column("status", width=100, anchor=CENTER)
        self.Order_table.column("date", width=300, anchor=CENTER)

        self.Order_table.pack(fill=BOTH, expand=1)


        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`, `name`,  `category`,"
                              " `description`, `quantity`, `price`,`status`, `date` "
                              "FROM `booking_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.Order_table.bind("<<TreeviewSelect>>", self.show_order_data)




    def v_details_search(self,event):
        self.v_check_query = ("select * from vendor_table where `v_name`=%s")
        vals = (self.vendor_name.get(),)
        self.cursor.execute(self.v_check_query, vals)
        self.result = self.cursor.fetchall()
        # print(self.result)
        if self.result :
            self.v_add = self.result[0][3]
            self.v_phn = self.result[0][2]
            self.vendor_address.set(self.v_add)
            self.vendor_phone.set(self.v_phn)
        self.result.clear()


    def p_details_search(self,event):
        self.p_check_query = ("select * from vendor_table where `name`=%s AND `category`=%s")
        vals = (self.p_name.get(), self.p_cat.get())
        self.cursor.execute(self.p_check_query, vals)
        self.result = self.cursor.fetchall()
        # print(self.result)
        if self.result:
            self.o_p_desc = self.result[0][6]
            self.p_desc.set(self.o_p_desc)
        self.result.clear()




    def show_order_data(self, event):
        self.curr_position = self.Order_table.selection()
        self.curr_position = self.Order_table.item(self.curr_position)
        # print(self.curr_position["values"][0])
        self.len_curr_position = len(self.curr_position["values"])
        if (self.len_curr_position < 11):
            print("Colomn count doesn't match")
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
            self.p_status.set(self.curr_position["values"][9])
            self.p_date.set(self.curr_position["values"][10])















    def add_order_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0.0 or self.p_price.get() == 0 or
                self.p_status.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")

        else:
            # Todo : If entry exist then ask user  if he approves to Add new entry
            self.check_query = ("select * from booking_table where `v_name`=%s AND `name`=%s AND `category`=%s")
            vals = (self.vendor_name.get(),self.p_name.get(),self.p_cat.get())
            self.cursor.execute(self.check_query, vals)
            # self.connection.commit()
            self.result = self.cursor.fetchall()
            if self.result:
                # print("data found")
                # Todo : add the message box for askokcancel if ok then execute query and if no then pass
                self.outcome = messagebox.askokcancel(title="Question",message=f"{self.p_name.get()} is already ordered from {self.vendor_name.get()} vendor.\n Do you wish to place order again ? ")
                if self.outcome :
                    joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
                    self.p_date.set(joining_date)
                    self.insert_query = (
                        "INSERT INTO `booking_table`(`v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                        " `quantity`, `price`,`status`, `date`) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    vals = (self.vendor_name.get(), self.vendor_phone.get(), self.vendor_address.get(), self.p_name.get(),
                            self.p_cat.get(), self.p_desc.get(), self.p_stock.get(), self.p_price.get(), self.p_status.get(),
                            self.p_date.get())
                    self.cursor.execute(self.insert_query, vals)
                    self.connection.commit()

                    self.vendor_name.set("")
                    self.vendor_phone.set("")
                    self.vendor_address.set("")
                    self.p_name.set("")
                    self.p_cat.set("")
                    self.p_desc.set("")
                    self.p_stock.set(0.0)
                    self.p_price.set(0)
                    self.p_status.set("")
                    # self.p_date.set("")

                    self.Order_table.delete(*self.Order_table.get_children())
                    # Todo Complete : Added connectivity to show the data to the treeview
                    try:
                        self.sql_query = (
                            "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                            " `quantity`, `price`, `status`, `date` "
                            "FROM `booking_table`")
                        self.cursor.execute(self.sql_query)
                        self.results = self.cursor.fetchall()
                        # print(self.results)
                        for self.idx, self.values in enumerate(self.results):
                            # print(self.values)
                            self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent",values=self.values)
                    except Exception as server_error:
                        tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")


                else:
                    print(" User cancelled")
                    self.vendor_name.set("")
                    self.vendor_phone.set("")
                    self.vendor_address.set("")
                    self.p_name.set("")
                    self.p_cat.set("")
                    self.p_desc.set("")
                    self.p_stock.set(0.0)
                    self.p_price.set(0)
                    self.p_status.set("")


            else:
                # print("Data not Found")
                joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
                self.p_date.set(joining_date)
                self.insert_query = (
                    "INSERT INTO `booking_table`(`v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                    " `quantity`, `price`,`status`, `date`) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                vals = (
                    self.vendor_name.get(), self.vendor_phone.get(), self.vendor_address.get(), self.p_name.get(),
                    self.p_cat.get(), self.p_desc.get(), self.p_stock.get(), self.p_price.get(), self.p_status.get(),
                    self.p_date.get())
                self.cursor.execute(self.insert_query, vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Order Added Successfully")

                self.vendor_name.set("")
                self.vendor_phone.set("")
                self.vendor_address.set("")
                self.p_name.set("")
                self.p_cat.set("")
                self.p_desc.set("")
                self.p_stock.set(0)
                self.p_price.set(0)
                self.p_status.set("")
                # self.p_date.set("")

                self.Order_table.delete(*self.Order_table.get_children())
                # Todo Complete : Added connectivity to show the data to the treeview
                try:
                    self.sql_query = (
                        "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                        " `quantity`, `price`, `status`, `date` "
                        "FROM `booking_table`")
                    self.cursor.execute(self.sql_query)
                    self.results = self.cursor.fetchall()
                    # print(self.results)
                    for self.idx, self.values in enumerate(self.results):
                        # print(self.values)
                        self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent",
                                                values=self.values)
                except Exception as server_error:
                    tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
    


    
    # update
    def update_order_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0 or self.p_price.get() == 0 or
                self.p_status.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")
        else:
            joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
            self.p_date.set(joining_date)
            self.update_query = ("UPDATE `booking_table` SET `v_name` = %s, `v_contact` = %s, `v_address` = %s, "
                                 "`name` = %s, `category` = %s, `description` = %s, `quantity` = %s, `price` = %s,"
                                 " `status` = %s, `date` = %s WHERE `Tran_id` = %s")
            vals = (self.vendor_name.get(), self.vendor_phone.get(), self.vendor_address.get(), self.p_name.get(),
                    self.p_cat.get(), self.p_desc.get(), self.p_stock.get(), self.p_price.get(), self.p_status.get(),
                    self.p_date.get(), self.Transaction_id.get())
            self.cursor.execute(self.update_query, vals)
            self.connection.commit()
            tmsg.showinfo("Success", "Transaction Updated Successfully")


            # Todo : Update the status and add it to purchase table and delete from booking
            self.r_status = 'Order Received'
            self.check_query = ("select * from booking_table where `status`=%s")
            self.vals = (self.r_status,)
            self.cursor.execute(self.check_query, self.vals)
            self.result = self.cursor.fetchall()
            if self.result:
                print(self.result)
                self.n_Transaction_id = self.result[0][0]
                self.n_vendor_name = self.result[0][1]
                self.n_vendor_phone = self.result[0][2]
                self.n_vendor_address = self.result[0][3]
                self.n_p_name = self.result[0][4]
                self.n_p_cat = self.result[0][5]
                self.n_p_desc = self.result[0][6]
                self.n_p_stock = self.result[0][7]
                self.n_p_price = self.result[0][8]
                self.n_p_status = self.result[0][9]
                self.n_p_date = self.result[0][10]

                # Todo : Purchase tabel done
                self.insert_query = ("INSERT INTO `vendor_table`(`v_name`, `v_contact`, `v_address`,`name`, "
                                     "`category`, `description`, `quantity`, `price`, `date`) "
                                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                self.vals = (self.n_vendor_name, self.n_vendor_phone, self.n_vendor_address, self.n_p_name,
                             self.n_p_cat, self.n_p_desc, self.n_p_stock, self.n_p_price, self.n_p_date)
                self.cursor.execute(self.insert_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Transaction Added To Purchase Successfully")
                # self.a_result = self.cursor.fetchall()



                # Todo : Add quantity and product in product table
                # self.check_n = self.n_p_name.get()
                self.check_query = ("select * from product_table where `name`=%s")
                self.vals = (self.n_p_name,)
                self.cursor.execute(self.check_query, self.vals)
                self.p_result = self.cursor.fetchall()
                if self.p_result:
                    # print(self.result)
                    self.stk_n = self.p_result[0][4]
                    self.check_stk = self.n_p_stock
                    self.check_n = self.n_p_name

                    self.updated_stk = self.stk_n + self.check_stk
                    self.add_query = ("UPDATE `product_table` SET `quantity` = %s WHERE `name`=%s")
                    self.vals = (self.updated_stk, self.check_n)
                    self.cursor.execute(self.add_query, self.vals)
                    self.connection.commit()
                    tmsg.showinfo("Success", "Transaction Added Successfully")

                else:
                    self.p_insert_query = (
                        "INSERT INTO `product_table`( `name`, `description`, `category`, `quantity`, `price`, `date`) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
                    self.vals = (self.n_p_name, self.n_p_desc, self.n_p_cat, self.n_p_stock, self.n_p_price, self.n_p_date)
                    self.cursor.execute(self.p_insert_query, self.vals)
                    self.connection.commit()
                    tmsg.showinfo("Success", "Transaction Added Successfully With New Product Data")


                # ToDo : deleting status received query from booking table
                self.del_query = ("DELETE from `booking_table` WHERE `name` = %s AND `category` = %s AND `status` = %s ")
                self.vals = (self.n_p_name,self.n_p_cat,self.r_status)
                self.cursor.execute(self.del_query,self.vals)
                self.connection.commit()
                print("deleted from database")
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
                self.p_status.set("")

                self.Order_table.delete(*self.Order_table.get_children())
                # Todo Complete : Added connectivity to show the data to the treeview
                try:
                    self.sql_query = (
                        "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                        " `quantity`, `price`, `status`, `date` "
                        "FROM `booking_table`")
                    self.cursor.execute(self.sql_query)
                    self.oresults = self.cursor.fetchall()
                    # print(self.results)
                    for self.idx, self.values in enumerate(self.oresults):
                        # print(self.values)
                        self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent",values=self.values)
                except Exception as server_error:
                    tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")


            self.result.clear()





    def delete_order_data(self):
        if (self.vendor_name.get() == "" or self.vendor_phone.get() == "" or
                self.vendor_address.get() == "" or self.p_name.get() == "" or
                self.p_cat.get() == "" or self.p_desc.get() == "" or
                self.p_stock.get() == 0 or self.p_price.get() == 0
                or self.p_status.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled correctly")
        else:
            self.del_query = ("DELETE from `booking_table` WHERE `Tran_id` = %s")
            vals = (self.Transaction_id.get(),)
            self.cursor.execute(self.del_query, vals)
            print("deleted from database")
            self.connection.commit()
            tmsg.showinfo("Success", "Transaction deleted successfully")

            self.vendor_name.set("")
            self.vendor_phone.set("")
            self.vendor_address.set("")
            self.p_name.set("")
            self.p_cat.set("")
            self.p_desc.set("")
            self.p_stock.set(0)
            self.p_price.set(0)
            self.p_status.set("")

            self.Order_table.delete(*self.Order_table.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = (
                    "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                    " `quantity`, `price`, `status`, `date` "
                    "FROM `booking_table`")
                self.cursor.execute(self.sql_query)
                self.oresults = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.oresults):
                    # print(self.values)
                    self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")




    def clear_order_fields(self):
        # self.Transaction_id.set(0)
        self.vendor_name.set("")
        self.vendor_phone.set("")
        self.vendor_address.set("")
        self.p_name.set("")
        self.p_cat.set("")
        self.p_desc.set("")
        self.p_stock.set(0)
        self.p_price.set(0)
        self.p_status.set("")

        self.Order_table.delete(*self.Order_table.get_children())
        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = (
                "SELECT `Tran_id`, `v_name`, `v_contact`, `v_address`,`name`,  `category`, `description`,"
                " `quantity`, `price`, `status`, `date` "
                "FROM `booking_table`")
            self.cursor.execute(self.sql_query)
            self.oresults = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.oresults):
                # print(self.values)
                self.Order_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

        self.v_search.set("")






    def check_cartclass_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_order_data()
        elif event.widget.cget("text") == "Update":
            self.update_order_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_order_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_order_fields()


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


    def set_back(self, ev):
        self.destroy()
        sys.exit()


    def cart_close(self):
        self.destroy()
        sys.exit()





if __name__ == '__main__':
    cart = Cartcls()
    cart.mainloop()
















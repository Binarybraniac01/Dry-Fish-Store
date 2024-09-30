from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import datetime

class Stockcls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770

        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)




        # variables

        self.prod_id = IntVar()
        self.prod_name = StringVar()
        self.prod_description = StringVar()
        self.prod_category = StringVar()
        self.prod_stock = DoubleVar()
        self.prod_add_stock = DoubleVar()
        self.prod_price = IntVar()
        self.prod_sp_price = IntVar()
        # self.prod_curr_stock = IntVar()
        self.curr_date = StringVar()

        self.Prod_search = StringVar()



        # Calling methods
        self.setgeometry()
        self.set_stk_frames()
        self.Prod_label()
        self.search_bar()
        self.Product_table()





    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")



    def set_stk_frames(self):
        self.ParentFrame = Frame(self, height=770, width=1450,bg="#DFD7BF")
        self.ParentFrame.place(x=0, y=146)

        self.stk_prodFrame = Frame(self.ParentFrame,bd=4, height=770,width=1450,bg="#DFD7BF")
        self.stk_prodFrame.place(x=0,y=0)

        # self.Prod_label()
        # self.stk_bttons()



    # ADDING LABELS AND TEXTFIELDS
    def Prod_label(self):

        self.prod_name_lbl = Label(self.stk_prodFrame, text="Product Name", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_name_lbl.place(x=50, y=100)
        self.prod_name_entry = Entry(self.stk_prodFrame, textvariable=self.prod_name, font=("comic", 20))
        self.prod_name_entry.place(x=300, y=100)

        self.prod_description_lbl = Label(self.stk_prodFrame, text="Description", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_description_lbl.place(x=50,y=170)
        self.prod_description_entry = Entry(self.stk_prodFrame,textvariable=self.prod_description,font=("comic",20))
        self.prod_description_entry.place(x=300,y=170)

        self.prod_category_lbl = Label(self.stk_prodFrame, text="Category", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_category_lbl.place(x=50, y=240)
        self.prod_category_entry = Entry(self.stk_prodFrame, textvariable=self.prod_category, font=("comic", 20))
        self.prod_category_entry.place(x=300, y=240)

        self.prod_stock_lbl = Label(self.stk_prodFrame, text="Quantity", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_stock_lbl.place(x=50, y=310)
        self.prod_stock_entry = Entry(self.stk_prodFrame, textvariable=self.prod_stock, font=("comic", 20),width=15)
        self.prod_stock_entry.place(x=300, y=310)
        # For KG
        self.prod_stock_lbl_kg = Label(self.stk_prodFrame, text="KG", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_stock_lbl_kg.place(x=550, y=310)


        self.prod_add_stock_lbl = Label(self.stk_prodFrame, text="Add Quantity", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_add_stock_lbl.place(x=50, y=380)
        self.prod_add_stock_entry = Entry(self.stk_prodFrame, textvariable=self.prod_add_stock, font=("comic", 20),width=15)
        self.prod_add_stock_entry.place(x=300, y=380)
        # for KG
        self.prod_add_stock_lbl_kg = Label(self.stk_prodFrame, text="KG", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_add_stock_lbl_kg.place(x=550, y=380)

        self.prod_price_lbl = Label(self.stk_prodFrame, text="Total Cost Price", font=("Poor Richard", 20, "bold"),bg="#DFD7BF")
        self.prod_price_lbl.place(x=50, y=420)
        self.prod_price_entry = Entry(self.stk_prodFrame, textvariable=self.prod_price, font=("comic", 20))
        self.prod_price_entry.place(x=300, y=420)

        self.prod_sp_price_lbl = Label(self.stk_prodFrame, text="S.P. Per KG", font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.prod_sp_price_lbl.place(x=50, y=460)
        self.prod_sp_price_entry = Entry(self.stk_prodFrame, textvariable=self.prod_sp_price, font=("comic", 20))
        self.prod_sp_price_entry.place(x=300, y=460)



    # ADDING  ALL BUTTONS BY FUNCTION
    def stk_bttons(self, btn_name, x, y):
        self.btn = Button(self.stk_prodFrame, text=btn_name, font=("Poor Richard",20, "bold"),bd=2, width=6, fg="white", bg="#3F2305")
        self.btn.place(x=x, y=y)
        self.btn.bind("<Button - 1>", self.check_inventory_btn_event)




    # SEARCH BAR OUERY
    def search_bar(self):

        self.search_Lable = Label(self.stk_prodFrame,text="Search Product By Name :",font=("Poor Richard", 20, "bold"),borderwidth=0,bg="#DFD7BF")
        self.search_Lable.place(x=700,y=60)

        self.search_Lable_entry = Entry(self.stk_prodFrame,textvariable=self.Prod_search,font=("comic", 20),borderwidth=0)
        self.search_Lable_entry.place(x=1000,y=60)
        self.search_Lable_entry.bind("<Key>",self.search)





    # PRODUCT TABLE
    def Product_table(self):

        self.P_frame = Frame(self.stk_prodFrame,bd=3,bg="#DFD7BF")
        self.P_frame.place(x=700,y=100,height=480,width=720)

        self.scollx = Scrollbar(self.P_frame,orient=HORIZONTAL)
        self.scolly = Scrollbar(self.P_frame, orient=VERTICAL)

        self.P_inven_table = ttk.Treeview(self.P_frame,columns=("pid", "name", "description", "category", "quantity",
                                                                "price", "sp_price"),
                                          xscrollcommand=self.scollx.set,yscrollcommand=self.scolly.set,)
        self.scollx.pack(side=BOTTOM, fill="x")
        self.scolly.pack(side=RIGHT, fill="y")

        self.scollx.config(command=self.P_inven_table.xview)
        self.scolly.config(command=self.P_inven_table.yview)


        # giving headings
        self.P_inven_table.heading("pid",text="Product Id")
        self.P_inven_table.heading("name", text="Product Name")
        self.P_inven_table.heading("description", text="Description")
        self.P_inven_table.heading("category", text="Category")
        self.P_inven_table.heading("quantity", text="Quantity")
        self.P_inven_table.heading("price", text="Total Cost Price")
        self.P_inven_table.heading("sp_price", text="Selling Price Per KG")

        self.P_inven_table["show"] = "headings"


        self.P_inven_table.column("pid",width=100,minwidth=100,anchor=CENTER)
        self.P_inven_table.column("name", width=150,minwidth=100,anchor=CENTER)
        self.P_inven_table.column("description",width=200,minwidth=100,anchor=CENTER)
        self.P_inven_table.column("category", width=150, minwidth=100,anchor=CENTER)
        self.P_inven_table.column("quantity", width=100,minwidth=100,anchor=CENTER)
        self.P_inven_table.column("price",width=100,minwidth=100,anchor=CENTER)
        self.P_inven_table.column("sp_price",width=200,minwidth=100,anchor=CENTER)


        self.P_inven_table.pack(fill=BOTH,expand=1)


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
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.P_inven_table.bind("<<TreeviewSelect>>", self.show_prod_data)


    # SHOWING DATA  OF THE TABLE ON REFRESH
    def show_prod_data(self, event):
        # global curr_position
        self.curr_position = self.P_inven_table.selection()
        self.curr_position = self.P_inven_table.item(self.curr_position)
        # print(self.curr_position["values"][0])
        self.len_curr_position = len(self.curr_position["values"])
        if (self.len_curr_position < 7):
            pass
        else:
            self.prod_id.set(int(self.curr_position["values"][0]))
            self.prod_name.set(self.curr_position["values"][1])
            self.prod_description.set(self.curr_position["values"][2])
            self.prod_category.set(self.curr_position["values"][3])
            self.prod_stock.set(float(self.curr_position["values"][4]))
            self.prod_price.set(int(self.curr_position["values"][5]))
            self.prod_sp_price.set(int(self.curr_position["values"][6]))
            self.prod_add_stock.set(0.0)



    # ADD BUTTON QUERY
    def add_product_data(self):
        search_query = ("select * from `product_table` where `name` = %s ")
        vals = (self.prod_name.get(),)
        self.cursor.execute(search_query, vals)
        result = self.cursor.fetchall()
        if result:
            print(f"{self.prod_name.get()} is already exist.")
            tmsg.showwarning("Warning", f"{self.prod_name.get()} "
                                        f"is already available.")
        else:
            joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
            self.curr_date.set(joining_date)
            self.insert_query = (
                "INSERT INTO `product_table`( `name`, `description`, `category`, `quantity`, `price`, `date`, `sp_price`) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            vals = (self.prod_name.get(), self.prod_description.get(), self.prod_category.get(), self.prod_stock.get(),
                    self.prod_price.get(), self.curr_date.get(), self.prod_sp_price.get())
            self.cursor.execute(self.insert_query, vals)
            self.connection.commit()
            tmsg.showinfo("Success", "Product Added Successfully")
            # self.prod_id.set("")
            self.prod_name.set("")
            self.prod_description.set("")
            self.prod_category.set("")
            self.prod_stock.set(0.0)
            self.prod_price.set(0)
            self.prod_sp_price.set(0)


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


    # UPDATE BUTTION QUERY
    def update_inventory_data(self):

        self.id = self.prod_id.get()
        self.name = self.prod_name.get()
        self.description = self.prod_description.get()
        self.category = self.prod_category.get()
        self.price = self.prod_price.get()
        self.add_stocks = self.prod_add_stock.get()
        self.selling_price = self.prod_sp_price.get()
        if self.add_stocks == 0.0 or self.add_stocks == "":
            self.prod_add_stock.set(0.0)
            self.current_stock = self.prod_stock.get()
        else:
            self.current_stock = (self.prod_stock.get()) + self.add_stocks

        if (self.prod_name.get() == "" or self.prod_category.get() == "" or
                self.prod_description.get() == "" or self.prod_price.get() == 0
                or self.prod_stock.get() == 0.0 or self.prod_sp_price.get() == 0):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:
            self.update_query = ("UPDATE `product_table` SET `name` = %s, `description` = %s, `category` = %s, "
                                 "`quantity` = %s, `price` = %s, `sp_price` = %s WHERE `pid` = %s")
            self.vals = (self.name, self.description, self.category, self.current_stock, self.price, self.selling_price, self.id)
            self.cursor.execute(self.update_query, self.vals)
            self.connection.commit()
            tmsg.showinfo("Success", "Product Updated Successfully")

            self.prod_name.set("")
            self.prod_description.set("")
            self.prod_category.set("")
            self.prod_stock.set(0.0)
            self.prod_add_stock.set(0.0)
            self.prod_price.set(0)
            self.prod_sp_price.set(0)


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



    # DELETE BUTTON QUERY
    def delete_inventory_data(self):
        if (self.prod_name.get() == "" or self.prod_category.get() == "" or
                self.prod_description.get() == "" or self.prod_price.get() == 0
                or self.prod_stock.get() == 0.0 or self.prod_sp_price.get() == 0):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:
            # self.id = self.prod_id.get()
            # print(self.id)
            self.del_query = ("DELETE from `product_table` WHERE `pid` = %s")
            vals = (self.prod_id.get(),)
            self.cursor.execute(self.del_query, vals)
            print("deleted from database")
            self.connection.commit()
            tmsg.showinfo("Success", "Product deleted successfully")
            self.prod_name.set("")
            self.prod_description.set("")
            self.prod_category.set("")
            self.prod_price.set(0)
            self.prod_sp_price.set(0)
            self.prod_stock.set(0.0)
            self.prod_add_stock.set(0.0)

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



    # CLEAR BUTTON QUERY
    def clear_inventory_fields(self):
        self.connection.commit()
        self.prod_name.set("")
        self.prod_description.set("")
        self.prod_category.set("")
        self.prod_price.set(0)
        self.prod_sp_price.set(0)
        self.prod_stock.set(0.0)
        self.prod_add_stock.set(0.0)

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

        self.Prod_search.set("")




    # TO CHECK WHICH BUTTON IS PRESSED
    def check_inventory_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_product_data()
        elif event.widget.cget("text") == "Update":
            self.update_inventory_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_inventory_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_inventory_fields()



    def check_inventory_quantity(self):
        try:
            self.search_query = ("SELECT `name`, `quantity` FROM product_table WHERE `quantity` < 5 ORDER BY `quantity` ASC LIMIT 10")
            self.cursor.execute(self.search_query)
            low_quantity_products = self.cursor.fetchall()

            if low_quantity_products:
                message = "Products with low quantity:\n"
                for product in low_quantity_products:
                    name, quantity = product
                    message += f"\nName: {name}\tQuantity: {quantity}\n"

                tmsg.showinfo("Low Quantity Alert", message)

            self.result = low_quantity_products

        except Exception as e:
            print(f"Error: {e}")
        # self.search_query = ("SELECT `pid`, `name`, `quantity` FROM product_table WHERE `quantity` < 5")
        # self.cursor.execute(self.search_query)
        # result = self.cursor.fetchall()





    # adding search bar
    def search(self,ev):
        try:
            self.search_query = ("SELECT `pid`, `name`, `description`, `category`, `quantity`, `price`, `sp_price` FROM product_table where name LIKE '%"+self.Prod_search.get()+"%'")
            self.cursor.execute(self.search_query)
            self.row = self.cursor.fetchall()
            #print(self.row)
            if len(self.row) > 0:
                self.P_inven_table.delete(*self.P_inven_table.get_children())
                for self.idx, self.values in enumerate(self.row):
                    # print(self.values)
                    self.P_inven_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            else:
                # print("table not found")
                self.P_inven_table.delete(*self.P_inven_table.get_children())

        except Exception as ex:
            tmsg.showerror(title="Connection Error", message=f"Error due to {str(ex)}")








if __name__ == '__main__':
    stk = Stockcls()
    stk.mainloop()



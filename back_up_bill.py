from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import random as rd
import os
import tempfile
import datetime

class Receipt(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        self.trans_id = StringVar()
        self.invoice_id = StringVar()
        self.bill_sr_no = IntVar(value=1)
        self.bill_prod_name = StringVar()
        self.bill_prod_category = StringVar()
        self.bill_prod_quantity = IntVar()
        self.bill_prod_price = IntVar()
        self.bill_cust_name = StringVar()
        self.bill_cust_phone = StringVar()
        self.bill_cust_email = StringVar()
        self.bill_cust_address = StringVar()
        self.total_bill = IntVar()

        self.billing_date = StringVar()
        self.billing_time = StringVar()

        self.purchased_products_prices = []
        self.selected_products = []
        self.added_product_quantity = []





        # Calling methods
        self.setgeometry()
        # self.set_frames()
        # self.child_frame_1()
        # self.child_frame_2()
        # self.billing_ui()


    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")

    def set_frames(self):
        self.recpt_Frame = Frame(self, height=770, width=1450, bg="#DFD7BF")
        self.recpt_Frame.place(x=0, y=146)

    def child_frame_1(self):
        self.child_frame1 = Frame(self.recpt_Frame, height=610, width=830, bg="#DFD7BF")
        self.child_frame1.place(x=1, y=2)

    def child_frame_2(self):
        self.child_frame2 = Frame(self.recpt_Frame, bd=2, relief=GROOVE, bg="#DFD7BF")
        self.child_frame2.place(x=880, y=40, height=550, width=510)

    def set_btn(self, btn_name, x, y, padx):
        self.btn = Button(self.child_frame1, text=btn_name, font=("bookman old style", 14, "bold"),
                          compound=TOP, relief=RAISED, padx=padx)
        self.btn.place(x=x, y=y)
        self.btn.bind("<Button - 1>", self.check_bill_btn_event)



    def billing_ui(self):
        self.customer_name_label = Label(self.child_frame1, text="Customer Name",
                                         font=("comic", 16, "bold"), bg="#C70163")
        self.customer_name_label.place(x=2, y=60)
        self.customer_contact_label = Label(self.child_frame1, text="Contact No.",
                                            font=("comic", 16, "bold"), bg="#C70163")
        self.customer_contact_label.place(x=2, y=110)
        self.product_name_label = Label(self.child_frame1, text="Product Name",
                                        font=("comic", 16, "bold"), bg="#C70163")
        self.product_name_label.place(x=2, y=160)
        self.product_category_label = Label(self.child_frame1, text="category",
                                        font=("comic", 16, "bold"), bg="#C70163")
        self.product_category_label.place(x=2, y=210)
        self.product_quantity_label = Label(self.child_frame1, text="Quantity",
                                            font=("comic", 16, "bold"), bg="#C70163")
        self.product_quantity_label.place(x=2, y=260)
        # self.product_price_label = Label(self.child_frame1, text="Price",
        #                           font=("comic", 16, "bold"), bg="#C70163")
        # self.product_price_label.place(x=2, y=310)

        self.customer_name_entry = Entry(self.child_frame1, textvariable=self.bill_cust_name,
                                         font="roboto 12 bold", width=30)
        self.customer_name_entry.place(x=200, y=61, height=30)
        self.customer_contact_entry = Entry(self.child_frame1, textvariable=self.bill_cust_phone,
                                            font="roboto 12 bold", width=30)
        self.customer_contact_entry.place(x=200, y=111, height=30)

        sql_query = (
            "SELECT `name`, `category`, `quantity` FROM `product_table`"
        )
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()

        # Products Names
        prod_names = []
        for idx, val in enumerate(result):
            prod_names.append(val[0])
        self.product_name_entry_combo = ttk.Combobox(self.child_frame1, values=list(set(prod_names)),
                                                     textvariable=self.bill_prod_name, font="roboto 12 bold", width=28)
        self.product_name_entry_combo.place(x=200, y=161, height=30)
        self.product_name_entry_combo.bind("<<ComboboxSelected>>", self.update_category_combo)

        # Product Category
        self.prod_category = []
        self.product_category_entry_combo = ttk.Combobox(self.child_frame1, values=self.prod_category,
                                                         textvariable=self.bill_prod_category, font="roboto 12 bold", width=28)
        self.product_category_entry_combo.place(x=200, y=211, height=30)
        self.product_category_entry_combo.bind("<<ComboboxSelected>>", self.show_available_stock)


        # Products Quantity
        self.product_quantity_entry = Entry(self.child_frame1, textvariable=self.bill_prod_quantity,
                                            font="roboto 12 bold", width=30)
        self.product_quantity_entry.place(x=200, y=261, height=30)

        # Available Stock In Inventory
        self.product_curr_stock = Label(self.child_frame1, text=f"Available Stock : ",
                                        font=("Bookman Old Style", 14, "bold"),
                                        bg="#C70163", fg="white")
        self.product_curr_stock.place(x=2, y=310)



    def bill_screen(self):
        self.billing_label = Label(self.child_frame2, text="Bill Window", font=("Bookman Old Style", 20, "bold"),
                                   fg="white", bg="grey60")
        self.billing_label.pack(fill=BOTH)

        self.scrollbary = Scrollbar(self.child_frame2, orient=VERTICAL)

        self.bill_textarea = Text(self.child_frame2, height=300, width=410, yscrollcommand=self.scrollbary.set,
                                  font=("comic", 10, "bold"))

        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.scrollbary.config(command=self.bill_textarea.yview)

        self.bill_textarea.pack()
        self.shop_bill_design()


    # Preventing reoccarence of specific id
    def validating_invoice_id(self):
        # print("Inside invoice id function")
        # checking if invoice_id is already present or not
        self.invoice_no = rd.randint(1000, 10000)
        check_invoice = (
            "SELECT `transaction_id` FROM `sales_table` WHERE `invoice_id` = %s"
        )
        vals = (self.invoice_no,)
        self.cursor.execute(check_invoice, vals)
        result = self.cursor.fetchall()
        if result:
            self.invoice_no = rd.randint(1000, 10000)

        self.invoice_id.set(str(self.invoice_no))



    def shop_bill_design(self):
        self.bill_textarea.delete(1.0, END)
        shop_details = ("\t\t           PREMIUM DRY FISH EMPORIUM\n"
                        "\t\t\t    Address : PEN - 402107\n"
                        "\t\t\t     Mob no. 1234567890\n"
                        "\t\t\t  GSTIN - 27DRYFISH9Z18\n")
        self.seperator = "\n============================================================"
        # name = "TEST USER"
        # phone = "0987615423"
        # self.bill_cust_phone.set(phone)
        # self.bill_cust_name.set(name)

        section_1 = (f"\nInvoice No.: {self.invoice_id.get()}\t\t\t\t           \n\n"
                     f"Customer Name: {self.bill_cust_name.get()}\t\t\tContact No.: "
                     f"{self.bill_cust_phone.get()}\n")
        section_2 = "\nProduct Name\t\t\tCategory\t\tQuantity\t\tPrice\n"
        self.bill_textarea.insert(END, shop_details)
        self.bill_textarea.insert(END, self.seperator)
        self.bill_textarea.insert(END, section_1)
        self.bill_textarea.insert(END, self.seperator)
        self.bill_textarea.insert(END, section_2)
        self.bill_textarea.insert(END, self.seperator)
        self.bill_textarea.insert(END, "\n")




    def add_product_to_bill(self):
        if (self.bill_cust_name.get() == "" or self.bill_cust_phone.get() == "" or self.bill_prod_name.get() == ""
                or self.bill_prod_category.get() == "" or self.bill_prod_quantity.get() == 0):

            tmsg.showwarning("Warning", "Make Sure to Fill all the Fields.")

        elif "Total" in self.bill_textarea.get("end-1l", "end"):
            tmsg.showwarning("Warning", "Bill Preview is Generated with Total Amount.\n"
                                        "First Clear the Bill Section and then add the new Items.")
        else:

            fetch_prod_price = (
                "SELECT `pid`, `price`, `quantity` from `product_table` WHERE `name`=%s and `category`=%s"
            )
            vals = (self.bill_prod_name.get(), self.bill_prod_category.get())
            self.cursor.execute(fetch_prod_price, vals)
            self.result = self.cursor.fetchall()
            # print("results : ", self.result)
            self.products_ids_ = int(self.result[0][0])

            # s_q_price = self.result[0][1] // self.result[0][2]
            # price_per_gram = s_q_price / 1000
            # qua_in_gram = float(self.bill_prod_quantity.get()) * 1000
            # price_ = price_per_gram * qua_in_gram

            price_ = int(self.result[0][1] * self.bill_prod_quantity.get())
            self.bill_prod_price.set(price_)

            self.product_string = (f"\n{self.bill_prod_name.get()}\t\t"
                                   f"\t{self.bill_prod_category.get()}\t\t    "
                                   f"{self.bill_prod_quantity.get()}\t  "
                                   f"    \t{self.bill_prod_price.get()}")

            self.bill_textarea.insert(END, self.product_string)
            self.purchased_products_prices.append(self.bill_prod_price.get())
            self.selected_products.append(self.products_ids_)
            self.added_product_quantity.append(self.bill_prod_quantity.get())

            self.total_bill.set(sum(self.purchased_products_prices))

            self.bill_prod_name.set("")
            self.bill_prod_category.set("")
            self.bill_prod_quantity.set(0)




    def remove_product_from_bill(self):
        if self.bill_textarea.get("end-1l", "end") == "\n":
            tmsg.showwarning("Warning", "No Product Added in Bill")

        elif "Total" in self.bill_textarea.get("end-1l", "end"):
            tmsg.showwarning("Warning", "Total Amount is Generated. \nUse Clear to Clear Bill.")

        else:
            self.bill_textarea.delete("end-1l", "end")
            self.purchased_products_prices.pop()
            self.selected_products.pop()
            self.added_product_quantity.pop()


        self.total_bill.set(sum(self.purchased_products_prices))




    def show_total_amount(self):

        if self.bill_textarea.get("end-1l", "end") == "\n":
            tmsg.showwarning("Warning", "Please First Add the Products in the Bill")
        elif "Total" in self.bill_textarea.get("end-1l", "end"):
            tmsg.showwarning("Warning", "The Bill with Total Amount has already Shown.")
        else:
            self.bill_textarea.insert(END, self.seperator)
            self.total_amount_string = (f"\n\n"
                                        f"\t    \t    \t    \t    \t    \tTotal : {self.total_bill.get()}")
            self.bill_textarea.insert(END, self.total_amount_string)


    def update_category_combo(self, event):
        # Filtering Results Based on the Selection Made - Product Name
        if self.bill_prod_name.get() != "":

            filter_query = (
                "SELECT `category` FROM `product_table` WHERE `name`=%s"
            )
            val = (self.bill_prod_name.get(),)
            self.cursor.execute(filter_query, val)
            category_result = self.cursor.fetchall()
            # print(category_result)
            for idx, val in enumerate(category_result):
                # print(val)
                self.prod_category.append(val[0])

        self.product_category_entry_combo.config(values=self.prod_category)
        self.prod_category.clear()
        self.bill_prod_category.set("")



    def show_available_stock(self, event):
        search_stock = (
            "SELECT `quantity` FROM `product_table` WHERE `name`=%s and `category`=%s"
        )
        vals = (self.product_name_entry_combo.get(), self.product_category_entry_combo.get())
        self.cursor.execute(search_stock, vals)
        stk = self.cursor.fetchall()
        # print(stk)
        self.product_curr_stock.config(text=f"Available Stock :   {stk[0][0]}")



    def database_interaction(self):
        """Very Essential AND Important Separate Function for Managing ALL
        The Necessary SQl queries When Generating The Final Bill."""

        # Database Work-Flow Section

        # Getting Current Date AND Time

        bill_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
        self.billing_date.set(bill_date)
        bill_time = str(datetime.datetime.now().strftime("%I:%M:%S"))
        self.billing_time.set(bill_time)

        # ----------------- #

        # Getting Product name, size, stock details from Product_table using corresponding Ids.

        for prod_id in self.selected_products:

            # Fetch required product info from Product Table
            fetch_query = (
                "SELECT `name`, `category`, `quantity` FROM `product_table` WHERE `pid` = %s"
            )
            val = (prod_id,)
            self.cursor.execute(fetch_query, val)
            result = self.cursor.fetchall()

            # ----------------- #

            # Getting Quantity and Price of Purchased Product form the Bill

            for quant, total_price in zip(self.added_product_quantity, self.purchased_products_prices):
                # Updating Stock - Deleting Sold No. of Idols from Original Stock
                old_stock = int(result[0][2])
                new_stock = int(old_stock - quant)

                update_query = (
                    "UPDATE `product_table` SET `quantity` = %s where `pid` = %s"
                )
                update_vals = (new_stock, prod_id)
                self.cursor.execute(update_query, update_vals)
                self.connection.commit()

                # ----------------- #


                # Inserting Corresponding Values to the Sales Table and Committing the Connection
                sales_insert_query = (
                    "INSERT INTO `sales_table` (`invoice_id`, `pname`, `category`, `quantity`, "
                    "`price`, `cust_name`, `cust_phone`, `date`, `time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )
                sales_vals = (self.invoice_id.get(), str(result[0][0]), str(result[0][1]), quant,
                              total_price, self.bill_cust_name.get(), self.bill_cust_phone.get(),
                              self.billing_date.get(), self.billing_time.get())
                self.cursor.execute(sales_insert_query, sales_vals)
                self.connection.commit()

                # ----------------- #


                # Inserting Corresponding Values to the Customer Table and Committing the Connection
                cust_query = (
                    "SELECT * FROM `customer_table` WHERE `cust_name` = %s AND `cust_contact` = %s"
                )
                val = (self.bill_cust_name.get(), self.bill_cust_phone.get())
                self.cursor.execute(cust_query, val)
                c_result = self.cursor.fetchall()

                if c_result :
                    old_pri = int(c_result[0][5])
                    new_pri = int(old_pri + total_price)
                    update_cust_query = (
                        "UPDATE `customer_table` SET `total_purchase` = %s where `cust_name` = %s AND `cust_contact` = %s"
                    )
                    update_cust_vals = (new_pri,self.bill_cust_name.get(), self.bill_cust_phone.get())
                    self.cursor.execute(update_cust_query, update_cust_vals)
                    self.connection.commit()
                else:
                    cust_insert_query = (
                        "INSERT INTO `customer_table` (`cust_name`, `cust_contact`, `total_purchase`) "
                        "VALUES (%s, %s, %s)"
                    )
                    insrt_vals = (self.bill_cust_name.get(), self.bill_cust_phone.get(),total_price)
                    self.cursor.execute(cust_insert_query, insrt_vals)
                    self.connection.commit()

                # ----------------- #



                # Removing Quantity and Price OF the Purchased Product for Better LOOP iteration
                self.added_product_quantity.remove(quant)
                self.purchased_products_prices.remove(total_price)

                # ----------------- #

                break  # Breaking the Nested ( 2nd ) for loop to avoid recursive iteration over same value

    # ----------------------------- #

    def generate_final_bill(self):
        """Function Responsible for Generating the Finalize Bill"""

        # Some Essential Validation to Avoid Errors
        if self.bill_textarea.get("end-1l", "end") == "\n":
            tmsg.showerror("Error", "Bill is Empty. NO Product Added.")
        elif "Total" not in self.bill_textarea.get("end-1l", "end"):
            tmsg.showwarning("Warning", "Please First Generate Total Amount by Clicking On `Total` Button.")
        elif not self.added_product_quantity:
            tmsg.showwarning("Warning", "Bill has been already Generated. To Generate New Bill Clear the "
                                        "Bill Window using `Clear` button.")
        else:

            # Getting User Confirmation Before Proceeding to Generate the Final Bill.
            answer = tmsg.askyesno("Confirmation", "Are you sure want to Generate the Bill")

            # IF User Grants Permission ( Select Yes )
            if answer:
                # Calling Database-Connectivity Function
                self.database_interaction()

                # Creating copy of Bill in txt file with name as - Bill_NO.txt
                bill_content = self.bill_textarea.get(1.0, END)
                saved_bills_location = "saved_bills\\"
                with open(f"{saved_bills_location}{self.invoice_id.get()}", "w") as f:
                    f.write(bill_content)

                    # Creating temp file for storing content in that file so we can further print it and create pdf
                    file = tempfile.mktemp(".txt")
                    open(file, "w").write(bill_content)
                    os.startfile(file, "print")
                    tmsg.showinfo("Success", "Bill Generated Successfully.")
            else:
                tmsg.showinfo("Confirmation", "Bill not Generated.")









    def clear_bill_screen_fields(self):
        self.bill_cust_name.set("")
        self.bill_cust_phone.set("")
        self.bill_prod_name.set("")
        self.bill_prod_category.set("")
        self.bill_prod_quantity.set(0)
        self.bill_textarea.delete(16.0, "end")

        self.selected_products.clear()
        self.purchased_products_prices.clear()
        self.added_product_quantity.clear()
        self.invoice_id.set("")






    def check_bill_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            # print(self.bill_textarea.get("end-1l", "end"))
            if self.bill_textarea.get("end-1l", "end") == "\n":
                self.validating_invoice_id()
                self.shop_bill_design()
            self.add_product_to_bill()
        elif event.widget.cget("text") == "Delete":
            self.remove_product_from_bill()
        elif event.widget.cget("text") == "Total":
            self.show_total_amount()
        elif event.widget.cget("text") == "Clear":
            self.clear_bill_screen_fields()
        elif event.widget.cget("text") == "Generate":
            self.generate_final_bill()






if __name__ == '__main__':
    rcpt = Receipt()
    rcpt.setgeometry()
    rcpt.set_frames()
    rcpt.child_frame_1()
    rcpt.child_frame_2()
    rcpt.billing_ui()
    rcpt.mainloop()
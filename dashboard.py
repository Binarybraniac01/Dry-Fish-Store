from tkinter import *
from stocks_n_products import Stockcls
from purchaseinfo import Vendorcls
from bill import Receipt
from sales_info import Salescls
from customer_info import Customercls
from worker_payment import WorkerPaymentCls
import mysql.connector
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import sys
import subprocess
from tkinter import messagebox






class Dashboardcls(Tk):
    def __init__(self):
        super().__init__()


        self.title("WELCOME")
        # variables of Stock class
        self.prod_id = IntVar()
        self.prod_name = StringVar()
        self.prod_description = StringVar()
        self.prod_category = StringVar()
        self.prod_stock = DoubleVar()
        self.prod_add_stock = DoubleVar()
        self.prod_price = IntVar()
        self.prod_sp_price = IntVar()
        self.curr_date = StringVar()
        self.Prod_search = StringVar()

        # Purchaseinfo variables
        self.Transaction_id = IntVar()
        self.vendor_name = StringVar()
        self.vendor_phone = IntVar()
        self.vendor_address = StringVar()
        self.p_name = StringVar()
        self.p_desc = StringVar()
        self.p_cat = StringVar()
        self.p_stock = DoubleVar()
        self.p_price = IntVar()
        self.p_date = StringVar()
        self.v_search = StringVar()


        # variables for receipt
        self.trans_id = StringVar()
        self.invoice_id = StringVar()
        self.bill_prod_name = StringVar()
        self.bill_prod_category = StringVar()
        self.bill_prod_quantity = DoubleVar()
        self.bill_prod_price = IntVar()
        self.bill_cust_name = StringVar()
        self.bill_cust_phone = StringVar()
        self.total_bill = IntVar()
        self.billing_date = StringVar()
        self.billing_time = StringVar()
        self.purchased_products_prices = []
        self.selected_products = []
        self.added_product_quantity = []

        # Variables for sale
        self.sale_trans_id = StringVar()
        self.sale_invoice_id = StringVar()
        self.sale_prod_name = StringVar()
        self.sale_prod_category = StringVar()
        self.sale_prod_quantity = DoubleVar()
        self.sale_prod_price = IntVar()
        self.sale_cust_name = StringVar()
        self.sale_cust_phone = StringVar()
        self.sale_date = StringVar()
        self.sale_time = StringVar()
        self.sale_Prod_search = StringVar()


        #  Customer variables
        self.cust_id = IntVar()
        self.cust_name = StringVar()
        self.cust_mail = StringVar()
        self.cust_contact = StringVar()
        self.cust_address = StringVar()
        self.cust_purchase = IntVar()
        self.cust_search = StringVar()

        # WorkerPaymentCls()
        self.pay_worker_id = IntVar()
        self.pay_worker_joining_date = StringVar()
        self.pay_worker_name = StringVar()
        self.pay_worker_designation = StringVar()
        self.pay_worker_salary = IntVar()
        self.payment_done = IntVar()
        self.payment_pending = IntVar()
        self.add_payment = IntVar()

        self.worker_pay_search = StringVar()



        self.width = 1450
        self.height = 770
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        self.protocol('WM_DELETE_WINDOW', self.dash_close)




        # self.screen_width = self.winfo_screenwidth()
        # self.screen_height = self.winfo_screenheight()
        # self.x = (self.screen_width / 2) - (self.width / 2)
        # print(self.x)
        # self.y = (self.screen_height / 2) - (self.height / 2)
        # print(self.y)





        # calling methods
        self.setgeometry()
        self.set_heading_label()
        self.Button_Frame()

        self.h_window()

        self.config(bg="#DFD7BF")
        # self.set_heading_label()
        # self.main_dash()
        # self.Button_Frame()

        ## self.set_nvbar_btns()

        # Connection
        self.establish_connection()



        # setting buttons on NavBar
        self.nav_buttons("Home")
        self.button.place(x=80, y=5)
        self.button.bind("<Button-1>", self.clicked)

        # self.nav_buttons("Profile")
        # self.button.place(x=200, y=5)

        self.nav_buttons("Stocks")
        self.button.place(x=240, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Sales")
        self.button.place(x=400, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Vendor Transactions")
        self.button.place(x=540, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Customer Details")
        self.button.place(x=790, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Receipt")
        self.button.place(x=1030, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Worker Payments")
        self.button.place(x=1200, y=5)
        self.button.bind("<Button-1>", self.clicked)












    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")

    def set_heading_label(self):
        self.heading_label = Label(self, text="Dry Fish Store", font=("Times New Roman", 28, "bold"), bd=4, relief=RIDGE,
                              height=2, bg="#F5F5F5")
        self.heading_label.pack(fill="x")





    # NAVIGATION BUTTON FRAME
    def Button_Frame(self):

        # top Navigation bar:
        self.topFrame = Frame(self, bg="#F2EAD3", bd=2, height=56, width=1450, relief=FLAT)
        self.topFrame.pack()


    def main_frame(self):
        self.imgFrame = Frame(self, height=700, width=1452, bg="#DFD7BF", relief=RAISED)
        self.imgFrame.place(x=-2, y=146)
        # self.imgFrame.pack(side=BOTTOM)


    def image_dash(self):
        self.mainFrame = Frame(self.imgFrame, height=700, width=1452, bg="#DFD7BF", relief=RAISED)
        self.mainFrame.place(x=-1,y=0)



    def image_bg(self):

        self.img = Image.open('All_images/home_img.jpeg')
        self.img = self.img.resize((1452, 700))
        self.photo = ImageTk.PhotoImage(self.img)
        self.label1 = Label(self.mainFrame, image=self.photo, relief=FLAT, bg="#DFD7BF")
        self.label1.pack(fill="y")

    def h_window(self):
        self.main_frame()
        self.image_dash()
        self.image_bg()






    def new_h_window(self):
        self.mainFrame.destroy()
        self.imgFrame.destroy()

        self.main_frame()
        self.image_dash()
        self.image_bg()






    # adding buttons
    def nav_buttons(self, btn_name=None):
        self.button = Button(self.topFrame, text=btn_name, font=("Poor Richard", 15, UNDERLINE), bg="#F2EAD3",
                             fg="black", relief="flat", borderwidth=0, padx=5, pady=5, activebackground="#F2EAD3")



    def clicked(self,event):
        self.clk_button = event.widget.cget("text")
        print(self.clk_button)

        if self.clk_button == "Home":
            self.home_window()

        elif self.clk_button == "Stocks":
            self.inventory_window()
            self.connection.commit()

        elif self.clk_button == "Vendor Transactions":
            self.purchase_window()
            self.connection.commit()

        elif self.clk_button == "Receipt":
            self.receipt_window()
            self.connection.commit()

        elif self.clk_button == "Sales":
            self.sales_window()
            self.connection.commit()

        elif self.clk_button == "Customer Details":
            self.customer_window()
            self.connection.commit()

        elif self.clk_button == "Worker Payments":
            self.worker_payment_window()
            self.connection.commit()

        else:
            print(self.clk_button)




    # def logout_btn(self, event):
    #     self.rvalue = messagebox.askyesno(title="Question", message=" Do you want to Logout ?")
    #     # print(self.rvalue)
    #     if self.rvalue == True:
    #         self.destroy()
    #         subprocess.call(["python", "login.py"])






    # Copying function from stockcls

    def show_prod_data(self, event):
        Stockcls.show_prod_data(self, event)

    def add_product_data(self):
        Stockcls.add_product_data(self)

    def update_inventory_data(self):
        Stockcls.update_inventory_data(self)

    def delete_inventory_data(self):
        Stockcls.delete_inventory_data(self)

    def clear_inventory_fields(self):
        Stockcls.clear_inventory_fields(self)

    def check_inventory_btn_event(self, event):
        Stockcls.check_inventory_btn_event(self, event)

    def search(self,ev):
        Stockcls.search(self,ev)

    def check_inventory_quantity(self):
        Stockcls.check_inventory_quantity(self)
    # END




    # Copying function from Vendorcls

    def show_purchase_data(self, event):
        Vendorcls.show_purchase_data(self,event)

    def add_purchase_data(self):
        Vendorcls.add_purchase_data(self)

    def update_purchase_data(self):
        Vendorcls.update_purchase_data(self)

    def delete_purchase_data(self):
        Vendorcls.delete_purchase_data(self)

    def clear_purchase_fields(self):
        Vendorcls.clear_purchase_fields(self)

    def check_vendorcls_btn_event(self, event):
        Vendorcls.check_vendorcls_btn_event(self,event)

    def V_search(self, ev):
        Vendorcls.V_search(self,ev)

    # GO TO CART Function
    def check_vendorcls_cart_btn_event(self, event):
        Vendorcls.check_vendorcls_cart_btn_event(self,event)

    def show_p_chart(self, event):
        Vendorcls.show_p_chart(self,event)

    #test
    # def show_p_chart(self):
    #     Vendorcls.show_p_chart(self)


    # End


    # Bill page
    def shop_bill_design(self):
        Receipt.shop_bill_design(self)

    def add_product_to_bill(self):
        Receipt.add_product_to_bill(self)

    def remove_product_from_bill(self):
        Receipt.remove_product_from_bill(self)

    def clear_bill_screen_fields(self):
        Receipt.clear_bill_screen_fields(self)

    def show_total_amount(self):
        Receipt.show_total_amount(self)

    def generate_final_bill(self):
        Receipt.generate_final_bill(self)

    def update_category_combo(self, event):
        Receipt.update_category_combo(self, event)

    def validating_invoice_id(self):
        Receipt.validating_invoice_id(self)

    def show_available_stock(self, event):
        Receipt.show_available_stock(self, event)

    def check_bill_btn_event(self, event):
        Receipt.check_bill_btn_event(self, event)


    # Very Important Function - DO NOT REMOVE OR REARRANGE IT'S POSITION
    def database_interaction(self):
        Receipt.database_interaction(self)

    # END OF Receipt()



    # Sales page
    def S_search(self,ev):
        Salescls.S_search(self,ev)

    def call_chart_window(self, event):
        Salescls.call_chart_window(self,event)

    # END



    # Customer page

    def show_cust_data(self, event):
        Customercls.show_cust_data(self, event)

    def add_cust_data(self):
        Customercls.add_cust_data(self)

    def update_cust_data(self):
        Customercls.update_cust_data(self)

    def delete_cust_data(self):
        Customercls.delete_cust_data(self)

    def clear_cust_fields(self):
        Customercls.clear_cust_fields(self)

    def check_cust_btn_event(self, event):
        Customercls.check_cust_btn_event(self, event)

    def c_search(self, ev):
        Customercls.c_search(self, ev)
    #END


    # Worker PAyment
    def show_worker_payment_data(self, event):
        WorkerPaymentCls.show_worker_payment_data(self, event)

    def check_worker_payment_btn_event_(self, event):
        WorkerPaymentCls.check_worker_payment_btn_event_(self, event)

    def update_worker_payment_data(self):
        WorkerPaymentCls.update_worker_payment_data(self)

    def search_worker_pay(self, event):
        WorkerPaymentCls.search_worker_pay(self, event)

    def clear_fields(self):
        WorkerPaymentCls.clear_fields(self)

    def go_to_details(self, event):
        WorkerPaymentCls.go_to_details(self,event)

    # END OF WorkerPaymentCls()











    # Creating Function to call structure of Stockcls


    def home_window(self):
        self.new_h_window()



    def inventory_window(self):
        Stockcls.set_stk_frames(self)
        Stockcls.Prod_label(self)
        Stockcls.search_bar(self)
        Stockcls.Product_table(self)

        # Buttons
        Stockcls.stk_bttons(self, "Add", x=50, y=530)
        Stockcls.stk_bttons(self, "Update", x=180, y=530)
        Stockcls.stk_bttons(self, "Delete", x=310, y=530)
        Stockcls.stk_bttons(self, "Clear", x=440, y=530)

        Stockcls.check_inventory_quantity(self)


    def purchase_window(self):
        Vendorcls.set_main_frame(self)
        Vendorcls.set_sub_frames(self)
        Vendorcls.Search_bar(self)
        Vendorcls.Purchase_details(self)

        # Buttons
        Vendorcls.Buttons(self,"Add", 890, 85)
        Vendorcls.Buttons(self,"Update", 1000, 85)
        Vendorcls.Buttons(self,"Delete", 1150, 85)
        Vendorcls.Buttons(self,"Clear", 1300, 85)
        Vendorcls.Buttons(self,"GO TO CART", 1268, 8, "cart_btn")
        Vendorcls.Buttons(self,"Purchase Chart",1000,8,"Chart")

    def receipt_window(self):
        Receipt.set_frames(self)
        Receipt.child_frame_1(self)
        Receipt.child_frame_2(self)
        Receipt.billing_ui(self)
        Receipt.bill_screen(self)

        # Buttons
        Receipt.set_btn(self, "Add", 100, 460, 25)
        Receipt.set_btn(self, "Delete", 250, 460,10)
        Receipt.set_btn(self, "Clear", 400, 460, 20)
        Receipt.set_btn(self, "Total", 550, 460, 20)
        Receipt.set_btn(self, "Receipt", 100, 520, 20)



    def sales_window(self):
        Salescls.set_stk_frames(self)
        Salescls.search_bar(self)
        Salescls.sales_info_table(self)

        Salescls.chart_btn(self,"Sales Chart",1200,10)



    def customer_window(self):
        Customercls.set_cust_frames(self)
        Customercls.sub_frame_1(self)
        Customercls.cust_label(self)
        Customercls.search_bar(self)
        Customercls.Customer_table(self)

        # Buttons
        Customercls.cust_bttons(self, "Add", x=50, y=500)
        Customercls.cust_bttons(self, "Update", x=180, y=500)
        Customercls.cust_bttons(self, "Delete", x=310, y=500)
        Customercls.cust_bttons(self, "Clear", x=440, y=500)




    def worker_payment_window(self):
        WorkerPaymentCls.set_frame(self)
        WorkerPaymentCls.child_frame_1(self)
        WorkerPaymentCls.child_frame_2(self)

        WorkerPaymentCls.worker_payment_ui(self)
        WorkerPaymentCls.worker_pay_search_bar(self)
        WorkerPaymentCls.worker_table(self)

        # Buttons
        WorkerPaymentCls.set_btn(self, "Update",  x=100, y=500)
        WorkerPaymentCls.set_btn(self, "Clear", x=370, y=500, padx=20)
        WorkerPaymentCls.set_btn(self, "Worker Details", 1200, 10, 20, "details")





    # Database Connectivity Section

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



    # Software Quit Window
    def dash_close(self):
        if tmsg.askyesno("Quit", " Leave Application?"):
            self.destroy()
            sys.exit()
            # exit(0)                      # FORCE SYSTEM TO EXIT





if __name__ == '__main__':
    dash = Dashboardcls()
    dash.mainloop()

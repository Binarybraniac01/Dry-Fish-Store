from tkinter import *
from stocks_n_products import Stockcls
from bill import Receipt
import mysql.connector
import tkinter.messagebox as tmsg

class Dashboard(Tk):
    def __init__(self):
        super().__init__()


        # variables of Stock class
        self.prod_id = IntVar()
        self.prod_name = StringVar()
        self.prod_description = StringVar()
        self.prod_category = StringVar()
        self.prod_stock = IntVar()
        self.prod_add_stock = IntVar()
        self.prod_price = IntVar()
        self.curr_date = StringVar()
        self.Prod_search = StringVar()




        # setting switch state:
        self.btnState = False

        # loading Navbar icon image:
        self.navIcon = PhotoImage(file="All_images/open.png")
        self.closeIcon = PhotoImage(file="close.png")


        self.width = 1450
        self.height = 770
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        # self.screen_width = self.winfo_screenwidth()
        # self.screen_height = self.winfo_screenheight()
        # self.x = (self.screen_width / 2) - (self.width / 2)
        # print(self.x)
        # self.y = (self.screen_height / 2) - (self.height / 2)
        # print(self.y)





        # calling methods
        self.setgeometry()
        self.set_heading_label()
        self.main_dash()
        self.set_nav_bar()
        # self.set_nvbar_btns()

        # Connection
        self.establish_connection()


        # setting buttons
        self.nav_buttons("Profile")
        self.button.place(x=20,y=80)

        self.nav_buttons("Stocks")
        self.button.place(x=20, y=150)
        self.button.bind("<Button-1>",self.clicked)

        self.nav_buttons("Client\nTransactions")
        self.button.place(x=20, y=220)

        self.nav_buttons("Vendor\nTransactions")
        self.button.place(x=20, y=320)

        self.nav_buttons("Receipt")
        self.button.place(x=20, y=420)
        self.button.bind("<Button-1>",self.clicked)










    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")

    def set_heading_label(self):
        self.heading_label = Label(self,text="Premium Dry Fish Emporium",font=("Times New Roman", 28, "bold"), bd=4, relief=RIDGE,
                             height=2, bg="green", fg="yellow")
        self.heading_label.pack(fill="x")

    # This is block to chnge(to do)

    def main_dash(self):
        self.mainFrame = Frame(self,height=770,width=1450,bg="yellow")
        self.mainFrame.place(x=0,y=90)


        # self.sub_frame = Frame(self.mainFrame,height=770,width=1450,bg="green")
        # self.sub_frame.place(x=0,y=55)
        # calling class
        # Stockcls.set_frames(self)





    #setting switch function:
    def set_switch(self):
        # global self.btnState
        if self.btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                self.navRoot.place(x=-x, y=0)
                self.topFrame.update()

            # resetting widget colors:
            self.navRoot.config(bg="sky blue")

            # turning button OFF:
            self.btnState = False
        else:
            # make root dim:
            self.navRoot.config(bg="red")

            # created animated Navbar opening:
            for x in range(-300, 0):
                self.navRoot.place(x=x, y=0)
                self.topFrame.update()

            # turing button ON:
            self.btnState = True


    # NAV BAR BUTTON
    def set_nav_bar(self):

        # top Navigation bar:
        self.topFrame = Frame(self.mainFrame, bg="orange", bd=2, height=56,width=1450)
        self.topFrame.place(x=0,y=0)

        self.navbaropenBtn = Button(self.topFrame,image=self.navIcon, bg="orange", activebackground="white", bd=4, padx=20, command=self.set_switch)
        self.navbaropenBtn.place(x=10, y=6)

        # setting Navbar frame:
        self.navRoot = Frame(self.mainFrame, bg="sky blue", height=770, width=300)
        self.navRoot.place(x=-300, y=0)
        # label  only for separating buttons and  also the bg for close button
        self.lbl_Frame = Frame(self.navRoot, bg="sky blue", height=55, width=300)
        self.lbl_Frame.place(x=0, y=0)

        self.label_for_btn = Label(self.lbl_Frame, text="Menu", font=("Poor Richard", 25), bg="sky blue", fg="red")
        self.label_for_btn.place(x=80, y=0)
        # Navbar Close Button:
        self.closeBtn = Button(self.navRoot, image=self.closeIcon, bg="black", activebackground="orange", bd=0, command=self.set_switch)
        self.closeBtn.place(x=250, y=10)



    #
    #
    # def set_nvbar_btns(self):
    #     self.bar_btn1 = Button(self.navRoot,text="Profile",font=("Poor Richard",20),activebackground="red",fg="red",padx=20)
    #     self.bar_btn1.place(x=20,y=80)
    #
    #     self.bar_btn2 = Button(self.navRoot, text="Stocks", font=("Poor Richard", 20), activebackground="red",fg="red", padx=20)
    #     self.bar_btn2.bind("<Button-1>",self.clicked)
    #     self.bar_btn2.place(x=20, y=150)
    #
    #     self.bar_btn3 = Button(self.navRoot, text="Client\nTransactions", font=("Poor Richard", 20), activebackground="red",fg="red", padx=20)
    #     self.bar_btn3.place(x=20, y=220)
    #
    #     self.bar_btn4 = Button(self.navRoot, text="Supplier\nTransactions", font=("Poor Richard", 20), activebackground="red",fg="red", padx=20)
    #     self.bar_btn4.place(x=20, y=320)
    #
    #     self.bar_btn5 = Button(self.navRoot, text="Receipt", font=("Poor Richard", 20), activebackground="red",fg="red", padx=20)
    #     # self.bar_btn5.bind("<Button-1>", self.clicked)
    #     self.bar_btn5.place(x=20, y=420)



    # To do ---------------  add button function and then call them in constructor and bind





    # adding buttons
    def nav_buttons(self,btn_name= None):
        self.button = Button(self.navRoot,text=btn_name,font=("Poor Richard", 20),activebackground="red",fg="red",padx=20)



    def clicked(self,event):
        self.clk_button = event.widget.cget("text")
        print(self.clk_button)
        if self.clk_button == "Stocks":
            self.inventory_window()

        elif self.clk_button == "Receipt":
            Receipt.set_frames(self)

        else:
            print(self.clk_button)



    # Copying function from stockcls
    def check_inventory_btn_event(self, event):
        Stockcls.check_inventory_btn_event(self, event)
    def add_product_data(self):
        Stockcls.add_product_data(self)

    def show_prod_data(self, event):
        Stockcls.show_prod_data(self, event)

    def update_inventory_data(self):
        Stockcls.update_inventory_data(self)

    def delete_inventory_data(self):
        Stockcls.delete_inventory_data(self)

    def clear_inventory_fields(self):
        Stockcls.clear_inventory_fields(self)

    # END





    # add specific functionality

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







if __name__ == '__main__':
    dash = Dashboard()
    dash.mainloop()

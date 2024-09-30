from tkinter import *
from stocks_n_products import Stockcls
from bill import Receipt


class Dashboard(Tk):
    def __init__(self):
        super().__init__()

        # setting switch state:
        self.btnState = False

        # loading Navbar icon image:
        self.navIcon = PhotoImage(file="All_images/open.png")
        self.closeIcon = PhotoImage(file="close.png")


        self.width = 1450
        self.height = 800

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        # variables
        self.prod_id = IntVar()
        self.prod_name = StringVar()
        self.prod_descrption = StringVar()
        self.prod_category = StringVar()
        self.prod_stock = IntVar()
        self.prod_add_stock = IntVar()
        self.prod_price = IntVar()


        # calling methods
        self.setgeometry()
        self.set_heading_label()
        self.Button_Frame()
        # self.set_nvbar_btns()
        self.main_dash()



        # setting buttons on NavBar
        self.nav_buttons("Profile")
        self.button.place(x=200, y=5)

        self.nav_buttons("Stocks")
        self.button.place(x=350, y=5)
        self.button.bind("<Button-1>", self.clicked)

        self.nav_buttons("Client Transactions")
        self.button.place(x=500, y=5)

        self.nav_buttons("Vendor Transactions")
        self.button.place(x=775, y=5)

        self.nav_buttons("Receipt")
        self.button.place(x=1070, y=5)
        self.button.bind("<Button-1>", self.clicked)








    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")

    def set_heading_label(self):
        self.heading_label = Label(self,text="Premium Dry Fish Emporium",font=("Times New Roman", 28, "bold"), bd=4, relief=RIDGE,
                             height=2, bg="green", fg="yellow")
        self.heading_label.pack(fill="x")


    def main_dash(self):
        self.mainFrame = Frame(self,height=710,width=1450,bg="red")
        self.mainFrame.place(x=0,y=159)



    # NAV BAR BUTTON
    def Button_Frame(self):

        # Top Button Frame
        self.topFrame = Frame(self, bg="orange", bd=2, height=65)
        self.topFrame.pack(fill=X)

        # self.navbaropenBtn = Button(self.topFrame,image=self.navIcon, bg="orange", activebackground="white", bd=4, padx=20, command=self.set_switch)
        # self.navbaropenBtn.place(x=10, y=10)
        #
        # # setting Navbar frame:
        # self.navRoot = Frame(self, bg="gray17", height=65, width=1450)
        # self.navRoot.place(x=-1450, y=95)
        # # label  only for separating buttons and  also the bg for close button
        #
        # self.lbl_Frame = Frame(self.navRoot,bg="sky blue",height=50,width=150)
        # self.lbl_Frame.place(x=0,y=5)
        #
        # self.label_for_menu = Label(self.lbl_Frame,text="Menu",font=("Poor Richard",25),bg="sky blue",fg="red")
        # self.label_for_menu.place(x=40,y=5)
        #
        # # Navbar Close Button:
        # self.closeBtn = Button(self.navRoot, image=self.closeIcon, bg="black", activebackground="orange", bd=0, command=self.set_switch)
        # self.closeBtn.place(x=1400, y=10)




    # adding  Navigation buttons
    def nav_buttons(self,btn_name= None):
        self.button = Button(self.topFrame,text=btn_name,font=("Poor Richard", 15,UNDERLINE),activebackground="orange",
                             bg ="orange",fg="black",relief="flat", borderwidth=0,padx=5,pady=5)

    def clicked(self, event):
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


if __name__ == '__main__':
    dash = Dashboard()
    dash.mainloop()

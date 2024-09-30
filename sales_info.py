from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import subprocess



class Salescls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770

        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)


        # Variables
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



        self.setgeometry()


    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")


    def set_stk_frames(self):
        self.ParentFrame = Frame(self, height=770, width=1450, bg="#DFD7BF")
        self.ParentFrame.place(x=0, y=146)



    def search_bar(self):
        self.search_Lable = Label(self.ParentFrame,text="Search Product By Name :",font=("Poor Richard", 20, "bold"),borderwidth=0,bg="#DFD7BF")
        self.search_Lable.place(x=100,y=60)

        self.search_Lable_entry = Entry(self.ParentFrame,textvariable=self.sale_Prod_search,font=("comic", 20),borderwidth=0)
        self.search_Lable_entry.place(x=400,y=60)
        self.search_Lable_entry.bind("<Key>",self.S_search)


    def sales_info_table(self):
        self.S_frame = Frame(self.ParentFrame,bd=3,bg="#DFD7BF")
        self.S_frame.place(x=50,y=100,height=480,width=1350)

        self.scollx = Scrollbar(self.S_frame,orient=HORIZONTAL)
        self.scolly = Scrollbar(self.S_frame, orient=VERTICAL)

        self.S_info_table = ttk.Treeview(self.S_frame,columns=("transaction_id", "invoice_id", "pname", "category",
                                                               "quantity", "price", "cust_name", "cust_phone",
                                                               "date", "time"),
                                         xscrollcommand=self.scollx.set,yscrollcommand=self.scolly.set,)
        self.scollx.pack(side=BOTTOM, fill="x")
        self.scolly.pack(side=RIGHT, fill="y")

        self.scollx.config(command=self.S_info_table.xview)
        self.scolly.config(command=self.S_info_table.yview)


        # giving headings
        self.S_info_table.heading("transaction_id",text="Transaction Id")
        self.S_info_table.heading("invoice_id", text="Invoice Id")
        self.S_info_table.heading("pname", text="Product Name")
        self.S_info_table.heading("category", text="Category")
        self.S_info_table.heading("quantity", text="Quantity")
        self.S_info_table.heading("price", text="Price")
        self.S_info_table.heading("cust_name", text="Customer Name")
        self.S_info_table.heading("cust_phone", text="Customer Contact")
        self.S_info_table.heading("date", text="Date")
        self.S_info_table.heading("time", text="Time")


        self.S_info_table["show"] = "headings"


        self.S_info_table.column("transaction_id",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("invoice_id",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("pname", width=150,minwidth=100,anchor=CENTER)
        self.S_info_table.column("category", width=150, minwidth=100,anchor=CENTER)
        self.S_info_table.column("quantity", width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("price",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("cust_name",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("cust_phone",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("date",width=100,minwidth=100,anchor=CENTER)
        self.S_info_table.column("time",width=100,minwidth=100,anchor=CENTER)



        self.S_info_table.pack(fill=BOTH,expand=1)



        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `transaction_id`, `invoice_id`,`pname`, `category`, `quantity`, `price`,"
                              " `cust_name`, `cust_phone`, `date`, `time` "
                              "FROM `sales_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.S_info_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            print(server_error)
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")


    def S_search(self,ev):
        try:
            self.search_query = ("SELECT * FROM sales_table where pname LIKE '%"+self.sale_Prod_search.get()+"%'")
            self.cursor.execute(self.search_query)
            self.row = self.cursor.fetchall()
            #print(self.row)
            if len(self.row) > 0:
                self.S_info_table.delete(*self.S_info_table.get_children())
                for self.idx, self.values in enumerate(self.row):
                    # print(self.values)
                    self.S_info_table.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            else:
                # print("table not found")
                self.S_info_table.delete(*self.S_info_table.get_children())

        except Exception as ex:
            tmsg.showerror(title="Connection Error", message=f"Error due to {str(ex)}")

    def chart_btn(self, btn_name, x, y):
        self.chart_btn = Button(self.ParentFrame, text=btn_name, font=("Poor Richard", 20, "bold"), bd=2, fg="white",
                                bg="#3F2305",padx=10)
        self.chart_btn.place(x=x, y=y)
        self.chart_btn.bind("<Button - 1>", self.call_chart_window)


    def call_chart_window(self,event):
        if event.widget.cget("text") == "Sales Chart":
            subprocess.call(["python", "show_sales_chart.py"])






if __name__ == '__main__':
    sale = Salescls()
    sale.mainloop()
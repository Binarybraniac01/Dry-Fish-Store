from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tmsg
import datetime
import sys


class Worker_details_cls(Tk):
    def __init__(self):
        super().__init__()

        self.title("WORKER DETAILS WINDOW")

        self.width = 1440
        self.height = 590
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        self.protocol('WM_DELETE_WINDOW', self.worker_win_close)


        self.worker_id = IntVar()
        self.worker_joining_date = StringVar()
        self.worker_name = StringVar()
        self.worker_phone_no = StringVar()
        self.worker_email = StringVar()
        self.worker_designation = StringVar()
        self.worker_address = StringVar()
        self.worker_salary = IntVar()
        self.payment_done_ = IntVar()
        self.payment_pending_ = IntVar()

        # Search Variable
        self.worker_search = StringVar()

        # Calling Methods
        self.setgeometry()
        self.set_frame()
        self.child_frame_1()
        self.child_frame_2()
        self.worker_details_ui()
        self.establish_connection()
        self.worker_dtl_search_bar()
        self.worker_table()

        self.set_btn("Add", 100, 440, 10)
        self.set_btn("Update", 250, 440, 10)
        self.set_btn("Delete", 400, 440, 10)
        # self.set_btn("Clear", 1300, 85)


    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{48}+{182}")


    def set_frame(self):
        self.worker_frame = Frame(self, bd=4, height=650, width=1450, bg="#DFD7BF")
        self.worker_frame.place(x=0, y=0)

    def child_frame_1(self):
        self.child_frame1 = Frame(self.worker_frame, height=600, width=850, bg="#DFD7BF")
        self.child_frame1.place(x=1, y=2)

    def child_frame_2(self):
        self.child_frame2 = Frame(self.worker_frame, bd=2, relief=GROOVE, bg="#DFD7BF")
        self.child_frame2.place(x=700, y=75, height=470, width=650)

    def set_btn(self, btn_name, x, y, padx=None):
        self.btn = Button(self.child_frame1, text=btn_name, font=("bookman old style", 14, "bold"),
                          compound=TOP, relief=RAISED, padx=padx,bg="#3F2305", fg="white")
        self.btn.place(x=x, y=y)
        self.btn.bind("<Button - 1>", self.check_worker_btn_event)

    def worker_details_ui(self):
        self.name_label = Label(self.child_frame1, text="Worker Name :",
                                font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.name_label.place(x=100, y=80)
        self.phone_label = Label(self.child_frame1, text="Phone No. :",
                                font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.phone_label.place(x=100, y=140)
        self.email_label = Label(self.child_frame1, text="Gmail :",
                               font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.email_label.place(x=100, y=200)
        self.designation_label = Label(self.child_frame1, text="Designation :",
                                 font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.designation_label.place(x=100, y=260)
        self.address_label = Label(self.child_frame1, text="Address :",
                                      font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.address_label.place(x=100, y=320)
        self.salary_label = Label(self.child_frame1, text="Salary :",
                                     font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.salary_label.place(x=100, y=380)

        self.name_entry = Entry(self.child_frame1, textvariable=self.worker_name,
                                font=("comic", 20))
        self.name_entry.place(x=300, y=80, height=30)
        self.phone_entry = Entry(self.child_frame1, textvariable=self.worker_phone_no,
                                font=("comic", 20))
        self.phone_entry.place(x=300, y=140, height=30)
        self.email_entry = Entry(self.child_frame1, textvariable=self.worker_email,
                                font=("comic", 20))
        self.email_entry.place(x=300, y=200, height=30)
        self.desig_entry = Entry(self.child_frame1, textvariable=self.worker_designation,
                                font=("comic", 20))
        self.desig_entry.place(x=300, y=260, height=30)
        self.address_entry = Entry(self.child_frame1, textvariable=self.worker_address,
                                font=("comic", 20))
        self.address_entry.place(x=300, y=320, height=30)
        self.salary_entry = Entry(self.child_frame1, textvariable=self.worker_salary,
                                font=("comic", 20))
        self.salary_entry.place(x=300, y=380, height=30)


    def worker_table(self):
        self.scrollbarx = Scrollbar(self.child_frame2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.child_frame2, orient=VERTICAL)


        self.worker_tree = ttk.Treeview(self.child_frame2,
                                        selectmode="browse",
                                        yscrollcommand=self.scrollbary.set,
                                        xscrollcommand=self.scrollbarx.set)

        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbary.config(command=self.worker_tree.yview)
        # self.scrollbarx.grid(row=2, column=0, sticky="we")
        self.scrollbarx.config(command=self.worker_tree.xview)
        # self.scrollbary.grid(row=1, column=1, sticky="ns")


        # Defining table columns
        self.worker_tree["columns"] = ("id", "name", "phone", "email", "designation", "address", "salary", "date")

        # Formatting table columns
        # Phantom column ( Default column )
        self.worker_tree.column("#0", width=0, minwidth=0, stretch=NO)
        self.worker_tree.column("id", width=50, minwidth=50, anchor=CENTER)
        self.worker_tree.column("name", width=120, minwidth=120, anchor=CENTER)
        self.worker_tree.column("phone", width=120, minwidth=120, anchor=CENTER)
        self.worker_tree.column("email", width=150, minwidth=150, anchor=CENTER)
        self.worker_tree.column("designation", width=120, minwidth=120, anchor=CENTER)
        self.worker_tree.column("address", width=100, minwidth=100, anchor=CENTER)
        self.worker_tree.column("salary", width=80, minwidth=80, anchor=CENTER)
        self.worker_tree.column("date", width=90, minwidth=90, anchor=CENTER)

        # Create headings
        # self.worker_tree.heading("#0", text="", anchor=W)
        self.worker_tree.heading("id", text="ID", anchor=CENTER)
        self.worker_tree.heading("name", text="Worker Name", anchor=CENTER)
        self.worker_tree.heading("phone", text="Phone No", anchor=CENTER)
        self.worker_tree.heading("email", text="Email", anchor=CENTER)
        self.worker_tree.heading("designation", text="Designation", anchor=CENTER)
        self.worker_tree.heading("address", text="Address", anchor=CENTER)
        self.worker_tree.heading("salary", text="Salary", anchor=CENTER)
        self.worker_tree.heading("date", text="Joinin Date", anchor=CENTER)

        # self.worker_tree.grid(row=1, column=0, sticky="e")
        # self.worker_tree.place(width=(1198 // 2) + 134)
        self.worker_tree.pack(fill=BOTH, expand=1)

        # self.scrollbary.config(command=self.worker_tree.yview)
        # self.scrollbarx.grid(row=2, column=0, sticky="we")
        # self.scrollbarx.config(command=self.worker_tree.xview)
        # self.scrollbary.grid(row=1, column=1, sticky="ns")

        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `id`, `name`, `phone`, `email`, `designation`, `address`, `salary`, "
                              "`joining_date` FROM `worker_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.worker_tree.bind("<<TreeviewSelect>>", self.show_worker_data)

    def show_worker_data(self, event):
        self.curr_position = self.worker_tree.selection()
        self.curr_position = self.worker_tree.item(self.curr_position)
        # print(self.curr_position["values"][0])
        self.len_curr_position = len(self.curr_position["values"])
        # print(self.len_curr_position)
        if self.len_curr_position == 8:
            self.worker_id.set(int(self.curr_position["values"][0]))  # Worker id
            self.worker_name.set(self.curr_position["values"][1])  # Worker name
            self.worker_phone_no.set(self.curr_position["values"][2])  # Worker Phone
            self.worker_email.set(self.curr_position["values"][3])  # Worker Email
            self.worker_designation.set(self.curr_position["values"][4])  # Worker Designation
            self.worker_address.set(self.curr_position["values"][5])  # Worker Address
            self.worker_salary.set(int(self.curr_position["values"][6]))  # Worker Salary

    def add_worker_data(self):
        if (self.worker_name.get() == "" or self.worker_phone_no.get() == "" or
                self.worker_email.get() == "" or self.worker_designation.get() == ""
                or self.worker_address.get() == "" or self.worker_salary.get() == 0):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:
            search_query = ("select * from `worker_table` where `email` = %s and `phone` = %s")
            vals = (self.worker_email.get(), self.worker_phone_no.get())
            self.cursor.execute(search_query, vals)
            result = self.cursor.fetchall()
            # print(result)
            if result:
                print(f"{self.worker_name.get()} is already exist.")
                tmsg.showwarning("Warning", f"{self.worker_name.get()} is already available.")
            else:
                joining_date = str(datetime.datetime.now().strftime("%y-%m-%d"))
                self.worker_joining_date.set(joining_date)
                salary = self.worker_salary.get()
                self.payment_pending_.set(salary)
                self.payment_done_.set(0)

                self.insert_query = (
                    "INSERT INTO `worker_table`(`name`, `phone`, `email`, `designation`, `address`, `salary`, "
                    "`joining_date`, `payment_done`, `payment_pending`) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                self.vals = (self.worker_name.get(), self.worker_phone_no.get(), self.worker_email.get(),
                             self.worker_designation.get(), self.worker_address.get(), self.worker_salary.get(),
                             self.worker_joining_date.get(), self.payment_done_.get(), self.payment_pending_.get())
                self.cursor.execute(self.insert_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Worker Added Successfully")
            self.worker_name.set("")
            self.worker_phone_no.set("")
            self.worker_email.set("")
            self.worker_designation.set("")
            self.worker_address.set("")
            self.worker_salary.set(0)
            self.worker_tree.delete(*self.worker_tree.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `id`, `name`, `phone`, `email`, `designation`, `address`, `salary`, "
                                  "`joining_date` FROM `worker_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def update_worker_data(self):
        if (self.worker_name.get() == "" or self.worker_phone_no.get() == "" or
                self.worker_email.get() == "" or self.worker_designation.get() == ""
                or self.worker_address.get() == "" or self.worker_salary.get() == 0):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:

            # Update Salary Logic for worker_details to reflect corresponding results in worker_payment
            salary = int(self.worker_salary.get())
            # Checking if provided salary is already available with requested worker id / worker name
            search_salary = ("select `payment_done` from `worker_table` "
                             "where `id` = %s and `salary` = %s")
            vals = (self.worker_id.get(), salary)
            self.cursor.execute(search_salary, vals)
            result = self.cursor.fetchall()

            # Checking if result variable contains any values
            if result:
                #  if results contains values
                #  as condition evaluates true worker_data will update normally
                self.update_query = ("UPDATE `worker_table` SET `name` = %s, `phone` = %s, `email` = %s, "
                                     "`designation` = %s, `address` = %s, `salary` = %s WHERE `id` = %s")
                self.vals = (self.worker_name.get(), self.worker_phone_no.get(), self.worker_email.get(),
                             self.worker_designation.get(), self.worker_address.get(), self.worker_salary.get(),
                             self.worker_id.get())
                self.cursor.execute(self.update_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Worker Updated Successfully")
            else:
                # if result contains no values
                # if the salary doesn't match with existing salary then the exiting salary will get updated with new one
                # along with other necessary changes .
                fetch_paid_amount = ("select `payment_done` from `worker_table` where `id` = %s")
                vals = (self.worker_id.get(),)
                self.cursor.execute(fetch_paid_amount, vals)
                result = self.cursor.fetchall()
                amount_paid = result[0][0]
                payment_pending = int(salary) - int(amount_paid)
                print(payment_pending)

                self.update_query = ("UPDATE `worker_table` SET `name` = %s, `phone` = %s, `email` = %s, "
                                     "`designation` = %s, `address` = %s, `salary` = %s, `payment_pending` = %s "
                                     "WHERE `id` = %s")
                self.vals = (self.worker_name.get(), self.worker_phone_no.get(), self.worker_email.get(),
                             self.worker_designation.get(), self.worker_address.get(), self.worker_salary.get(),
                             payment_pending, self.worker_id.get())
                self.cursor.execute(self.update_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Worker Updated Successfully")
            self.worker_name.set("")
            self.worker_phone_no.set("")
            self.worker_email.set("")
            self.worker_designation.set("")
            self.worker_address.set("")
            self.worker_salary.set(0)
            self.worker_tree.delete(*self.worker_tree.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `id`, `name`, `phone`, `email`, `designation`, `address`, `salary`, "
                                  "`joining_date` FROM `worker_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def delete_worker_data(self):
        if (self.worker_name.get() == "" or self.worker_phone_no.get() == "" or
                self.worker_email.get() == "" or self.worker_designation.get() == ""
                or self.worker_address.get() == "" or self.worker_salary.get() == 0):
            tmsg.showwarning(title="Validation", message="Click on the stock item to select the item"
                                                         "\nand then click on delete button.")
        else:
            answer = tmsg.askyesno("Confirmation", "Are you sure want to delete the worker ?")
            if answer:
                self.delete_query = ("DELETE FROM `worker_table` WHERE `id` = %s")
                print(self.worker_id.get())
                self.vals = (self.worker_id.get(),)
                self.cursor.execute(self.delete_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Worker deleted successfully.")
            else:
                tmsg.showinfo("Success", "Worker not deleted")

            self.worker_name.set("")
            self.worker_phone_no.set("")
            self.worker_email.set("")
            self.worker_designation.set("")
            self.worker_address.set("")
            self.worker_salary.set(0)
            self.worker_tree.delete(*self.worker_tree.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `id`, `name`, `phone`, `email`, `designation`, `address`, `salary`, "
                                  "`joining_date` FROM `worker_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def worker_dtl_search_bar(self):
        self.search_label = Label(self.worker_frame, text="Search Worker Name : ", bg="#DFD7BF", font=("Poor Richard", 20, "bold"),
                                  borderwidth=0)
        self.search_label.place(x=700, y=30)
        self.search_Entry = Entry(self.worker_frame, textvariable=self.worker_search, font=("comic", 20),
                                  borderwidth=0)
        self.search_Entry.place(x=950, y=30)
        self.search_Entry.bind("<Key>", self.search_worker_dtl)

    def search_worker_dtl(self, event):
        try:
            self.search_query = ("SELECT `id`, `name`, `phone`, `email`, `designation`, `address`, `salary`, "
                                 "`joining_date` FROM `worker_table` where `name` LIKE "
                                 "'%"+self.worker_search.get()+"%'")
            self.cursor.execute(self.search_query)
            self.row = self.cursor.fetchall()
            #print(self.row)
            if len(self.row) > 0:
                self.worker_tree.delete(*self.worker_tree.get_children())
                for i in self.row:
                    self.worker_tree.insert('', END, values=i)
            else:
                # print("table not found")
                self.worker_tree.delete(*self.worker_tree.get_children())

        except Exception as ex:
            tmsg.showerror(title="Connection Error", message=f"Error due to {str(ex)}")


    def check_worker_btn_event(self, event):
        if event.widget.cget("text") == "Add":
            self.add_worker_data()
        elif event.widget.cget("text") == "Update":
            self.update_worker_data()
        elif event.widget.cget("text") == "Delete":
            self.delete_worker_data()


    def worker_win_close(self):
        self.destroy()
        sys.exit()


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
    worker = Worker_details_cls()
    worker.mainloop()
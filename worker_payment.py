from tkinter import *
from tkinter import ttk
import subprocess
import tkinter.messagebox as tmsg


class WorkerPaymentCls(Tk):
    def __init__(self):
        super().__init__()

        self.width = 1450
        self.height = 770
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        self.pay_worker_id = IntVar()
        self.pay_worker_joining_date = StringVar()
        self.pay_worker_name = StringVar()
        self.pay_worker_designation = StringVar()
        self.pay_worker_salary = IntVar()
        self.payment_done = IntVar()
        self.payment_pending = IntVar()
        self.add_payment = IntVar()

        # Search Variable
        self.worker_pay_search = StringVar()


    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{43}+{5}")


    def set_frame(self):
        self.worker_frame = Frame(self, bd=4, height=650, width=1450, bg="#DFD7BF")
        self.worker_frame.place(x=0, y=146)

    def child_frame_1(self):
        self.child_frame1 = Frame(self.worker_frame, height=600, width=850, bg="#DFD7BF")
        self.child_frame1.place(x=1, y=2)

    def child_frame_2(self):
        self.child_frame2 = Frame(self.worker_frame, bd=2, relief=GROOVE, bg="#DFD7BF")
        self.child_frame2.place(x=700, y=110, height=470, width=650)

    def set_btn(self, btn_name, x, y, padx=10, btntype=None):
        if btntype == None:
            self.btn = Button(self.child_frame1, text=btn_name, font=("bookman old style", 14, "bold"),
                              compound=TOP, relief=RAISED, padx=padx,bg="#3F2305", fg="white")
            self.btn.place(x=x, y=y)
            self.btn.bind("<Button - 1>", self.check_worker_payment_btn_event_)

        else :
            self.btn = Button(self.worker_frame, text=btn_name, font=("bookman old style", 14, "bold"),
                              compound=TOP, relief=RAISED, padx=padx,bg="#3F2305", fg="white")
            self.btn.place(x=x, y=y)
            self.btn.bind("<Button - 1>", self.go_to_details)





    def worker_payment_ui(self):
        self.name_label = Label(self.child_frame1, text="Worker Name :", font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.name_label.place(x=100, y=120)
        self.designation_label = Label(self.child_frame1, text="Designation :", font=("Poor Richard", 20, "bold"), bg="#DFD7BF")
        self.designation_label.place(x=100, y=180)
        self.salary_label = Label(self.child_frame1, text="Salary :", font=("Poor Richard", 20, "bold"),
                                       bg="#DFD7BF")
        self.salary_label.place(x=100, y=240)
        self.payment_done_label = Label(self.child_frame1, text="Payment Done :", font=("Poor Richard", 20, "bold"),
                                        bg="#DFD7BF")
        self.payment_done_label.place(x=100, y=300)
        self.payment_pending_label = Label(self.child_frame1, text="Payment Pending :", font=("Poor Richard", 20, "bold"),
                                        bg="#DFD7BF")
        self.payment_pending_label.place(x=100, y=360)
        self.add_payment_label = Label(self.child_frame1, text="Add Payment :", font=("Poor Richard", 20, "bold"),
                                           bg="#DFD7BF")
        self.add_payment_label.place(x=100, y=420)


        self.name_entry = Entry(self.child_frame1, textvariable=self.pay_worker_name,
                                font=("comic", 20),width=15)
        self.name_entry.place(x=320, y=120, height=30)
        self.designation_entry = Entry(self.child_frame1, textvariable=self.pay_worker_designation,
                                 font=("comic", 20),width=15)
        self.designation_entry.place(x=320, y=180, height=30)
        self.salary_entry = Entry(self.child_frame1, textvariable=self.pay_worker_salary,
                                 font=("comic", 20),width=15)
        self.salary_entry.place(x=320, y=240, height=30)
        self.payment_done_entry = Entry(self.child_frame1, textvariable=self.payment_done,
                                 font=("comic", 20),width=15)
        self.payment_done_entry.place(x=320, y=300, height=30)
        self.payment_pending_entry = Entry(self.child_frame1, textvariable=self.payment_pending,
                                   font=("comic", 20),width=15)
        self.payment_pending_entry.place(x=320, y=360, height=30)
        self.add_payment_entry = Entry(self.child_frame1, textvariable=self.add_payment,
                                  font=("comic", 20),width=15)
        self.add_payment_entry.place(x=320, y=420, height=30)



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
        self.scrollbarx.config(command=self.worker_tree.xview)



        # Defining table columns
        self.worker_tree["columns"] = ("id", "name", "designation", "salary", "payment_done", "payment_pending", "date")

        # Formatting table columns
        # Phantom column ( Default column )
        self.worker_tree.column("#0", width=0, minwidth=0, stretch=NO)
        self.worker_tree.column("id", width=50, minwidth=50, anchor=CENTER)
        self.worker_tree.column("name", width=110, minwidth=110, anchor=CENTER)
        self.worker_tree.column("designation", width=120, minwidth=120, anchor=CENTER)
        self.worker_tree.column("salary", width=120, minwidth=120, anchor=CENTER)
        self.worker_tree.column("payment_done", width=150, minwidth=150, anchor=CENTER)
        self.worker_tree.column("payment_pending", width=150, minwidth=150, anchor=CENTER)
        self.worker_tree.column("date", width=80, minwidth=80, anchor=CENTER)
        # self.worker_tree.column("date", width=80, minwidth=80, anchor=CENTER)

        # Create headings
        # self.worker_tree.heading("#0", text="", anchor=W)
        self.worker_tree.heading("id", text="ID", anchor=CENTER)
        self.worker_tree.heading("name", text="Worker Name", anchor=CENTER)
        self.worker_tree.heading("designation", text="Designation", anchor=CENTER)
        self.worker_tree.heading("salary", text="Salary", anchor=CENTER)
        self.worker_tree.heading("payment_done", text="Payment Done", anchor=CENTER)
        self.worker_tree.heading("payment_pending", text="Payment Pending", anchor=CENTER)
        self.worker_tree.heading("date", text="Joining Date", anchor=CENTER)
        # self.worker_tree.heading("date", text="Joinin Date", anchor=CENTER)

        # self.worker_tree.grid(row=1, column=0, sticky="e")
        # self.worker_tree.place(width=(1198 // 2) + 134)
        self.worker_tree.pack(fill=BOTH, expand=1)

        # self.scrollbary.config(command=self.worker_tree.yview)
        # self.scrollbarx.grid(row=2, column=0, sticky="we")
        # self.scrollbarx.config(command=self.worker_tree.xview)
        # self.scrollbary.grid(row=1, column=1, sticky="ns")

        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `id`, `name`, `designation`, `salary`, `payment_done`, "
                              "`payment_pending`, `joining_date` FROM `worker_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")
        self.worker_tree.bind("<<TreeviewSelect>>", self.show_worker_payment_data)

    def show_worker_payment_data(self, event):
        self.curr_position = self.worker_tree.selection()
        self.curr_position = self.worker_tree.item(self.curr_position)
        # print(self.curr_position["values"][0])
        self.len_curr_position = len(self.curr_position["values"])
        # print(self.len_curr_position)
        if self.len_curr_position == 7:
            self.pay_worker_id.set(int(self.curr_position["values"][0]))  # Worker id
            self.pay_worker_name.set(self.curr_position["values"][1])  # Worker name
            self.pay_worker_designation.set(self.curr_position["values"][2])  # Worker Designation
            self.pay_worker_salary.set(int(self.curr_position["values"][3]))  # Worker Salary
            self.payment_done.set(int(self.curr_position["values"][4]))  # Worker Payment done
            self.payment_pending.set(int(self.curr_position["values"][5]))  # Worker Payment Pending
            self.add_payment.set(int(0))  # Worker Add Payment

    def update_worker_payment_data(self):
        if (self.pay_worker_name.get() == "" or self.pay_worker_designation.get() == ""):
            tmsg.showwarning(title="Validation", message="All fields must be filled")
        else:
            # Payment Logic
            if int(self.pay_worker_salary.get()) < int(self.add_payment.get()):
                print(f"{int(self.add_payment.get())} is More than the Agreed.")
                tmsg.showwarning("Warning", f"Payment issued of Rs.{self.add_payment.get()} is more than "
                                            f"agreed Salary Rs.{self.pay_worker_salary.get()}.")
            # elif int(self.)
            elif int(self.add_payment.get()) > int(self.payment_pending.get()):
                tmsg.showwarning("Warning", f"Rs.{self.add_payment.get()} is More than the pending "
                                            f"amount of Rs.{self.payment_pending.get()}")
            else:
                salary_paid = int(self.payment_done.get()) + int(self.add_payment.get())
                self.payment_done.set(salary_paid)
                remaining_salary = int(self.pay_worker_salary.get()) - salary_paid
                self.payment_pending.set(remaining_salary)

                self.update_query = ("UPDATE `worker_table` SET `name` = %s, `designation` = %s, `salary` = %s, "
                                     "`payment_done` = %s, `payment_pending` = %s WHERE `id` = %s")
                self.vals = (self.pay_worker_name.get(), self.pay_worker_designation.get(), self.pay_worker_salary.get(),
                             self.payment_done.get(), self.payment_pending.get(), self.pay_worker_id.get())
                self.cursor.execute(self.update_query, self.vals)
                self.connection.commit()
                tmsg.showinfo("Success", "Worker Updated Successfully")
            self.pay_worker_name.set("")
            self.pay_worker_designation.set("")
            self.pay_worker_salary.set(0)
            self.payment_done.set(0)
            self.payment_pending.set(0)
            self.add_payment.set(0)
            self.worker_tree.delete(*self.worker_tree.get_children())
            # Todo Complete : Added connectivity to show the data to the treeview
            try:
                self.sql_query = ("SELECT `id`, `name`, `designation`, `salary`, `payment_done`, "
                                  "`payment_pending`, `joining_date` FROM `worker_table`")
                self.cursor.execute(self.sql_query)
                self.results = self.cursor.fetchall()
                # print(self.results)
                for self.idx, self.values in enumerate(self.results):
                    # print(self.values)
                    self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
            except Exception as server_error:
                tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def clear_fields(self):
        self.pay_worker_name.set("")
        self.pay_worker_designation.set("")
        self.pay_worker_salary.set(0)
        self.payment_done.set(0)
        self.payment_pending.set(0)
        self.add_payment.set(0)
        self.worker_pay_search.set("")

        self.worker_tree.delete(*self.worker_tree.get_children())
        # Todo Complete : Added connectivity to show the data to the treeview
        try:
            self.sql_query = ("SELECT `id`, `name`, `designation`, `salary`, `payment_done`, "
                              "`payment_pending`, `joining_date` FROM `worker_table`")
            self.cursor.execute(self.sql_query)
            self.results = self.cursor.fetchall()
            # print(self.results)
            for self.idx, self.values in enumerate(self.results):
                # print(self.values)
                self.worker_tree.insert(parent="", index="end", iid=self.idx, text="Parent", values=self.values)
        except Exception as server_error:
            tmsg.showerror(title="Connection Error", message="Unable to connect the MySql server")

    def worker_pay_search_bar(self):
        self.search_label = Label(self.worker_frame, text="Search Worker Name : ", bg="#DFD7BF", font=("Poor Richard", 20, "bold"),
                                  borderwidth=0)
        self.search_label.place(x=700, y=70)
        self.search_Entry = Entry(self.worker_frame, textvariable=self.worker_pay_search, font=("comic", 20),
                                  borderwidth=0, width=20)
        self.search_Entry.place(x=950, y=70)
        self.search_Entry.bind("<Key>", self.search_worker_pay)

    def search_worker_pay(self, event):
        try:
            self.search_query = ("SELECT `id`, `name`, `designation`, `salary`, `payment_done`, "
                                 "`payment_pending`, `joining_date` FROM `worker_table` where `name` LIKE "
                                 "'%"+self.worker_pay_search.get()+"%'")
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

    def check_worker_payment_btn_event_(self, event):
        if event.widget.cget("text") == "Update":
            self.update_worker_payment_data()
        elif event.widget.cget("text") == "Clear":
            self.clear_fields()



    def go_to_details(self,event):
        if event.widget.cget("text") == "Worker Details":
            subprocess.call(["python", "worker_info.py"])
        # pass



if __name__ == '__main__':
    worker = WorkerPaymentCls()
    worker.mainloop()
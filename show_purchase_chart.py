from tkinter import *
import mysql.connector
import tkinter.messagebox as tmsg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import sys


class PurchaseChartCls(Tk):
    def __init__(self):
        super().__init__()

        self.title("Purchase Chart")
        # self.state('zoomed')

        self.width = 1440
        self.height = 650
        self.resizable(FALSE, FALSE)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        self.protocol('WM_DELETE_WINDOW', self.chart_close)






        # Create an empty dictionary to store the product quantity data for each month
        self.product_quantity_by_month = {}



        # calling Methods
        self.setgeometry()
        self.set_chart_frame()
        self.establish_connection()
        self.getting_graph_data()
        self.show_chart()




    def setgeometry(self):
        self.geometry(f"{self.width}x{self.height}+{208}+{262}")


    def set_chart_frame(self):
        self.chart_frame = Frame(self, bg="#DFD7BF")
        self.chart_frame.place(x=0, y=0, height=650, width=1440)

    def getting_graph_data(self):
        '''Execute the SQL query to get the product quantity data for each month'''

        self.sql_qury = ("SELECT MONTH(date), SUM(quantity) AS quantity FROM"
                         " vendor_table GROUP BY MONTH(date)")
        self.cursor.execute(self.sql_qury)

        # Fetch all the results from the cursor
        results = self.cursor.fetchall()
        # self.connection.commit()

        # Map month numbers to their corresponding month names
        month_names = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
        }

        # Iterate through the results and add the product quantity data to the dictionary
        for row in results:
            month_number = row[0]
            month_name = month_names[month_number]
            product_quantity = int(row[1])

            self.product_quantity_by_month[month_name] = product_quantity

        # Print the dictionary
        # print(self.product_quantity_by_month)



    def show_chart(self):
        plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

        # Chart 1 : Line chart
        fig1, ax1 =plt.subplots()
        # ax1.fill_between(self.product_quantity_by_month.keys(), self.product_quantity_by_month.values())
        ax1.bar(self.product_quantity_by_month.keys(), self.product_quantity_by_month.values())
        # ax1.plot(list(self.product_quantity_by_month.keys()),list(self.product_quantity_by_month.values()))
        ax1.set_title("Purchase by Month")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Purchased Stocks in Kg")
        # plt.show()

        canvas1 = FigureCanvasTkAgg(fig1,self.chart_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill="both", expand=True)

        toolbar = NavigationToolbar2Tk(canvas1, self.chart_frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(anchor="w", fill=X)




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


    def chart_close(self):
        plt.close('all')  # Close all Matplotlib figures  # Most important
        self.destroy()
        print("destroy")
        sys.exit()







if __name__ == '__main__':
    purchase = PurchaseChartCls()
    purchase.mainloop()



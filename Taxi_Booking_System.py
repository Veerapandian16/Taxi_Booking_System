from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3

# Create database and users table at program startup
with sqlite3.connect('Users.db') as db:
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL, password TEXT NOT NULL)')
    db.commit()

class User:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()
            find_user = 'SELECT * FROM user WHERE username = ? AND password = ?'
            c.execute(find_user, (self.username.get(), self.password.get()))
            result = c.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] = "Welcome, " + self.username.get()
                self.head.configure(fg="green")
                self.head.pack(fill=X)
                application = Travel(self.master)
            else:
                ms.showerror('Oops!', 'Username or Password Not Found.')

    def new_user(self):
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()
            find_user = 'SELECT * FROM user WHERE username = ?'
            c.execute(find_user, (self.n_username.get(),))
            if c.fetchall():
                ms.showerror('Error!', 'Username Already Taken!')
            else:
                insert = 'INSERT INTO user(username, password) VALUES(?, ?)'
                c.execute(insert, (self.n_username.get(), self.n_password.get()))
                db.commit()
                ms.showinfo('Success!', 'Account Created!')
                self.log()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()
        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)

class Travel:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System In LPU")
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+0+0")
        self.root.configure(background='black')

        self.DateofOrder = StringVar()
        self.DateofOrder.set(time.strftime("%d/%m/%Y"))
        self.Receipt_Ref = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.journeyType = IntVar()
        self.carType = IntVar()
        self.varl1 = StringVar()
        self.varl2 = StringVar()
        self.varl3 = StringVar()
        self.reset_counter = 0
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.Postcode = StringVar()
        self.Mobile = StringVar()
        self.Telephone = StringVar()
        self.Email = StringVar()
        self.TaxiTax = StringVar()
        self.Km = StringVar()
        self.Travel_Ins = StringVar()
        self.Luggage = StringVar()
        self.Receipt = StringVar()
        self.Standard = StringVar()
        self.PrimeSedan = StringVar()
        self.PremiumSedan = StringVar()
        self.TaxiTax.set("0")
        self.Km.set("0")
        self.Travel_Ins.set("0")
        self.Luggage.set("0")
        self.Standard.set("0")
        self.PrimeSedan.set("0")
        self.PremiumSedan.set("0")
        self.Item1 = 0
        self.Item3 = 0
        self.Item4 = 0
        self.Item5 = 0

        self.widgets()

    def iExit(self):
        iExit = ms.askyesno("Prompt!", "Do you want to exit?")
        if iExit:
            self.root.destroy()

    def Reset(self):
        self.TaxiTax.set("0")
        self.Km.set("0")
        self.Travel_Ins.set("0")
        self.Luggage.set("0")
        self.Standard.set("0")
        self.PrimeSedan.set("0")
        self.PremiumSedan.set("0")
        self.Firstname.set("")
        self.Surname.set("")
        self.Address.set("")
        self.Postcode.set("")
        self.Mobile.set("")
        self.Telephone.set("")
        self.Email.set("")
        self.PaidTax.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.txtReceipt1.delete("1.0", END)
        self.txtReceipt2.delete("1.0", END)
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.journeyType.set(0)
        self.carType.set(0)
        self.varl1.set("")
        self.varl2.set("")
        self.varl3.set("")
        self.cboPickup.current(0)
        self.cboDrop.current(0)
        self.cboPooling.current(0)
        self.txtTaxiTax.configure(state=DISABLED)
        self.txtKm.configure(state=DISABLED)
        self.txtTravel_Ins.configure(state=DISABLED)
        self.txtLuggage.configure(state=DISABLED)
        self.txtStandard.configure(state=DISABLED)
        self.txtPrimeSedan.configure(state=DISABLED)
        self.txtPremiumSedan.configure(state=DISABLED)
        self(reset_counter=1)

    def Receiptt(self):
        if self.reset_counter == 0 and all([self.Firstname.get(), self.Surname.get(), self.Address.get(), 
                                            self.Postcode.get(), self.Mobile.get(), self.Telephone.get(), self.Email.get()]):
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)
            x = random.randint(10853, 500831)
            randomRef = str(x)
            self.Receipt_Ref.set(randomRef)
            self.txtReceipt1.insert(END, "Receipt Ref:\n")
            self.txtReceipt2.insert(END, self.Receipt_Ref.get() + "\n")
            self.txtReceipt1.insert(END, 'Date:\n')
            self.txtReceipt2.insert(END, self.DateofOrder.get() + "\n")
            self.txtReceipt1.insert(END, 'Taxi No:\n')
            self.txtReceipt2.insert(END, 'TR ' + self.Receipt_Ref.get() + " BW\n")
            self.txtReceipt1.insert(END, 'Firstname:\n')
            self.txtReceipt2.insert(END, self.Firstname.get() + "\n")
            self.txtReceipt1.insert(END, 'Surname:\n')
            self.txtReceipt2.insert(END, self.Surname.get() + "\n")
            self.txtReceipt1.insert(END, 'Address:\n')
            self.txtReceipt2.insert(END, self.Address.get() + "\n")
            self.txtReceipt1.insert(END, 'Postal Code:\n')
            self.txtReceipt2.insert(END, self.Postcode.get() + "\n")
            self.txtReceipt1.insert(END, 'Telephone:\n')
            self.txtReceipt2.insert(END, self.Telephone.get() + "\n")
            self.txtReceipt1.insert(END, 'Mobile:\n')
            self.txtReceipt2.insert(END, self.Mobile.get() + "\n")
            self.txtReceipt1.insert(END, 'Email:\n')
            self.txtReceipt2.insert(END, self.Email.get() + "\n")
            self.txtReceipt1.insert(END, 'From:\n')
            self.txtReceipt2.insert(END, self.varl1.get() + "\n")
            self.txtReceipt1.insert(END, 'To:\n')
            self.txtReceipt2.insert(END, self.varl2.get() + "\n")
            self.txtReceipt1.insert(END, 'Pooling:\n')
            self.txtReceipt2.insert(END, self.varl3.get() + "\n")
            self.txtReceipt1.insert(END, 'Standard:\n')
            self.txtReceipt2.insert(END, self.Standard.get() + "\n")
            self.txtReceipt1.insert(END, 'Prime Sedan:\n')
            self.txtReceipt2.insert(END, self.PrimeSedan.get() + "\n")
            self.txtReceipt1.insert(END, 'Premium Sedan:\n')
            self.txtReceipt2.insert(END, self.PremiumSedan.get() + "\n")
            self.txtReceipt1.insert(END, 'Paid:\n')
            self.txtReceipt2.insert(END, self.PaidTax.get() + "\n")
            self.txtReceipt1.insert(END, 'SubTotal:\n')
            self.txtReceipt2.insert(END, str(self.SubTotal.get()) + "\n")
            self.txtReceipt1.insert(END, 'Total Cost:\n')
            self.txtReceipt2.insert(END, str(self.TotalCost.get()))
        else:
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)
            self.txtReceipt1.insert(END, "\nNo Input")

    def Taxi_Tax(self):
        if self.var1.get() == 1:
            self.txtTaxiTax.configure(state=NORMAL)
            self.Item1 = float(50)
            self.TaxiTax.set("Rs " + str(self.Item1))
        else:
            self.txtTaxiTax.configure(state=DISABLED)
            self.TaxiTax.set("0")
            self.Item1 = 0

    def Kilo(self):
        if self.var2.get() == 0:
            self.txtKm.configure(state=DISABLED)
            self.Km.set("0")
        elif self.var2.get() == 1 and self.varl1.get() != "" and self.varl2.get() != "":
            self.txtKm.configure(state=NORMAL)
            distance_map = {
                "CampusCafe": {"BoysHostel": 10, "GirlsHostel": 8, "AdmissionBlock": 6, "CampusCafe": 0},
                "BoysHostel": {"BoysHostel": 0, "GirlsHostel": 2, "AdmissionBlock": 5, "CampusCafe": 10},
                "GirlsHostel": {"BoysHostel": 2, "GirlsHostel": 0, "AdmissionBlock": 3, "CampusCafe": 8},
                "AdmissionBlock": {"BoysHostel": 5, "GirlsHostel": 3, "AdmissionBlock": 0, "CampusCafe": 6}
            }
            self.Km.set(distance_map[self.varl1.get()][self.varl2.get()])

    def Travelling(self):
        if self.var3.get() == 1:
            self.txtTravel_Ins.configure(state=NORMAL)
            self.Item3 = float(10)
            self.Travel_Ins.set("Rs " + str(self.Item3))
        else:
            self.txtTravel_Ins.configure(state=DISABLED)
            self.Travel_Ins.set("0")
            self.Item3 = 0

    def Lug(self):
        if self.var4.get() == 1:
            self.txtLuggage.configure(state=NORMAL)
            self.Item4 = float(30)
            self.Luggage.set("Rs " + str(self.Item4))
        else:
            self.txtLuggage.configure(state=DISABLED)
            self.Luggage.set("0")
            self.Item4 = 0

    def selectCar(self):
        if self.carType.get() == 1:
            self.txtPrimeSedan.configure(state=DISABLED)
            self.PrimeSedan.set("0")
            self.txtPremiumSedan.configure(state=DISABLED)
            self.PremiumSedan.set("0")
            self.txtStandard.configure(state=NORMAL)
            self.Item5 = float(8)
            self.Standard.set("Rs " + str(self.Item5))
        elif self.carType.get() == 2:
            self.txtStandard.configure(state=DISABLED)
            self.Standard.set("0")
            self.txtPremiumSedan.configure(state=DISABLED)
            self.PremiumSedan.set("0")
            self.txtPrimeSedan.configure(state=NORMAL)
            self.Item5 = float(10)
            self.PrimeSedan.set("Rs " + str(self.Item5))
        else:
            self.txtStandard.configure(state=DISABLED)
            self.Standard.set("0")
            self.txtPrimeSedan.configure(state=DISABLED)
            self.PrimeSedan.set("0")
            self.txtPremiumSedan.configure(state=NORMAL)
            self.Item5 = float(15)
            self.PremiumSedan.set("Rs " + str(self.Item5))

    def Total_Paid(self):
        if (self.var1.get() == 1 and self.var2.get() == 1 and self.carType.get() != 0 and 
            self.journeyType.get() != 0 and self.varl1.get() != "" and self.varl2.get() != ""):
            Item2 = float(self.Km.get())
            if self.journeyType.get() == 1:
                Cost_of_fare = self.Item1 + (Item2 * self.Item5) + self.Item3 + self.Item4
            elif self.journeyType.get() == 2:
                Cost_of_fare = self.Item1 + (Item2 * self.Item5 * 1.5) + self.Item3 + self.Item4
            else:
                Cost_of_fare = self.Item1 + (Item2 * self.Item5 * 2) + self.Item3 + self.Item4
            Tax = "Rs " + str('%.2f' % (Cost_of_fare * 0.09))
            ST = "Rs " + str('%.2f' % Cost_of_fare)
            TT = "Rs " + str('%.2f' % (Cost_of_fare + (Cost_of_fare * 0.09)))
            self.PaidTax.set(Tax)
            self.SubTotal.set(ST)
            self.TotalCost.set(TT)
        else:
            ms.showwarning("Error!", "Invalid Input\nPlease try again!!!")

    def widgets(self):
        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=True)
        Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE)
        Tops.pack(side=TOP, fill=BOTH, expand=True)
        self.lblTitle = Label(Tops, font=('arial', 70, 'bold'), text=" Taxi Booking System in LPU ")
        self.lblTitle.grid()
        CustomerDetailsFrame = LabelFrame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        FrameDetails = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)
        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=10, font=('arial', 12, 'bold'), text="Customer Name", relief=RIDGE)
        CustomerName.grid(row=0, column=0)
        TravelFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=('arial', 12, 'bold'), text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0, column=1)
        Book_Frame = LabelFrame(FrameDetails, width=300, height=150, relief=FLAT)
        Book_Frame.grid(row=1, column=0)
        CostFrame = LabelFrame(FrameDetails, width=150, height=150, bd=5, relief=FLAT)
        CostFrame.grid(row=1, column=1)
        Receipt_BottonFrame = LabelFrame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT, fill=BOTH, expand=True)
        ReceiptFrame = LabelFrame(Receipt_BottonFrame, width=350, height=300, font=('arial', 12, 'bold'), text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0)
        ButtonFrame = LabelFrame(Receipt_BottonFrame, width=350, height=100, relief=RIDGE)
        ButtonFrame.grid(row=1, column=0)
        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Firstname, bd=7, insertwidth=2, justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1)
        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Surname, bd=7, insertwidth=2, justify=RIGHT)
        self.txtSurname.grid(row=1, column=1, sticky=W)
        self.lblAddress = Label(CustomerName, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Address, bd=7, insertwidth=2, justify=RIGHT)
        self.txtAddress.grid(row=2, column=1)
        self.lblPostcode = Label(CustomerName, font=('arial', 14, 'bold'), text="Postcode", bd=7)
        self.lblPostcode.grid(row=3, column=0, sticky=W)
        self.txtPostcode = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Postcode, bd=7, insertwidth=2, justify=RIGHT)
        self.txtPostcode.grid(row=3, column=1)
        self.lblTelephone = Label(CustomerName, font=('arial', 14, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=4, column=0, sticky=W)
        self.txtTelephone = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Telephone, bd=7, insertwidth=2, justify=RIGHT)
        self.txtTelephone.grid(row=4, column=1)
        self.lblMobile = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Mobile, bd=7, insertwidth=2, justify=RIGHT)
        self.txtMobile.grid(row=5, column=1)
        self.lblEmail = Label(CustomerName, font=('arial', 14, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=self.Email, bd=7, insertwidth=2, justify=RIGHT)
        self.txtEmail.grid(row=6, column=1)
        self.lblPickup = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pickup", bd=7)
        self.lblPickup.grid(row=0, column=0, sticky=W)
        self.cboPickup = ttk.Combobox(TravelFrame, textvariable=self.varl1, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboPickup['values'] = ('', 'CampusCafe', 'AdmissionBlock', 'GirlsHostel', 'BoysHostel')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0, column=1)
        self.lblDrop = Label(TravelFrame, font=('arial', 14, 'bold'), text="Drop", bd=7)
        self.lblDrop.grid(row=1, column=0, sticky=W)
        self.cboDrop = ttk.Combobox(TravelFrame, textvariable=self.varl2, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboDrop['values'] = ('', 'BoysHostel', 'GirlsHostel', 'CampusCafe', 'AdmissionBlock')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1, column=1)
        self.lblPooling = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pooling", bd=7)
        self.lblPooling.grid(row=2, column=0, sticky=W)
        self.cboPooling = ttk.Combobox(TravelFrame, textvariable=self.varl3, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboPooling['values'] = ('', '1', '2', '3', '4')
        self.cboPooling.current(0)
        self.cboPooling.grid(row=2, column=1)
        self.chkTaxiTax = Checkbutton(TravelFrame, text="Taxi Tax(Base Charge) *", variable=self.var1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'), command=self.Taxi_Tax)
        self.chkTaxiTax.grid(row=3, column=0, sticky=W)
        self.txtTaxiTax = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.TaxiTax, bd=6, width=18, bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTaxiTax.grid(row=3, column=1)
        self.chkKm = Checkbutton(TravelFrame, text="Distance(KMs) *", variable=self.var2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'), command=self.Kilo)
        self.chkKm.grid(row=4, column=0, sticky=W)
        self.txtKm = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.Km, bd=6, width=18, bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtKm.grid(row=4, column=1)
        self.chkTravel_Ins = Checkbutton(TravelFrame, text="Travelling Insurance *", variable=self.var3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'), command=self.Travelling)
        self.chkTravel_Ins.grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.Travel_Ins, bd=6, width=18, bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5, column=1)
        self.chkLuggage = Checkbutton(TravelFrame, text="Extra Luggage", variable=self.var4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'), command=self.Lug)
        self.chkLuggage.grid(row=6, column=0, sticky=W)
        self.txtLuggage = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=self.Luggage, bd=6, width=18, bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtLuggage.grid(row=6, column=1)
        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Paid Tax\t\t", bd=7)
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=self.PaidTax, bd=7, width=26, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPaidTax.grid(row=0, column=3)
        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=7)
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=self.SubTotal, bd=7, width=26, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1, column=3)
        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=self.TotalCost, bd=7, width=26, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2, column=3)
        self.chkStandard = Radiobutton(Book_Frame, text="Standard", value=1, variable=self.carType, font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkStandard.grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame, font=('arial', 14, 'bold'), width=7, textvariable=self.Standard, bd=5, state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtStandard.grid(row=0, column=1)
        self.chkPrimeSedan = Radiobutton(Book_Frame, text="PrimeSedan", value=2, variable=self.carType, font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkPrimeSedan.grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan = Label(Book_Frame, font=('arial', 14, 'bold'), width=7, textvariable=self.PrimeSedan, bd=5, state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPrimeSedan.grid(row=1, column=1)
        self.chkPremiumSedan = Radiobutton(Book_Frame, text="PremiumSedan", value=3, variable=self.carType, font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkPremiumSedan.grid(row=2, column=0)
        self.txtPremiumSedan = Label(Book_Frame, font=('arial', 14, 'bold'), width=7, textvariable=self.PremiumSedan, bd=5, state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2, column=1)
        self.chkSingle = Radiobutton(Book_Frame, text="Single", value=1, variable=self.journeyType, font=('arial', 14, 'bold'))
        self.chkSingle.grid(row=0, column=2, sticky=W)
        self.chkReturn = Radiobutton(Book_Frame, text="Return", value=2, variable=self.journeyType, font=('arial', 14, 'bold'))
        self.chkReturn.grid(row=1, column=2, sticky=W)
        self.chkSpecialsNeeds = Radiobutton(Book_Frame, text="SpecialNeeds", value=3, variable=self.journeyType, font=('arial', 14, 'bold'))
        self.chkSpecialsNeeds.grid(row=2, column=2, sticky=W)
        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)
        self.btnTotal = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Total', command=self.Total_Paid)
        self.btnTotal.grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Receipt', command=self.Receiptt)
        self.btnReceipt.grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Reset', command=self.Reset)
        self.btnReset.grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Exit', command=self.iExit)
        self.btnExit.grid(row=0, column=3)

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = User(root)
    root.mainloop()
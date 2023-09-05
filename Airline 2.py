from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime
import mysql.connector 
loggedUser=""

def main():
    root=Tk()
    app=Window1(root)

def databaseSetup():
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="BS55")
    mycursor=mydb.cursor
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Air;")
    mycursor.execute("use Air")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Customer_Details(First_Name VARCHAR(20),Surname VARCHAR(20),Address VARCHAR(20),PostCode INT,Telephone INT,Mobile INT,Email EMAIL)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS International_Airlines(Airport_Name VARCHAR(20),Departure VARCHAR(20),Arrival VARCHAR(20),TerminalNo INT,Timing DATETIME,Passangers INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Domestic_Airlines(Airport_Name VARCHAR(20),Departure VARCHAR(20),Arrival VARCHAR(20),TerminalNo INT,Timing DATETIME,Passangers INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Restaurant(Fries VARCHAR(20),Noodles VARCHAR(20),Soup VARCHAR(20),Drinks VARCHAR(20),Burger VARCHAR(20),Sandwich VARCHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Restaurant(FirstClass VARCHAR(20),BusinessClass VARCHAR(20),EconomyClass VARCHAR(20),TerminalNo VARCHAR(20),Timing DATETIME)")
    mycursor.close()
    mydb.close()


class window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Travel Management System")
        self.master.geometry('1585x820+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        self.Username=StringVar()
        self.Passward=StringVar()

        self.LabelTitle=Label(self.frame,text='Airport Management System',font=('Copperplate Gothic Bold',50,'bold'),bd=20,
                              )
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=40)


        self.Loginframe1=Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3=Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)

        #========================================================================================
        self.lblUsername=Label(self.Loginframe1,text='Username',font=('arial',30,'bold'),bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,
                               textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)


        self.lblPassward=Label(self.Loginframe1,text='Passward',font=('arial',30,'bold'),bd=22)
        self.lblPassward.grid(row=1,column=0)
        self.txtPassward=Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,show="**",
                               textvariable=self.Passward)
        self.txtPassward.grid(row=1,column=1,padx=85)
        #========================================================================================

        self.btnLogin=Button(self.Loginframe2,text="Login",width=17,font=('arial',20,'bold'),
                             command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset=Button(self.Loginframe2,text="Reset",width=17,font=('arial',20,'bold'),
                             command=self.Reset)
        self.btnReset.grid(row=0,column=1)
 
        self.btnExit=Button(self.Loginframe2,text="Exit",width=17,font=('arial',20,'bold'),
                            command=self.iExit)
                           
        self.btnExit.grid(row=0,column=2)
        
        #========================================================================================


        self.btnCustomer=Button(self.Loginframe3,text="Customer Details",
                                state=DISABLED,command=self.Customer_window,font=('arial',15,'bold'))
        self.btnCustomer.grid(row=0,column=0)
        
        self.btnInternational=Button(self.Loginframe3,text="International Airlines",
                                state=DISABLED,command=self.International_window,font=('arial',15,'bold'))
        self.btnInternational.grid(row=0,column=1)
        
        self.btnDomestic=Button(self.Loginframe3,text="Domestic Airlines",
                                state=DISABLED,command=self.Domestic_window,font=('arial',15,'bold'))
        self.btnDomestic.grid(row=0,column=2)
        
        self.btnRestaurant=Button(self.Loginframe3,text="Restaurant",
                                state=DISABLED,command=self.Restaurant_window,font=('arial',15,'bold'))
        self.btnRestaurant.grid(row=0,column=3)
        
        self.btnTicket=Button(self.Loginframe3,text="Ticket Counter",
                                state=DISABLED,command=self.TicketCounter_window,font=('arial',15,'bold'))
        self.btnTicket.grid(row=0,column=4)

        #========================================================================================
    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Passward.get())

        if (user==str(1234)) and (pas==str(2345)):
            self.btnCustomer.config(state=NORMAL)
            self.btnInternational.config(state=NORMAL)
            self.btnDomestic.config(state=NORMAL)
            self.btnRestaurant.config(state=NORMAL)
            self.btnTicket.config(state=NORMAL)
        elif (user==str(2345)) and (pas==str(3456)):
            self.btnCustomer.config(state=NORMAL)
            self.btnInternational.config(state=NORMAL)
            self.btnDomestic.config(state=NORMAL)
            self.btnRestaurant.config(state=NORMAL)
            self.btnTicket.config(state=NORMAL)
        elif (user==str(3456)) and (pas==str(4567)):
            self.btnCustomer.config(state=NORMAL)
            self.btnInternational.config(state=NORMAL)
            self.btnDomestic.config(state=NORMAL)
            self.btnRestaurant.config(state=NORMAL)
            self.btnTicket.config(state=NORMAL)
        elif (user==str(4567)) and (pas==str(5678)):
            self.btnCustomer.config(state=NORMAL)
            self.btnInternational.config(state=NORMAL)
            self.btnDomestic.config(state=NORMAL)
            self.btnRestaurant.config(state=NORMAL)
            self.btnTicket.config(state=NORMAL)
        elif (user==str(5678)) and (pas==str(6789)):
            self.btnCustomer.config(state=NORMAL)
            self.btnInternational.config(state=NORMAL)
            self.btnDomestic.config(state=NORMAL)
            self.btnRestaurant.config(state=NORMAL)
            self.btnTicket.config(state=NORMAL)
        
        else:
            tkinter.messagebox.askyesno("Airport Management System","You have entered an invalid login details")
            self.btnCustomer.config(state=DISABLED)
            self.btnInternational.config(state=DISABLED)
            self.btnDomestic.config(state=DISABLED)
            self.btnRestaurant.config(state=DISABLED)
            self.btnTicket.config(state=DISABLED)
            self.Username.set("")
            self.Passward.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnCustomer.config(state=DISABLED)
        self.btnInternational.config(state=DISABLED)
        self.btnDomestic.config(state=DISABLED)
        self.btnRestaurant.config(state=DISABLED)
        self.btnTicket.config(state=DISABLED)
        self.Username.set("")
        self.Passward.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Airport Management System","Confirm if you want to exit")
        if self.iExit>0:
            self.master.destroy()
        return

        #========================================================================================

               
                            

    def Customer_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)
    def International_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)
    def Domestic_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)
    def Restaurant_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)
    def TicketCounter_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window6(self.newWindow)
        

class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Customer Details")
        self.master.geometry("1585x820+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        #========================================================================================
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Mobile=StringVar()
        Email=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()

        #============================================Defined Function==============================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Airport Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Mobile.set("")
            Email.set("")
            self.txtReceipt.delete("1.0",END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Details:"+ randomRef)

            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get()+ "\n")
            self.txtReceipt.insert(END,'Firstname:\t\t\t\t\t'+ Firstname.get()+ "\n")
            self.txtReceipt.insert(END,'Surname:\t\t\t\t\t'+ Surname.get()+ "\n")
            self.txtReceipt.insert(END,'Address:\t\t\t\t\t'+ Address.get()+ "\n")
            self.txtReceipt.insert(END,'PostCode:\t\t\t\t\t'+ PostCode.get()+ "\n")
            self.txtReceipt.insert(END,'Telephone:\t\t\t\t\t'+ Telephone.get()+ "\n")
            self.txtReceipt.insert(END,'Mobile:\t\t\t\t\t'+ Mobile.get()+ "\n")
            self.txtReceipt.insert(END,'Email:\t\t\t\t\t'+ Email.get()+ "\n")

        #========================================Frame========================================================
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=35, width=1350,padx=35,relief= RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('Copperplate Gothic Bold',60,'bold'),text=" Customer Details ")
        self.lblTitle.grid()

        #===========================CustomerName====================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=1000, bd=20, pady=5,relief= RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)

        
        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=4000, bd=10, pady=5,relief= RIDGE)
        FrameDetails.pack(side=LEFT)
        


        CustomerName=LabelFrame(FrameDetails, width=150,height=250, bd=20,
                                font=('arial',12,'bold'), text='Customer Name', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        #========================================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=450,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)


        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',10,'bold'), text='Customer Details', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)


        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,
                                font=('arial',10,'bold'), text='Buttons', relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        #========================================================================================================

        self.lblFirstname=Label(CustomerName, font=('arial',14,'bold'),text="First Name",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Firstname,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)

        self.lblSurname=Label(CustomerName, font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Surname,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1)

        
        self.lblAddress=Label(CustomerName, font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Address,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)

        self.lblPostCode=Label(CustomerName, font=('arial',14,'bold'),text="PostCode",bd=7)
        self.lblPostCode.grid(row=3,column=0,sticky=W)
        self.txtPostCode=Entry(CustomerName, font=('arial',14,'bold'),textvariable=PostCode,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtPostCode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName, font=('arial',14,'bold'),text="Telephone",bd=7)
        
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Telephone,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)


        self.lblMobile=Label(CustomerName, font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.lblMobile=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Mobile,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblMobile.grid(row=5,column=1)


        self.lblEmail=Label(CustomerName, font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Email,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)
        
        #=======================================Receipt=================================================================
        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #========================================Buttons======================================================
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=15,
                             text='Customer Details',command=Receipt ).grid(row=0,column=1)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iExit).grid(row=0,column=3)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=Reset).grid(row=0,column=2)
        #========================================================================================================

class Window3:
    def __init__(self,master):
        self.master=master
        self.master.title("International Airlines")
        self.master.geometry("1585x820+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        #========================================================================================
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()

        AirportName=StringVar()
        Departure=StringVar()
        Arrival=StringVar()
        TerminalNo=StringVar()
        Timing=StringVar()
        Passangers=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()

        #============================================Defined Function==============================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Airport Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            AirportName.set("")
            Departure.set("")
            Arrival.set("")
            TerminalNo.set("")
            Timing.set("")
            Passangers.set("")
            self.txtReceipt.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Details:"+ randomRef)

            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get()+ "\n")
            self.txtReceipt.insert(END,'AirportName:\t\t\t\t\t'+ AirportName.get()+ "\n")
            self.txtReceipt.insert(END,'Departure:\t\t\t\t\t'+ Departure.get()+ "\n")
            self.txtReceipt.insert(END,'Arrival:\t\t\t\t\t'+ Arrival.get()+ "\n")
            self.txtReceipt.insert(END,'TerminalNo:\t\t\t\t\t'+ TerminalNo.get()+ "\n")
            self.txtReceipt.insert(END,'Timing:\t\t\t\t\t'+ Timing.get()+ "\n")
            self.txtReceipt.insert(END,'Passangers:\t\t\t\t\t'+ Passangers.get()+ "\n")

        #========================================Frame========================================================
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=35, width=1350,padx=35,relief= RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('Copperplate Gothic Bold',60,'bold'),text=" International Airlines")
        self.lblTitle.grid()

        #===========================TravelDetails====================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=1000, bd=20, pady=5,relief= RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)
        

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=4000, bd=10, pady=5,relief= RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250, bd=20,
                                font=('arial',12,'bold'), text='Travel Details', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        #========================================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=450,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)


        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',10,'bold'), text='Travel Details', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)


        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,
                                font=('arial',10,'bold'), text='Buttons', relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        #========================================================================================================

        self.lblAirportName=Label(CustomerName, font=('arial',14,'bold'),text="Airport Name",bd=7)
        self.lblAirportName.grid(row=0,column=0,sticky=W)
        self.txtAirportName=Entry(CustomerName, font=('arial',14,'bold'),textvariable=AirportName,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtAirportName.grid(row=0,column=1)

        self.lblDeparture=Label(CustomerName, font=('arial',14,'bold'),text="Departure",bd=7)
        self.lblDeparture.grid(row=1,column=0,sticky=W)
        self.txtDeparture=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Departure,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtDeparture.grid(row=1,column=1)

        
        self.lblArrival=Label(CustomerName, font=('arial',14,'bold'),text="Arrival",bd=7)
        self.lblArrival.grid(row=2,column=0,sticky=W)
        self.txtArrival=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Arrival,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtArrival.grid(row=2,column=1)

        self.lblTerminalNo=Label(CustomerName, font=('arial',14,'bold'),text="TerminalNo",bd=7)
        self.lblTerminalNo.grid(row=3,column=0,sticky=W)
        self.txtTerminalNo=Entry(CustomerName, font=('arial',14,'bold'),textvariable=TerminalNo,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTerminalNo.grid(row=3,column=1)


        self.lblTiming=Label(CustomerName, font=('arial',14,'bold'),text="Timing",bd=7)
        self.lblTiming.grid(row=4,column=0,sticky=W)
        self.txtTiming=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Timing,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTiming.grid(row=4,column=1)


        self.lblPassangers=Label(CustomerName, font=('arial',14,'bold'),text="Passangers",bd=7)
        self.lblPassangers.grid(row=5,column=0,sticky=W)
        self.lblPassangers=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Passangers,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblPassangers.grid(row=5,column=1)

        #=======================================Receipt=================================================================
        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #========================================Buttons======================================================
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=15,
                             text='Travel Details',command=Receipt ).grid(row=0,column=1)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iExit).grid(row=0,column=3)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=Reset).grid(row=0,column=2)

        #========================================================================================


class Window4:
    def __init__(self,master):
        self.master=master
        self.master.title("Domestic Airlines")
        self.master.geometry("1585x820+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        #========================================================================================
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()

        AirportName=StringVar()
        Departure=StringVar()
        Arrival=StringVar()
        TerminalNo=StringVar()
        Timing=StringVar()
        Passangers=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()

        #============================================Defined Function==============================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Airport Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            AirportName.set("")
            Departure.set("")
            Arrival.set("")
            TerminalNo.set("")
            Timing.set("")
            Passangers.set("")
            self.txtReceipt.delete("1.0",END)
            
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Details:"+ randomRef)

            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get()+ "\n")
            self.txtReceipt.insert(END,'AirportName:\t\t\t\t\t'+ AirportName.get()+ "\n")
            self.txtReceipt.insert(END,'Departure:\t\t\t\t\t'+ Departure.get()+ "\n")
            self.txtReceipt.insert(END,'Arrival:\t\t\t\t\t'+ Arrival.get()+ "\n")
            self.txtReceipt.insert(END,'TerminalNo:\t\t\t\t\t'+ TerminalNo.get()+ "\n")
            self.txtReceipt.insert(END,'Timing:\t\t\t\t\t'+ Timing.get()+ "\n")
            self.txtReceipt.insert(END,'Passangers:\t\t\t\t\t'+ Passangers.get()+ "\n")

        #========================================Frame========================================================
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=35, width=1350,padx=35,relief= RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('Copperplate Gothic Bold',60,'bold'),text=" Domestic Airlines")
        self.lblTitle.grid()

        #===========================TravelDetails====================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=1000, bd=20, pady=5,relief= RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)
        

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=4000, bd=10, pady=5,relief= RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250, bd=20,
                                font=('arial',12,'bold'), text='Travel Details', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        #========================================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=450,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)


        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',10,'bold'), text='Travel Details', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)


        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,
                                font=('arial',10,'bold'), text='Buttons', relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        #========================================================================================================

        self.lblAirportName=Label(CustomerName, font=('arial',14,'bold'),text="Airport Name",bd=7)
        self.lblAirportName.grid(row=0,column=0,sticky=W)
        self.txtAirportName=Entry(CustomerName, font=('arial',14,'bold'),textvariable=AirportName,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtAirportName.grid(row=0,column=1)

        self.lblDeparture=Label(CustomerName, font=('arial',14,'bold'),text="Departure",bd=7)
        self.lblDeparture.grid(row=1,column=0,sticky=W)
        self.txtDeparture=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Departure,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtDeparture.grid(row=1,column=1)

        
        self.lblArrival=Label(CustomerName, font=('arial',14,'bold'),text="Arrival",bd=7)
        self.lblArrival.grid(row=2,column=0,sticky=W)
        self.txtArrival=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Arrival,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtArrival.grid(row=2,column=1)

        self.lblTerminalNo=Label(CustomerName, font=('arial',14,'bold'),text="TerminalNo",bd=7)
        self.lblTerminalNo.grid(row=3,column=0,sticky=W)
        self.txtTerminalNo=Entry(CustomerName, font=('arial',14,'bold'),textvariable=TerminalNo,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTerminalNo.grid(row=3,column=1)


        self.lblTiming=Label(CustomerName, font=('arial',14,'bold'),text="Timing",bd=7)
        self.lblTiming.grid(row=4,column=0,sticky=W)
        self.txtTiming=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Timing,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTiming.grid(row=4,column=1)


        self.lblPassangers=Label(CustomerName, font=('arial',14,'bold'),text="Passangers",bd=7)
        self.lblPassangers.grid(row=5,column=0,sticky=W)
        self.lblPassangers=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Passangers,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblPassangers.grid(row=5,column=1)

        #=======================================Receipt=================================================================
        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #========================================Buttons======================================================
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=15,
                             text='Travel Details',command=Receipt ).grid(row=0,column=1)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iExit).grid(row=0,column=3)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=Reset).grid(row=0,column=2)

        #=======================================================================================




class Window5:
    def __init__(self,master):
        self.master=master
        self.master.title("Restaurant")
        self.master.geometry("1585x820+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        #========================================================================================
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()


        Fries=StringVar()
        Noodles=StringVar()
        Soup=StringVar()
        Drinks=StringVar()
        Burger=StringVar()
        Sandwich=StringVar()
        Total=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()


        
        #============================================Defined Function==============================================

        def Ref():
            if (Fries.get()==""):
                CoFries=0
            else:
                CoFries=float(Fries.get())

            if (Noodles.get()==""):
                CoNoodles=0
            else:
                CoNoodles=float(Noodles.get())

            if (Soup.get()==""):
                CoSoup=0
            else:
                CoSoup=float(Soup.get())

            if (Burger.get()==""):
                CoBurger=0
            else:
                CoBurger=float(Burger.get())

            if (Sandwich.get()==""):
                CoSandwich=0
            else:
                CoSandwich=float(Sandwich.get())

            if (Drinks.get()==""):
                CoD=0
            else:
                CoD=float(Drinks.get())

            CostofFries =CoFries*140
            CostofDrinks=CoD*65
            CostofNoodles = CoNoodles*90
            CostofSoup = CoSoup*140
            CostBurger = CoBurger*260
            CostSandwich=CoSandwich*300

            TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)

            OverAllCost ="Rs", str ('%.2f' % (TotalCost))

            Total.set(OverAllCost)
            


        def iExit():
            iExit=tkinter.messagebox.askyesno("Airport Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            Fries.set("")
            Noodles.set("")
            Soup.set("")
            Drinks.set("")
            Burger.set("")
            Sandwich.set("")
            Total.set("")
            self.txtReceipt.delete("1.0",END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Details:"+ randomRef)

            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get()+ "\n")
            self.txtReceipt.insert(END,'Noodles:\t\t\t\t\t'+ Noodles.get()+ "\n")
            self.txtReceipt.insert(END,'Soup:\t\t\t\t\t'+ Soup.get()+ "\n")
            self.txtReceipt.insert(END,'Fries:\t\t\t\t\t'+ Fries.get()+ "\n")
            self.txtReceipt.insert(END,'Drinks:\t\t\t\t\t'+ Drinks.get()+ "\n")
            self.txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ Sandwich.get()+ "\n")
            self.txtReceipt.insert(END,'Burger:\t\t\t\t\t'+ Burger.get()+ "\n")
            self.txtReceipt.insert(END,'TotalCost:\t\t\t\t\t'+ Total.get()+ "\n")
        
            
        #========================================Frame========================================================
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=35, width=1350,padx=35,relief= RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('Copperplate Gothic Bold',60,'bold'),text=" Restaurant")
        self.lblTitle.grid()

        #===========================RestaurantDetails====================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=1000, bd=20, pady=5,relief= RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)
        

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=4000, bd=10, pady=5,relief= RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails, width=250,height=250, bd=20,
                                font=('arial',12,'bold'), text='Restaurant Details', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        #========================================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=450,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)


        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',10,'bold'), text='Receipt', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)


        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,
                                font=('arial',10,'bold'), text='Buttons', relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        #========================================================================================================

        self.lblFries=Label(CustomerName, font=('arial',14,'bold'),text="Fries",bd=7)
        self.lblFries.grid(row=0,column=0,sticky=W)
        self.txtFries=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Fries,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtFries.grid(row=0,column=1)

        self.lblNoodles=Label(CustomerName, font=('arial',14,'bold'),text="Noodles",bd=7)
        self.lblNoodles.grid(row=1,column=0,sticky=W)
        self.txtNoodles=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Noodles,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtNoodles.grid(row=1,column=1)

        
        self.lblSoup=Label(CustomerName, font=('arial',14,'bold'),text="Soup",bd=7)
        self.lblSoup.grid(row=2,column=0,sticky=W)
        self.txtSoup=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Soup,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtSoup.grid(row=2,column=1)

        self.lblDrinks=Label(CustomerName, font=('arial',14,'bold'),text="Drinks",bd=7)
        self.lblDrinks.grid(row=3,column=0,sticky=W)
        self.txtDrinks=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Drinks,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtDrinks.grid(row=3,column=1)


        self.lblBurger=Label(CustomerName, font=('arial',14,'bold'),text="Burger",bd=7)
        self.lblBurger.grid(row=4,column=0,sticky=W)
        self.txtBurger=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Burger,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtBurger.grid(row=4,column=1)


        self.lblSandwich=Label(CustomerName, font=('arial',14,'bold'),text="Sandwich",bd=7)
        self.lblSandwich.grid(row=5,column=0,sticky=W)
        self.lblSandwich=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Sandwich,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblSandwich.grid(row=5,column=1)

        self.lblTotalCost=Label(CustomerName, font=('arial',14,'bold'),text="TotalCost",bd=7)
        self.lblTotalCost.grid(row=6,column=0,sticky=W)
        self.lblTotalCost=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Total,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblTotalCost.grid(row=6,column=1)
        

        
     
        #=======================================Receipt=================================================================
        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #========================================Buttons======================================================
        self.btnRef=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Total',command=Ref ).grid(row=0,column=4)
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Receipt',command=Receipt ).grid(row=0,column=1)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iExit).grid(row=0,column=3)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=Reset).grid(row=0,column=2)



        #========================================================================================
        

class Window6:
    def __init__(self,master):
        self.master=master
        self.master.title("Ticket Counter")
        self.master.geometry("1585x820+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()
        #========================================================================================

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()

        FirstClass=StringVar()
        BusinessClass=StringVar()
        EconomyClass=StringVar()
        TerminalNo=StringVar()
        Timing=StringVar()
        Total=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        
        #============================================Defined Function==============================================

        def Ref():
            if (FirstClass.get()==""):
                CoFirst=0
            else:
                CoFirst=float(FirstClass.get())

            if (BusinessClass.get()==""):
                CoBusiness=0
            else:
                CoBusiness=float(BusinessClass.get())

            if (EconomyClass.get()==""):
                CoEconomy=0
            else:
                CoEconomy=float(EconomyClass.get())

            CostofFirst =CoFirst*80000
            CostofBusiness=CoBusiness*60000
            CostofEconomy = CoEconomy*50000
            
            TotalCost=(CostofFirst+CostofBusiness+CostofEconomy)

            OverAllCost ="Rs", str ('%.2f' % (TotalCost))

            Total.set(OverAllCost)
            


        def iExit():
            iExit=tkinter.messagebox.askyesno("Airport Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            FirstClass.set("")
            BusinessClass.set("")
            EconomyClass.set("")
            TerminalNo.set("")
            Timing.set("")
            Total.set("")
            self.txtReceipt.delete("1.0",END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            
            

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef=str(x)
            Receipt_Ref.set("Details:"+ randomRef)

            self.txtReceipt.insert(END,'Date:\t\t\t\t\t'+ DateofOrder.get()+ "\n")
            self.txtReceipt.insert(END,'FC Tickets:\t\t\t\t\t'+ FirstClass.get()+ "\n")
            self.txtReceipt.insert(END,'BC Tickets:\t\t\t\t\t'+ BusinessClass.get()+ "\n")
            self.txtReceipt.insert(END,'EC Tickets:\t\t\t\t\t'+ EconomyClass.get()+ "\n")
            self.txtReceipt.insert(END,'Terminal No:\t\t\t\t\t'+ TerminalNo.get()+ "\n")
            self.txtReceipt.insert(END,'Timing:\t\t\t\t\t'+ Timing.get()+ "\n")
            self.txtReceipt.insert(END,'Total:\t\t\t\t\t'+ Total.get()+ "\n")

        #========================================Frame========================================================
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=35, width=1350,padx=35,relief= RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('Copperplate Gothic Bold',60,'bold'),text="Ticket Counter")
        self.lblTitle.grid()

        #===========================CounterDetails====================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=1000, bd=20, pady=5,relief= RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)
        

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=4000, bd=10, pady=5,relief= RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails, width=250,height=250, bd=20,
                                font=('arial',12,'bold'), text='Counter Details', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        #========================================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=450,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)


        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',10,'bold'), text='Details', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)


        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,
                                font=('arial',10,'bold'), text='Buttons', relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        #========================================================================================================

        self.lblFirstClass=Label(CustomerName, font=('arial',14,'bold'),text="First Class",bd=7)
        self.lblFirstClass.grid(row=0,column=0,sticky=W)
        self.txtFirstClass=Entry(CustomerName, font=('arial',14,'bold'),textvariable=FirstClass,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtFirstClass.grid(row=0,column=1)

        self.lblBusinessClass=Label(CustomerName, font=('arial',14,'bold'),text="Business Class",bd=7)
        self.lblBusinessClass.grid(row=1,column=0,sticky=W)
        self.txtBusinessClass=Entry(CustomerName, font=('arial',14,'bold'),textvariable=BusinessClass,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtBusinessClass.grid(row=1,column=1)

        
        self.lblEconomyClass=Label(CustomerName, font=('arial',14,'bold'),text="EconomyClass",bd=7)
        self.lblEconomyClass.grid(row=2,column=0,sticky=W)
        self.txtEconomyClass=Entry(CustomerName, font=('arial',14,'bold'),textvariable=EconomyClass,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtEconomyClass.grid(row=2,column=1)

        self.lblTerminalNo=Label(CustomerName, font=('arial',14,'bold'),text="Terminal No",bd=7)
        self.lblTerminalNo.grid(row=3,column=0,sticky=W)
        self.txtTerminalNo=Entry(CustomerName, font=('arial',14,'bold'),textvariable=TerminalNo,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTerminalNo.grid(row=3,column=1)


        self.lblTiming=Label(CustomerName, font=('arial',14,'bold'),text="Timing",bd=7)
        self.lblTiming.grid(row=4,column=0,sticky=W)
        self.txtTiming=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Timing,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.txtTiming.grid(row=4,column=1)

        self.lblTotalCost=Label(CustomerName, font=('arial',14,'bold'),text="TotalCost",bd=7)
        self.lblTotalCost.grid(row=6,column=0,sticky=W)
        self.lblTotalCost=Entry(CustomerName, font=('arial',14,'bold'),textvariable=Total,bd=7,
                                insertwidth=2,justify=RIGHT)
        self.lblTotalCost.grid(row=6,column=1)

        
       
     
        #=======================================Receipt=================================================================
        self.txtReceipt=Text(ReceiptFrame,width=60,height=21,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #========================================Buttons======================================================
        self.btnRef=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Total',command=Ref ).grid(row=0,column=1)
        self.btnReceipt=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Receipt',command=Receipt ).grid(row=0,column=2)
        self.btnExit=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iExit).grid(row=0,column=3)
        self.btnReset=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=Reset).grid(row=0,column=4)
        self.btnMode=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Mode',command=Reset).grid(row=0,column=5)
        

        
            
        

        #========================================================================================

        
        #========================================================================================
        
        
if __name__=='__main__':
                 root = Tk()
                 application = window1 (root)
                 root.mainloop()

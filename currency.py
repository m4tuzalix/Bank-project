import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from logs import logs
from currency_transfer import currency_trans

class currency(tk.Toplevel):    
    def __init__(self, master, nick, balance=0):
        self.nick = nick
        self.balance = balance
        self.path_customers = 'customers\\'
        self.path_logs = "logs\\"
        self.log = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "400x400")
        tk.Tk.title(self, "Currency Menu")
        global check
        self.depo = tk.IntVar()
        self.check = tk.StringVar(self,"Currency control menu")
        tk.Label(self, textvariable=self.check, fg="green", font = ("Algerian", 13)).pack() 
        tk.Label(self, text="").pack()                                                              ######
        tk.Label(self, text="Check your current ballance").pack()                           ########          MAIN BODY WITH BUTTONS/ENTRIES ETC.
        tk.Button(self, text="Check", bg="green", command=self.status).pack()
        tk.Label(self, text="").pack()
        self.depo2_entry = tk.Entry(self, bg="yellow")
        self.depo2_entry.pack()
        tk.Button(self, text="Deposit", bg="green", command=self.deposit_usd).pack()
        tk.Label(self, text="").pack()
        self.with_entry = tk.Entry(self, bg="yellow")
        self.with_entry.pack()
        tk.Button(self, text="Withdraw", bg="green", command=self.withdraw_usd).pack()
        tk.Button(self, text="Transfer", bg="green", command=self.trans_menu).pack()

    def trans_menu(self):           ### Recalls new window for currency transfers
        self.screen = tk.Toplevel(self)
        self.screen.geometry("350x200")
        self.screen.title("transfers")
        tk.Label(self.screen, text = "Do you transfers", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self.screen, text="").pack()
        global login
        global amount
        self.login = tk.Entry(self.screen, bg="yellow")
        self.login.insert(0, "Put user here")
        self.login.pack()
        tk.Label(self, text="").pack()
        self.amount = tk.Entry(self.screen, bg="yellow")
        self.amount.insert(0, "Put money amount here")
        self.amount.pack()
        tk.Button(self.screen, text="transfer", bg="green", command=self.systems).pack()

    def systems(self):          ## currency transfer system
        users_list = os.listdir(self.path_customers)
        self.login_load = self.login.get()
        self.amount_load = float(self.amount.get())
        balance=open(self.path_customers+self.nick, "r")             ###### Opens owner file
        balance2 = balance.readlines()  #<----- splits file to be readable line by line
        if self.login_load not in users_list:
            messagebox.showerror("error", "User doesn't exist")
        else:
            balance3=open(self.path_customers+self.login_load, "r")  ######### opens file of person we want to transfer money
            balance4 = balance3.readlines()   #<----- splits file to be readable line by line

            if self.login_load not in users_list:
                messagebox.showerror("error", "User doesn't exist")

            if balance4[4] == "Account not opened"+"\n": #<--- Checks if person has opened currency account
                messagebox.showerror("error", "User has not opened currency account yet")
            
            elif float(balance2[4]) > self.amount_load:
                with open(self.path_customers+self.nick, "r") as file3:
                    lines2 = file3.readlines()
                with open(self.path_customers+self.nick, "w") as file3:
                    lines2[2]=str(float(lines2[4])-self.amount_load)+'\n'
                    for x in lines2:
                        file3.write(x)
            #----------------------------------------#
                with open(self.path_customers+self.login_load, "r") as file2:
                    lines = file2.readlines()
                with open(self.path_customers+self.login_load, "w") as file2:
                    lines[4]=str(float(lines[4])+self.amount_load)+'\n'
                    for x in lines:
                        file2.write(x)
                    var = ('%s' % float(self.amount_load)) #<---- Transform decimal value to string to be displayable
                    messagebox.showinfo("success", "You have transfered: "+var+" usd")
                    self.log.transfer_usd_logs(self.nick, self.login_load, self.amount_load)
            else:
                balance.close
                messagebox.showerror("error", "No funds!")
    
    def status(self): ###### current balance of currency accoount
        file=open(self.path_customers+self.nick, "r")
        lines = file.readlines()
        self.check.set("Your current balance: "+lines[4]+" USD")

    def deposit_usd(self):
        self.usd = float(self.depo2_entry.get()) 

        if self.usd < 0:                                            #### Exactly the same mechanism like in bank.py
            self.balance = self.balance
            print("You cannot deposit negative amount")

        else:
            self.balance = float(self.balance) + self.usd
            with open(self.path_customers+self.nick, "r") as file:
                lines = file.readlines()

            with open(self.path_customers+self.nick, "w") as file:
                lines[4]=str(float(lines[4])+self.usd)+'\n'
                for x in lines:
                    file.write(x)

            messagebox.showinfo("balance","You have deposit: "+str(self.usd)+" usd")
            self.log.depo_usd_logs(self.nick, self.usd)

    def withdraw_usd(self):
        self.balance = float(self.balance)
        self.usd = float(self.with_entry.get()) 
        balance=open(self.path_customers+self.nick, "r")
        lines = balance.readlines()                                     #### Exactly the same mechanism like in bank.py


        if float(lines[4]) < self.usd:
            self.balance = self.balance
            with open(self.path_customers+self.nick, "w") as balance2:
                lines[4]=str(float(lines[4]))+'\n'
                for x in lines:
                    balance2.write(x)
            messagebox.showerror("error","No funds")


        elif self.usd < 0:
            self.balance = self.balance
            messagebox.showerror("error","You cannot wihdraw negative amount")

        else:
            self.balance = float(self.balance) - self.usd
            with open(self.path_customers+self.nick, "r") as file:
                lines = file.readlines()

            with open(self.path_customers+self.nick, "w") as file:
                lines[4]=str(float(lines[4])-self.usd)+'\n'
                for x in lines:
                    file.write(x)

                messagebox.showinfo("balance","You have withdraw: "+str(self.usd)+" usd")
                self.log.with_usd_logs(self.nick, self.usd)


class currency_new(tk.Toplevel):
    def __init__(self, master, nick, kill):
        self.kill = kill
        self.nick = nick
        self.path_customers = "customers\\"
        self.log = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Currency account creation")
        tk.Label(self, text = "Currency menu", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Create", bg="green", command=self.create).pack()
        tk.Label(self, text="").pack()

    def create(self):
        with open(self.path_customers+self.nick, "r") as file:
            lines = file.readlines()
        with open(self.path_customers+self.nick, "w") as file2:
            lines[4] = "0"+"\n"
            for x in lines:
                file2.write(x)
            tk.Label(self, text="Currency account opened", fg="green", font=("calibri", 11)).pack()
            file2.close
            tk.Label(self.kill, text='').pack()
            tk.Button(self.kill, text="Add funds to currency", bg="red", command=lambda:currency_trans(self, self.nick)).pack()
            self.log.currency_logs_on(self.nick)
            self.withdraw()


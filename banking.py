import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
import string
from transfers import trans
from currency import currency, currency_new
from tokenik import token
from logs import logs
from currency_transfer import currency_trans
from admin import admin_chat
from hazard import roulete, lotto, lotto_los




class bank(tk.Tk):

    def __init__(self, name, password, code, balance=0): ## Script opens for person who provide login/password/security code

        self.balance = balance
        self.name = name
        self.password = password
        self.code = code
        self.log = logs()
        self.path_customers = "customers\\"
        self.path_logs = "logs\\"



        tk.Tk.__init__(self)
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            lines[8] = "ONLINE"+'\n'
            for x in lines:
                file2.write(x)
        tk.Tk.title(self, "Smiglo bank "+'logged as: '+str(self.name))
        tk.Tk.geometry(self,"400x500")
        tk.Tk.protocol(self,'WM_DELETE_WINDOW', self.x_disable)
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="deposit", bg="red", command=self.deposit).pack()    ##### Main Body
        self.depo_entry = tk.Entry(self, bg="yellow")
        self.depo_entry.pack()
        tk.Button(self, text="withdraw", bg="red", command=self.withdraw).pack()
        self.withh_entry = tk.Entry(self, bg="yellow")
        self.withh_entry.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Check balance", bg="red", command=self.check).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Log Off", bg="pink", command=self.log_off).pack(side=tk.BOTTOM)
        tk.Tk.after(self, 100, self.currency_check)
        tk.Tk.after(self, 100, self.token_check)

    # Submenus
        menu = tk.Menu(self)
        tk.Tk.config(self, menu=menu)

        Sub = tk.Menu(menu)
        menu.add_cascade(label="transfers", menu=Sub) #####     Submenu for transfers
        Sub.add_command(label="Do transfer", command=lambda: trans(self, self.name))######

        Sub2 = tk.Menu(menu)
        menu.add_cascade(label="Currency", menu=Sub2) #####     SuBmenu for currency
        Sub2.add_command(label="Currency manu", command=self.currency) #######

        Sub3 = tk.Menu(menu)
        menu.add_cascade(label="Admin chat", menu=Sub3)
        Sub3.add_command(label="Open admin chat", command=lambda: admin_chat(self, self.name, self.password, self.code))

        Sub4 = tk.Menu(menu)
        menu.add_cascade(label="Roulete", menu=Sub4)
        Sub4.add_command(label="Play roulete", command=lambda: roulete(self, self.name))

        Sub5 = tk.Menu(menu)
        menu.add_cascade(label="Lotto", menu=Sub5)
        Sub5.add_command(label="Play lotto", command=lambda: lotto_los(self, self.name))
    
    def log_off(self):
        self.log.log_on(self.name)
        with open(self.path_customers+self.name, "r") as file:
            line = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            line[8] = "OFFLINE"
            for x in line:
                file2.write(x)
            file2.close
        self.destroy()
        
    def currency_check(self):
        with open(self.path_customers+self.name, 'r') as file:
            lines = file.readlines()
            if lines[4] != "Account not opened"+"\n":
                tk.Button(self, text="Add funds to currency", bg="red", command=lambda: currency_trans(self, self.name)).pack()
                tk.Label(self, text="").pack()
            else:
                pass

    def x_disable(self):
        pass

    def token_check(self):
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
            if lines[7] == "No token"+"\n":
                global button
                self.button = tk.Button(self, text="Activate_token", bg="red", command=self.activation)
                self.button.pack()
            else:
                global button2
                self.button2 = tk.Button(self, text="Deactivation", bg="red", command=self.deactiv)
                self.button2.pack()
    
    def activation(self):
        self.button.destroy()
        self.button2 = tk.Button(self, text="Deactivation", bg="red", command=self.deactiv)
        self.button2.pack()
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            lines[7] = "Activated"+"\n"
            for x in lines:
                file2.write(x)
            file2.close
            self.log.token_logs_on(self.name)

    def deactiv(self):
        self.button2.destroy()
        self.button = tk.Button(self, text="Activate_token", bg="red", command=self.activation)
        self.button.pack()
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            lines[7] = "No token"+"\n"
            for x in lines:
                file2.write(x)
            self.log.token_logs_off(self.name)



    def currency(self):
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
            if lines[4] == "Account not opened"+"\n":
                currency_new(self,self.name,self)
            else:
                currency(self,self.name)
            

    def transfer(self): ### Opens menu transfers
        trans(self, self.name)

    def check(self): ### Allows to check the current ballance basing on the line where it is saved in file
        file=open(self.path_customers+self.name, "r")
        lines = file.readlines() 
        messagebox.showinfo("Balance status", "Current Balance: "+lines[3]) 
    
    def deposit(self): ### Allows to add funds to account
        self.secur = self.depo_entry.get()
        if not self.secur:
            messagebox.showerror('erro', 'empty field')
        else:
            self.amt = float(self.depo_entry.get())
        
                         # Amount to deposit
            if self.amt < 0:
                self.balance = self.balance
                print("You cannot deposit negative amount")         
                                                        
            else:
                self.balance = float(self.balance) + self.amt
                with open(self.path_customers+self.name, "r") as file:
                    lines = file.readlines()

                with open(self.path_customers+self.name, "w") as file:
                    lines[3]=str(float(lines[3])+self.amt)+'\n'
                    for x in lines:
                        file.write(x)

                messagebox.showinfo("balance","You have deposit: "+str(self.amt)+" pln")
                self.log.depo_logs(self.name, self.amt)

    def withdraw(self): 
        self.secur = self.depo_entry.get()
        if not self.secur:
            messagebox.showerror('erro', 'empty field')
        else: 
            self.amt = float(self.withh_entry.get())
       
            if self.amt > self.balance:
                self.balance = self.balance
                messagebox.showinfo('balance','insufficient funds')                                   ##### Opposite to deposit (Same mechanism though)

            elif self.amt < 0:
                self.balance = self.balance
                messagebox.showinfo("balance",self.name+", you cannot withdraw negative amount")
            else:
                self.balance = float(self.balance) - self.amt
                with open(self.path_customers+self.name, "r") as file:
                    lines = file.readlines()
                with open(self.path_customers+self.name, "w") as file:
                    lines[3]=str(float(lines[3])-self.amt)+'\n'
                    for x in lines:
                        file.write(x)
                    messagebox.showinfo("balance","You have withdraw: "+str(self.amt)+" pln")
                    self.log.with_logs(self.name, self.amt)
import tkinter as tk 
import math
from tkinter import messagebox

class currency_trans(tk.Toplevel):
    def __init__(self, master, name):
        self.name=name
        self.path_customers = "customers\\"
        tk.Toplevel.__init__(self, master)
        global file
        with open(self.path_customers+self.name, 'r') as file:
            lines=file.readlines()
        self.title("Add funds to currency")
        self.geometry("350x250")
        self.balance = tk.StringVar(self, "Available balance: "+lines[3])
        self.info = tk.Label(self, textvariable=self.balance, fg="green", font = ("Algerian", 13))
        self.info.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        self.funds = tk.Entry(self)
        self.funds.pack()
        tk.Button(self, text="proceed", command=self.mechanism).pack()
        self.info2 = tk.StringVar(self)
        tk.Label(self, textvariable=self.info2, fg="green").pack()

    def mechanism(self):
        self.amount = float(self.funds.get())
        if self.amount < 0:
            messagebox.showerror('error', 'cannot proceed negative amount')
        else:  
            with open(self.path_customers+self.name, 'r') as file:
                lines=file.readlines()
            if float(lines[3]) < self.amount:
                messagebox.showerror('error', 'No funds')
            else:
                with open(self.path_customers+self.name, 'w') as file2:
                    lines[3]=str(float(lines[3])-self.amount)+'\n'
                    lines[4]=str(float(lines[4])+round(self.amount/3.70,2))+'\n'
                    for x in lines:
                        file2.write(x)
                self.balance.set('%s' % (float(lines[3]) - self.amount))
                self.info2.set("Succes, "+'%s' % (round(self.amount/3.70, 2))+" usd added")
                
                
            
            

    
        
        

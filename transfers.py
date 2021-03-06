import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from logs import logs


class trans(tk.Toplevel):
    def __init__(self, master, nick):
        self.nick = nick
        self.path_customers = "C:\\Users\\Mateusz\\Desktop\\bank project\\customers\\"
        self.path_logs = "C:\\Users\\Mateusz\\Desktop\\bank project\\logs\\"
        self.logs = logs()
        tk.Toplevel.__init__(self, master)
        tk.Tk.configure(self, bg="white")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Transfer Menu")
        tk.Label(self, text = "DO you transfers", bg="blue", font = ("Algerian", 13)).pack()
        tk.Label(self, text="").pack()
        global tescik
        global tescik2
        self.tescik = tk.Entry(self, bg="yellow")
        self.tescik.insert(0, "Put user here")
        self.tescik.pack()
        tk.Label(self, text="").pack()
        self.tescik2 = tk.Entry(self, bg="yellow")
        self.tescik2.insert(0, "Put amount here")
        self.tescik2.pack()
        tk.Button(self, text="transfer", bg="green", command=self.send).pack()




    def send(self):      ##### Transfers script
        self.login_load = self.tescik.get()
        user_list = os.listdir(self.path_customers)
        if self.login_load not in user_list:
            messagebox.showerror("error", "User not found")
        else:
            self.amount_load = float(self.tescik2.get())
            balance=open(self.path_customers+self.nick, "r")
            balance2 = balance.readlines()
    ## First step checks if we have enough funds to make payement
            if float(balance2[3]) > self.amount_load:
                with open(self.path_customers+self.nick, "r") as file3:
                    lines2 = file3.readlines()
                with open(self.path_customers+self.nick, "w") as file3:
                    lines2[3]=str(float(lines2[3])-self.amount_load)+'\n'
                    for x in lines2:
                        file3.write(x)
                    file3.close
                    
    ## Second if funds are enough then script opens client's account and upates the balance after payement has been made
                with open(self.path_customers+self.login_load, "r") as file2:
                    lines = file2.readlines()
                with open(self.path_customers+self.login_load, "w") as file2:
                    lines[3]=str(float(lines[3])+self.amount_load)+'\n'
                    for x in lines:
                        file2.write(x)
                    file2.close
                    
                    var = ('%s' % float(self.amount_load)) ## transfers decimal into string so it can be displayed in messagebox
                    messagebox.showinfo("success", "You have transfered: "+var+" pln")
                    self.logs.transfer_logs(self.nick, self.login_load, self.amount_load)
                    

            else:
                balance.close
                messagebox.showerror("error", "No funds!")


import tkinter as tk 
import os
import string
import random
import time
import threading
import math

class token(tk.Tk):
    def __init__(self, master, name):
        self.name = name
        self.path_customers = 'customers\\'
        self.path_logs = "logs\\"
        tk.Toplevel.__init__(self, master)
        global conti
        global q,w,e,r,t,y
        q = random.choice(string.ascii_letters)
        w = random.choice(string.ascii_letters)
        e = random.choice(string.ascii_letters)
        r = random.choice(string.ascii_letters)
        t = random.randint(10,99)
        y = q+w+str(t)+e+r
        with open(self.path_customers+self.name, "r") as file:
            lines = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            lines[7] = y+"\n"
            for x in lines:
                file2.write(x)
        self.conti = tk.StringVar()
        self.bar_container = tk.StringVar()
        self.conti.set(y)
        tk.Tk.geometry(self, "350x250")
        tk.Tk.protocol(self,'WM_DELETE_WINDOW', self.x_disable)
        tk.Tk.title(self, "Token by Smiglo")
        tk.Label(self, text="Token", font=13).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, textvariable=self.conti).pack()
        self.main_container = tk.Label(self, textvariable=self.bar_container)
        self.main_container.pack()
        tk.Tk.after(self, 100, self.licz)
    
    def x_disable(self):
        pass
        


    def counter(self):
        q = random.choice(string.ascii_letters)
        w = random.choice(string.ascii_letters)
        e = random.choice(string.ascii_letters)
        r = random.choice(string.ascii_letters)
        t = random.randint(10,99)
        y = q+w+str(t)+e+r
        self.conti.set(y)
        with open(self.path_customers+self.name, "r") as file:
            lin = file.readlines()
        with open(self.path_customers+self.name, "w") as file2:
            lin[7] = y+"\n"
            for x in lin:
                file2.write(x)
           
        self.licz()
    
    
    def licz(self):
        for x in range(10000, 20000, 10000):
            tk.Tk.after(self, x, self.counter)
        self.main_container.config(bg="red")
        self.bar_thread = threading.Thread(target=self.token_bar, args=[10])
        self.bar_thread.start()

    def token_bar(self, bar):
        if bar > 0:
            self.bar_container.set(bar*"   ")
            time.sleep(1)
            self.token_bar(bar-1)

            

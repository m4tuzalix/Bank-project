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
        self.path_customers = "D:\\banki_projects\\customers\\"
        self.path_logs = "D:\\banki_projects\\\logs\\"
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
            file2.write(lines[0])
            file2.write(lines[1])
            file2.write(lines[2])
            file2.write(lines[3])
            file2.write(lines[4])
            file2.write(lines[5])
            file2.write(lines[6])
            lines[7] = y+"\n"
            file2.write(lines[7])
            file2.write(lines[8])
        self.conti = tk.StringVar()
        self.bar_container = tk.StringVar()
        self.conti.set(y)
        tk.Tk.geometry(self, "350x250")
        tk.Tk.title(self, "Token by Smiglo")
        tk.Label(self, text="Token", font=13).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, textvariable=self.conti).pack()
        self.main_container = tk.Label(self, textvariable=self.bar_container)
        self.main_container.pack()
        tk.Tk.after(self, 100, self.licz)
        


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
                file2.write(lin[0])
                file2.write(lin[1])
                file2.write(lin[2])
                file2.write(lin[3])
                file2.write(lin[4])
                file2.write(lin[5])
                file2.write(lin[6])
                lin[7] = y+"\n"
                file2.write(lin[7])
                file2.write(lin[8])
           
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

            

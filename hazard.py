import tkinter as tk 
import random
from tkinter import messagebox
from random import shuffle
import math
import time


class roulete(tk.Toplevel):
    def __init__(self, master, login):
        self.login = login
        tk.Toplevel.__init__(self, master)
        self.geometry('300x200')
        self.title('roulete')
        tk.Label(self, text="Choose game mode", font=('Arial', 12, 'bold')).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="50 percent chance", command=lambda: fifty(self, self.login)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="30 percent chance", command=lambda: thirty(self, self.login)).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="10 percent chance", command=lambda: ten(self, self.login)).pack()

class change():
    def __init__(self):
        pass
    def change_window(self, option, option2):
        self.option = option
        self.option2 = option2
        self.option.deiconify()
        self.option2.destroy()
        


class fifty(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.path_customers = "D:\\banki_projects\\customers\\"
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.number = random.randint(1,2)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])+round(self.bet_score/5)))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score/5)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])-self.bet_score))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('loose', "you lost")


class thirty(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.path_customers = "D:\\banki_projects\\customers\\"
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.number = random.randint(1,4)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])+round(self.bet_score/2)))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score/2)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])-self.bet_score))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('loose', "you lost")



class ten(tk.Tk):
    def __init__(self, parent, login):
        self.login = login
        self.path_customers = "D:\\banki_projects\\customers\\"
        self.t = change()
        self.parent = parent
        self.bet = tk.StringVar()
        tk.Tk.__init__(self)
        self.parent.withdraw()
        self.geometry("200x200")
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Spin", command=self.check).pack()
        tk.Button(self, text="change mode", command=lambda: self.t.change_window(self.parent, self)).pack(side=tk.BOTTOM)

    def check(self):
        self.number = random.randint(1,6)
        self.bet_score = float(self.entry.get())
        with open(self.path_customers+self.login, "r") as file:
            lines = file.readlines()
            if float(lines[3]) < self.bet_score:
                messagebox.showerror('error', 'no funds')
            else:
                if self.number == 1:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])+round(self.bet_score)))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('great','You won: '+str(round(self.bet_score)))
                else:
                    with open(self.path_customers+self.login, "w") as file2:
                        file2.write(lines[0])
                        file2.write(lines[1])
                        file2.write(lines[2])
                        file2.write("%s \n" % (float(lines[3])-self.bet_score))               
                        file2.write(lines[4])
                        file2.write(lines[5])
                        file2.write(lines[6])
                        file2.write(lines[7])
                        file2.write(lines[8])
                        messagebox.showinfo('loose', "you lost")


class lotto(tk.Toplevel):
    def __init__(self, master, login, counter=0):
        self.login = login
        self.counter = counter
        tk.Toplevel.__init__(self, master)
        self.geometry('350x300')
        tk.Label(self, text="Put 6 numbers").pack()
        self.entry1 = tk.Entry(self, bg='yellow')
        self.entry2 = tk.Entry(self, bg='yellow')
        self.entry3 = tk.Entry(self, bg='yellow')
        self.entry4 = tk.Entry(self, bg='yellow')
        self.entry5 = tk.Entry(self, bg='yellow')
        self.entry6 = tk.Entry(self, bg='yellow')
        self.entry1.place(x=60, y=50, width=30)
        self.entry2.place(x=100, y=50, width=30)
        self.entry3.place(x=140, y=50, width=30)
        self.entry4.place(x=180, y=50, width=30)
        self.entry5.place(x=220, y=50, width=30)
        self.entry6.place(x=260, y=50, width=30)
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="").pack()
        self.info = tk.Label(self, text="Numbers")
        self.info.pack()
        tk.Label(self, text="").pack()
        self.but = tk.Button(self, text="check", command=self.three_try)
        self.but.pack()
        self.info2 = tk.Label(self, text="You guess")
        self.info2.pack()

    def one_try(self):
        self.roll_numbers()
        if self.counter == 1:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.destroy()

    def three_try(self):
        self.roll_numbers()
        if self.counter == 3:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.destroy()

    def five_try(self):
        self.roll_numbers()
        if self.counter == 5:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.destroy()

    def ten_try(self):
        self.roll_numbers()
        if self.counter == 10:
            self.but.configure(state=tk.DISABLED)
            messagebox.showinfo('End','The end, buy more tickets to continue')
            self.destroy()

        

    def roll_numbers(self):
        self.info2.config(text="No score")
        lottery = list(range(1,49))
        numbers = []
        hit = []
        entries = [(self.entry1.get()), (self.entry2.get()), (self.entry3.get()), (self.entry4.get()), (self.entry5.get()), (self.entry6.get())]
        double_check = set(entries)  #### set returns value without duplicates

        if len(double_check) != len(entries): ### if duplicates exist, double_check length is lower then the original length of the list
            messagebox.showerror('error', 'Value cannot be doubled!')
        elif any(int(e)<0 for e in entries):
            messagebox.showerror('error', 'Value cannot be negative')
        elif any(int(e)==0 for e in entries):
            messagebox.showerror('error', 'Value cannot be zero')
        
    
        else:
            for i in range(6):
                shuffle(lottery) ## each time changes the list order
                x = lottery.pop() ## takes one random number         ### REPEATS 6 TIMES
                numbers.append(x) ## adds it to 'numbers' 
                for entry in entries:
                    if int(entry) == numbers[i]:
                        hit.append(int(entry))
                        self.info2.config(text='You have guessed: '+str(hit))
        self.info.config(text=str(numbers))
        if len(hit) >= 3:
            messagebox.showinfo('win', 'wygrales')
        self.counter = self.counter + 1
        
    
class lotto_los(tk.Toplevel):
    def __init__(self, master, login):
        self.login = login
        tk.Toplevel.__init__(self, master)
        self.geometry('350x300')
        tk.Label(self, text="Pick how many tries you want").pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="1 try", command=self.one).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="3 tries", command=self.three).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="5 tries", command=self.five).pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="10 tries", command=self.ten).pack()

    def one(self):
        self.t = lotto(self, self.login)
        self.b = self.t.but
        self.b.configure(command=self.t.one_try)
        self.t

    def three(self):
        self.t = lotto(self, self.login)
        self.b = self.t.but
        self.b.configure(command=self.t.three_try)
        self.t

    def five(self):
        self.t = lotto(self, self.login)
        self.b = self.t.but
        self.b.configure(command=self.t.five_try)
        self.t

    def ten(self):
        self.t = lotto(self, self.login)
        self.b = self.t.but
        self.b.configure(command=self.t.ten_try)
        self.t
        
        
    
    
    
    

            
        
        
                

        
            
        
            




        
    
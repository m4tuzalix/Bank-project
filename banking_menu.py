import tkinter as tk
import os
import random
from tkinter import messagebox
from tkinter import font as tkfont
from banking import bank
import string
from tokenik import token
from logs import logs
from admin import admins
import time
from credentials import back


class menu(tk.Tk):
    if os.path.isdir('customers') is False:
        os.mkdir('customers')
    elif os.path.isdir('admin') is False:
        os.mkdir('admin')
    elif os.path.isdir('logs') is False:
        os.mkdir('logs')
    elif os.path.isdir('bank_account') is False:
        os.mkdir('bank_account')
    else:
        pass

    def __init__(self):
        tk.Tk.__init__(self)
        self.logi = logs()
        self.path_customers = 'customers\\'
        self.path_logs = "logs\\"
        self.path_admin = "admin\\"
        tk.Tk.configure(self, bg="red")
        tk.Tk.geometry(self, "300x250")
        tk.Tk.title(self, "Smiglo Bank")
        tk.Label(self, text = "Welcome to Smiglo Bank", bg="pink", font = ("Algerian", 13)).pack()
        tk.Label(self, text = "").pack()
        self.but = tk.Button(self, text="Login", width=20, command=self.login)
        self.but.pack()
        tk.Label(self, text = "").pack()
        self.but2 = tk.Button(self, text="Register", width=20, command=self.register)
        self.but2.pack()
        tk.Label(self, text = "").pack()
        self.but3 = tk.Button(self, text="Forgot your credentials?", width=20, command=lambda:back(self, self.but3))
        self.but3.pack()

    # register system

    def register_user(self):
        self.but2.configure(state=tk.ACTIVE)
        self.check = self.choice.get()
        self.answer_check = self.answer.get()
        self.us = self.username.get()
        self.pas = self.password.get() 
        list_of_files = os.listdir(self.path_customers)
        if self.us in list_of_files:
            messagebox.showerror("exist", "User already exists!")
        else:
            if self.check == questions[0]:
                messagebox.showerror("error","You have not choosen your secret question!")
            elif not self.answer_check:
                messagebox.showerror("error","You have not provided your answer!")
            elif not self.us:
                messagebox.showerror("error","You have not provided your login!")
            elif not self.pas:
                messagebox.showerror("error","You have not provided your password!")
            else:
                c = str(random.randint(1000, 9000))
                self.cash = "0"
                self.username_info = self.username.get() #gets value from entry and sets it as the login
                self.password_info = self.password.get() #gets value from entry and sets it as the password
                self.code_info = c #random number rolled
                self.currency = "Account not opened"
                self.question = self.check
                self.answer = self.answer_check
                self.token = "No token"

                
                file=open(self.path_customers+self.username_info, "w")
                file2=open(self.path_logs+self.username_info+"_logs", "a")
                file.write(self.username_info+"\n") # <-------- All DATA IS SAVED HERE
                file.write(self.password_info+"\n")
                file.write(self.code_info+"\n")
                file.write(self.cash+"\n")
                file.write(self.currency+"\n")
                file.write(self.question+"\n")
                file.write(self.answer+"\n")
                file.write(self.token+"\n")
                file.write("OFFLINE")
                file.close

                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)

                tk.Label(self.screen1, text="Registration succes", fg="green", font=("calibri", 11)).pack()
                messagebox.showinfo("Success", "your security code is: "+self.code_info)
                self.screen1.destroy()

    # register window

    def register(self):
        self.but2.configure(state=tk.DISABLED)

        self.screen1 = tk.Frame(self.master)
        global questions
        global screen1
        global choice
        global answer

        questions = ["Choose your secret question", "Your mother name", "Your favourite food", "Your best friend name"]
        self.choice = tk.StringVar(self)
        self.answer = tk.StringVar(self)
        self.choice.set(questions[0])
        global screen1

        self.screen1 = tk.Toplevel(self)
        self.screen1.title("register")
        self.screen1.geometry("350x300")
        self.screen1.protocol('WM_DELETE_WINDOW', lambda:self.close(self.but2, self.screen1))

        global username
        global password
        global username_entry
        global password_entry

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.screen1, text ="Please enter details").pack()
        tk.Label(self.screen1, text ="").pack()

        tk.Label(self.screen1, text ="Username *").pack()
        self.username_entry = tk.Entry(self.screen1, textvariable=self.username)
        self.username_entry.pack()

        tk.Label(self.screen1, text ="Password *").pack()
        self.password_entry = tk.Entry(self.screen1, textvariable=self.password)
        self.password_entry.pack()

        self.option_menu = tk.OptionMenu(self.screen1, self.choice, *questions)
        self.option_menu.pack()

        self.question_entry = tk.Entry(self.screen1, textvariable=self.answer)
        self.question_entry.pack()

        tk.Label(self.screen1, text ="").pack()
        tk.Button(self.screen1, text="register", width=20, command=self.register_user).pack()

    

    #login system

    def login_verify(self):
        self.but.configure(state=tk.ACTIVE)

        self.login_details = self.username2.get()
        self.password_details = self.password2.get()
        self.security_code_details = self.security_code.get()
        self.username_entry2.delete(0, tk.END)
        self.password_entry2.delete(0, tk.END)
        self.security_code_entry.delete(0, tk.END)
        
        
        
        list_of_files = os.listdir(self.path_customers)
        list_of_admins = os.listdir(self.path_admin)
        if self.login_details in list_of_files:
            file1 = open(self.path_customers+self.login_details, "r")
            lines = file1.readlines()
            
            if '\n' in lines[8]:
                messagebox.showerror('error', 'account has been suspended')
            else:
        
                if lines[1] == self.password_details+"\n" and lines[2] == self.security_code_details+'\n':
                    self.logi.log_on(self.login_details) 
                    bank(self.login_details, self.password_details, self.security_code_details)
                elif lines[1] != self.password_details+'\n':
                    messagebox.showinfo("password error", "Password is incorrect")
                else:
                    messagebox.showinfo("code error", "Code is incorrect")
        elif self.login_details in list_of_admins:
            file2 = open(self.path_admin+self.login_details, "r")
            lines = file2.readlines()
            if lines[1] == self.password_details+"\n" and lines[2] == self.security_code_details+'\n':
                admins(self.login_details, self.password_details, self.security_code_details)
            else:
                messagebox.showerror('error', 'Not this time')
        else:
            messagebox.showinfo("user error", "User not found")

    #login window

    def login(self):
        self.but.configure(state=tk.DISABLED)

        global screen2
        self.screen2 = tk.Toplevel(self)
        self.screen2.title("login")
        self.screen2.geometry("300x250")
        self.screen2.protocol('WM_DELETE_WINDOW', lambda:self.close(self.but, self.screen2))

        global username2
        global password2
        global security_code
        global username_entry2
        global password_entry2
        global security_code_entry

        self.username2 = tk.StringVar()
        self.password2 = tk.StringVar()
        self.security_code = tk.StringVar()

        tk.Label(self.screen2, text ="Username *").pack()
        self.username_entry2 = tk.Entry(self.screen2, textvariable=self.username2)
        self.username_entry2.pack()

        tk.Label(self.screen2, text ="Password *").pack()
        self.password_entry2 = tk.Entry(self.screen2, textvariable=self.password2)
        self.password_entry2.pack()

        tk.Label(self.screen2, text ="Security Code *").pack()
        self.security_code_entry = tk.Entry(self.screen2, textvariable=self.security_code)
        self.security_code_entry.pack()

        tk.Label(self.screen2, text ="").pack()
        self.login_but = tk.Button(self.screen2, text="login", width=20, command=self.token_check)
        self.login_but.pack()
    
    def close(self, buto, wind):
        self.buto = buto
        self.wind = wind
        self.buto.configure(state=tk.ACTIVE)
        self.wind.destroy()
    
        
    
    def token_check(self):
        global var
        global log 
        list_of_files = os.listdir(self.path_customers)
        list_of_admins = os.listdir(self.path_admin)
        self.log = self.username2.get()
        self.var = tk.StringVar()
        if self.log in list_of_files:
            with open(self.path_customers+self.log, "r") as file:
                lines = file.readlines()
                if lines[8] == "ONLINE" or lines[8] == 'ONLINE'+'\n':
                    messagebox.showinfo("Online", "Account already online")
                else:
                    if lines[7] == "No token"+"\n":
                        self.login_verify()
                        self.screen2.destroy()
                    elif lines[7] != "No token"+"\n":
                        self.t = token(self, self.log)
                        self.screen2.geometry("350x300")
                        tk.Label(self.screen2, text="").pack()
                        tk.Label(self.screen2, text='Provide your token').pack()
                        self.token_entry = tk.Entry(self.screen2, textvariable=self.var)
                        self.token_entry.pack()
                        self.login_but.configure(command=self.token_verify)
        elif self.log not in list_of_files and self.log in list_of_admins:
            self.login_verify()
        else:
            messagebox.showerror('error','Account does not exist')
                    
    
    def token_verify(self):
        self.autho = self.var.get()
        with open(self.path_customers+self.log, "r") as file:
            lines = file.readlines()
            if not self.token_entry:
                messagebox.showerror('error', 'empty gap')
            if lines[7] == self.autho+"\n":
                self.t.destroy()
                self.token_entry.destroy()
                self.login_verify()
                self.screen2.destroy()
            else:
                messagebox.showerror("error", "wrong token")

    
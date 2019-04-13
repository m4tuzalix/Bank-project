import tkinter as tk 
import os
from tkinter import messagebox


class admins(tk.Tk):
    def __init__(self, login, password, code):
        self.login = login
        self.password = password
        self.code = code
        self.path_admin = "D:\\banki_projects\\admin\\"
        tk.Tk.__init__(self)
        with open("D:\\banki_projects\\admin\\"+self.login, "r") as file:
            lines = file.readlines()
        with open("D:\\banki_projects\\admin\\"+self.login, "w") as file2:
            file2.write(lines[0])
            file2.write(lines[1])
            file2.write(lines[2])
            lines[3] = 'ONLINE'
            file2.write(lines[3])
        tk.Tk.protocol(self,'WM_DELETE_WINDOW', self.offline_switch)
        tk.Tk.geometry(self,"400x300")
        tk.Tk.title(self, "Admin menu")
        tk.Label(self, text='Open user details').pack()
        self.info = tk.Entry(self, bg="yellow")
        self.info.pack()
        tk.Button(self, text='proceed', command=self.get_user).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Delete user account").pack()
        self.info2 = tk.Entry(self, bg="yellow")
        self.info2.pack()
        tk.Button(self, text='proceed', command=self.delete).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Suspend user account").pack()
        self.info3 = tk.Entry(self, bg="yellow")
        self.info3.pack()
        tk.Button(self, text='proceed', command=self.ban).pack()
    
    def offline_switch(self):
        with open(self.path_admin+self.login, "r") as file:
            lines = file.readlines()
        with open(self.path_admin+self.login, "w") as file2:
            file2.write(lines[0])
            file2.write(lines[1])
            file2.write(lines[2])
            lines[3] = 'OFFLINE'
            file2.write(lines[3])
            self.destroy()
    
    def get_user(self):
        self.check = self.info.get()
        list_of_users = os.listdir('D:/banki_projects/customers')

        if self.check in list_of_users:
            self.screen = tk.Toplevel(self)
            self.screen.geometry('450x400')
            self.text = tk.Text(self.screen)
            with open('D:\\banki_projects\\customers\\'+self.check, 'r') as file:
                lines = file.readlines()
                tk.Label(self.screen, text="login:      "+lines[0]).pack()
                tk.Label(self.screen, text="password:       "+lines[1]).pack()
                tk.Label(self.screen, text="security code:      "+lines[2]).pack()
                tk.Label(self.screen, text="Account balance:        "+lines[3]).pack()
                tk.Label(self.screen, text="Currency account:       "+lines[4]).pack()
                tk.Label(self.screen, text="Secret question:        "+lines[5]).pack()
                tk.Label(self.screen, text="Secret answer:      "+lines[6]).pack()
                tk.Label(self.screen, text="Token status:       "+lines[7]).pack()
                tk.Label(self.screen, text="online status:      "+lines[8]).pack()
                if "\n" in lines[8]:
                  tk.Label(self.screen, text="ACCOUNT SUSPENDED", fg="red").pack()  
        else:
            messagebox.showerror('error', 'No user found in database')

    def delete(self):
        self.check = self.info2.get()
        list_of_users = os.listdir('D:/banki_projects/customers')
        if self.check in list_of_users:
            self.choice = messagebox.askquestion('delete', 'Do you want to delete '+self.check+" ?")
            if self.choice == 'yes':
                os.remove("D:/banki_projects/customers/"+self.check)
            else:
                pass
        else:
            messagebox.showerror('error', 'No user in database')

    def ban(self):
        self.check = self.info3.get()
        list_of_users = os.listdir('D:/banki_projects/customers')
        if self.check in list_of_users:
            self.choice2 = messagebox.askquestion('ban',"Do you want to suspend "+self.check)
            if self.choice2 == 'yes':
                with open("D:\\banki_projects\\customers\\"+self.check, 'r') as file:
                    lines = file.readlines()
                    if "\n" in lines[8]:
                        messagebox.showerror('error', 'Account has already been suspended')
                    else:
                        with open("D:\\banki_projects\\customers\\"+self.check, 'a') as file2:
                            file2.write("\n"+'BAN')
        else:
            messagebox.showerror('error', 'No user in database')

    def chat_start(self):
        messagebox.askquestion("chat", 'Start chat ?')


class admin_chat(tk.Toplevel):
    def __init__(self, master, login, haslo, kod):
        self.login = login
        self.haslo = haslo
        self.kod = kod
        tk.Toplevel.__init__(self, master)
        self.geometry("300x200")
        self.title("Admin chat")
        tk.Label(self, text="Check on-line Admins").pack()
        self.action = tk.Button(self, text="Go", command=self.who_is_online)
        self.action.pack()
        self.info = tk.Label(self, text='')
        self.info.pack()
        


    def who_is_online(self):
        for files in os.listdir("D:/banki_projects/admin/"):
            with open("D:/banki_projects/admin/"+files, "r") as file:
                lines = file.readlines()
        if lines[3] == "ONLINE":
            self.info.config(text='Admin is online: '+files, fg="green")
            file.close
        else:
            self.info.config(text="admin is offline", fg="red")

    

    




  

            
            
            
                
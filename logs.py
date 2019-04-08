from datetime import datetime
class logs():
    def __init__(self):
        self.t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.path_customers = "D:\\banki_projects\\customers\\"
        self.path_logs = "D:\\banki_projects\\\logs\\"
        pass
    
    def depo_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Deposit: "+str(self.value)+" pln"+"\n")
        file.close

    def depo_usd_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Deposit: "+str(self.value)+" usd"+"\n")
        file.close

    def with_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Withdraw: "+str(self.value)+" pln"+"\n") 
        file.close

    def with_usd_logs(self, name, value):
        self.name = name
        self.value = value
        file= open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Withdraw: "+str(self.value)+" usd"+"\n") 
        file.close

    def transfer_logs(self, name, customer, value):
        self.name = name
        self.customer = customer
        self.value = value
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Transfered "+str(self.value)+".pln to"+" "+str(self.customer)+"\n")
        file.close
        file = open(self.path_logs+self.customer+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Received transfer from "+str(self.name)+" "+str(self.value)+".pln"+"\n")
        file.close

    def transfer_usd_logs(self, name, customer, value):
        self.name = name
        self.customer = customer
        self.value = value
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Currency transfer for "+str(self.value)+" usd to"+" "+str(self.customer)+"\n")
        file.close
        file = open(self.path_logs+self.customer+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Received currency transfer from "+str(self.name)+" "+str(self.value)+" usd"+"\n")
        file.close

    def token_logs_on(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Token activated"+"\n")

    def token_logs_off(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Token deactivated"+"\n")

    def currency_logs_on(self, name):
        self.name = name
        file = open(self.path_logs+self.name+"_logs", "a")
        file.write("<"+self.t+">"+" "+"Currency account activated"+"\n")

    def log_on(self, name):
        self.name = name
        file=open(self.path_customers+self.name, "r")
        lines = file.readlines()
        if lines[8] == "OFFLINE" or lines[8] == "OFFLINE"+"\n" :
            file = open(self.path_logs+self.name+"_logs", "a")
            file.write("<"+self.t+">"+" "+"Logged in"+"\n")
        else:
            file = open(self.path_logs+self.name+"_logs", "a")
            file.write("<"+self.t+">"+" "+"Logged out"+"\n")
        


           
        
# Bank-project
Banking application with many useful features. Application allows user to create account which is saved as indenpendent file. Each file contatins 9 lines of text which are responsisible for different things. Registration proccess requires login, password, secret question and secret answer. Additionaly each account has security code, automatically generated if user has registered account succesfully.

In short application contains:

- deposit system
- withdraw system
- transfer system (send money to other users)
- currency account system
- currency transfers (equal system to normal transfer)
- adding funds from usual account to currency account. The current currency is USD and usual is PLN. My application USD rate has been set to 3.80
- token system (activation or deactivation) If token is active, indenpendent window pops up after each positive log-in process before leting to get into bank account. Window contains random code made from asci letters and numbers which changes after each 10 seconds. To get into account, user must rewrite the code correctly.
- logs system - All actions performed on account as log-in, log-out, money operations etc. are saved in separate folder, in spearate file related with username. Each action is written in separate line with exact date and time next to it.

- admin system - System with admin gui to control users' accounts. Currently admin can display all data stored in common user file, line by line. Admin can delete accounts or suspend them. This system is going to be rebuilded yet in order to add more options. Admin accounts are created manually and stored in special folder.

- admin chat system - Currently i'm working on it. System which allows user to check if any admin is online and if so, start the chat between user and admin account.


I've been working on this application since one month. I'm beginner with short experiance with started in September of 2018. I've fallen in love in programming, especially in python and I spend most of my time doing it. I'm open for any critics or advices or maybe some further ideas regarding this application. 

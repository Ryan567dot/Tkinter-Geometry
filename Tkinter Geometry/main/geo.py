from tkinter import *

class LoginApp:
    username = ["Ryan","Zaheen","Tahmid","Atiya"]
    password = [1234,2345,3456,4567]
    
    def login(self):
        self.window = Tk()
        self.window.title("Login App")
        self.window.geometry("400x500")
        
        self.UserLabel = Label{self.window,text="Enter Username",font=("Alice",13"bold"),bg="lightblue",fg="black"}
        self.UserLabel.pack()
        
        self.UserEntry = Entry(self.window,font=("Alice",13,"bold"))
        self.UserEntry.pack()
        
        self.PassEntry = Entry(self.window,font=("Alice",13,"bold"))
        self.PassEntry.pack()
        
        Label(self.window,bg="lightblue").pack()
        
        def ConfirmLogin():
            myusername = self.UserEntry.get()
            mypassword = self.PassEntry.get()
            
            if myusername in username:
                verify = username.index(username)
                if mypassword == password[verify]:
                    print("Login Successful")
            else: print("Wrong Passoword")
        else: print("Username not foun!")
            
        self.Confirm = Button(self.window,text="Login",font=("Alice",13,"bold"),bg="lightblue",fg="white",command=ConfirmLogin)
        self.Confirm.pack()
        
        
        
        
        
self.window.mainloop()
mylogin = LoginApp()
mylogin.login()

print(username.index("Ryan"))
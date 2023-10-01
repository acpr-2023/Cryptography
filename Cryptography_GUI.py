
# Activity 4 | Angel Cyrhen Recaña

from tkinter import *
from tkinter import messagebox

class cryp(Frame):
    

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Cryptography")
        self.pack()
        self.Lbl1= Label(self,text = " Choose SENDER to encrypt a message and RECEIVER to decrypt a message", font = ("Courier New (Courier)", 10,"underline"), fg = "dark slate gray")
        self.Lbl1.pack(pady = 20)

        self.Lbl1= Label(self,text = "MESSAGE", font = ("Helvitica", 20,'bold'), fg = "dark slate gray")
        self.Lbl1.pack(pady = 20)

        
        self.Msg= Entry(self, font = ("Helvitica", 15), fg= "dark slate gray", background = "light steel blue") 
        self.Msg.pack(pady = 20)

        self.Lbl1= Label(self,text = "PASSWORD", font = ("Helvitica", 20,'bold'), fg = "dark slate gray")
        self.Lbl1.pack(pady = 20)

        self.passVar= StringVar()
        self.passVarEntry = Entry(self, font = ("Helvitica", 15), textvariable = self.passVar, fg= "dark slate gray", background = "light steel blue" )
        self.passVarEntry.pack(pady = 20)

        self.Lbl1= Label(self,text = "[ WHO ARE YOU? ]", font = ("Courier New (Courier)", 18), fg = "dark slate gray")
        self.Lbl1.pack(pady = 20)

        self.Btn = Button(self, text = " Sender ", font = ("Helvitica", 18), command = self.encrypt, fg= "antique white", background = "dark slate gray" ) #Button widget
        self.Btn.pack(pady = 20)

        self.Btn = Button(self, text = " Receiver", font = ("Helvitica", 18), command = self.decrypt, fg= "antique white", background = "dark slate gray") #Button widget
        self.Btn.pack(pady = 20)

    def encrypt(self):
       
            msg = self.Msg.get()
            key = (self.passVarEntry.get())
            emsg= ""

            for ch in msg:
                if ch == " ":
                    emsg += " "
                else:
                    emsg+= chr(ord(ch) + len(key))
            
            messagebox.showinfo("WELCOME SENDER", f" ENCRYPTED MESSAGE:\n {emsg}")

    def decrypt(self):
        
            emsg = self.Msg.get()
            key = (self.passVarEntry.get())
            msg= ""

            for ch in emsg:
                if ch == " ":
                    msg += " "
                else:
                    msg+= chr(ord(ch) - len(key))
        
            
            messagebox.showinfo("WELCOME RECEIVER", f"DECRYPTED MESSAGE: \n {msg}")

        
def main():

    cryp().mainloop()
main()
from tkinter import *
import random

root=Tk()
root.title("random word")
root.geometry("400x400")

label1=Label(root)

def Genword():
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    r1=random.randint(0,25)
    r2=random.randint(0,25)
    r3=random.randint(0,25)
    r4=random.randint(0,25)
    r5=random.randint(0,25)
    
    ar1=alpha[r1]
    ar2=alpha[r2]
    ar3=alpha[r3]
    ar4=alpha[r4]
    ar5=alpha[r5]
    
    label1["text"]=ar1+ar2+ar3+ar4+ar5

btn1 = Button(root, text="Generate random word  ", command = Genword)
btn1.place(relx=0.5,rely=0.5,anchor = CENTER)
label1.place(relx=0.5,rely=0.6,anchor = CENTER)

root.mainloop()
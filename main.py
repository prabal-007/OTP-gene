from tkinter import *
import math, random

def getOTP():
    digits = '0123456789'
    otp = ''
    for i in range(int(r1var.get())):
        otp += digits[math.floor(random.random() * 10)]
    otpvar.set(otp)

root = Tk()
root.title('OTP Generator')
root.geometry('240x240')
frm1 = Frame(root)
r1var = StringVar()
r1var.set(4)
Label(frm1,text='Size',font='arial 9 bold').pack(side=LEFT,padx=8)
r1 =Radiobutton(frm1,text='Four', variable=r1var, value=4,padx='5',bg='orange').pack(side=LEFT)
r2 =Radiobutton(frm1,text='Six', variable=r1var, value=6,padx='5',bg='orange').pack(side=LEFT)
frm1.pack(pady=20)
# frm2 = Frame(root)
Button(root,text='get OTP',font='arial 8 bold', command=getOTP,activebackground='yellow').pack(padx=5)
# frm2.pack()
otpvar = IntVar()
Entry(root,textvariable=otpvar,font='arial 10 bold', width='18').pack(pady=10)
Button(root,text='Exit',font='arial 8 bold',command=exit,activebackground='red').pack(padx=5)
root.mainloop()

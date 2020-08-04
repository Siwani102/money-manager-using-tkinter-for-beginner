from tkinter import *
import tkinter.messagebox
messagebox.showinfo("Welcome","Welcome to money manager\nEnter you username and password\nto login.")
amount=10000
total=""
def Submit():
    if(e1.get()=='money manager'):
        print(e1.get())
        if(e2.get()=='1234'):
            print(e2.get())
            login()
        else:
            print("Wrong password")
    else:
        print("wrong username")
def quit():
    root.destroy()

root=Tk()

l1=Label(root,text="MONEY MANAGER",fg="violet",font="elephant")
l1.grid(row=0)
l2=Label(root,text="Username",font="bold")
l2.grid(row=1)
e1=Entry(root)
e1.grid(row=1,column=1)
l2=Label(root,text="Password",font="bold")
l2.grid(row=1,column=2)
e2=Entry(root)
e2.grid(row=1,column=3)
b2=Button(root,text="Quit",fg="black",bg="red",font="bold",command=quit)
b2.grid(row=2,column=2)

def login():
    def Quit():
        var.destroy()
    def done():
        var.destroy()    

    def deposit():
        
        global amount
        global total
        total=int(e5.get())+amount
        
        
        with open ("program.txt","a") as f:
            f.write("\namount to be added:")
            f.write(e5.get())
            f.write("\ncurrent balance is:")
            f.write(str(total))
    def click():
         Lb.insert(1,"1.electricity Pay Rs.2000")
         Lb.insert(2,"2.Rent Pay Rs.5000")
         Lb.insert(3,"3.food Pay Rs.3000")
         Lb.insert(4,"4.Entertainment Pay Rs.3500")
         Lb.grid(row=3,column=1)
         b5.grid(row=3,column=2)
            
    def selection():
        a=Lb.curselection()
        print(a)
        for i in a:
            print(Lb.get(i))
        global total    
        if 0 in a:
            messagebox.showinfo("Bill","electricity bill is sucessfully paid")
            b=total-2000
            print("current balance:",b)
            total=b
            
            with open("program.txt","a") as f:
                f.write("\namount to be deducted in Elecricity:2000")
                f.write("\nNow the current balance is:")
                f.write(str(total))
        elif 1 in a:
            messagebox.showinfo("Bill","rent is sucessfully paid")
            b=total-5000
            print("current balance:",b)
            total=b
           
            with open("program.txt","a") as f:
                f.write("\namount to be deducted in Rent:5000")
                f.write("\nNow the current balance is:")
                f.write(str(total))  
    
        elif 2 in a:
            messagebox.showinfo("Bill","food bill is sucessfully paid")
            b=total-3000
            print("current balance:",b)
            total=b
           
            with open("program.txt","a") as f:
                f.write("\namount to be deducted in Food:3000")
                f.write("\nNow the current balance is:")
                f.write(str(total))
        else:
            messagebox.showinfo("Bill","entertainment bill is sucessfully paid") 
            b=total-3500
            print("current balance:",b)
            total=b
           
            with open("program.txt","a") as f:
                f.write("namount to be deducted in Entertainment:3500")
                f.write("\nNow the current balance is:")
                f.write(str(total))
   
    var=Toplevel()
    
   
    
        
   
    s1=Label(var,text="userpin:",fg="violet",font="bold")
    e1=Entry(var)
    e1.grid(row=0,column=1)
    s1.grid(row=0,column=0)
    e1.insert(10,"webtech")
    s2=Label(var,text="Current\nBalance:",font="bold")
    s2.grid(row=0,column=2)
    e2=Entry(var)
    e2.grid(row=0,column=3)
    e2.insert(10,"10000")
    s3=Label(var,text="Add\nAmount",font="bold")
    e5=Entry(var)
    s3.grid(row=2)
    e5.grid(row=2,column=1)
    with open ("program.txt","w") as f:
        f.write("username=webtech")
        f.write("\npassword=1234")
        f.write("\ncurrent balance=10,000")
        
        
    b3=Button(var,text="Logout",fg="black",font="bold",bg="red",width="9",command=Quit)
    b3.grid(row=1,column=3)
    b4=Button(var,text="Deposit",fg="black",font="bold",bg="red",width="9",command=deposit)
   
    b4.grid(row=2,column=2)

 
    Lb=Listbox(var,selectmode=EXTENDED,width="35")
    b5=Button(var,text="PAY",fg="yellow",bg="red",font="algerian",command=selection)
    b6=Button(var,text="to pay\nbills\nclick\nhere",fg="black",bg="light blue",width="9",height="5",command=click)
    b6.grid(row=3)

    b7=Button(var,text="All Done",font="bold",fg="black",bg="light green",command=done)
    b7.grid(row=4,column=2)
    
    

    
    var.mainloop()

b1=Button(root,text="submit",fg="white",bg="green",font="bold",command=Submit)
b1.grid(row=2,column=1)
root.mainloop()
    
    

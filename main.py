from distutils import command
from optparse import Values
from tkinter import *
from tkinter import messagebox
from turtle import width
import dao.taskdao as task

def todo():
    global home,ll,list_v
   
    home = Tk()
    home.title("todo list")    
    home.geometry("350x350")


    
    list_v = StringVar(value=task.gettaskonly())    
    Label(home,text="To-Do-List",font="arial 10").place(x=40,y=20)

    Label(home,text="Enter Task Name :",font="arial 10").place(x=40,y=80)
    
    global taskname
    taskname = StringVar(home)
    Entry(home,width="14",font="aria",textvariable=taskname).place(x=40,y=110)
    
   
    
    def add():
        task.savetask(taskname.get())
        ll.delete(0,END)
        for itm in task.showalltask():
            ll.insert(ACTIVE,itm[1])
    def deleteall():
        task.deleteall()
        ll.delete(0,END)
    def delete():
        task.deletebytaskname(ll.get(ACTIVE))    
        ll.delete(0,END)
        for itm in task.showalltask():
            ll.insert(ACTIVE,itm[1])
    def exit():
        home.destroy()
    ll=Listbox(home,listvariable=list_v,height=11,selectmode=SINGLE)
    ll.place(x=180,y=80)
    
    Button(home,text="Add Task" ,width="15",bd=1,relief="ridge",command=add).place(x=40,y=140)
    Button(home,text="Delete",width="15",bd=1,relief="ridge",command=delete).place(x=40,y=170)
    Button(home,text="Delete All",width="15",bd=1,relief="ridge",command=deleteall).place(x=40,y=200)
    Button(home,text="Exit",width="15",bd=1,relief="ridge",command=exit).place(x=40,y=230)


     
    
    home.mainloop()
    
todo()
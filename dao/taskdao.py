import sqlite3
from turtle import update

from numpy import save

con = sqlite3.connect("task.db")


def createtable():
    con.execute(
        "create table if not exists task(tid INTEGER PRIMARY KEY AUTOINCREMENT,tname text)")
    con.commit()


def savetask(tname):
    con.execute("insert into task(tname) values('"+tname+"')")
    con.commit()


def updatetask(tid, tname):
    data = (tname, tid)
    con.execute("update task set tname=? where tid=?", data)
    con.commit()


def delete(tid):
    con.execute("delete from task where tid='"+tid+"'")


def deleteall():
    con.execute("delete from task where 1=1")
    con.commit()


def showtask(tid):
    cur = con.execute("select * from task where tid='"+tid+"'")
    data = cur.fetchall()
    return data

def showalltask():
    cur = con.execute("select * from task")
    data = cur.fetchall()
    return data
def gettaskonly():
    task = []
    
    for i in showalltask():
        task.append(i[1])
                
    return task
def gettidonly():
    tid = []
    
    for i in showalltask():
        task.append(i[0])
    return tid
def deletebytaskname(tname):
    con.execute("delete from task where tname='"+tname+"'")
    con.commit()
    

createtable()
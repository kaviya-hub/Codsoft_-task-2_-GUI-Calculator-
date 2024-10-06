import tkinter
from tkinter import *

node=Tk()
node.title("Calculator")
node.geometry("570x600+100+200")
node.resizable(False,False)
node.configure(bg="#17161b")

calculation =""


def calculate():
    global calculation
    result=""
    if calculation !="":
        try:
            result= eval(calculation)
        except:
            result="SYNTAX ERROR"
            calculation=""
    label_result.config(text=result)

def clear():
    global calculation
    calculation=""
    label_result.config(text=calculation)


def show(value):
    global calculation
    calculation+=value
    label_result.config(text=calculation)
     

label_result=Label(node,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(node,text="C", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#ff0000",bg="#2a2d36",command=lambda: clear()).place(x=10,y=100)
Button(node,text="/", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#008000",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
Button(node,text="%", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#008000",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
Button(node,text="*", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#008000",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)

Button(node,text="7", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
Button(node,text="8", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(node,text="9", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200),
Button(node,text="-", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#008000",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=200)

Button(node,text="4", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
Button(node,text="5", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(node,text="6", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(node,text="+", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#008000",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=300)

Button(node,text="1", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
Button(node,text="2", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(node,text="3", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(node,text="0", width=11, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)


Button(node,text=".", width=5, height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
Button(node,text="=", width=5, height=3,font=("arial",30,"bold"), bd=1, fg="#2a2d36",bg="#008000",command=lambda: calculate()).place(x=430,y=400)
node.mainloop()

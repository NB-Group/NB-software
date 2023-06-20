import tkinter as tk
from tkinter import *
import os
import tkinter.messagebox
import subprocess
from pynput.keyboard import *
import time

k = Controller()


def new_password(user, p):
    os.system("start")
    time.sleep(0.5)
    k.type(f"net user {user} {p}\r")
    time.sleep(0.5)
    k.type("exit\r")
    time.sleep(0.5)


def run_cmd(text):
    f = subprocess.Popen(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    a = ""
    while True:
        result = f.stdout.readline()
        if result != b"":
            try:
                a += result.decode("gbk")
            except :
                a += result.decode("utf-8")
        else:
            break
    return a


def password():
    if entry2.get() == entry3.get():
        if not entry1.get() in run_cmd("net user"):
            tkinter.messagebox.showerror("错误", "没有这个用户!")
            return
        new_password(entry1.get(), entry2.get())
        tkinter.messagebox.showinfo("提示", "更改完毕！")
    else:
        tkinter.messagebox.showerror("错误", "密码和确认密码不一样！")


def get_user():
    entry.delete(0.0, END)
    text = run_cmd("net user") + "一般为Administrator"
    text = text.replace("------------------------------", "", 1)
    entry.insert(0.0, text)


if __name__ == "__main__":
    app = tk.Tk()
    app.title("黑客工具·破译密码")
    app.geometry('500x450')
    app.minsize(500, 450)
    labelframe = LabelFrame(width=400, height=200, text="获取用户")  # 框架，以下对象都是对于labelframe中添加的
    labelframe.grid(column=0, row=0, padx=10, pady=10)
    entry = tk.Text(labelframe, width=50, height=10)
    entry.place(x=10, y=10)
    button = tk.Button(labelframe, text='获取用户名', command=get_user)
    button.place(x=300, y=140)

    password_ = LabelFrame(width=300, height=100, text="更改密码(密码栏填写的是要更改的密码)")  # 框架，以下对象都是对于labelframe中添加的
    password_.place(x=10, y=240)
    label = Label(password_, text='''用户名:''')
    label.place(x=5, y=9)
    entry1 = tk.Entry(password_, width=20)
    entry1.place(x=60, y=10)
    label = Label(password_, text='''密码:''')
    label.place(x=5, y=29)
    entry2 = tk.Entry(password_, width=20)
    entry2.place(x=61, y=30)
    label = Label(password_, text='''确认密码:''')
    label.place(x=5, y=49)
    entry3 = tk.Entry(password_, width=20)
    entry3.place(x=61, y=50)
    button = tk.Button(password_, text='更改密码', command=password)
    button.place(x=200, y=50)

    app.mainloop()

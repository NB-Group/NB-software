from pynput.mouse import Button as Bu
from pynput.mouse import Controller as Ctrl1
from time import sleep
from tkinter.messagebox import showinfo
from ttkbootstrap import Combobox
from tkinter import Tk, Label, Entry, Button
from keyboard import wait

mouse = Ctrl1()


def start():
    showinfo("提示", "准备连点,按下k键开始。")
    wait('k')
    if cli.get() == "左键连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.left)
            sleep(1 / int(entry.get()))
    elif cli.get() == "左键双击连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.left, 2)
            sleep(1 / int(entry.get()))
    elif cli.get() == "右键连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.right)
            sleep(1 / int(entry.get()))
    elif cli.get() == "右键双击连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.right, 2)
            sleep(1 / int(entry.get()))
    showinfo("提示", "连点结束。")


if __name__ == "__main__":
    app = Tk()
    app.title("连点器")
    app.geometry('250x100')

    label = Label(app, text='''连点按键:''')
    label.place(x=8, y=10)
    label1 = Label(app, text='''连点总数:''')
    label1.place(x=8, y=30)
    label1 = Label(app, text='''频率(秒/次):''')
    label1.place(x=8, y=50)
    cli = Combobox(app)  # 初始化
    cli["values"] = ("左键连点", "左键双击连点", "右键连点", "右键双击连点")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=80, y=2)

    entry1 = Entry(app, width=20)
    entry1.place(x=80, y=30)
    entry = Entry(app, width=20)
    entry.place(x=80, y=50)

    button = Button(app, text='开始连点', command=start)
    button.place(x=80, y=70)
    app.mainloop()

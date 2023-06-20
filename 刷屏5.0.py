import time
from pynput.keyboard import Key, Controller
import tkinter.messagebox
from tkinter import simpledialog
from ttkbootstrap import *


def start():
    ci = simpledialog.askstring(title='请输入', prompt='请问您想刷几个')
    try:
        ci = int(ci)
    except:
        tkinter.messagebox.showinfo('提示', "请不要乱输")
    shua = simpledialog.askstring(title='请输入', prompt='请问您要刷啥')
    su = 1
    if tkinter.messagebox.askokcancel('提问', '需要指定刷屏速度吗'):
        try:
            su //= int(simpledialog.askstring(title='请输入', prompt='请输入您的刷屏速度(次每秒)'))
        except:
            tkinter.messagebox.showinfo('提示', "请不要乱输")
    for i in range(ci):
        k.type(shua + "\n")  # 先复制
        time.sleep(su)


if __name__ == "__main__":
    k = Controller()
    style = Style()
    style = Style(theme='superhero')

    app = style.master

    app.title("牛逼录屏")
    app.resizable(False, False)
    app.geometry('400x200')
    app.minsize(400, 200)
    app.maxsize(400, 200)
    button1 = tk.Button(app, text='开始刷屏', command=start)
    button1.place(x=50, y=110)
    label = Label(app, text='''文件名:''')
    label.place(x=8, y=10)
    label1 = Label(app, text='''帧率:''')
    label1.place(x=11, y=30)
    label1 = Label(app, text='''编码:''')
    label1.place(x=11, y=55)
    label1 = Label(app, text='''路径:''')
    label1.place(x=11, y=80)
    cli = ttk.Combobox(app)  # 初始化
    cli["values"] = ("XVID", "DIVX")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=50, y=50)
    entry1 = Entry(app, width=24)
    entry1.place(x=50, y=10)
    entry = Entry(app, width=24)
    entry.place(x=50, y=30)
    entry2 = Entry(app, width=24)
    entry2.place(x=50, y=80)
    app.mainloop()

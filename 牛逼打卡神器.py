from tkinter import *
import tkinter.filedialog
from tkinter.simpledialog import askstring
import tkinter.messagebox
from ttkbootstrap import ttk
from pynput.mouse import Button as Bu
import keyboard
import pynput
import time
import threading

Note = None
feil = ""
ctr2 = pynput.keyboard.Controller()
ctr = pynput.mouse.Controller()


def run(f):
    app.geometry('400x200+9999+9999')
    Note = open(f, mode='r')
    i = Note.read()
    try:
        h = i.split("|")[1]
    except:
        ling = i
        i = "|"
        i += ling
        h = i.split("|")[1]
    i = i.split("|")[0]
    i = i.split(" ")
    h = h.split(" ")

    def hhh():

        for n in range(1, len(h), 2):
            if h[n] == "" or h[n] == "right":
                continue
            if float(h[n - 1]) <= 0:
                pass
            else:
                time.sleep(float(h[n - 1]))
            if h[n] == "shift":
                ctr2.type([pynput.keyboard.Key.shift])
                continue
            try:
                if h[n] + h[n + 1] == "capslock":
                    ctr2.type([pynput.keyboard.Key.caps_lock])
                    continue
            except:
                pass
            if h[n] == "enter":
                ctr2.type([pynput.keyboard.Key.enter])
                continue
            if h[n] == "tab":
                ctr2.type([pynput.keyboard.Key.tab])
                continue
            if h[n] == "backspace":
                ctr2.type([pynput.keyboard.Key.backspace])
                continue
            if h[n] == "ctrl":
                ctr2.type([pynput.keyboard.Key.ctrl])
                continue
            if h[n] == "alt":
                ctr2.type([pynput.keyboard.Key.alt])
                continue
            if h[n] == "space":
                ctr2.type(" ")
                continue
            if h[n] == "  ":
                continue
            ctr2.type(h[n])

    t = threading.Thread(target=hhh, daemon=True)
    t.start()

    for n in range(0, len(i) - 1, 4):
        try:
            time.sleep(float(i[n + 3]))
        except:
            pass
        ctr.position = (i[n], i[n + 1])
        if i[n + 2] == "左键":
            ctr.click(pynput.mouse.Button.left)
        if i[n + 2] == "右键":
            ctr.click(pynput.mouse.Button.right)
        app.geometry('400x200+100+100')


def f():
    global feil
    if cli.get() == "录制":
        feil = tkinter.filedialog.askdirectory()
        entry2.delete(0, END)
        if feil == "":
            tkinter.messagebox.showerror('错误', '请选择正确的路径')
            return
        entry2.insert(INSERT, feil)
    else:
        feil = tkinter.filedialog.askopenfilenames()[0]
        entry2.delete(0, END)
        if feil == "":
            tkinter.messagebox.showerror('错误', '请选择正确的路径')
            return
        entry2.insert(INSERT, feil)


b = "|"
t_b = time.time()


def jiuji(f):
    a = ""
    t = time.time()
    app.geometry('400x200+9999+9999')
    tkinter.messagebox.showinfo("提示", "录制开始,按下鼠标中键(鼠标滚轮)结束")

    def test(x):
        global t_b
        global b
        x = str(x)
        if not "up" in x:
            x = x[14:-5]
            b += str(time.time() - t_b)
            b += " "
            b += x
            t_b = time.time()

    keyboard.hook(test)
    with pynput.mouse.Events() as event:
        for i in event:
            # 迭代用法。

            if isinstance(i, pynput.mouse.Events.Click):
                # 鼠标点击事件。

                # 这个i.button就是上文所说的“鼠标按键”中的一个，用is语句判断即可。
                if i.button == Bu.middle:
                    keyboard.unhook(test)
                    Note = open(f + ".fct", mode='w')
                    Note.write(a + b)
                    app.geometry('400x200+100+100')
                    return
                if i.button == Bu.left and i.pressed:
                    a += str(i.x) + " " + str(i.y) + " " + "左键" + " " + str(time.time() - t) + " "
                if i.button == Bu.right and i.pressed:
                    a += str(i.x) + " " + str(i.y) + " " + "右键" + " " + str(time.time() - t) + " "
                t = time.time()

        i = event.get(1)


def start():
    if cli.get() == "运行":
        run(feil)
    else:
        jiuji(feil + askstring(title='请输入', prompt='请输入文件名(不包括拓展名)'))
        tkinter.messagebox.showinfo("提示", "录制结束！")


app = Tk()
app.title("录制器")
app.geometry('400x200')

entry2 = Entry(app, width=30)
entry2.place(x=100, y=30)
label1 = Label(app, text=r'保存\脚本路径:')
label1.place(x=11, y=30)
button = Button(app, text='选择路径', command=f)
button.place(x=300, y=30)

cli = ttk.Combobox(app)  # 初始化
cli["values"] = ("录制", "运行")
cli.current(0)
cli.configure(state='readonly')
cli.place(x=100, y=50)

label1 = Label(app, text=r'运行\录制:')
label1.place(x=11, y=55)

label1 = Label(app, text='注意:请先选择此项')
label1.place(x=260, y=55)

button1 = Button(app, text=r'开始录制\运行', command=start)
button1.place(x=11, y=90)

app.mainloop()

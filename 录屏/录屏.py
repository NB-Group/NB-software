from PIL import ImageGrab
import numpy as np
import cv2
from pynput import keyboard
import tkinter.messagebox
import tkinter.filedialog
import threading
import time
import tkinter.messagebox
from tkinter import *
import keyboard as k
from ttkbootstrap import *

flag = False  # 停止标志位
name = ""
zhen = 0
bian = ""


def if_contain_symbol(keyword):
    symbols = "~!@#$%^&*()_+-*/<>,.[]\/"
    for symbol in symbols:
        if symbol in keyword:
            return True
    else:
        return False


def ding():
    global name
    global zhen
    global bian

    def que():
        global name
        global zhen
        global bian
        if entry1 == "":
            tk.messagebox.showerror('错误', '请输入正确的文件名')
            return
        else:
            name = entry1.get()
        bian = cli.get()
        try:
            if entry.get() == "":
                tk.messagebox.showerror('错误', '请输入正确的帧率')
                return
            zhen = int(entry.get())
        except:
            tk.messagebox.showerror('错误', '请输入正确的帧率')
            return
        root.destroy()

    root = tkinter.Tk()
    root.iconbitmap('录.ico')
    root.title('请选择信息')
    root.geometry('200x100')
    label = Label(root, text='''文件名:''')
    label.place(x=8, y=10)
    label1 = Label(root, text='''帧率:''')
    label1.place(x=11, y=30)
    label1 = Label(root, text='''编码:''')
    label1.place(x=11, y=50)
    cli = ttk.Combobox(root)  # 初始化
    cli["values"] = ("XVID", "DIVX")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=50, y=50)
    entry1 = tk.Entry(root, width=20)
    entry1.place(x=50, y=10)
    entry = tk.Entry(root, width=20)
    entry.place(x=50, y=30)
    button = tk.Button(root, text='确定', command=que).place(x=150, y=70)
    root.mainloop()


def select_area():
    area = [0, 0, 0, 0]
    rectangle_id = None

    def _press(event):
        area[0], area[1] = event.x, event.y

    def _move_label(event, text=None):
        nonlocal tip_id, rectangle_id
        text = text or "拖曳选择录制区域,Enter确定(%d, %d)" % (event.x, event.y)
        cv.delete(tip_id)
        tip_id = cv.create_text((event.x + 8, event.y),
                                text=text, anchor=tk.W, justify=tk.LEFT)

    def _drag(event):
        nonlocal rectangle_id
        if rectangle_id is not None: cv.delete(rectangle_id)
        rectangle_id = cv.create_rectangle(area[0], area[1],
                                           event.x, event.y)
        _move_label(event)

    def _release(event):
        area[2], area[3] = event.x, event.y
        _move_label(event, "按Enter键接受, 拖曳可重新选择")
        window.bind_all('<Key-Return>', _accept)

    def _accept(event):
        window.destroy()

    window = tk.Tk()
    window.title("选择录制区域")
    window.protocol("WM_DELETE_WINDOW", lambda: None)  # 防止窗口被异常关闭
    cv = tk.Canvas(window, bg='white', cursor="target")
    cv.pack(expand=True, fill=tk.BOTH)
    tip_id = cv.create_text((cv.winfo_screenwidth() // 2,
                             cv.winfo_screenheight() // 2),
                            text="拖曳选择录制区域",
                            anchor=tk.W, justify=tk.LEFT)
    window.attributes("-alpha", 0.6)
    window.attributes("-topmost", True)
    window.attributes("-fullscreen", True)
    window.bind('<Button-1>', _press)
    window.bind('<Motion>', _move_label)
    window.bind('<B1-Motion>', _drag, )
    window.bind('<B1-ButtonRelease>', _release)

    while 1:
        try:
            window.update()
            time.sleep(0.01)
        except tk.TclError:
            break  # 窗口已关闭
    return area


def video_record():
    """
    屏幕录制！
    :return:
    """
    area = select_area()
    p = ImageGrab.grab()  # 获得当前屏幕
    fourcc = cv2.VideoWriter_fourcc(*bian)  # 编码格式
    video = cv2.VideoWriter(feil + name + '.avi', fourcc, zhen,
                            (area[2] - area[0], area[3] - area[1]))  # 输出文件命名为test.mp4,帧率为16，可以自己设置
    tkinter.messagebox.showinfo("提示", "准备录制,按下k键开始,按home键退出")
    k.wait('k')
    time.sleep(1)
    while True:
        im = ImageGrab.grab(area)
        imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
        video.write(imm)
        if flag:
            tkinter.messagebox.showinfo("提示", "录制结束！")
            break
    video.release()


def on_press(key):
    """
    键盘监听事件！！！
    :param key:
    :return:
    """
    # print(key)
    global flag
    if key == keyboard.Key.home:
        flag = True
        return False  # 返回False，键盘监听结束！


def kai():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def start():
    global name
    global zhen
    global bian
    global name
    global zhen
    global bian
    if entry1.get() == "" and not if_contain_symbol(entry1.get()):
        tk.messagebox.showerror('错误', '请输入正确的文件名')
        return
    else:
        name = entry1.get()
    bian = cli.get()
    try:

        if entry.get() == "":
            int(entry.get())
        zhen = int(entry.get())
    except:
        tk.messagebox.showerror('错误', '请输入正确的帧率')
        return
    th = threading.Thread(target=video_record)
    th.start()
    th1 = threading.Thread(target=kai)
    th1.start()


def san():
    Tk().deiconify()
    Tk().focus_force()


def f():
    global feil
    feil = ""
    feil = tkinter.filedialog.askdirectory()
    entry2.delete(0, END)
    if feil == "":
        tk.messagebox.showerror('错误', '请选择正确的路径')
        return
    entry2.insert(tk.INSERT, feil)


if __name__ == '__main__':  # x
    app = tk.Tk()
    tn = "superhero"
    sty = Style(tn)
    app.title("牛逼录屏")
    app.resizable(False, False)
    app.geometry('400x200')
    app.minsize(400, 200)
    app.maxsize(400, 200)
    button1 = tk.Button(app, text='开始录屏', command=start)
    button1.place(x=50, y=110)
    button = tk.Button(app, text='选择路径', command=f)
    button.place(x=250, y=80)
    app.iconbitmap('录.ico')
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
    entry1 = tk.Entry(app, width=24)
    entry1.place(x=50, y=10)
    entry = tk.Entry(app, width=24)
    entry.place(x=50, y=30)
    entry2 = tk.Entry(app, width=24)
    entry2.place(x=50, y=80)
    app.mainloop()

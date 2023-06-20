# -*- coding: utf-8 -*
import wenxin_api  # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.composition import Composition
import tkinter.messagebox
import tkinter.filedialog
import tkinter.messagebox
from ttkbootstrap import *

wenxin_api.ak = ""
wenxin_api.sk = "O1YwzpuNvXAl5cBgosLbE07Tv1dTGnMM"
flag = False  # 停止标志位
name = ""
zhen = 0
bian = ""


def start():
    global app
    app.title("牛逼AI.生成器-生成中 请稍等字数过多会延长时间")
    app.update()
    input_dict = {
        "text": entry.get(),
        "seq_len": int(entry3.get()),
        "topp": 0.0,
        "penalty_score": 1.2,
        "min_dec_len": int(entry4.get()),
        "is_unidirectional": 0,
        "task_prompt": cli.get().replace("作文", "zuowen").replace("摘要", "Summarization").replace("对联", "couplet")
    }
    rst = Composition.create(**input_dict)
    fb = open(entry2.get() + entry1.get() + ".txt", mode='a', encoding="utf-8")
    fb.write(rst["result"])
    app.title("牛逼AI.生成器")
    app.update()


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
    app.title("牛逼AI.生成器")
    app.resizable(False, False)
    app.geometry('400x200')
    app.minsize(400, 200)
    app.maxsize(400, 200)
    button1 = tk.Button(app, text='开始生成', command=start)
    button1.place(x=11, y=160)
    button = tk.Button(app, text='选择路径', command=f)
    button.place(x=260, y=100)
    label = Label(app, text='''导出文件名:''')
    label.place(x=11, y=10)
    label1 = Label(app, text='''标题/文章/上联:''')
    label1.place(x=11, y=30)
    label1 = Label(app, text='''生成类型:''')
    label1.place(x=11, y=65)
    label1 = Label(app, text='''导出路径:''')
    label1.place(x=11, y=100)
    label1 = Label(app, text='''最大字数:''')
    label1.place(x=11, y=120)
    label1 = Label(app, text='''最小字数:''')
    label1.place(x=11, y=140)
    cli = ttk.Combobox(app)  # 初始化
    cli["values"] = ("作文", "摘要", "对联")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=100, y=60)

    entry1 = tk.Entry(app, width=24)
    entry1.place(x=100, y=10)

    entry = tk.Entry(app, width=24)
    entry.place(x=100, y=30)

    entry2 = tk.Entry(app, width=24)
    entry2.place(x=100, y=100)

    entry3 = tk.Entry(app, width=24)
    entry3.place(x=100, y=120)

    entry4 = tk.Entry(app, width=24)
    entry4.place(x=100, y=140)

    app.mainloop()

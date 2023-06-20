import tkinter as tk
from ttkbootstrap import Style
import requests as re
import pyttsx3
from json import loads

engine = pyttsx3.init()

global res
res = ""

def pprint(i):
    niu.delete(0.0, tk.END)  # 清空内容 0.0是lineNumber.colNumber的表示方法
    niu.insert(0.0, i)


def fanyi():
    global res
    a = ""
    name = entry.get(0.0, tk.END)
    scr = "https://api.qingyunke.com/api.php?key=free&appid=0&msg=翻译" + name
    res = re.get(scr, verify=False)
    res = res.content.decode('utf-8')
    res = res.replace("{br}", r"\n")
    res = loads(res)["content"]
    res = res.split("：")
    if res == ['呀，这是火星语吧，菲菲翻译不出来~']:
        pprint("请输入正确的文字")
    else:
        pprint(res[2])


def speak():
    global res
    engine.say(res[2])
    engine.runAndWait()


app = tk.Tk()
tn = "superhero"
sty = Style(tn)
app.title("牛逼翻译")
app.geometry('400x200')
app.maxsize(400, 200)
label = tk.Label(app, text='''           __________                                _________
 语言:|自动检测|      ---->      语言:|自动检测|
''')
label.pack()
entry = tk.Text(app, width=40, height=3)
entry.pack(side="top")

niu = tk.Text(app, width=40, height=3)
niu.pack(side="top")
button = tk.Button(app, text='翻译', command=fanyi).pack(side="left")
button = tk.Button(app, text='朗读', command=speak).pack(side="left")
app.mainloop()

import ttkbootstrap as ttk
import speedtest
from random import randint
import threading
from time import sleep
import tkinter.messagebox

flag = True


def k():
    global flag
    global meter
    meter.configure(subtext="准备测速ing...")

    # 创建实例对象
    try:
        test = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError:
        tkinter.messagebox.showerror('错误', '未连网或者网络不可用')
        return
    # 获取可用于测试的服务器列表
    test.get_servers()

    # 筛选出最佳服务器
    best = test.get_best_server()

    meter.configure(subtext="测速服务器\n" + best['sponsor'])

    # 下载速度
    download_speed = int(test.download() / 1024 / 1024)
    # 上传速度
    upload_speed = int(test.upload() / 1024 / 1024)

    # 输出结果

    flag = False
    meter.configure(amountused=int((upload_speed + download_speed) / 2))
    w = str(int((upload_speed + download_speed) / 2))
    meter.configure(subtext="平均网速" + w + "MB/s")


def kai():
    global flag
    global meter
    flag = True
    meter.configure(subtext="开始测速")
    t = threading.Thread(target=k, daemon=True)
    t.start()
    while flag:
        app.update()
        meter.configure(amountused=randint(0, 100))
        sleep(0.5)


if __name__ == "__main__":
    app = ttk.Window()
    app.title("网速测速·牛逼出品")
    app.minsize(400, 250)
    app.geometry("400x280")
    meter = ttk.Meter(
        metersize=180,
        padding=10,
        amountused=10,
        metertype="semi",
        subtext="miles per hour",
        interactive=False,
        textright="MB/s",
        stripethickness=2
    )
    meter.pack()

    meter.configure(amountused=0)
    meter.step(0)
    button = ttk.Button(app, text='开始测速', command=kai)
    button.pack()
    meter.configure(subtext="可以测速")

    app.mainloop()

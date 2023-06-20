import os
import tkinter.messagebox
import tkinter.filedialog
from aip import AipOcr
from ttkbootstrap import *
from PIL import Image, ImageGrab


def pprint(values):
    #    man.delete(0.0, tk.END)  # 清空内容 0.0是lineNumber.colNumber的表示方法
    man.insert(tk.INSERT, values)  # 添加文字


# 选择图片函数
def chooseImg():
    fileName = tk.filedialog.askopenfilename(title='选择图片',
                                             filetype=[('图片文件', '*.jpg'), ('图片文件', '*.png'), ('图片文件', '*.bmp'),
                                                       ('不支持的图片文件', '*.gif'), ('所有类型文件', '*.*')])
    if fileName:
        varFileName.set(fileName)
        # 预览图片
        showImg(fileName)
        # 百度图片识别文字
        baiduOCR(fileName)


# 预览图片函数
def showImg(fileName):
    # 动态给label设置图片,支持所有格式图片
    img_open = Image.open(fileName)
    imgTk = ImageTk.PhotoImage(img_open)
    labelImg.config(image=imgTk)
    labelImg.image = imgTk


# 百度图片识别文字
def baiduOCR(picfile):
    # 初始化
    APP_ID = '26236256'  # 刚才获取的 ID，下同
    API_KEY = 'acrGzkE5zjtlpTDxdVYyQ0dh'
    SECRECT_KEY = '3dwbSYlo9R1rCpH8BdYnUFG2IdUWgaCt'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    pprint("正在识别图片：\t" + picfile)
    if varHighAccurate.get():  # True 高精度识图
        pprint("高精度识图中....")
        message = client.basicAccurate(img)  # 通用文字高精度识别
    else:  # False 普通识图
        pprint("普通识图中...")
        message = client.basicGeneral(img)  # 通用文字识别
    pprint("识别成功！ 文字是:")
    pprint(message)
    i.close();
    if message.get('error_code'):  # 出错了
        tk.messagebox.showerror(title='图片提取文字出错了', message='可能网络中断')
    else:
        showMsg(message)  # 识别出来了,就显示结果信息


# 显示结果信息
def showMsg(message):
    string = ''
    for txt in message.get('words_result'):
        string += txt.get('words') + '\n'
        pprint(string)
    txtResult.delete(0.0, tk.END)  # 清空内容 0.0是lineNumber.colNumber的表示方法
    txtResult.insert(tk.INSERT, string)  # 添加文字


# 一键复制结果信息
def Copy():
    txtResult.clipboard_clear()
    string = txtResult.get(0.0, tk.END)
    txtResult.clipboard_append(string)
    pprint("复制的字符是:" + string)


# 粘贴路径之后再识别
def start():
    path = entryFileName.get()
    path = path.strip(' ').strip('"')  # 去掉字符串开头结尾的空格和双引号
    if len(path) <= 0:
        return
    pprint(path)
    showImg(path)
    baiduOCR(path)


# 从粘贴板获取图片,并且识图
def clipboard():
    # 从粘贴板获取
    img_open = ImageGrab.grabclipboard()
    if isinstance(img_open, Image.Image):  # 如果是图片
        pprint("剪切板中有图片")
        imgTk = ImageTk.PhotoImage(img_open)  # 需要导入PIL中的ImageTk
        # 预览图片
        labelImg.config(image=imgTk)
        labelImg.image = imgTk
        # 保存图片
        tempFileName = 'D:/删除.jpg'
        img_open.save(tempFileName)
        # 百度识图
        baiduOCR(tempFileName)
        # 再删除缓存的图片
        if (os.path.exists(tempFileName)):
            os.remove(tempFileName)
    else:
        if tkinter.messagebox.askokcancel('提示', '你的剪贴板里没有图片，点击\'确定\'可以定范围识别,点击\'取消\'请自己点击PrtSc(截图键)并重新点击此按钮'):
            tkinter.messagebox.showinfo('提示', '请点击新建,选择文字识别区域,并复制,复制后若从此程序无响应,请关闭截图程序')
            os.system('SnippingTool.exe')  # 此处已经设置好了该exe文件的环境变量
            img_open = ImageGrab.grabclipboard()
            if isinstance(img_open, Image.Image):  # 如果是图片
                pprint("剪切板中有图片")
                imgTk = ImageTk.PhotoImage(img_open)  # 需要导入PIL中的ImageTk
                # 预览图片
                labelImg.config(image=imgTk)
                labelImg.image = imgTk
                # 保存图片
                tempFileName = 'D:/删除.jpg'
                img_open.save(tempFileName)
                # 百度识图
                baiduOCR(tempFileName)
                # 再删除缓存的图片
                if (os.path.exists(tempFileName)):
                    os.remove(tempFileName)
            else:
                tkinter.messagebox.showinfo('提示', '剪贴失败,请重试')


if __name__ == "__main__":
    # 窗口
    app = tk.Tk()
    app.title("图片提取文字|梁皓文制作")
    app.geometry('1000x500')
    style = Style()
    style = Style(theme="superhero")
    # 想要切换主题，修改theme值即可，有以下这么多的主题，自己尝试吧：['classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
    TOP6 = style.master
    # 图片路径
    varFileName = tk.StringVar()
    varFileName.set('')
    # 结果信息
    varTxtMsg = tk.StringVar()
    varTxtMsg.set('')
    # 百度高精度识图,默认false
    varHighAccurate = tk.BooleanVar()
    varHighAccurate.set(False)

    # 图片路径输入框
    entryFileName = tk.Entry(app, width=35, textvariable=varFileName)
    entryFileName.place(x=90, y=10)

    # 选择图片并且识别按钮
    btn_chooseImg = tk.Button(app, text='选择图片', command=chooseImg)
    btn_chooseImg.place(x=10, y=5)

    # 开始识别按钮
    btn_start = tk.Button(app, text='开始识别', command=start)
    btn_start.place(x=400, y=5)

    # 从粘贴板导入图片并且识别
    btn_clipboard = tk.Button(app, text='从粘贴板导入图片并且识别', command=clipboard)
    btn_clipboard.place(x=15, y=55)

    # 预览图片的标签
    labelImg = tk.Label(app)
    labelImg.place(x=500, y=5)

    # 是否高精度识图
    tk.Radiobutton(app, text="普通识图", variable=varHighAccurate, value=False).place(x=30, y=110)
    tk.Radiobutton(app, text="高精度识图", variable=varHighAccurate, value=True).place(x=240, y=110)

    # 显示结果的文本框
    txtResult = tk.Text(app, width=50, height=15)
    txtResult.place(x=15, y=200)

    # 文本结果信息添加到粘贴板中
    tk.Button(app, text='全部复制', command=Copy).place(x=160, y=150)

    man = tk.Text(app, width=50, height=2)
    man.place(x=15, y=425)
    app.iconbitmap("ao5dp-ygtbo-001.ico")
    app.mainloop()

import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter as tk
from tkinter import *
from ttkbootstrap import *
p = " "
def chaoji(file):
    if cli.get()=="文件夹":
        os.system(f"rmdir /s/q \"{file}\"")
    else:

        os.system(f"del \"{file}\"")

def rmdir(dir):
    global p
    if r_value.get() == "1":
        chaoji(dir)
        return
    if dir == "D:/":
        return
    #判断是否是文件夹，如果是，递归调用rmdir()函数
    if(os.path.isdir(dir)):
        #遍历地址下的所有文件及文件夹
        for file in os.listdir(dir):
            #进入下一个文件夹中进行删除
            rmdir(os.path.join(dir,file))
        #如果是空文件夹，直接删除
        if (os.path.exists(dir)):
            try:
                os.rmdir(dir)
                p += dir + "文件夹删除成功\n"
            except:
                p += dir + "文件夹删除失败\n"
    #如果是文件，直接删除
    else:
        if(os.path.exists(dir)):
            try:
                os.remove(dir)
                p += dir + "文件删除成功\n"
            except:
                p += dir + "文件删除失败\n"
def start():
    if cli.get()=="文件夹":
        feil = tkinter.filedialog.askdirectory()
        rmdir(feil)
        tkinter.messagebox.showinfo("提示", "请查看文件详情："+p)
    else:
        filename = tk.filedialog.askopenfilename()
        rmdir(filename)
        tkinter.messagebox.showinfo("提示", "请查看文件详情：" + p)
#调用定义函数
if __name__ == "__main__":

    app = tk.Tk()
    app.title("厉害文件粉碎机")
    app.geometry('400x200')
    label = Label(app, text='''请选择删除的数据类型:''')
    label.place(x=30,y=50)
    cli = ttk.Combobox(app)  # 初始化
    cli["values"] = ("文件夹","文件")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=170,y=50)
    button = tk.Button(app, text='开始清理', command=start).place(x=30, y=10)
    # app.iconbitmap('录.ico')
    # Importing Tkinter module
    from tkinter import *
    from tkinter.ttk import *

    r_value = IntVar()  # 我们创建一个Int类型的容器
    Radiobutton(app, text='普通清理(时间较快)', variable=r_value, value=1).place(x=30,y=70)
    Radiobutton(app, text='究极清理！(时间超长，但无坚不摧)', variable=r_value, value=2).place(x=30,y=90)

    app.mainloop()


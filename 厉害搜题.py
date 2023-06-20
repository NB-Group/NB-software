# encoding: utf-8
import tkinter as tk
import requests as re
import time
import tkinter.messagebox
import os
def show(html):
    def text_create(name, msg):
        desktop_path = ""
        full_path = desktop_path + name + '.html'
        file = open(full_path, 'w')
        file.write(msg)
    text_create('1',html)
    os.system("start D:\code\python\\1.html")
    time.sleep(5)
    os.remove("1.html")
res = ""
def start():
    global res
    i = niu.get()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    uil = f"https://www.baidu.com/s?wd={i}&rsv_spt=1&rsv_iqid=0x93ba8a7f000163ee&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=ts_0&rsv_enter=0&rsv_btype=t&inputT=10966&rsv_t=42faLS4DVjRL%2B8cKq5Xmltcvfh0IBXoclenIFpRJ2F%2BSN2f94MIBp%2Fto35Fv2vTPGFny&oq=%25E5%2589%258D%25E8%25BF%259B%25E5%25B0%258F%25E5%25AD%25A6%25E7%258E%25AF%25E4%25BF%259D%25E5%258D%25AB%25E5%25A3%25AB%25E5%25B0%258F%25E5%2588%2586%25E9%2598%259F11%25E4%25BA%25BA%25E5%258F%2582%25E5%258A%25A0%25E6%258D%25A1%25E5%25BA%259F%25E6%2597%25A7%25E5%25A1%2591%25E6%2596%2599%25E7%2593%25B6%25E6%25B4%25BB%25E5%258A%25A8&rsv_pq=94eaf06b000007f3&rsv_sug3=476&rsv_sug1=443&rsv_sug7=100&rsv_sug2=1&prefixsug=%25E5%25BC%25BA%25E5%25BC%25BA%25E4%25B8%2580%25E6%25AC%25A1&rsp=0&rsv_sug4=11083"

    res = re.get(uil,headers=headers)
    res = res.content.decode('utf-8')
    res = res.replace("{br}", r"\n")
    # print(res)
    index_start = res.find("kuaizhao\":{\"text\":\"百度快照\",\"url\":",706)
    index_end = res.find("\"},\"urlSign\"",index_start)


    uil = res[index_start + 1 +len("kuaizhao\":{\"text\":\"百度快照\",\"url\":"):index_end]
    # print(uil)
    try:
        res = re.get(uil,headers=headers)
    except:
        tk.messagebox.showerror('错误', '没有搜到')
        return
    # res.apparent_encoding
    bian = res.apparent_encoding
    res = res.content.decode(bian)
    # print(res)
    res = res.replace("{br}", r"\n")

    index_start = res.find("<div id=\"bd_snap\">")
    index_end = res.find("<div id=\"bd_snap_ln\"></div>")
    res += "\n<title>梁牛逼分析题目</title>"
    res += "\n<link rel=\"shortcut icon\" href=\"favicon.ico\">"
    res = res[:index_start] + res[index_end:]
    # res += "\n<meta name=\"description\" content=\"讲解！\" bdsfid=\"6\">"
    index_start = res.find("<meta name=\"description\" content=\"")
    index_end = res.find("bdsfid=\"6\">")
    # res = res.replace()
    str_list = list(res)
    str_list.insert(0,"<link rel=\"shortcut icon\" href=\"favicon.ico\">")
    res = ''.join(str_list)
    str_list = list(res)
    str_list.insert(0,"<title>梁牛逼分析题目</title>")
    res = ''.join(str_list)
    res= res.replace("#bd_snap_logo{width:162px;height:38px;display:block;background:url(http://www.baidu.com/img/logo-snap.png) no-repeat;margin-right:15px;float:left}","")
def s():
    show(res)
app = tk.Tk()
app.title("厉害搜题")
app.geometry('400x200')
label = tk.Label(app, text='''梁牛逼制作：究极搜题神器
赶紧试试看吧''')
label.pack()
niu = tk.Entry(app,width=30)
niu.place(x= 90,y=60)
button = tk.Button(app,text='牛逼一下',command=start).place(x=280,y=60)
button = tk.Button(app,text='直接打开',command=s).place(x=160,y=80)

app.mainloop()
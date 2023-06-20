
import matplotlib.image
import cv2
import tkinter as tk
from tkinter import *
import win32api, win32con
import time
import tkinter.messagebox
import sys
import threading

ni = ""
x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴

y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
root = ""

# 导入方法模块
flag_jiuji = False

flag_exit = False


def pan():
    global flag_exit
    if ni.get() == "exit":
        flag_exit = True
        return
    if ni.get() == "p":
        root.destroy()
        return
    else:
        tkinter.messagebox.showwarning("警告", "哼,别想动我电脑")


def chengfa():
    global root
    global ni
    root = tk.Tk()
    root.minsize(x, y)
    label1 = Label(root, text='''由于你看着不像主人，所以触发此程序。
    在此填写密码：\t\t\t''')
    label1.place(x=x / 2 - 100, y=y / 2)

    ni = tk.Entry(root, width=20, show="*")
    ni.place(x=x / 2 + 10, y=y / 2 + 20)

    ga = tk.Button(root, text='确定密码', command=pan)
    ga.place(x=x / 2 - 90, y=y / 2 + 40)

    root.overrideredirect(True)
    root.update()
    while True:
        if flag_exit:
            sys.exit(0)

        try:
            root.wm_attributes('-topmost', 1)
            root.update()
        except:
            break
        ret, frame = cap.read()
        cv2.imwrite(str(index) + ".bmp", frame)
        img = cv2.imread("niu.bmp")
        cropped = img[0:490, 144:480]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite("niu.bmp", cropped)
        I = image_matrix("niu.bmp")
        I = I[0]
        K = [[1, 0, 1],
             [0, 1, 0],
             [1, 0, 1]]

        # 补全扫描“行”数
        d_i = len(I)
        d_j = len(I[0])
        I_K = []
        q = []
        p = 1
        for i in range(d_i - 2):
            # 填入恰当的变量
            for j in range(d_j - 2):
                re = get_sum(I, K, i, j)
                # 将结果加入到列表I_K中
                q.append(re)
                if p % 4 == 0:
                    p = 0
                    I_K.append(q)
                    q = []
                p += 1

        ls = I_K
        # show(ls)

        pooling = []
        q = []
        f = False
        # 将range函数补充完整，使得步长为2
        for i in range(0, len(ls), 2):
            # 补充完整，使步长为2，并注意范围
            for j in range(0, len(ls[0]), 2):
                try:
                    sub_ls = [ls[i][j], ls[i + 1][j], ls[i][j + 1], ls[i + 1][j + 1]]

                    q.append(max(sub_ls))
                except:
                    break
                    f = True
            if f:
                break
            pooling.append(q)
            q = []

        niu = dig_lists(pooling)
        cnt = 0
        for i in range(min(len(bi), len(niu))):
            if round(bi[i], -2) != round(niu[i], -2):
                cnt += 1
        if cnt >= 30:
            pass
        else:
            root.destroy()
            break


def image_matrix(filename):
    im = matplotlib.image.imread(filename)
    return im


def dig_lists(pram_list):
    output = []
    for e in pram_list:
        if isinstance(e, list):
            output += dig_lists(e)
        else:
            output.append(e)
    return output


def get_sum(list_1, list_2, di, dj):
    sum = 0
    for i in range(len(list_2)):
        for j in range(len(list_2[i])):
            sum += list_2[i][j] * list_1[i + di][j + dj]
    return sum


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
flag = cap.isOpened()
index = "niu"
fl = 0
while True:
    ret, frame = cap.read()
    cv2.imwrite(str(index) + ".bmp", frame)
    img = cv2.imread("niu.bmp")
    cropped = img[0:490, 144:480]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("niu.bmp", cropped)
    I = image_matrix("niu.bmp")
    I = I[0]
    K = [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]

    # 补全扫描“行”数
    d_i = len(I)
    d_j = len(I[0])
    I_K = []
    q = []
    p = 1
    for i in range(d_i - 2):
        # 填入恰当的变量
        for j in range(d_j - 2):
            re = get_sum(I, K, i, j)
            # 将结果加入到列表I_K中
            q.append(re)
            if p % 4 == 0:
                p = 0
                I_K.append(q)
                q = []
            p += 1

    ls = I_K
    # show(ls)

    pooling = []
    q = []
    f = False
    # 将range函数补充完整，使得步长为2
    for i in range(0, len(ls), 2):
        # 补充完整，使步长为2，并注意范围
        for j in range(0, len(ls[0]), 2):
            try:
                sub_ls = [ls[i][j], ls[i + 1][j], ls[i][j + 1], ls[i + 1][j + 1]]

                q.append(max(sub_ls))
            except:
                break
                f = True
        if f:
            break
        pooling.append(q)
        q = []

    niu = dig_lists(pooling)
    bi = [421, 403, 379, 375, 367, 373, 374, 381, 373, 380, 379, 378, 392, 388, 388, 391, 401, 400, 389, 377, 386, 392,
          395, 394, 394, 388, 388, 383, 404, 398, 380, 375, 379, 390, 394, 392, 374, 377, 383, 383, 367, 354, 348, 324,
          217, 225, 226, 229, 322, 356, 380, 392, 402, 403, 389, 387, 438, 434, 458, 456, 450, 446, 421, 426, 419, 428,
          431, 425, 429, 424, 435, 440, 419, 420, 420, 428, 435, 429, 424, 425, 419, 415]
    b2 = [220, 213, 224, 250, 257, 253, 259, 257, 224, 222, 245, 254, 255, 249, 242, 239, 288, 309, 310, 316, 304, 304,
          318, 314, 335, 332, 296, 264, 270, 263, 260, 273, 301, 305, 289, 302, 343, 342, 344, 342, 330, 324, 324, 345,
          355, 340, 324, 320, 327, 324, 368, 358, 344, 347, 370, 364, 370, 374, 371, 381, 390, 384, 388, 396, 396, 392,
          400, 401, 404, 409, 398, 399, 404, 398, 374, 371, 359, 363, 366, 346, 365, 372]
    print(niu)
    cnt = 0
    for i in range(min(len(bi), len(niu))):
        if round(bi[i], -2) != round(niu[i], -2 and not niu[i] >= 1000):
            cnt += 1
    cnt_b2 = 0
    for i in range(min(len(b2), len(niu))):
        if round(b2[i], -2) != round(niu[i], -2) and not niu[i] >= 1000:
            cnt_b2 += 1
    print("图一错误率:", int(cnt / 82 * 100), "%")
    print("图一错误数:", cnt)
    print("图二错误率:", int(cnt_b2 / 82 * 100), "%")
    print("图二错误数:", cnt_b2)
    # print(fl)
    if cnt <= 30 or cnt_b2 <= 30:
        fl = 0
        time.sleep(3)
        pass
    else:
        time.sleep(3)
        if fl >= 3:
            chengfa()
            f = 0
        fl += 1

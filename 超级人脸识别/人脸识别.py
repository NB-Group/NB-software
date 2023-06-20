import matplotlib.image
import cv2
import tkinter as tk
from tkinter import *
import win32api, win32con
import datetime
import tkinter.messagebox
import sys
import os
from pynput import keyboard
import time
import face_recognition as face
import threading

ctr2 = keyboard.Controller()


def pand():
    t = time.time()
    images = os.listdir(r'D:\data')

    image_to_be_matched = face.load_image_file(r'D:\niu.jpg')
    try:
        image_to_be_matched_encoded = face.face_encodings(image_to_be_matched)[0]
    except:
        time.sleep(5)
        # print("未发现匹配图片！")
        return True
    cnt = 0
    for image in images:

        current_image = face.load_image_file(r"D:/data/" + image)

        try:
            current_image_encoded = face.face_encodings(current_image)[0]
        except:
            # print("未发现匹配图片！")
            return
        try:
            result = face.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        except:
            # print("未发现匹配图片！")
            return
        now = datetime.datetime.now()
        # print(now.strftime("%Y-%m-%d %H:%M:%S"), "扫描")
        if result[0]:
            # print("匹配: " + image)
            cnt += 1
            break
    # print("共用时:",time.time() - t,"秒")
    if cnt <= 0:
        # print("未发现匹配图片！")
        return True
    return False


ni = ""
x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴

y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
root = ""

# 导入方法模块
flag_jiuji = False

flag_exit = False

flag_exit_pan = False

stop_pan = False


def pan():
    global flag_exit
    print(ni.get())
    if ni.get() == "exit":
        flag_exit = True
        return
    if ni.get() == "q":
        root.destroy()
        return
    else:
        tkinter.messagebox.showwarning("警告", "哼,别想动我电脑")


def chengfa_pan():
    global flag_exit_pan
    global stop_pan
    while True:
        ret, frame = cap.read()
        cv2.imwrite(str(index) + ".jpg", frame)
        if not pand():
            flag_exit_pan = True
            break
        if stop_pan:
            stop_pan = False
            break


def chengfa():
    global root
    global ni
    global stop_pan
    global flag_exit_pan

    lis = threading.Thread(target=chengfa_pan)
    lis.start()
    time.sleep(10)

    root = tk.Tk()
    root.minsize(x, y)
    label1 = Label(root, text='''由于你看着不像主人，所以触发此程序。
    在此填写密码：\t\t\t''')
    label1.place(x=x / 2 - 100, y=y / 2)

    ni = tk.Entry(root, width=20)
    ni.place(x=x / 2 + 10, y=y / 2 + 20)

    ga = tk.Button(root, text='确定密码', command=pan)
    ga.place(x=x / 2 - 90, y=y / 2 + 40)

    root.overrideredirect(True)
    root.update()

    th = threading.Thread(target=chengfa_pan)
    th.start()

    while True:
        if flag_exit:
            sys.exit(0)
        if flag_exit_pan:
            root.destroy()
            stop_pan = True
            flag_exit_pan = False
            break
        try:
            root.wm_attributes('-topmost', 1)
            root.update()
        except:
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
index = r"D:\niu"
fl = 0
while True:
    ret, frame = cap.read()
    cv2.imwrite(str(index) + ".jpg", frame)
    img = cv2.imread(r"D:\niu.jpg")
    if pand():
        chengfa()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先导入
import requests
import json
import pandas as pd
import sys
sys.path.append('/home/chenjl96/Documents/python&deep learning')
import module_for_homework1 as mo1
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('天気の子')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('900x1200')  # 这里的乘是小x
 
# 第4步，在图形界面上设定标签
#var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
#l = tk.Label(window, textvariable = var, font=('Arial', 12))
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
checkvar01 = tk.IntVar()
checkvar02 = tk.IntVar()
checkvar03 = tk.IntVar()
checkvar04 = tk.IntVar()
checkvar05 = tk.IntVar()
checkvar06 = tk.IntVar()
checkvar07 = tk.IntVar()
checkvar08 = tk.IntVar() 
checkvar09 = tk.IntVar() 
checkvar10 = tk.IntVar() 
checkvar11 = tk.IntVar() 
checkvar12 = tk.IntVar() 
checkvar13 = tk.IntVar() 
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名

'''def hit_me():
    filename = tkfd.askopenfilename()
    var.set(filename)
    img = cv2.imread(filename)
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    l.config(image = imgtk)
    l.image = imgtk
    print("吃饱了没")'''
def data_get(e1,e2,e3):
    global dataraw
    stationname = e3.get()
    #print(stationname)
    stationdata = pd.read_excel('/home/chenjl96/Documents/python&deep learning/China_SURF_Station.xlsx')
    station = stationdata[stationdata['站名'] == stationname]
    #print(station)
    stationid = int(station['区站号'].values)
    stationlng = int(station['经度'].values)
    stationlat = int(station['纬度'].values)
    time1 = e1.get()
    time2 = e2.get()
    list1 = [time1,time2,stationid]
    #print(list1)
    r = requests.get("http://api.data.cma.cn:8090/api?userId=617872880039g1NWk&pwd=BGd13Lx&dataFormat=json&interfaceId=getSurfEleByTimeRangeAndStaID&timeRange=[{}0000,{}0000]&staIDs={}&elements=TEM,TEM_Max,TEM_Min,PRS,RHU,windpower,WIN_D_S_Max,WIN_S_Max,PRE_1h,CLO_Cov,WEP_Now,Station_Id_C,Year,Mon,Day,Hour&dataCode=SURF_CHN_MUL_HOR".format(*list1))
    hjson = json.loads(r.text)
    print(stationlng,stationlat)
    dataraw = mo1.Weather(hjson,stationlng,stationlat,stationname)
    return dataraw

# 第5步，在窗口界面设置放置Button按键
l1 = tk.Label(text="请输入要查询的起始时间",font=('fangsong ti', 20))
e1 = tk.Entry()
l2 = tk.Label(text="请输入要查询的终止时间",font=('fangsong ti', 20))
e2 = tk.Entry()
l3 = tk.Label(text="请输入要查询的地区（中文形式即可）",font=('fangsong ti', 20))
e3 = tk.Entry()
b = tk.Button(window, text='获取数据', font=('fangsong ti', 25), width=10, height=1, command=lambda:data_get(e1,e2,e3))
c01 = tk.Checkbutton(text='最高气温', variable=checkvar01, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxTem())
c02 = tk.Checkbutton(text='最低气温', variable=checkvar02, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.minTem())
c03 = tk.Checkbutton(text='最高气压', variable=checkvar03, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxPrs())
c04 = tk.Checkbutton(text='最低气压', variable=checkvar04, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.minPrs())
c05 = tk.Checkbutton(text='最高相对湿度', variable=checkvar05, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxRhu())
c06 = tk.Checkbutton(text='最低相对湿度', variable=checkvar06, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.minRhu())
c07 = tk.Checkbutton(text='最高风力', variable=checkvar07, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxWp())
c08 = tk.Checkbutton(text='最高最大风速', variable=checkvar08, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxWinsmax())
c09 = tk.Checkbutton(text='最高每小时降水量', variable=checkvar09, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxPre1h())
c10 = tk.Checkbutton(text='累积降水量', variable=checkvar10, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.accumulatedPre())
c11 = tk.Checkbutton(text='最高总云量', variable=checkvar11, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.maxClo())
c12 = tk.Checkbutton(text='最低总云量', variable=checkvar12, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.minClo())
c13 = tk.Checkbutton(text='适合观测的天区', variable=checkvar13, font=('fangsong ti', 15), height=2, width=15, command=lambda:dataraw.scope())

b.pack()
l1.pack() 
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
c01.pack()
c02.pack()
c03.pack()
c04.pack()
c05.pack()
c06.pack()
c07.pack()
c08.pack()
c09.pack()
c10.pack()
c11.pack()
c12.pack()
c13.pack()
# 第6步，主窗口循环显示
window.mainloop()
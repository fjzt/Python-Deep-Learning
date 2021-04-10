#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:10:49 2021

@author: chenjl96
"""

#这是第一次大作业的模块文件


class Weather:
    def __init__(self, hjson, stlng, stlat, stname):
        self.hjson = hjson
        self.stlng = stlng/100  #经度
        self.stlat = stlat/100  #纬度
        self.stname = stname
    def scope(self):                                 #计算给定日期夜晚适合观测的天球坐标（赤道坐标系）
        #time = str(self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'])
        time_mon = int(self.hjson['DS'][0]['Mon'])
        time_day = int(self.hjson['DS'][0]['Day'])
        if time_mon < 9:
            difference = (23+30*(9-time_mon-1)+30-time_day)*236
            RA_midnight = 24*3600-difference
            RA_midnight_min, RA_midnight_sec = divmod(RA_midnight, 60)
            RA_midnight_hour, RA_midnight_min = divmod(RA_midnight_min, 60)
        elif time_mon == 9:
            if time_day < 23:
                difference = (23-time_day)*236
                RA_midnight = 24*3600-difference
                RA_midnight_min, RA_midnight_sec = divmod(RA_midnight, 60)
                RA_midnight_hour, RA_midnight_min = divmod(RA_midnight_min, 60)
            else:
                difference = (time_day-23)*236
                RA_midnight = difference
                RA_midnight_min, RA_midnight_sec = divmod(RA_midnight, 60)
                RA_midnight_hour, RA_midnight_min = divmod(RA_midnight_min, 60)
        else:
            difference = ((30-23)+30*(time_mon-9-1)+time_day)*236
            RA_midnight = difference
            RA_midnight_min, RA_midnight_sec = divmod(RA_midnight, 60)
            RA_midnight_hour, RA_midnight_min = divmod(RA_midnight_min, 60)
        if RA_midnight_hour-4 < 0:
            RA_midnight_hour_from = 24+(RA_midnight_hour-4)
            RA_midnight_hour_to = RA_midnight_hour+4
        elif RA_midnight_hour+4 >= 24:
            RA_midnight_hour_from = RA_midnight_hour-4
            RA_midnight_hour_to = (RA_midnight_hour+4)-24
        else:
            RA_midnight_hour_from = RA_midnight_hour-4
            RA_midnight_hour_to = RA_midnight_hour+4
        RA = {'hour_from':str(RA_midnight_hour_from), 'hour_to':str(RA_midnight_hour_to), 'min':str(RA_midnight_min), 'sec':str(RA_midnight_sec)}
        # RA即赤经
        if self.stlat-60 < -90:
            Dec_from = -90
            Dec_to = self.stlat+60
        elif self.stlat+60 > 90:
            Dec_from = self.stlat-60
            Dec_to = 90
        else:
            Dec_from = self.stlat-60
            Dec_to = self.stlat+60
        Dec = {'from':Dec_from,'to':Dec_to}
        #Dec即赤纬
        print("%d月%d日%s夜晚适宜观测的天区为：赤纬%s-%s度，赤经%sh%smin%ss-%sh%smin%ss"%(time_mon,time_day,self.stname,Dec['from'],Dec['to'],RA['hour_from'].zfill(2),RA['min'].zfill(2),RA['sec'].zfill(2),RA['hour_to'].zfill(2),RA['min'].zfill(2),RA['sec'].zfill(2)))
        #return RA,Dec
    
    
    def maxTem(self):   #最高气温
        maxtem = -273.15
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        for x in range(len(self.hjson["DS"])):
            test = float(self.hjson['DS'][x]['TEM_Max'])
            #print(self.hjson['DS'][x]['TEM_Max'],str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2)))
            if maxtem < test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxtem = test
        print("最高气温为%s摄氏度，出现时间为%s" %(maxtem,time))
        return maxtem, time
    
    def minTem(self):   #最低气温
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        mintem = 100
        for x in range(len(self.hjson["DS"])):
            test = float(self.hjson['DS'][x]['TEM_Min'])
            if mintem > test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                mintem = test
        print("最低气温为%s摄氏度，出现时间为%s" %(mintem,time))
        return mintem, time
    
    def maxPrs(self):   #最高气压
        maxprs = 0
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['PRS'])
            test = float(self.hjson['DS'][x]['PRS'])
            if maxprs < test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxprs = test
        print("最高气压为%s百帕，出现时间为%s" %(maxprs,time))
        return maxprs, time
    
    def minPrs(self):   #最低气压
        minprs = 10000
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['PRS'])
            test = float(self.hjson['DS'][x]['PRS'])
            if minprs > test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                minprs = test
        print("最低气压为%s百帕，出现时间为%s" %(minprs,time))
        return minprs, time

    def maxRhu(self):   #最高相对湿度
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        maxrhu = 0
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['RHU'])
            test = float(self.hjson['DS'][x]['RHU'])
            if maxrhu < test and test <= 100:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxrhu = test
        print("最高相对湿度为%s%%，出现时间为%s" %(maxrhu,time))
        return maxrhu, time
    
    def minRhu(self):   #最低相对湿度
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        minrhu = 100
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['RHU'])
            test = float(self.hjson['DS'][x]['RHU'])
            if minrhu > test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                minrhu = test
        print("最低相对湿度为%s%%，出现时间为%s" %(minrhu,time))
        return minrhu ,time
    
    def maxWp(self):    #最大风力
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        maxwp = 0
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['windpower'])
            test = float(self.hjson['DS'][x]['windpower'])
            if maxwp < test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxwp = test
        print("最大风力为%s级，出现时间为%s" %(maxwp,time))
        return maxwp, time
    
    def maxWinsmax(self):   #最高最大风速和对应角度
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        maxwinsmax = 0
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['WIN_S_Max'],self.hjson['DS'][x]['WIN_D_S_Max'])
            test = float(self.hjson['DS'][x]['WIN_S_Max'])
            if maxwinsmax < test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxwinsmax = test
                angle = self.hjson['DS'][x]['WIN_D_S_Max']
        print("最高最大风速为%sm/s，方向为%s度，出现时间为%s" %(maxwinsmax,angle,time))
        return maxwinsmax, angle, time
    
    def maxPre1h(self):     #最大每小时降水量
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        maxpre1h = 0
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['PRE_1h'])
            test = float(self.hjson['DS'][x]['PRE_1h'])
            if maxpre1h < test:
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxpre1h = test
        print("最高每小时降水为%smm，出现时间为%s" %(maxpre1h,time))
        return maxpre1h, time
    
    def accumulatedPre(self):   #累计降水量
        time1 = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        pre = 0
        for x in range(len(self.hjson["DS"])):
            pre = pre + float(self.hjson['DS'][x]['PRE_1h'])
            time2 = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
        print("从%s到%s的累积降水量为%smm" %(time1,time2,pre))
        return pre
    
    def maxClo(self):   #最大总云量
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        maxclo = 0
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['CLO_Cov'])
            if self.hjson['DS'][x]['CLO_Cov'] == '':
                self.hjson['DS'][x]['CLO_Cov'] = 0
            test = float(self.hjson['DS'][x]['CLO_Cov'])
            if maxclo < test and test <= 100:            #数据集中可能有错误数据，所以加入上限限制
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                maxclo = test
        print("最高总云量为%s%%，出现时间为%s" %(maxclo,time))
    #    print(maxclo)
        return maxclo, time
    
    def minClo(self):   #最小总云量
        time = str(self.hjson['DS'][0]['Year']+self.hjson['DS'][0]['Mon'].zfill(2)+self.hjson['DS'][0]['Day'].zfill(2)+self.hjson['DS'][0]['Hour'].zfill(2))
        minclo = 100
        for x in range(len(self.hjson["DS"])):
            #print(self.hjson['DS'][x]['CLO_Cov'])
            if self.hjson['DS'][x]['CLO_Cov'] == '':
                self.hjson['DS'][x]['CLO_Cov'] = 0
            test = float(self.hjson['DS'][x]['CLO_Cov'])
            if minclo > test and test <= 100:            #数据集中可能有错误数据，所以加入上限限制
                time = str(self.hjson['DS'][x]['Year']+self.hjson['DS'][x]['Mon'].zfill(2)+self.hjson['DS'][x]['Day'].zfill(2)+self.hjson['DS'][x]['Hour'].zfill(2))
                minclo = test
        print("最低总云量为%s%%，出现时间为%s" %(minclo,time))
        return minclo, time
    


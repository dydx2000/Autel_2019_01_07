import os
import re

def getMem():
    lines = os.popen("adb shell dumpsys meminfo com.autel.explorer").readlines() #逐行读取
    total = "TOTAL"
    i=0

    for line in lines:


            if re.findall(total, line): # 找到TOTAL 这一行
                if i == 0:
                    lis = line.split(" ")  #将这一行，按空格分割成一个list
                    # print(lis)
                    while '' in lis:       # 将list中的空元素删除
                        lis.remove('')
                        # print(lis)
                    mem=int(lis[1])/1024
                    # print(mem)
                    # print(mem/2048)
                    print("Memory Usage is: ", round(mem / 2048 * 100, 2), "%")

                i+=1
            # return lis[1] #返回总共内存使用


def getCpu():
    # li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    li = os.popen('adb shell dumpsys cpuinfo |findstr "com.autel.explorer"').readlines()
    # print(li)
    # li = os.popen("adb shell top").readlines()
    # i=0
    for line in li:
        # if i == 0:

            cpulist = line.split(" ")
            while ''  in cpulist:
                cpulist.remove('')
                # print(cpulist)
            print("CPU Usage is:  ", cpulist[0].strip('%'), '%')
        # i+=1
    '''
    
    name = "com.autel.explore"
    for line in li:
        if re.findall(name,line):
            cpulist = line.split(" ")
            # print(cpulist)
            
            if cpulist[-1].strip() == 'com.autel.explorer':
            # if cpulist[-1].strip() == 'com.autel.explorer':
                while '' in cpulist:       # 将list中的空元素删除
                    cpulist.remove('')
                print("Cpu Usage is:       ", cpulist[8], '%')
                    # print(cpulist)
                # print(cpulist[2])
                # return float(cpulist[2].strip('%')) #去掉百分号，返回一个float
                # break
    '''

def getTemp():
    temp = os.popen("adb shell cat /sys/class/thermal/thermal_zone0/temp").readlines()
    temp = float(temp[0]) /1000
    print('Temperature is: ',str(temp)+' ℃')

getCpu()

getMem()
getTemp()
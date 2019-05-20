from appium import webdriver
list1=[1,325,69,87,32,23]

for i in range(0,len(list1)):
    for j in range(0,len(list1)-1-i):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)

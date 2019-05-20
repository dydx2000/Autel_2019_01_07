from selenium import webdriver
import time
import random
# from openpyxl import load_workbook

#登录账号密码
dir = webdriver.Chrome()
dir.implicitly_wait(10)
dir.maximize_window()
dir.get("https://run.e-stronger.com/admin/index/login?url=%2Fadmin%2Fdashboard%3Fref%3Daddtabs")
dir.find_element_by_xpath('//*[@id="pd-form-username"]').send_keys("change")
dir.find_element_by_xpath('//*[@id="pd-form-password"]').send_keys("a13790625338")
dir.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

#进入运营管理
dir.find_element_by_xpath('//*[@id="tabs"]/div/aside[1]/div/section/ul/li[6]/a').click()
dir.find_element_by_xpath('//*[@id="tabs"]/div/aside[1]/div/section/ul/li[6]/ul/li/a').click()
iframe = dir.find_elements_by_tag_name("iframe")[1]
dir.switch_to.frame(iframe)
time.sleep(5)
dir.find_element_by_css_selector('#toolbar > a.btn.btn-success.btn-add').click()

# getLoad=load_workbook("userAdd.xlsx")
# # 读取Excel里的Sheet栏
# getStudent=getLoad["Sheet1"]
# for i in getStudent.rows:
#     print(i)
#     print(i[0].value)
#     print(i[1].value)

# # 获取表格
# getLoad = load_workbook("userAdd.xlsx")
# getStudent = getLoad["Sheet1"]
# for i in getStudent.row:

iframe = dir.find_elements_by_tag_name("iframe")[0]
dir.switch_to.frame(iframe)
dir.find_element_by_xpath('//*[@id="c-title"]').send_keys("hehe")
dir.find_element_by_xpath('//*[@id="c-content"]').send_keys("okok")
dir.find_element_by_xpath('//*[@id="c-target_text"]').click()

# 随机选取发送目标
dir.find_element_by_xpath('//*[@id="c-target_text"]').click()
time.sleep(2)
suiji=random.randint(1,9)
dir.find_element_by_css_selector\
    ('body > div.sp_result_area.sp_result_area_open.shadowDown > ul > li:nth-child({})'.format(suiji)).click()



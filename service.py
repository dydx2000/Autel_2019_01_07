from selenium import webdriver
import unittest
# from openpyxl import load_workbook
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Test(unittest.TestCase):
    def setUp(self):
        self.dir=webdriver.Chrome()
        self.dir.maximize_window()
        self.dir.get("https://run.e-stronger.com/admin/index/login?url=%2Fadmin%2Fdashboard%3Fref%3Daddtabs")


    def testlogin(self):
            # 登录账号
            WebDriverWait(self.dir, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="pd-form-username"]'))).send_keys("change")
            # 登录密码
            WebDriverWait(self.dir, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="pd-form-password"]'))).send_keys("a13790625338")
            # 点击登录
            WebDriverWait(self.dir, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="login-form"]/div[5]/button'))).click()
            self.dir.find_element_by_class_name('active').click()

            time.sleep(60)


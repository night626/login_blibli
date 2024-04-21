from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json
from selenium import webdriver

class GetCookies:
    def __init__(self, url):
        self.cookies = {}
        self.url = url

    def __call__(self):
        # 实例化 EdgeOptions
        options = webdriver.EdgeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('--disable-blink-features=AutomationControlled')

        # 实例化 Edge WebDriver
        driver = webdriver.Edge(options=options)
        driver.get(self.url)
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/ul[2]/li[1]/li/div[1]/div/span')))
        # 点击登录
        element.click()
        sleep(1)
        # 点击短信验证
        first_link = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[1]/div[3]')
        first_link.click()
        sleep(1)
        # 输入手机号
        search_box = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[2]/form/div[1]/input')
        search_box.send_keys("19574854616")
        sleep(1)
        # 点击获取验证码
        second_link = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[2]/form/div[1]/div[3]')
        second_link.click()
        # 输入验证码
        sleep(20)

        # 获取当前页面的所有 Cookie
        cookies = driver.get_cookies()

        timestamp = datetime.now().strftime("%Y-%m-%d")

        # 将获取到的 Cookie 写入文件
        with open(f"cookies_{timestamp}.txt", "w", encoding="utf-8") as file:
            json.dump(cookies, file)
        # 返回当前存放cookie的文件名
        return f"cookies_{timestamp}.txt"

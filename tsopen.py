from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.EdgeOptions()
options.add_argument('--disable-gpu')
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('--disable-blink-features=AutomationControlled')

# 实例化 Edge WebDriver
driver = webdriver.Edge(options=options)
driver.get("https://space.bilibili.com/1964454421/favlist?spm_id_from=333.337.0.0")
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/ul[2]/li[1]/li/div[1]/div/span')))
# 点击登录
element.click()
sleep(1)
# 点击短信验证
first_link = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[1]/div[3]')
first_link.click()
sleep(5)
# 输入手机号
search_box = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[2]/form/div[1]/input')
search_box.send_keys("19574854616")
sleep(5)
# 点击获取验证码
second_link = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div[2]/form/div[1]/div[3]')
second_link.click()
# 输入验证码
sleep(15)

input("nihoa")

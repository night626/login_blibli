import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_blibli.GetCookies import GetCookies

url = "https://space.bilibili.com/1964454421/favlist?spm_id_from=333.337.0.0"

# 获取网页cookie，需要手动登录
def get_cookies(url):
    # 实例化
    get_cookie = GetCookies(url=url)
    # 调用call方法
    file_name = get_cookie()
    return file_name

# 规避检测
options = webdriver.EdgeOptions()
options.add_argument('--disable-gpu')
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('--disable-blink-features=AutomationControlled')

# 实例化 Edge WebDriver
driver = webdriver.Edge(options=options)

driver.get(url)
# 清除无效cookie
driver.delete_all_cookies()

# 将获取到的 Cookie 添加到驱动中
# 再次操作的时候，直接用文件名替换get_cookies(url)
with open(get_cookies(url), "r") as file:
    cookies = json.load(file)
    for i in cookies:
        driver.add_cookie(i)

# 使用显示等待，至元素可见
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-fav"]/div[1]/div[2]/div[1]/div/div/div[3]/a')))

# 执行点击操作
element.click()

# 防止 Selenium 跟着 Python 进程关闭
input("waiting")

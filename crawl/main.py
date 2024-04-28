import requests
from bs4 import BeautifulSoup

import pymysql

# 连接到MySQL数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="abc123123",
    database="crawl",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标对象
cursor = conn.cursor()


# 定义爬取函数
def crawl_web_page(url):
    # 发送请求并获取HTML内容
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text

        # 使用Beautiful Soup解析HTML
        soup = BeautifulSoup(html, 'html.parser')

        example_divs = soup.find_all('div', class_='emoji_card')
        for div in example_divs:
            name = div.find('a', class_='emoji_name truncate').text
            icon = div.find('a', class_='emoji_font').text

            print("name:", name, "icon:", icon)
            sql = "INSERT INTO Emoticons (name, icon) VALUES (%s, %s);"
            values = (name, icon)
            cursor.execute(sql, values)

            if name == "海盗旗":
                break
        # 提交事务
        conn.commit()

        print(f"Successfully crawled: {url}")
    else:
        print(f"Failed to crawl: {url}")


# 要爬取的网页
crawl_web_page("https://www.emojiall.com/zh-hans/all-emojis?type=normal")

# 关闭数据库连接
cursor.close()
conn.close()

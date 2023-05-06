import re
from Collector.collector import *


t66y_url = "https://t66y.com/thread0806.php?fid=7"
base_url = "http://www.t66y.com/"


def get_t66y(url):
    browser = mechanicalsoup.StatefulBrowser(
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1")
    # TODO 这里header 应该要自动放到colletor里面支持
    header = {"Referer": "http://www.t66y.com"}
    browser.open(t66y_url, headers=header)
    p = browser.page
    # 用chatgpt写的。。。
    main_page = p.find('tbody', {'id': 'tbody', 'style': 'table-layout:fixed;'})
    if main_page:
        topics = main_page.find_all("tr", "tr3 t_one tac")
        for topic in topics:
            name = topic.find("a").get_text()
            url = base_url + topic.find("a").get("href")
            thumbsup = topic.find("span", "s3").get_text()
            comments = topic.find_all("td")[3].get_text().strip()
            # '05-07 01:14' 没有年份
            # 回复时间
            reply_time = topic.find_all("td")[4].find("a").get_text().strip()
            author = topic.find_all("td")[2].find("a").get_text()
            timestamp = topic.find_all("td")[2].find("span", "s3").get("data-timestamp")

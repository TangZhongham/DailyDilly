import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

# TODO 暂时只能使用 selenium 爬取。应该是需要开启js

pincong = "https://pincong.rocks"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36	"
header = {"Referer": "https://pincong.rocks/"}
pc_list = []

def get_pc(pc):
    # 貌似还不让我用 headless 模式妈的
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')  # 设置option
    chrome_service = ChromeService(executable_path='../storage/chromedriver')
    dr = webdriver.Chrome(service=chrome_service)
    dr.get(pc)
    html = dr.page_source
    soup = BeautifulSoup(html, 'html.parser')
    topics = soup.find("div", "aw-common-list").find_all("div", "aw-item")
    for each in topics:
        title = each.find("h4").get_text().strip()
        url = pincong + each.find("h4").find("a").get("href")
        _time = each.find_all('span', class_='aw-small-text aw-nowrap')[1].get_text()
        # 发帖时间
        time = re.findall(r'\d{4}-\d{2}-\d{2}', _time)[0]
        _comments = each.find_all('span', class_='aw-small-text aw-nowrap')[-1].get_text()
        finds = re.findall(r'\d+', _comments)
        if len(finds) == 1:
            # 只有浏览数暂时没有回复
            comments = 0
            reads = finds[0]
        elif len(finds) == 2:
            # 回复
            comments = re.findall(r'\d+', _comments)[0]
            # 浏览量
            reads = re.findall(r'\d+', _comments)[1]
        else:
            comments = 0
            reads = 0

        pc_list.append({
            "title": title,
            "time": time,
            "url": url,
            "comments": comments,
            "reads": reads
        })
    dr.close()


if __name__ == '__main__':
    get_pc(pincong)
    print(pc_list)
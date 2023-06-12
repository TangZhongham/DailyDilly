import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

# TODO: 每天爬两次加航官网，看看有没有特价机票


aircanada = "https://www.aircanada.com/cn/zh/aco/home/app.html#/faredriven"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36	"
header = {"Referer": "https://www.aircanada.com/cn/zh/aco/home.html"}
price_list = []


def get_prices(ac):
    chrome_service = ChromeService(executable_path='../storage/chromedriver')
    dr = webdriver.Chrome(service=chrome_service)
    dr.get(ac)
    html = dr.page_source
    soup = BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    get_prices("https://www.aircanada.com/cn/zh/aco/home.html")
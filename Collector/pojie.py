import mechanicalsoup
import re

url = "https://www.52pojie.cn/index.php"


def get_pojie(pojie):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(pojie)
    p = browser.page
    top = p.find("tr", "fl_row")
    top4 = top.find_all("div", "boxbg_7ree")
    if len(top4) == 5:
        new_threads = top4[0]
        tech_share = top4[1]
        hot_threads = top4[2]
        best_threads = top4[3]


def get_info(threads):
    for thread in threads.find_all("a"):
        thread_name = thread.get_text()
        thread_url = thread.get("href")
        thread_tips =thread.get("tips")


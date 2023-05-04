import mechanicalsoup
import re

url = "https://news.ycombinator.com/"

today_yc = {}


def get_yc(yc):
    browser = mechanicalsoup.StatefulBrowser()
    bs = browser.open(yc)
    p = browser.page
    # url
    for i in p.find_all("span", "titleline"):
        # print(i)
        today_yc["title"] = i.get_text()
        today_yc["url"] = i.find("a").get("href")

    # 作者，points 数，时间。（可以获得当天内的top10帖子
    for x in p.find_all("td", "subtext"):
        # print(x)
        # 存在没有score 的条目
        _score = x.find("span", "score").get_text() if x.find("span", "score") else ""
        if re.findall("[0-9]+", _score):
            score = re.findall("[0-9]+", _score)[0]
            print(score)
        # '2023-05-03T10:32:10'
        timestamp = x.find("span", "age").get("title")
        today_yc["timestamp"] = timestamp
        # time from now
        time = x.find("span", "age").get_text()
        today_yc["time"] = time
        writer = x.find("a", "hnuser").get_text() if x.find("a", "hnuser") else ""
        _comments = x.find_all("a")[-1].get_text()
        if re.findall("[0-9]+", _comments):
            comments = re.findall("[0-9]+", _comments)[0]
            print(comments)


if __name__ == '__main__':
    get_yc(url)

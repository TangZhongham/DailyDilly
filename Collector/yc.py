import mechanicalsoup
import re
import csv

# TODO:
# 1. 入csv
# 2. 权重计算（可交给fastapi做，这边只管入库，排序解耦

url = "https://news.ycombinator.com/"

ycs = {}
today_yc = []
a = []
b = []


def get_yc(yc):
    browser = mechanicalsoup.StatefulBrowser()
    bs = browser.open(yc)
    p = browser.page
    # url
    for i in p.find_all("span", "titleline"):
        # print(i)
        title_dic = {"title": i.get_text(), "url": i.find("a").get("href")}
        a.append(title_dic)

    # 作者，points 数，时间。（可以获得当天内的top10帖子
    for x in p.find_all("td", "subtext"):
        score_dic = {}
        # 存在没有score 的条目
        _score = x.find("span", "score").get_text() if x.find("span", "score") else ""
        if re.findall("[0-9]+", _score):
            score = re.findall("[0-9]+", _score)[0]
            score_dic["score"] = score
        # '2023-05-03T10:32:10'
        timestamp = x.find("span", "age").get("title")
        score_dic["timestamp"] = timestamp
        # time from now
        time = x.find("span", "age").get_text()
        score_dic["time"] = time
        writer = x.find("a", "hnuser").get_text() if x.find("a", "hnuser") else ""
        score_dic["writer"] = writer
        _comments = x.find_all("a")[-1].get_text()
        if re.findall("[0-9]+", _comments):
            comments = re.findall("[0-9]+", _comments)[0]
            score_dic["comments"] = comments
        b.append(score_dic)


def sink_csv(result):
    ## TODO 需要添加对比模块功能，目前只对比title即可
    header = ["title", "score", "comments", "writer", "time", "timestamp", "url"]
    with open('../storage/csv/yc.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter='|')
        # writer.writeheader()
        writer.writerows(result)
    print("更新完成")


def calculate_quanzhong():
    # 计算展示的权重
    pass



if __name__ == '__main__':
    get_yc(url)
    final = []
    for x, y in zip(a,b):
        z = x | y
        final.append(z)
    # [{'title': 'Prime Video ', 'url': 'https://www.primevideotech.com', 'score': '444', 'timestamp':
    # '2023-05-04T06:04:56', 'time': '2 hours ago', 'writer': 'debdut', 'comments': '204'} ]
    print(a)
    print(len(a))
    print(b)
    print(len(b))
    print(final)
    sink_csv(final)

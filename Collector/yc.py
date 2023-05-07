import re
from Collector.collector import *

# TODO:
# 1. 入csv
# 2. 权重计算（可交给fastapi做，这边只管入库，排序解耦

url = "https://news.ycombinator.com/"

ycs = {}
today_yc = []
a = []
b = []


def get_yc(yc):
    p = get_page(yc)
    # url
    for i in p.find_all("span", "titleline"):
        # print(i)
        title_dic = {"title": i.get_text(), "url": i.find("a").get("href")}
        a.append(title_dic)

    # 作者，points 数，时间。（可以获得当天内的top10帖子
    for x in p.find_all("td", "subtext"):
        score_dic = {}
        score = ""
        comments = ""

        # '2023-05-03T10:32:10'
        timestamp = x.find("span", "age").get("title")
        # time from now
        time = x.find("span", "age").get_text()
        writer = x.find("a", "hnuser").get_text() if x.find("a", "hnuser") else ""

        # 存在没有score 的条目
        _score = x.find("span", "score").get_text() if x.find("span", "score") else ""
        if re.findall("[0-9]+", _score):
            score = re.findall("[0-9]+", _score)[0]
        else:
            # threads like hiring does not have a score
            score = 0

        _comments = x.find_all("a")[-1].get_text()
        if re.findall("[0-9]+", _comments):
            comments = re.findall("[0-9]+", _comments)[0]
        else:
            comments = 0
        b.append(
            {
                "writer": writer,
                "score": score,
                "comments": comments,
                "time": time,
                "timestamp": timestamp
            }
        )


def is_new(threads):
    # 确定是否已经爬取过
    pass


def calculate_weights(threads):
    # 计算展示的权重
    # score 前五 + comments 前五
    top5_score = get_topn(threads,"score", 5)
    top5_comments = get_topn(threads,"comments", 5)
    print("a")


def get_topn(threads,section,number):
    return sorted(threads, key=lambda one: int(one.__getitem__(section)), reverse=True)[:number]


if __name__ == '__main__':
    header = ["title", "score", "comments", "writer", "time", "timestamp", "url"]
    get_yc(url)
    final = []
    for x, y in zip(a, b):
        z = x | y
        final.append(z)
    # [{'title': 'Prime Video ', 'url': 'https://www.primevideotech.com', 'score': '444', 'timestamp':
    # '2023-05-04T06:04:56', 'time': '2 hours ago', 'writer': 'debdut', 'comments': '204'} ]
    print(a)
    print(len(a))
    print(b)
    print(len(b))
    print(final)
    calculate_weights(final)

    yc_csv = '../storage/csv/yc.csv'
    sink_csv(final, yc_csv, header)
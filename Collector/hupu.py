import re
from Collector.collector import *

# 定制页，论坛
# 计算方式: 亮+回复

base_url = "https://bbs.hupu.com"
url = "https://bbs.hupu.com/all-nba"
header = ["name", "type", "lights", "comments", "url"]

subscribe_topic_list = ["lakers", "mancity", "topic", "vote"]

file_name = "../storage/csv/hupu.csv"
hupu_list = []


def get_hupu_mainpage(hupu):
    p = get_page(hupu)
    main_page = p.find("div", "bbs-index-web-middle")
    topics = main_page.find_all("div", "t-info")

    for each in topics:
        main_dic = {}
        title = each.find("a").get_text()
        # lights = each.find("span", "t-lights").get_text()
        url = base_url + each.find("a").get("href")
        _comments = each.find("span", "t-replies").get_text()
        comments = re.findall("^\d+", _comments)[0]
        # main_dic["title"] = title
        # main_dic["comments"] = comments
        # main_dic["url"] = url
        # main_dic["type"] = "all-nba"
        hupu_list.append(
            {
                "title": title,
                "comments": comments,
                "url": url,
                "type": "all-nba"
            }
        )


def get_hupu_bbs(topic):
    topic_url = base_url + "/" + topic
    p = get_page(topic_url)
    topics = p.find_all("li", "bbs-sl-web-post-body")
    for each in topics:
        main_dic = {}
        title = each.find("a").get_text()
        url = base_url + each.find("a").get("href")
        _comments = each.find("div", "post-datum").get_text()
        comments = re.findall("^\d+", _comments)[0]
        # main_dic["title"] = title
        # main_dic["comments"] = comments
        # main_dic["url"] = url
        # main_dic["type"] = topic
        # hupu_list.append(main_dic)
        hupu_list.append(
            {
                "title": title,
                "comments": comments,
                "url": url,
                "type": topic
            }
        )


if __name__ == '__main__':
    get_hupu_mainpage(url)
    for each_topic in subscribe_topic_list:
        get_hupu_bbs(each_topic)
    print(hupu_list)

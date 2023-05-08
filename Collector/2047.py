import re
from Collector.collector import *


two047_url = "https://2047.one"
two047_list = []


def get_2047(url):
    p = get_page(url)
    topics = p.find_all("li", "sz-item padtd")
    for each in topics:
        title = each.find("div", "right").find("h2").get_text()
        url = two047_url + each.find("div", "right").find("a").get("href")
        create_date = each.find("div", "right").find("footer").find_all("a")[2].get_text()
        two047_list.append(
            {
                "title": title,
                "url": url,
                "create_date": create_date
            }
        )


if __name__ == '__main__':
    get_2047(two047_url)
    print(two047_list)
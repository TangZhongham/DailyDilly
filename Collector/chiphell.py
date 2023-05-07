import re
from Collector.collector import *


# 定制页，轮胎
# chiphell 社区有带验证码的登陆，需要走selenium，暂时不搞
# 但是可以搞几个板块

base_url = "https://www.chiphell.com/portal.php?mod=list&catid="

# 掌摄 摄影 照片 模型 败家 时尚
topic_list = ["36", "31", "3", "30", "33", "118"]
chiphell_list = []


def get_chiphell(cp):
    p = get_page(cp)
    main_page = p.find("div", "bm_c xld")
    topics = main_page.find_all("dl", "bbda cl")
    for each in topics:
        cp_dic = {}
        name = each.find("a").get_text()
        url = "" + each.find("a").get("href")
        description = each.find("dd", "xs2 cl").get_text()
        timestamp = each.find("span", "xg1").get_text().strip()

        chiphell_list.append(
            {
                "name": name,
                "description": description,
                "url": "https://www.chiphell.com/" + url,
                "timestamp": timestamp
            }
        )


if __name__ == '__main__':
    for i in topic_list:
        url = base_url + i
        get_chiphell(url)

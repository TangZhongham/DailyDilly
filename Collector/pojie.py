import re
from Collector.collector import *

# TODO:
# 1 比较规则入库
# 2 weights

url = "https://www.52pojie.cn/index.php"
header = ["name", "type", "writer", "url", "timestamp"]
file_name = "../storage/csv/pojie.csv"
pojie = []


def get_pojie(pojie):
    p = get_page(pojie)
    top = p.find("tr", "fl_row")
    top4 = top.find_all("div", "boxbg_7ree")
    if len(top4) == 5:
        new_threads = top4[0]
        get_info(new_threads)
        tech_share = top4[1]
        get_info(tech_share)
        hot_threads = top4[2]
        get_info(hot_threads)
        best_threads = top4[3]
        get_info(best_threads)


def get_info(threads):
    for thread in threads.find_all("a"):
        thread_name = thread.get_text()
        thread_url = thread.get("href")
        thread_tips = thread.get("tips")
        if thread_tips:
            thread_writer = re.findall("作者：(.+?)<br>", thread_tips)[0]
            thread_timestamp = re.findall("时间：(.+?)<br>", thread_tips)[0]
            thread_type = re.findall("版块：(.+?)<br>", thread_tips)[0]
            pojie.append(
                {
                    "name": thread_name,
                    "type": thread_type,
                    "writer": thread_writer,
                    "url": "https://www.52pojie.cn/" + thread_url,
                    "timestamp": thread_timestamp
                }
            )
            print({"name": thread_name, "type": thread_type, "writer": thread_writer,
                          "url": "https://www.52pojie.cn/" + thread_url, "timestamp": thread_timestamp})


if __name__ == '__main__':
    get_pojie(url)
    sink_csv(pojie, filename=file_name, header=header)

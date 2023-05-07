import re
from Collector.collector import *

# TODO 要么只抓第一页，要么多抓几页，后期可以控制

gcore_url = "https://www.gcores.com/articles"
gcore_articles = []


def get_gcores(gcore_url):
    p = get_page(gcore_url)
    main_page = p.find("div", "row")
    if main_page:
        topics = main_page.find_all("div", "am_card_inner")
        for each in topics:
            title = each.find("h3").get_text()
            url = "https://www.gcores.com" + each.find_all("a")[1].get("href")
            author = each.find("div", "avatar_text").find("h3").get_text()
            thumbs_up = each.find("span", "me-3").get_text()
            comments = each.find_all("span")[-1].get_text()

            gcore_articles.append(
                {
                    "title": title,
                    "author": author,
                    "url": url,
                    "thumbs_up": thumbs_up,
                    "comments": comments
                }
            )


if __name__ == '__main__':
    get_gcores(gcore_url)
    print(gcore_articles)



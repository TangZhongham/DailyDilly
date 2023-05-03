import mechanicalsoup

url = "https://news.ycombinator.com/"


def get_yc(yc):
    browser = mechanicalsoup.StatefulBrowser()
    bs = browser.open(yc)
    p = browser.page
    # url
    for i in p.find_all("span", "titleline"):
        print(i)
    # 作者，points 数，时间。（可以获得当天内的top10帖子
    for x in p.find_all("td", "subtext"):
        print(x)


if __name__ == '__main__':
    get_yc(url)

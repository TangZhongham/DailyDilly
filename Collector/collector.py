import csv
import mechanicalsoup


def get_page(url):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    p = browser.page
    return p


def sink_csv(result, filename, header):
    ## TODO 需要添加对比模块功能，目前只对比title即可
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter='|')
        # writer = csv.DictWriter(csvfile, delimiter='|')
        # writer.writeheader()
        writer.writerows(result)
    print("更新完成")
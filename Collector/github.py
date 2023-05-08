# 提供登录后 个人推荐页内容展示
# 感觉没啥好玩的需要爬
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
soup_config={'features': 'lxml'},
raise_on_404=True,
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
)

github_url = "https://github.com"

browser.open(github_url)
browser.follow_link("login")
browser.select_form('#login form')

browser["login"] = ''
browser["password"] = ''
resp = browser.submit_selected()

# browser.launch_browser()
page = browser.page
browser.follow_link("/explore")
np = browser.page

trending = np.find("div", "Box color-shadow-small mb-4")
trending_repositories = trending.find_all("article", "Box-row")
for each_repo in trending_repositories:
    repo = each_repo.find("h4").get("title")
    repo_stars = each_repo.find("a").get_text().strip()
    repo_url = github_url + each_repo.find("h4").find_all("a")[-1].get("href")
    repo_description = each_repo.find("p").get_text().strip()

# github 的feed 感觉没什么营养。。。但是 https://github.com/trending 好像不需要登陆
feed = np
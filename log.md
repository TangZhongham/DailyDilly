# 开发日志

## 项目目标

1. 锻炼代码能力

2. 提高个人网页信息迅速获取能力

## 项目设计

爬取自己常用的信息源，包装成web服务，同时支持rss订阅。

✅ 前端：

内容展示：支持web/手机，支持暗黑模式，页面功能：预览，

支持邮件展示（foundation 构造漂亮帅气的邮件）

✅ 后端：

内容爬取：先使用自己爬取的raw 网页，包装成rss。目前的有的网页提供了rss，（主要是前端展示部分还没做。python dic 格式 -》jinja2？）
然后保证服务可以独立以rss标准格式推出。

内容purify：raw 网页转csv格式，raw 网页转rss格式。先用csv格式？后期走通了再支持数据库
（不知道nosql有没有类似sqlite 的服务，或者sqlite当nosqlyong）

内容计算：权重计算，爬取内容比较。新闻细节用gpt总结。新闻权重对比（https://www.newsminimalist.com/ 这个思路很牛逼），

内容存储：csv/rss/sqlite/notion （考虑需不需要用sqlite，毕竟个网站需要

### 功能

网页爬虫，热帖规则计算

邮件功能

网页host功能

支持 Notion API （网页端，支持点击后自动保存notion）

通过model做一个每日简报，比方说top10个网站的热文，用chatgpt之类的总结再输出。

存储层支持csv/xml（rss）/sqlite

用sqlite数据库存储，了解该数据库原理

前端看看有没有类似bootstrap 的框架

### 网站汇总

#### ❎ 金融知识获取：哪些比较好的网站？

#### ❎ 留学信息

#### 🏄 娱乐

🏄 hupu
🏄 t66y：自己爬了没用rsshub，https://rsshub.app/t66y/7    
❎ v2ex：https://v2ex.com/index.xml
❎ pingcong
🏄 机核
🏄 chiphell
🏄 吾爱破解
❎ 支持 github 登陆的推荐抓取
❎ twitter？不知道现在还行不行


#### ❎ AI 知识

#### 🏄 新闻

🏄 yc hackernews

参考 https://github.com/echosoar/news 有很多新闻网站的api 可以直接爬取用 （搜github新闻聚合

freebuf https://www.freebuf.com/feed

simhash 算法去重

#### 每日随机文章（随想？）

❎ daily fiction: https://dailysciencefiction.com/

❎ 可以自己学习的英语单词也对接进来。（每日单词

#### swiftui 知识？twitter 爬虫？

#### Kijiji 通用爬虫？

## 项目架构

1. 爬虫存本地db

2. web 服务读db，发邮件 or 页面刷新触发爬取

先用csv存，然后后期开发db功能（爬取和读取分离）

存notion？

可以用免费的chatgpt 集合做一个内容摘要功能：https://github.com/LiLittleCat/awesome-free-chatgpt

前端：

发现email 也有框架美化 https://get.foundation/emails/email-templates.html


## 前端

前端要求：

- 手机电脑都能用
- 最好有黑暗模式
- 新闻聚合类

前端选择：

Bootstrap5

Foundation：有 email 的template


## 原理

了解bs源码等项目源码

## log

0504 把基本 yc/pojie 写完了爬取的部分。打算选几个网站，然后把框架搭好。

0505 了解了一个很好玩的项目，帮助了这个项目定位。感觉先不要横向铺太开，专注完成几个最小可行方案，一条路走通。

先再爬几个网站，然后考虑权重计算，前端展示，rss 定义。---- 说白了自己想搞一个网站聚合版的 "今日头条/抖音"

0506

写了hupu 和 chiphell。明天上午再写俩个差不多就可以开始搞下一步了。
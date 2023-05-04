# 开发日志

## 项目目标

1. 锻炼代码能力

2. 提高个人网页信息迅速获取能力

## 项目设计

### 功能

网页爬虫，热帖规则计算

邮件功能

网页host功能

支持 Notion API

通过model做一个每日简报，比方说top10个网站的热文，用chatgpt之类的总结再输出。

用sqlite数据库存储，了解该数据库原理

前端看看有没有类似bootstrap 的框架

### 网站汇总

#### ❎ 金融知识获取：哪些比较好的网站？

#### ❎ 留学信息

#### 🏄 娱乐

❎ hupu
❎ t66y
❎ v2ex
❎ pingcong
❎ 机核
❎ chiphell
🏄 吾爱破解

#### ❎ AI 知识

#### 🏄 新闻

🏄 yc hackernews

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

## 原理

了解bs源码等项目源码

## log

0504 把基本 yc/pojie 写完了爬取的部分。打算选几个网站，然后把框架搭好。

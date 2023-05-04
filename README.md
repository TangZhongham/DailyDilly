# DailyDilly

An async personal newshub

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

金融知识获取：哪些比较好的网站？

留学信息？

个人常逛的网页合并:

hupu，t66y，v2ex，pingcong，

AI 知识

吾爱破解

chiphell

每日随机文章（随想？）

swiftui 知识？twitter 爬虫？

Kijiji 通用爬虫？

存储方案？

每日热帖：hackernews

## 项目架构

1. 爬虫存本地db

2. web 服务读db，发邮件 or 页面刷新触发爬取

## 原理

了解bs源码等项目源码

## 依赖

python 3.9 (type hints)

uvicorn[standard]

fastapi

MechanicalSoup
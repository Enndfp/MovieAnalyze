import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

movies = []  # 用于存储电影数据的列表

# 发送HTTP请求获取网页内容
resp = requests.get(url, headers=headers)

# 检查请求的响应状态码
if resp.status_code == 200:
    page_content = resp.text

    # 使用正则表达式匹配电影信息
    obj = re.compile(
        r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
        r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp;'
        r'(?P<area>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
        r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>.*?'
        r'<span class="inq">(?P<desc>.*?)</span>',
        re.S
    )

    # 在页面内容中查找匹配的电影信息
    result = obj.finditer(page_content)

    # 提取电影信息并添加到movies列表中
    for item in result:
        dic = item.groupdict()
        dic['year'] = re.search(r'\d{4}', dic['year']).group()  # 提取4位数字作为年份
        dic['area'] = dic['area'].replace(" ", "")  # 去除空格
        movies.append(dic)

    # 检查是否成功获取到电影数据
    if movies:
        # 将数据存入CSV文件
        with open("data/MoviesData.csv", mode="w", encoding="UTF-8", newline="") as f:
            csvWriter = csv.writer(f)
            csvWriter.writerow(["电影名", "年份", "地区", "评分", "评价人数", "电影简介"])

            # 将电影数据逐行写入CSV文件
            for movie in movies:
                csvWriter.writerow(movie.values())

        print("数据爬取完成！")
    else:
        print("未获取到数据！")
else:
    print("请求失败，请检查网络连接或URL。")

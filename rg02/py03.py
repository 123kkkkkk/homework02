from cgitb import text

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.luogu.com.cn/problem/list"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4533.400"
}

resp = requests.get(url,headers=header)
# print(resp.text)

page_content = BeautifulSoup(resp.text, "html.parser")
page_main_content = page_content.find("div",attrs={"class": "lg-container"})
# print(page_main_content)

# problem_list = obj.finditer(page_content)
#
# for i in problem_list:
#     print(i.group("name"))
problem_list = page_main_content.find_all("li")
# print(problem_list)
obj = re.compile(r'<li>(?P<id>.*?)<a href=".*?">(?P<name>.*?)</a></li>')

# test_str = '<li>P1035 <a href="P1035">[NOIP2002 普及组] 级数求和</a></li>'
# iterator = obj.finditer(test_str)
# for i in iterator:
#     print(i.group("name"))
with open("problem.txt", mode="w", encoding="utf-8") as f:

    for i in problem_list:
        # print(str(i))
        ite = obj.finditer(str(i))
        for j in ite:

                print(j.group("name"))
                f.write(j.group("name")+'\n')

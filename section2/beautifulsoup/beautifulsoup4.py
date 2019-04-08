from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html", encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

#print("1", soup.select_one("li:nth-of-type(8)").string)
#print("1", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li 태그 그룹의 4번째 요소 선택
print("2", soup.select("li")[7].string)
print("3", soup.select("li:nth-of-type(4)")[0].string)
print("4", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("5", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("6", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {"data-lo": "cn", "class": "alcohol"}

print("7", soup.find("li", param).string)
print("8", soup.find(id="ac-list").find("li", param).string)


for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print("data-lo == us", ac.string)

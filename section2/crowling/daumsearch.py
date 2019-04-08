from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net"

res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')

# print(soup.prettify())
#
# for issue in soup.select("span.txt_issue"):
#    if issue.find(tabindex='-1') is not None:
#        print(issue.string, issue.select('a')[0]['href'])
#
#
#
# top10 = soup.find_all("a", tabindex='-1')
# for i in top10:
#    print(i.string, i.attrs['href'])
#
#
# find10 = soup.find_all("a", tabindex='-1')
# for i in find10:
#    print('find10', i)
#
# select10 = soup.select("a", tabindex='-1')
# for i in select10:
#     print('select10', i.attrs)
#
#
# find10 = soup.find_all("a", tabindex='-1')
# for i in find10:
#    print('find10', i.attrs)


top10 = soup.select("div.realtime_part > .list_hotissue.issue_row > li > div > div[aria-hidden='true'] > span.txt_issue a")

for e in top10:
    print(e.string)
    print(e['href'])

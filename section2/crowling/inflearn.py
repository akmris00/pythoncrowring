from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"

quote = rep.quote_plus("추천-강좌")# 한글을 유니코드로 바꿔주는것
#print(quote)

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')

#print(soup)

recommand = soup.select("ul.slides")[0]
#print(recommand)

for i,e in enumerate(recommand, 1):
    if i < 11: print(i, e.select_one("h4.block_title > a").string)

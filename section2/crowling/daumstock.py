from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net"
res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')

#print(soup.prettify())

top = soup.select("ul#topMyListNo1 > li")

for i,e in enumerate(top):
    print(i,",",e.find("a").string, " : ",e.find("span").string)

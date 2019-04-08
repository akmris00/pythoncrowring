from bs4 import BeautifulSoup
import sys
import io
import os
import urllib.request as req
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

qoute = rep.quote_plus("사자")

url = base + qoute

print(url)

res = req.urlopen(url)
savePath = "C:/Users/analysis/Desktop/imagedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, img_list in enumerate(img_list,1):
#    print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")

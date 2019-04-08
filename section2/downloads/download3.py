import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20090918_6%2Fsunmoon8874_1253260279597y5kIx_jpg%2F9_sunmoon8874.jpg&type=b400"
htmlURL = "http://google.com"
savePATH1 = "C:/Users/analysis/Desktop/test1.jpg"
savePATH2 = "C:/Users/analysis/Desktop/index.html"

f = dw.urlopen(imgURL).read()
f2 = dw.urlopen(htmlURL).read()
saveFile1 = open(savePATH1, 'wb') # w: write , r: read, a: add
saveFile1.write(f)
saveFile1.close()

with open(savePATH2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("완료")

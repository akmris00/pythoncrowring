import sys
import io
import urllib.request as req
from urllib.parse import urlencode


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://nv.veta.naver.com/fxshow"
API2 = "nrefreshx=0"
value1 = {'su' : 'SU10079'}
value2 = {'su' : 'SU10078'}



print('before', value1)
print('before', value2)
param1 = urlencode(value1)
param2 = urlencode(value2)
print('after', param1)
print('after', param2)

URL1 = API + '?' + param1 + '&' + API2
URL2 = API + '?' + param2 + '&' + API2

print(URL1)
print(URL2)
savePATH1 = "C:/Users/analysis/Desktop/test1.html"
savePATH2 = "C:/Users/analysis/Desktop/test2.html"

#req.urlretrieve(URL1, savePATH1)
#req.urlretrieve(URL2, savePATH2)


reqData1 = req.urlopen(URL1).read()
reqData2 = req.urlopen(URL2).read()

with open(savePATH1, 'wb') as saveFile1:
    saveFile1.write(reqData1)

with open(savePATH2, 'wb') as saveFile2:
    saveFile2.write(reqData2)

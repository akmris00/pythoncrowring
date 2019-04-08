import sys
import io
import urllib.request as req
from urllib.parse import urlencode


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api.ipify.org"
values = {
    'format' : 'jsonp'
}

#print('before', values)
params = urlencode(values)
#print('after', params)


URL = API + '?' + params

print('요청', URL)

reqData = req.urlopen(URL).read().decode('utf-8')
#reqData = req.urlopen(url).read().decode('utf-8')

print(reqData)

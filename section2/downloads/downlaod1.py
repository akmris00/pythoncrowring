import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20090918_6%2Fsunmoon8874_1253260279597y5kIx_jpg%2F9_sunmoon8874.jpg&type=b400"
savePATH = "C:/Users/analysis/Desktop/test1.jpg"

urllib.request.urlretrieve(imgURL, savePATH)

print("완료")

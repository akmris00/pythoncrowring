from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a id='naver' href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, features='html.parser')

#print(soup.find(id='naver'))
# q = soup.find_all(id='naver')
# p = soup.find(id='naver')
# r = soup.select("li")
# s = soup.select_one('li')
#
# print('find_all:', type(q))
# print(q)
# print('find: ', type(p))
# print(p)
# print('select:', type(r))
# print(r)
# print('select_one:', type(s))
# print(s)

print(soup.find(href=re.compile('https')))


li = soup.find_all(href=re.compile("^https://"))

#for e in li:
#    print(e.attrs['href'])

import sqlite3
import simplejson as json
import datetime

#DB 생성
conn = sqlite3.connect('c:/Atom/Crowring/section5/databases/sqlite1.db', isolation_level=None) #AutoCommit(isolation_level=None)

#DB 생성(메모리 DB)
#conn = sqlite3.connect(":memory:")

#날짜 생성
now = datetime.datetime.now()
print('now', now)
nowDatetime = now.strftime('%y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

#sqlite3 버전 확인
print('sqlite3.version', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

#커서 연결
c = conn.cursor()
#print(type(c))

#테이블 생성(sqlite3 datatype : TEXT, NUMERIC, INTEGER, REAL, BOLB)
c.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)") #AUTOINCREMENT

#데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-000-0000', 'kim.co.kr', ?)", (nowDatetime,))

userList = (
    (2, 'kim', 'kim@naver.com', '010-000-0000', 'kim.co.kr', nowDatetime),
    (3, 'kim', 'kim@naver.com', '010-000-0000', 'kim.co.kr', nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-000-0000', 'kim.co.kr', nowDatetime)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

with open('c:/Atom/Crowring/section5/data/users.json', 'r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        #print(t)
        userData.append(t)
    #print(userData)
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userData)


#데이터 삭세
#print("user db delete", conn.execute("delete from user"). rowcount, "rows")


#conn.commit()
conn.close()
#conn.rollback()

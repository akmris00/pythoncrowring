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
c.execute("")

#conn.commit()
#conn.rollback()

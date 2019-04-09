import sqlite3

#DB 생성
conn = sqlite3.connect('c:/Atom/Crowring/section5/databases/sqlite1.db', isolation_level=None) #AutoCommit(isolation_level=None)

#커서 연결
c = conn.cursor()

#데이터 수정
c.execute("UPDATE users SET username = ? WHERE id=?", ('niceman',1))

c.execute("UPDATE users SET username = :name WHERE id = :id",{"name":"goodboy", "id": 2})

c.execute("UPDATE users SET username='%s' WHERE id='%s'" % ('cuteboy', 3))


#데이터 삭제
c.execute("DELETE FROM users WHERE id=?",(4,))


#중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

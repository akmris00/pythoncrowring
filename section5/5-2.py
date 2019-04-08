import simplejson as json
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

#파일 DB 생성
db = TinyDB('c:/Atom/section5/databases/database.db', default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#users 테이블 출력
for item in users:
    print(item['username'], ' : ', item['phone'])

#todos 테이블 출력
for item in todos:
    print(item['title'], ' : ', item['completed'])

#연결 관계 출력
for item in users:
    print('[',item['username'],']')
    for todo in todos:
        if todo['userId'] == item['id']:
            print(todo['title'])

#쿼리 객체 사용 조회
#SQL = Query()
Users = Query()
Todos = Query()
user_3 = users.search(Users.id == 3) # >, <, >=, <=
print(user_3)

#수정
users.update({'username':'kim'}, Users.id ==3 )
user_3 = users.search(Users.id == 3) # >, <, >=, <=
print(user_3)

#삭제
users.remove(Users.id == 3)
user_3 = users.search(Users.id == 3) # >, <, >=, <=
print(user_3)

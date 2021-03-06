import simplejson as json
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

#파일 DB 생성
db = TinyDB('c:/Atom/section5/databases/database.db', default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#테이블 데이터 삽입
#users.insert({'name':'kim', 'email':'test@google.com'})
#todos.insert({'name':'homework', 'complete':False})

#테이블 데이터 전체 삽입
with open('c:/Atom/section5/data/users.json', 'r') as infile:
    r = json.loads(infile.read())
    for u in r:
        #print(u)
        users.insert(u)

#테이블 데이터 전체 삽입2
with open('c:/Atom/section5/data/todos.json', 'r') as infile:
    r = json.loads(infile.read())
    for t in r:
        #print(u)
        todos.insert(t)

#전체 데이터 출력
print(users.all())
print(todos.all())

#테이블 목록 조회
print(db.tables())

#전체 데이터 삭제
#users.purge()
#todos.purge()
#db.purge_table("users")
#db.purge_table("todos")
#db.purge_tables()

db.close()
